# -*- coding: utf-8 -*-
"""T203–T207 — evidence, report schema, hugohe3, team DAGs."""

from __future__ import annotations

from pathlib import Path

import pytest

from domain.information_sources.documents import DocumentStore
from domain.information_sources.evidence import EvidenceStore
from domain.information_sources.hugohe3 import hugohe3_render
from domain.information_sources.pipelines import (
    run_ai_news_60s_pipeline,
    run_dufu_world_intel_pipeline,
)
from domain.information_sources.report_schemas import validate_report


@pytest.fixture
def tmp_stores(tmp_path: Path):
    return {
        "evidence": EvidenceStore(tmp_path / "evidence"),
        "docs": DocumentStore(tmp_path / "docs"),
    }


@pytest.mark.asyncio
async def test_ai60_pipeline_fixture_produces_versioned_html(tmp_stores):
    result = await run_ai_news_60s_pipeline(
        evidence_store=tmp_stores["evidence"],
        document_store=tmp_stores["docs"],
    )
    assert result["channel"] == "ai_news_60s"
    assert result["version"] >= 1
    doc = tmp_stores["docs"].get_latest("ai_news_60s")
    assert doc is not None
    assert doc.html
    assert "非投资建议" in doc.html or "不构成投资建议" in doc.html
    assert "signal-map" in doc.html
    assert "seconds-strip" in doc.html
    assert "analysis-dashboard" in doc.html
    assert "analysis-progress-track" in doc.html
    assert "analysis-overview" in doc.html
    assert "高分信号排行" in doc.html
    assert "Agent 阶段流程" not in doc.html
    assert "判断路径" in doc.html
    assert "业务影响传导" in doc.html
    assert "待验证问题清单" in doc.html
    assert "research-deck" in doc.html
    assert "20 CARD RESEARCH DECK" in doc.html
    assert "background:#0d141e" in doc.html
    assert "border-color:#304255" in doc.html
    for card_id in (
        "cover",
        "editor-note",
        "executive-summary",
        "signal-landscape",
        "evidence-pulse",
        "two-state-gap",
        "confidence-bubble",
        "evidence-donut",
        "top-three",
        "source-ranking",
        "dual-track",
        "second-tier",
        "focal-signal",
        "flow-map",
        "pareto",
        "evidence-hub",
        "uncertainty",
        "adoption-cost-proxy",
        "risk-quadrant",
        "closing",
    ):
        assert f"data-card-id='{card_id}'" in doc.html
    assert "grid-template-columns:minmax(0,1.15fr) minmax(280px,.85fr)" in doc.html
    assert "@media (max-width:820px)" in doc.html
    assert doc.report["analysis"]["topic_clusters"]
    assert doc.report["analysis"]["source_breakdown"]
    assert doc.report["analysis"]["score_distribution"]
    assert doc.report["analysis"]["reasoning_steps"]
    assert doc.report["analysis"]["deck_contract_version"] == "ai-capital-overview-deck/v1"
    assert "risk_matrix" in doc.report["analysis"]
    assert "relationship_edges" in doc.report["analysis"]
    assert any(step.get("summary") for step in result["steps"])
    assert doc.run_id == result["run_id"]
    assert doc.evidence_ids
    assert doc.content_hashes


@pytest.mark.asyncio
async def test_ai60_pipeline_reuses_own_cached_evidence_after_dedupe(tmp_stores):
    """A second unchanged RSS/fixture pass keeps the report data-rich."""
    await run_ai_news_60s_pipeline(
        evidence_store=tmp_stores["evidence"],
        document_store=tmp_stores["docs"],
    )
    second = await run_ai_news_60s_pipeline(
        evidence_store=tmp_stores["evidence"],
        document_store=tmp_stores["docs"],
    )
    doc = tmp_stores["docs"].get_latest("ai_news_60s")
    assert doc is not None
    assert second["evidence_count"] >= 3
    scout = next(step for step in second["steps"] if step["step"] == "scout_normalize")
    assert scout["fresh_evidence"] == 0
    assert scout["cached_evidence"] >= 3
    assert doc.report["analysis"]["source_count"] >= 3


@pytest.mark.asyncio
async def test_dufu_pipeline_fixture(tmp_stores):
    result = await run_dufu_world_intel_pipeline(
        evidence_store=tmp_stores["evidence"],
        document_store=tmp_stores["docs"],
    )
    assert result["channel"] == "dufu_world_intel"
    doc = tmp_stores["docs"].get_latest("dufu_world_intel")
    assert doc is not None
    assert "optimistic" in doc.html or "情景" in doc.html
    assert "独夫之心 · 世界趋势研判" in doc.html
    assert "data-card-id='risk-quadrant'" in doc.html
    report = validate_report("dufu_world_intel", doc.report)
    assert len(report.scenarios) == 3
    assert report.analysis["deck_contract_version"] == "ai-capital-overview-deck/v1"


