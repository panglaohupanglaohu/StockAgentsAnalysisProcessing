# -*- coding: utf-8 -*-
from domain.information_sources.brief import build_run_brief


def test_ai60_brief_prefers_headline_not_process_noise():
    brief = build_run_brief(
        channel="ai_news_60s",
        report={
            "headline": "开源模型基准提升引发企业采用讨论",
            "bullets": [
                {"text": "实验室发布权重，基准提升。"},
                {"text": "正在清洗数据"},  # noise should be skipped if others exist
            ],
            "why_it_matters": [{"text": "采用成本与合规仍是障碍。"}],
            "risks_and_counterpoints": [{"text": "单一来源可能放大叙事。"}],
            "citations": [
                {"url": "https://a.example/x", "title": "a", "fetched_at": "t"},
                {"url": "https://b.example/y", "title": "b", "fetched_at": "t"},
            ],
            "analysis": {"topic_clusters": [{"name": "模型与开源", "share": 0.4}], "signal_strength": "中"},
        },
        document={
            "as_of": "2026-08-01T00:00:00+00:00",
            "evidence_ids": ["e1", "e2"],
            "document_id": "d1",
            "version": 3,
            "run_id": "r1",
        },
    )
    assert "开源模型" in brief["headline"]
    assert "正在清洗" not in brief["headline"]
    assert brief["focus_items"]
    assert brief["distinctive_insights"]
    assert len({x["title"] for x in brief["distinctive_insights"]}) == len(brief["distinctive_insights"])
    assert any("来源：" in x["body"] for x in brief["trending_news"])
    assert any("投资建议" in x for x in brief["evidence_limits"])
    assert brief["as_of"].startswith("2026")
    assert all(not b.startswith("http") for b in brief["bullets"])


def test_single_source_marks_inference_limit():
    brief = build_run_brief(
        channel="dufu_world_intel",
        report={
            "what_happened": {"text": "多边会谈取得阶段性进展"},
            "timeline": [{"text": "周一：声明发布"}],
            "drivers": [{"text": "政策协调"}],
            "citations": [{"url": "https://only.example/z", "title": "o", "fetched_at": "t"}],
        },
        document={"evidence_ids": ["e1"], "as_of": "2026-08-01T00:00:00+00:00"},
    )
    assert brief["headline"]
    assert any("独立来源不足" in x for x in brief["evidence_limits"])


def test_url_only_bullets_rewritten_from_citations_and_topics():
    """Real RSS often leaves claim text as URL — brief must not ship bare links."""
    brief = build_run_brief(
        channel="ai_news_60s",
        report={
            "headline": "AI 情报研判：企业落地成为主要信号",
            "bullets": [
                {"text": "https://www.v2ex.com/t/1231413#reply1", "label": "fact"},
                {"text": "https://36kr.com/p/foo", "label": "fact"},
            ],
            "why_it_matters": [],
            "citations": [
                {
                    "url": "https://www.v2ex.com/t/1231413#reply1",
                    "title": "某开源工具发布新版本",
                    "fetched_at": "2026-08-01T00:00:00+00:00",
                },
                {
                    "url": "https://36kr.com/p/foo",
                    "title": "企业 AI 落地案例观察",
                    "fetched_at": "2026-08-01T00:00:00+00:00",
                },
            ],
            "analysis": {
                "topic_clusters": [{"name": "企业落地", "share": 0.5, "count": 4}],
                "signal_strength": "中",
                "source_count": 2,
                "source_diversity": 2,
            },
        },
        document={"evidence_ids": ["e1", "e2"], "as_of": "2026-08-01T00:00:00+00:00"},
    )
    assert all("http" not in b for b in brief["bullets"])
    assert any("开源" in b or "企业" in b or "落地" in b or "主题" in b for b in brief["bullets"])
    assert all("http" not in (i.get("body") or "") for i in brief["trending_news"])
