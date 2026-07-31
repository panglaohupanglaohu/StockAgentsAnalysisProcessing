# -*- coding: utf-8 -*-
"""P1-5 tool_loop 上下文预算：分级截断 / 重复调用缓存 / 历史摘要压缩。"""

from __future__ import annotations

import json

import pytest

from agents.chat_harness import ProviderConfig
from agents.runtime import tool_loop as tl


def test_truncate_tool_payload_tiers():
    big = "X" * 20_000
    low_c, low_f, low_t = tl.truncate_tool_payload("list_files", big, tool_result={"ok": True})
    med_c, med_f, med_t = tl.truncate_tool_payload("read_file", big, tool_result={"ok": True})
    high_c, high_f, high_t = tl.truncate_tool_payload(
        "write_file", big, tool_result={"ok": True, "path": "a.py"}
    )
    fail_c, fail_f, fail_t = tl.truncate_tool_payload(
        "list_files", big, tool_result={"ok": False, "error": "boom"}
    )
    assert low_t == "low" and med_t == "medium" and high_t == "high" and fail_t == "high"
    assert len(low_c) < len(med_c) <= len(high_c)
    assert low_f > 0 and med_f > 0
    # 失败走 high，比 low 保留更多
    assert len(fail_c) > len(low_c)
    assert "truncated" in low_c


def test_tool_call_cache_key_normalizes_json_key_order():
    a = tl.tool_call_cache_key("read_file", '{"path":"a.py","offset":1}')
    b = tl.tool_call_cache_key("read_file", '{"offset":1,"path":"a.py"}')
    c = tl.tool_call_cache_key("read_file", '{"path":"b.py","offset":1}')
    assert a == b
    assert a != c


def test_compact_old_tool_results_and_history_compress():
    messages = [
        {"role": "system", "content": "sys"},
        {"role": "user", "content": "do work"},
    ]
    # 造很多大 tool 结果，超过小预算
    for i in range(12):
        messages.append(
            {
                "role": "assistant",
                "content": f"thinking {i}",
                "tool_calls": [{"id": f"c{i}", "function": {"name": "read_file", "arguments": "{}"}}],
            }
        )
        messages.append(
            {
                "role": "tool",
                "name": "read_file",
                "tool_call_id": f"c{i}",
                "content": "Y" * 3000,
            }
        )
    before = tl._messages_char_count(messages)
    stats = tl._compact_old_tool_results(messages, budget_chars=8_000)
    after = tl._messages_char_count(messages)
    assert stats["freed_chars"] > 0
    assert after < before
    # 12×3k tool ≈ 36k+ → 应砍到预算附近（含 assistant tool_calls 余量）
    assert after < before * 0.55
    assert after < 20_000
    roles = [m.get("role") for m in messages]
    assert "system" in roles
    joined = " ".join(str(m.get("content") or "") for m in messages)
    assert ("history compressed" in joined) or ("truncated" in joined) or ("compacted" in joined)


@pytest.mark.asyncio
async def test_duplicate_read_file_uses_cache(monkeypatch):
    class _BudgetCheck:
        allowed = True
        events = []

    class _BudgetGuard:
        def check(self, **kwargs):
            return _BudgetCheck()

        def record_usage(self, record):
            return None

    dispatch_calls = []

    def fake_dispatch(name, args_json):
        dispatch_calls.append((name, args_json))
        return {"ok": True, "path": "a.py", "content": "hello " + ("z" * 100)}

    # 两轮：两次相同 read_file，然后 finish
    responses = [
        {
            "choices": [
                {
                    "message": {
                        "content": "",
                        "tool_calls": [
                            {
                                "id": "r1",
                                "function": {
                                    "name": "read_file",
                                    "arguments": json.dumps({"path": "a.py"}),
                                },
                            }
                        ],
                    },
                    "finish_reason": "tool_calls",
                }
            ],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        },
        {
            "choices": [
                {
                    "message": {
                        "content": "",
                        "tool_calls": [
                            {
                                "id": "r2",
                                "function": {
                                    "name": "read_file",
                                    "arguments": json.dumps({"path": "a.py"}),
                                },
                            }
                        ],
                    },
                    "finish_reason": "tool_calls",
                }
            ],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        },
        {
            "choices": [
                {
                    "message": {
                        "content": "",
                        "tool_calls": [
                            {
                                "id": "f1",
                                "function": {
                                    "name": "finish",
                                    "arguments": json.dumps({"summary": "ok"}),
                                },
                            }
                        ],
                    },
                    "finish_reason": "tool_calls",
                }
            ],
            "usage": {},
        },
    ]

    async def fake_chat_completion(self, *args, **kwargs):
        return responses.pop(0)

    events = []
    monkeypatch.setattr(tl, "get_budget_guard", lambda: _BudgetGuard())
    monkeypatch.setattr(tl.LLMClient, "chat_completion", fake_chat_completion)
    monkeypatch.setattr(tl, "dispatch_tool_call", fake_dispatch)
    # 确保 read_file 在 role 工具集里：直接放宽 tool_name_set 路径 —— dispatch 被 mock 时
    # 仍需 name in tool_name_set；用 developer role 通常含 read_file
    result = await tl.run_tool_loop(
        prompt="read twice",
        config=ProviderConfig(api_key="k", api_base_url="https://example.com/v1", model="m"),
        role="developer",
        system_prompt="sys",
        max_iterations=5,
        on_event=lambda kind, payload: events.append((kind, payload)),
    )
    assert result.ok is True
    # 相同 args 的 read_file 只真实 dispatch 一次
    read_dispatches = [c for c in dispatch_calls if c[0] == "read_file"]
    assert len(read_dispatches) == 1, dispatch_calls
    cached_events = [p for k, p in events if k == "tool_result" and p.get("cached")]
    assert len(cached_events) >= 1
    assert any(e.get("cached") for e in result.log if e.get("name") == "read_file")


@pytest.mark.asyncio
async def test_append_applies_tier_limit_on_write(monkeypatch):
    """写入 messages 时即按 tier 截断，而非等 compact。"""
    messages: list = []
    tool_log: list = []
    huge = {"ok": True, "path": "x.py", "blob": "Q" * 50_000}
    entry = tl._append_regular_tool_result(
        tool_call_id="t1",
        name="list_files",
        args_raw="{}",
        tool_result=huge,
        tool_log=tool_log,
        messages=messages,
    )
    assert entry["tier"] == "low"
    assert entry["truncated_chars"] > 0
    assert len(messages[0]["content"]) < 5_000