@pytest.mark.asyncio
async def test_ai60_pipeline_summarizes_html_feed_content(tmp_stores):
    from domain.information_sources.models import SourceConfig

    source = SourceConfig(
        source_id="html-feed",
        kind="fixture",
        name="HTML feed",
        options={
            "items": [
                {
                    "title": "企业 AI 更新",
                    "url": "https://example.com/html-feed",
                    "content": "<p><strong>作者</strong>：测试</p>" + (" 长文" * 300),
                }
            ]
        },
    )
    await run_ai_news_60s_pipeline(
        sources=[source], evidence_store=tmp_stores["evidence"], document_store=tmp_stores["docs"]
    )
    doc = tmp_stores["docs"].get_latest("ai_news_60s")
    assert doc is not None
    bullet = doc.report["bullets"][0]["text"]
    assert "<p>" not in bullet
    assert len(bullet) <= 260


def test_hugohe3_rejects_script_injection():
    from domain.information_sources.hugohe3 import validate_csp_html
    import pytest

    with pytest.raises(ValueError):
        validate_csp_html('<div><script>alert(1)</script></div>')


def test_report_requires_uncertainty_and_citations():
    with pytest.raises(Exception):
        validate_report(
            "ai_news_60s",
            {
                "headline": "x",
                "bullets": [],
                "why_it_matters": [],
                "risks_and_counterpoints": [],
                "citations": [],
                "data_cutoff": "2026-01-01",
                "run_id": "r1",
            },
        )


def test_ai60_report_accepts_empty_evidence_text():
    """Real sources can return blank title/summary/content — must not 500 on schema."""
    from domain.information_sources.evidence import EvidenceRecord
    from domain.information_sources.pipelines import build_ai60_report, build_dufu_report

    blank = EvidenceRecord(
        evidence_id="e-blank",
        source_id="rss-1",
        run_id="run-blank",
        url="https://example.com/blank",
        title="",
        content="",
        summary="",
        content_hash="b" * 64,
        fetched_at="2026-07-31T12:00:00+00:00",
    )
    ai60 = build_ai60_report([blank], "run-blank", "2026-07-31T12:00:00+00:00")
    report = validate_report("ai_news_60s", ai60)
    assert report.bullets
    assert all(b.text.strip() for b in report.bullets)

    dufu = build_dufu_report([blank], "run-blank", "2026-07-31T12:00:00+00:00")
    world = validate_report("dufu_world_intel", dufu)
    assert world.what_happened.text.strip()
    assert all(item.text.strip() for item in world.timeline)


def test_ai60_quiet_run_renders_research_gaps_instead_of_dividing_by_zero():
    """A fully deduplicated scheduler run must still publish a useful report."""
    from domain.information_sources.pipelines import build_ai60_report

    report = validate_report(
        "ai_news_60s",
        build_ai60_report([], "run-quiet", "2026-08-01T00:00:00+00:00"),
    )
    rendered = hugohe3_render(report)
    assert "research-deck" in rendered
    assert "研究缺口" in rendered
    assert "data-card-id='closing'" in rendered


def test_every_research_card_leads_with_conclusion_tuple():
    from domain.information_sources.pipelines import build_ai60_report

    report = validate_report("ai_news_60s", build_ai60_report([], "run-conclusion", "2026-08-01T00:00:00+00:00"))
    rendered = hugohe3_render(report)
    assert rendered.count("class='card-conclusion'") == 20
    for label in ("时间", "地点", "对象", "事件", "结果", "影响", "行动"):
        assert rendered.count(f">{label}</span>") == 20


