# -*- coding: utf-8 -*-
"""T302–T406 — investment simulation, adapters, future-leakage, portfolio."""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from domain.information_sources.documents import DocumentStore, InformationDocument
from domain.investment_simulation.orchestrator import create_simulation, start_simulation
from domain.investment_simulation.portfolio import PaperPortfolio, apply_decision, parse_structured_decision
from domain.investment_simulation.store import SimulationStore
from integrations.tradingagents.config_mapper import map_agent_config, normalize_provider, validate_mapped_config
from integrations.tradingagents.context_provider import SourceContextProvider
from integrations.tradingagents.graph_adapter import StockAgentsTradingGraph


def test_provider_mapping_coverage():
    for p in (
        "openai",
        "openai-compatible",
        "anthropic",
        "google",
        "xai",
        "grok",
        "deepseek",
        "qwen",
        "ollama",
    ):
        assert normalize_provider(p)


def test_config_mapper_validate():
    cfg = map_agent_config(
        quick_model={"provider": "deepseek", "name": "deepseek-chat", "model_id": "q"},
        deep_model={"provider": "deepseek", "name": "deepseek-reasoner", "model_id": "d"},
        debate_rounds=2,
        risk_rounds=1,
    )
    assert cfg["max_debate_rounds"] == 2
    assert validate_mapped_config(cfg)["ok"] is True


def test_paper_portfolio_buy_sell_hold():
    pf = PaperPortfolio(cash=10_000)
    apply_decision(pf, {"action": "BUY", "ticker": "NVDA", "confidence": 0.8, "price": 100}, ts="t1")
    assert pf.positions.get("NVDA", 0) > 0
    apply_decision(pf, {"action": "SELL", "ticker": "NVDA", "confidence": 0.5, "price": 110}, ts="t2")
    apply_decision(pf, {"action": "HOLD", "ticker": "NVDA", "confidence": 0.5, "price": 110}, ts="t3")
    assert parse_structured_decision({"action": "WAIT"}).get("action") == "HOLD"
    d = pf.to_dict()
    assert d["broker"] is None
    assert "不构成投资建议" in d["disclaimer"] or "research" in d["disclaimer"].lower()


def test_context_no_future_docs(tmp_path: Path):
    docs = DocumentStore(tmp_path / "docs")
    docs.save(
        InformationDocument(
            document_id="past",
            channel="ai_news_60s",
            version=1,
            title="past",
            run_id="r1",
            as_of="2026-01-01T00:00:00+00:00",
            html="<p>past</p>",
            report={"headline": "past NVDA"},
            evidence_urls=["https://example.com/p"],
        )
    )
    docs.save(
        InformationDocument(
            document_id="future",
            channel="ai_news_60s",
            version=2,
            title="future",
            run_id="r2",
            as_of="2026-12-31T00:00:00+00:00",
            html="<p>future leak</p>",
            report={"headline": "future secret"},
            evidence_urls=["https://example.com/f"],
        )
    )
    ctx = SourceContextProvider(docs).for_ticker(ticker="NVDA", before="2026-06-01T00:00:00+00:00")
    ids = {d["document_id"] for d in ctx.docs}
    assert "past" in ids
    assert "future" not in ids
    prompt = ctx.to_prompt()
    assert "future secret" not in prompt


@pytest.mark.asyncio
async def test_fixture_graph_run():
    g = StockAgentsTradingGraph(force_fixture=True)
    result = await g.run(ticker="NVDA", trade_date="2026-07-01", mode="fixture")
    assert result.final_decision["action"] in ("BUY", "SELL", "HOLD")
    assert "market_analyst" in result.reports
    assert result.mode == "fixture"
    assert result.graph_shape


@pytest.mark.asyncio
async def test_simulation_e2e(tmp_path: Path, monkeypatch):
    store = SimulationStore(tmp_path / "sims")
    # Patch store singleton used by orchestrator
    import domain.investment_simulation.orchestrator as orch
    import domain.investment_simulation.store as store_mod

    monkeypatch.setattr(store_mod, "_store", store)
    monkeypatch.setattr(orch, "get_simulation_store", lambda: store)

    sim = await create_simulation(
        {
            "ticker": "NVDA",
            "trade_date": "2026-07-01",
            "sector": "ai_compute",
            "initial_cash": 50000,
            "mode": "fixture",
            "deep_model": {"provider": "deepseek", "name": "deepseek-reasoner"},
            "quick_model": {"provider": "deepseek", "name": "deepseek-chat"},
        },
        store=store,
    )
    assert sim.status == "queued"
    assert sim.sector == "ai_compute"
    assert "plaza_id" not in sim.to_dict()

    await start_simulation(sim.run_id, store=store)
    # Wait for background task
    for _ in range(100):
        cur = store.get(sim.run_id)
        if cur and cur.status in ("completed", "failed", "cancelled"):
            break
        await asyncio.sleep(0.05)
    cur = store.get(sim.run_id)
    assert cur is not None
    assert cur.status == "completed", cur.error
    events = store.list_events(sim.run_id)
    assert len(events) > 5
    pf = store.get_portfolio(sim.run_id)
    assert pf is not None
    reports = store.get_reports_index(sim.run_id)
    assert reports is not None


def test_ticker_validation():
    d = parse_structured_decision({"action": "BUY", "ticker": "aapl", "confidence": 1})
    assert d["ticker"] == "AAPL"
