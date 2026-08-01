# -*- coding: utf-8 -*-
"""P9 — run store, queue, worker, async API smoke."""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def run_env(tmp_path, monkeypatch):
    from domain.information_sources import run_queue as rq
    from domain.information_sources import run_store as rs
    from domain.information_sources import worker as w
    from domain.information_sources import documents as doc
    from domain.information_sources import evidence as ev
    from domain.information_sources import source_store as ss

    run_repo = rs.FileRunRepository(tmp_path / "runs")
    event_repo = rs.FileEventRepository(tmp_path / "runs")
    rs.reset_run_stores_for_tests(run_repo, event_repo)
    queue = rq.FileRunQueue(run_repo)
    rq.reset_run_queue_for_tests(queue)
    worker = w.InformationWorker(repo=run_repo, events=event_repo, queue=queue, poll_seconds=0.05)
    w.reset_worker_for_tests(worker)

    monkeypatch.setattr(ev, "_store", ev.EvidenceStore(tmp_path / "ev"))
    monkeypatch.setattr(doc, "_doc_store", doc.DocumentStore(tmp_path / "docs"))
    monkeypatch.setattr(ss, "_src_store", ss.SourceConfigStore(tmp_path / "sources.json"))

    yield {"run_repo": run_repo, "event_repo": event_repo, "queue": queue, "worker": worker}

    # best-effort stop if a loop started the worker during the test
    if worker._task is not None:
        worker._stopping = True
        worker._task.cancel()
    w.reset_worker_for_tests(None)
    rs.reset_run_stores_for_tests(None, None)
    rq.reset_run_queue_for_tests(None)


def test_compile_twenty_cards_complete():
    from domain.information_sources.run_store import REQUIRED_CARD_IDS, compile_twenty_cards

    cards = compile_twenty_cards(
        team_id="ai_news_60s",
        report={"headline": "测试标题", "analysis": {"topic_clusters": [{"name": "模型与开源", "count": 2}], "evidence_score": 0.5, "signal_strength": "中"}},
        evidence_ids=["e1", "e2"],
        as_of="2026-08-01T00:00:00+00:00",
    )
    assert {c.card_id for c in cards} == set(REQUIRED_CARD_IDS)
    assert all(c.status in {"observed", "inferred", "gap"} for c in cards)
    # No fabricated revenue card as observed without data
    proxy = next(c for c in cards if c.card_id == "adoption-cost-proxy")
    assert proxy.status == "gap"


def test_idempotent_enqueue(run_env):
    from domain.information_sources.run_service import create_and_enqueue_run

    a = create_and_enqueue_run(
        team_id="ai_news_60s",
        source_ids=[],
        trigger="schedule",
        schedule_id="sch1",
        idempotency_key="sch1:bucket",
    )
    b = create_and_enqueue_run(
        team_id="ai_news_60s",
        source_ids=[],
        trigger="schedule",
        schedule_id="sch1",
        idempotency_key="sch1:bucket",
    )
    assert a.run_id == b.run_id


@pytest.mark.asyncio
async def test_worker_completes_fixture_run(run_env):
    from domain.information_sources.run_service import enqueue_run_async, wait_for_run

    run = await enqueue_run_async(team_id="ai_news_60s", source_ids=[], trigger="manual")
    finished = await wait_for_run(run.run_id, timeout=60.0, poll=0.1)
    assert finished.status in ("completed", "degraded")
    assert finished.result.get("channel") == "ai_news_60s"
    assert len(finished.cards) == 20
    events = run_env["event_repo"].list_after(run.run_id, 0)
    assert events
    assert any(e.status == "started" for e in events)


def test_async_api_202_and_poll(run_env):
    from domain.api_routes import router

    app = FastAPI()
    app.include_router(router)
    with TestClient(app) as client:
        r = client.post(
            "/api/v1/information-runs",
            json={"team_id": "ai_news_60s", "source_ids": []},
        )
        assert r.status_code == 202
        run_id = r.json()["run_id"]
        # wait path
        r2 = client.post(
            "/api/v1/information-runs",
            json={"team_id": "ai_news_60s", "source_ids": [], "wait": True, "wait_timeout_seconds": 60},
        )
        assert r2.status_code == 200
        body = r2.json()
        assert body["status"] in ("completed", "degraded", "failed", "queued", "fetching", "analyzing", "publishing", "rendering")
        # poll first run
        import time

        deadline = time.time() + 60
        final = None
        while time.time() < deadline:
            g = client.get(f"/api/v1/information-runs/{run_id}")
            assert g.status_code == 200
            final = g.json()
            if final["status"] in ("completed", "degraded", "failed"):
                break
            time.sleep(0.2)
        assert final is not None
        assert final["status"] in ("completed", "degraded", "failed")
        ev = client.get(f"/api/v1/information-runs/{run_id}/events")
        assert ev.status_code == 200
        assert "events" in ev.json()


def test_team_run_default_async(run_env):
    from domain.api_routes import router

    app = FastAPI()
    app.include_router(router)
    with TestClient(app) as client:
        r = client.post(
            "/api/v1/information-sources/teams/ai_news_60s/run",
            json={"source_ids": []},
        )
        assert r.status_code == 202
        assert r.json()["async"] is True
        r2 = client.post(
            "/api/v1/information-sources/teams/ai_news_60s/run",
            json={"source_ids": [], "wait": True, "wait_timeout_seconds": 60},
        )
        assert r2.status_code == 200
        assert r2.json().get("channel") == "ai_news_60s" or r2.json().get("status") in (
            "completed",
            "degraded",
        )