def test_ai60_bullets_extract_brief_not_html_body():
    from domain.information_sources.evidence import EvidenceRecord
    from domain.information_sources.pipelines import build_ai60_report

    body = (
        "<p><strong>作者 |&nbsp;</strong>谢芸子 黄绎达</p>"
        "<p><strong>编辑 |</strong>&nbsp;张帆</p>"
        "<p>开云的转型初见成效。</p>"
        "<p>7月28日，法国开云集团Kering发布2026年上半年财报，实现营收72.2亿欧元，"
        "可比口径下同比增长1%。</p>"
        "<p>更关键的信号藏在第二季度——单季营收36.52亿欧元，同比增长2%。"
        "在中东局势仍不明朗、全球消费进入下行周期的情况下，开云实现三年来的首次单季度正增长。</p>"
    )
    rec = EvidenceRecord(
        evidence_id="e-kering",
        source_id="rss-36kr",
        run_id="run-k",
        url="https://example.com/kering",
        title="开云集团上半年营收72.2亿欧元 二季度实现三年来首次单季正增长",
        content=body,
        summary=body,
        content_hash="c" * 64,
        fetched_at="2026-07-31T12:00:00+00:00",
    )
    report = validate_report(
        "ai_news_60s",
        build_ai60_report([rec], "run-k", "2026-07-31T12:00:00+00:00"),
    )
    bullet = report.bullets[0].text
    assert "<p>" not in bullet
    assert "作者" not in bullet and "编辑" not in bullet
    assert "开云" in bullet
    assert len(bullet) <= 130
    assert "中东局势" not in bullet


def test_ai60_url_only_feed_item_is_not_presented_as_fact():
    from domain.information_sources.evidence import EvidenceRecord
    from domain.information_sources.pipelines import build_ai60_report

    url = "https://www.v2ex.com/t/1231413#reply1"
    rec = EvidenceRecord(
        evidence_id="e-url-only",
        source_id="rss-v2ex",
        run_id="run-url-only",
        url=url,
        title=url,
        content="",
        summary="",
        content_hash="u" * 64,
        fetched_at="2026-08-01T05:00:00+00:00",
    )
    report = validate_report("ai_news_60s", build_ai60_report([rec], "run-url-only", "2026-08-01T05:00:00+00:00"))
    bullet = report.bullets[0]
    assert url not in bullet.text
    assert bullet.label.value == "inference"
    assert "缺少可读标题" in bullet.text
    assert "不能形成事实判断" in bullet.uncertainty
    html = hugohe3_render(report)
    assert "来源条目缺少可读标题或摘要（仅有链接，无法形成判断）" in html


def test_ai60_question_title_cannot_be_top_signal():
    from domain.information_sources.evidence import EvidenceRecord
    from domain.information_sources.pipelines import build_ai60_report

    def rec(eid, title, content):
        return EvidenceRecord(evidence_id=eid, source_id="rss", run_id="run-q", url=f"https://example.com/{eid}", title=title, content=content, summary=content, content_hash=eid * 64, fetched_at="2026-08-01T05:00:00+00:00")

    question = rec("q", "历史上有没有出现过位于岛屿上的内陆国？", "网友讨论这个问题，暂无可核实数据。")
    fact = rec("f", "Open source model release improves inference efficiency", "A published release reports a measured reduction in inference cost.")
    report = validate_report("ai_news_60s", build_ai60_report([question, fact], "run-q", "2026-08-01T05:00:00+00:00"))
    top = report.analysis.get("top_signals") or []
    assert top and top[0]["title"] != question.title
    assert all("有没有" not in item["title"] for item in top)


def test_world_cover_skips_url_only_row_when_selecting_event_title():
    from domain.information_sources.evidence import EvidenceRecord
    from domain.information_sources.pipelines import build_dufu_report

    def rec(eid, title, content):
        return EvidenceRecord(evidence_id=eid, source_id="rss", run_id="run-world-title", url=f"https://example.com/{eid}", title=title, content=content, summary=content, content_hash=eid * 64, fetched_at="2026-08-01T05:00:00+00:00")

    report = build_dufu_report([
        rec("url", "https://example.com/thread", ""),
        rec("event", "马斯克对特斯拉剥离的表态影响能源与航运成本", "马斯克与特斯拉的公开表态引发成本传导讨论。"),
    ], "run-world-title", "2026-08-01T05:00:00+00:00")
    assert "马斯克" in report["what_happened"]["text"]
    assert "来源条目缺少可读标题" not in report["what_happened"]["text"]


@pytest.mark.asyncio
async def test_evidence_dedupe(tmp_stores):
    from domain.information_sources.models import FetchBatch, FetchItem, SourceConfig

    store = tmp_stores["evidence"]
    cfg = SourceConfig(source_id="s1", kind="fixture", name="s1")
    item = FetchItem(title="t", url="https://example.com/a", content="body")
    batch = FetchBatch(source_id="s1", items=[item, item])
    r1 = store.normalize_and_store(batch, cfg, run_id="run1")
    assert r1.duplicates_skipped == 1
    assert len(r1.records) == 1
    r2 = store.normalize_and_store(batch, cfg, run_id="run2")
    assert len(r2.records) == 0
    assert r2.duplicates_skipped == 2
