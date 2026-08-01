# -*- coding: utf-8 -*-
"""P8 Engine Live Cockpit — assembly, structured events, SSE, snapshots."""

from __future__ import annotations

import asyncio
import time
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def client(monkeypatch, tmp_path):
    from domain.api_routes import router as domain_router
    from domain.information_sources import documents as doc
    from domain.information_sources import evidence as ev
    from domain.information_sources import source_store as ss
    from domain.investment_simulation import store as simstore
    import domain.investment_simulation.orchestrator as orch

    monkeypatch.setattr(ev, "_store", ev.EvidenceStore(tmp_path / "ev"))
    monkeypatch.setattr(doc, "_doc_store", doc.DocumentStore(tmp_path / "docs"))
    monkeypatch.setattr(ss, "_src_store", ss.SourceConfigStore(tmp_path / "sources.json"))
    store = simstore.SimulationStore(tmp_path / "sims")
    monkeypatch.setattr(simstore, "_store", store)
    monkeypatch.setattr(orch, "get_simulation_store", lambda: store)

    app = FastAPI()
    app.include_router(domain_router)
    with TestClient(app) as c:
        yield c


def test_compile_assembly_team_and_source():
    from domain.investment_simulation.assembly import compile_assembly

    plan = compile_assembly(
        [
            {"module_id": "team:ai_news_60s", "kind": "team", "priority": 1, "name": "AI60"},
            {"module_id": "src-1", "kind": "source", "priority": 2},
            {"module_id": "team:ai_news_60s", "kind": "team", "priority": 3},  # dedupe channel
        ],
        ticker="NVDA",
        cutoff="2026-07-01",
    )
    assert plan.channels == ["ai_news_60s"]
    assert plan.source_ids == ["src-1"]
    assert plan.module_order[0] == "team:ai_news_60s"
    assert plan.snapshot_hash


def test_compile_drops_future_document():
    from domain.investment_simulation.assembly import compile_assembly

    plan = compile_assembly(
        [
            {
                "module_id": "doc-future",
                "kind": "document",
                "priority": 1,
                "config": {"as_of": "2026-12-31T00:00:00+00:00"},
            },
            {
                "module_id": "doc-past",
                "kind": "document",
                "priority": 2,
                "config": {"as_of": "2026-01-01T00:00:00+00:00"},
            },
        ],
        ticker="NVDA",
        cutoff="2026-06-01T00:00:00+00:00",
        known_document_as_of={
            "doc-future": "2026-12-31T00:00:00+00:00",
            "doc-past": "2026-01-01T00:00:00+00:00",
        },
    )
    assert "doc-future" not in plan.document_ids
    assert "doc-past" in plan.document_ids
    assert plan.warnings


def test_fixture_graph_has_context_and_structured():
    async def _run():
        from integrations.tradingagents.graph_adapter import StockAgentsTradingGraph

        g = StockAgentsTradingGraph(force_fixture=True)
        result = await g.run(
            ticker="NVDA",
            trade_date="2026-07-01",
            mode="fixture",
        )
        phases = {e.phase for e in result.events}
        assert "context" in phases
        assert "analysis" in phases
        assert "planning" in phases or "debate" in phases
        assert "risk" in phases
        assert "portfolio" in phases or "decision" in phases
        assert "reflection" in phases
        structured_events = [e for e in result.events if e.structured]
        assert len(structured_events) >= 5
        return result

    asyncio.get_event_loop().run_until_complete(_run()) if False else None
    # pytest-asyncio style:
    # use sync helper
    import asyncio as aio

    result = aio.run(_run())
    assert result.final_decision.get("action")


def test_create_with_assembly_snapshot(client):
    r = client.post(
        "/api/v1/investment-simulations",
        json={
            "ticker": "NVDA",
            "trade_date": "2026-07-01",
            "mode": "fixture",
            "initial_cash": 20000,
            "assembly": [
                {
                    "module_id": "team:ai_news_60s",
                    "kind": "team",
                    "name": "AI60",
                    "priority": 1,
                },
                {
                    "module_id": "team:dufu_world_intel",
                    "kind": "team",
                    "name": "Dufu",
                    "priority": 2,
                },
            ],
            "deep_model": {"provider": "deepseek", "name": "x"},
            "quick_model": {"provider": "deepseek", "name": "y"},
        },
    )
    assert r.status_code == 200, r.text
    body = r.json()
    snap = body.get("assembly_snapshot") or {}
    assert snap.get("immutable") is True
    assert "ai_news_60s" in (snap.get("channels") or [])
    assert snap.get("snapshot_hash")
    assert body.get("engine_config_snapshot")


def test_auto_start_and_structured_events(client):
    r = client.post(
        "/api/v1/investment-simulations",
        json={
            "ticker": "NVDA",
            "trade_date": "2026-07-01",
            "mode": "fixture",
            "auto_start": True,
            "assembly": [
                {"module_id": "team:ai_news_60s", "kind": "team", "priority": 1}
            ],
            "deep_model": {"provider": "deepseek", "name": "x"},
            "quick_model": {"provider": "deepseek", "name": "y"},
        },
    )
    assert r.status_code == 200
    run_id = r.json()["run_id"]
    assert r.json()["status"] in ("running", "queued", "completed")

    for _ in range(120):
        g = client.get(f"/api/v1/investment-simulations/{run_id}")
        if g.json().get("status") in ("completed", "failed", "cancelled"):
            break
        time.sleep(0.05)
    g = client.get(f"/api/v1/investment-simulations/{run_id}")
    assert g.json()["status"] == "completed", g.json()
    # Snapshot immutability: still present after run
    assert g.json().get("assembly_snapshot", {}).get("immutable") is True

    ev = client.get(f"/api/v1/investment-simulations/{run_id}/events")
    events = ev.json()["events"]
    assert len(events) >= 10
    phases = {e["phase"] for e in events}
    assert "context" in phases
    assert any(e.get("structured") for e in events)

    # SSE endpoint exists and yields data
    with client.stream(
        "GET",
        f"/api/v1/investment-simulations/{run_id}/events/stream?after_seq=0",
    ) as resp:
        assert resp.status_code == 200
        # read a few lines
        chunks = []
        for line in resp.iter_lines():
            if line:
                chunks.append(line)
            if len(chunks) >= 3:
                break
        assert chunks


def test_assembly_not_mutated_by_later_draft(client):
    r = client.post(
        "/api/v1/investment-simulations",
        json={
            "ticker": "AAPL",
            "trade_date": "2026-07-01",
            "mode": "fixture",
            "assembly": [
                {"module_id": "team:ai_news_60s", "kind": "team", "priority": 1}
            ],
            "deep_model": {"provider": "deepseek", "name": "x"},
            "quick_model": {"provider": "deepseek", "name": "y"},
        },
    )
    run_id = r.json()["run_id"]
    original_hash = r.json()["assembly_snapshot"]["snapshot_hash"]
    # Re-fetch after time — snapshot must match
    g = client.get(f"/api/v1/investment-simulations/{run_id}")
    assert g.json()["assembly_snapshot"]["snapshot_hash"] == original_hash
