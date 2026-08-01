# -*- coding: utf-8 -*-
"""T601/T602/T605 — domain API smoke + security rejects.

Uses a minimal FastAPI app with only the StockAgents domain router to avoid
full main.py channel registry re-registration and auth middleware noise.
"""

from __future__ import annotations

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
    from domain.information_sources import scheduler as scheduler_module

    monkeypatch.setattr(ev, "_store", ev.EvidenceStore(tmp_path / "ev"))
    monkeypatch.setattr(doc, "_doc_store", doc.DocumentStore(tmp_path / "docs"))
    monkeypatch.setattr(ss, "_src_store", ss.SourceConfigStore(tmp_path / "sources.json"))
    monkeypatch.setattr(simstore, "_store", simstore.SimulationStore(tmp_path / "sims"))
    monkeypatch.setattr(
        scheduler_module,
        "_scheduler",
        scheduler_module.InformationScheduler(scheduler_module.ScheduleStore(tmp_path / "schedules.json")),
    )

    # orchestrator uses get_simulation_store singleton
    import domain.investment_simulation.orchestrator as orch

    monkeypatch.setattr(orch, "get_simulation_store", lambda: simstore._store)

    app = FastAPI()
    app.include_router(domain_router)
    with TestClient(app) as c:
        yield c


def test_trading_runtime_health(client):
    r = client.get("/api/v1/trading-runtime/health")
    assert r.status_code == 200
    body = r.json()
    assert "layer" in body
    assert body.get("auto_upgrade") is False


def test_config_schema_and_validate(client):
    r = client.get("/api/v1/trading-runtime/config-schema")
    assert r.status_code == 200
    body = r.json()
    assert "properties" in body
    r2 = client.post(
        "/api/v1/trading-runtime/config/validate",
        json={
            "deep_model": {"provider": "openai", "name": "gpt-4o"},
            "quick_model": {"provider": "openai", "name": "gpt-4o-mini"},
            "debate_rounds": 1,
        },
    )
    assert r2.status_code == 200
    assert r2.json()["ok"] is True


def test_source_secret_refs_must_be_env(client):
    r = client.post(
        "/api/v1/information-sources",
        json={
            "kind": "fixture",
            "name": "bad-secret",
            "secret_refs": {"token": "sk-live-not-allowed"},
            "options": {"items": []},
        },
    )
    assert r.status_code == 400


def test_source_fixture_and_team_run(client):
    r = client.post(
        "/api/v1/information-sources",
        json={
            "kind": "fixture",
            "name": "demo",
            "options": {
                "items": [
                    {
                        "title": "t",
                        "url": "https://example.com/t",
                        "content": "c",
                    }
                ]
            },
        },
    )
    assert r.status_code == 200
    sid = r.json()["source_id"]
    t = client.post(f"/api/v1/information-sources/{sid}/test")
    assert t.status_code == 200
    assert t.json()["ok"] is True

    saved = client.patch(f"/api/v1/information-sources/{sid}", json={"enabled": False})
    assert saved.status_code == 200
    assert saved.json()["enabled"] is False
    persisted = client.get(f"/api/v1/information-sources/{sid}")
    assert persisted.status_code == 200
    assert persisted.json()["enabled"] is False

    # P9: default is async 202; wait=true keeps fixture E2E deterministic
    run = client.post(
        "/api/v1/information-sources/teams/ai_news_60s/run",
        json={"wait": True, "wait_timeout_seconds": 90},
    )
    assert run.status_code == 200
    assert run.json()["document_id"]

    latest = client.get("/api/v1/information-documents/latest/ai_news_60s")
    assert latest.status_code == 200
    assert latest.json()["html"]
    doc = latest.json()
    metadata = client.get(
        f"/api/v1/information-documents/{doc['document_id']}/versions/{doc['version']}?include_html=false"
    )
    assert metadata.status_code == 200
    assert "html" not in metadata.json()
    assert metadata.json()["render_contract"]["stable_card_anchors"] is True
    rendered = client.get(
        f"/api/v1/information-documents/{doc['document_id']}/versions/{doc['version']}/render"
    )
    assert rendered.status_code == 200
    assert rendered.headers["content-type"].startswith("text/html")
    assert "frame-ancestors 'self'" in rendered.headers["content-security-policy"]
    assert "X-Content-Type-Options" in rendered.headers
    assert "data-card-id='cover'" in rendered.text
    assert "target='_blank'" in rendered.text
    missing = client.get("/api/v1/information-documents/missing/versions/1/render")
    assert missing.status_code == 404


def test_directory_import_preview_and_explicit_commit(client, monkeypatch):
    from domain.information_sources import directory_parser

    async def fake_preview(url, max_items=200, check_health=False):
        return {
            "directory_url": url,
            "count": 1,
            "candidates": [
                {
                    "name": "Example feed",
                    "url": "https://feed.example/rss.xml",
                    "kind": "rss",
                    "status": "ok",
                    "source_id": "rss-example",
                }
            ],
        }

    monkeypatch.setattr(directory_parser, "preview_directory", fake_preview)
    preview = client.post(
        "/api/v1/information-sources/import-directory/preview",
        json={"url": "https://directory.example/readme", "check_health": True},
    )
    assert preview.status_code == 200
    assert preview.json()["count"] == 1

    payload = {
        "directory_url": "https://directory.example/readme",
        "profile": "both",
        "items": preview.json()["candidates"],
    }
    committed = client.post("/api/v1/information-sources/import-directory/commit", json=payload)
    assert committed.status_code == 200
    assert committed.json()["count"] == 1
    duplicate = client.post("/api/v1/information-sources/import-directory/commit", json=payload)
    assert duplicate.status_code == 200
    assert len(duplicate.json()["skipped"]) == 1

    blocked = client.post(
        "/api/v1/information-sources/import-directory/commit",
        json={"items": [{"name": "private", "url": "http://127.0.0.1/feed"}]},
    )
    assert blocked.status_code == 200
    assert blocked.json()["errors"]


def test_information_schedule_crud(client):
    bad = client.post(
        "/api/v1/information-schedules",
        json={"name": "bad", "team_id": "build_system", "interval_minutes": 10},
    )
    assert bad.status_code == 400

    created = client.post(
        "/api/v1/information-schedules",
        json={"name": "AI 每小时", "team_id": "ai_news_60s", "interval_minutes": 60},
    )
    assert created.status_code == 200
    schedule_id = created.json()["schedule_id"]
    assert created.json()["next_run_at"]

    listed = client.get("/api/v1/information-schedules")
    assert listed.status_code == 200
    assert listed.json()["schedules"][0]["schedule_id"] == schedule_id

    patched = client.patch(
        f"/api/v1/information-schedules/{schedule_id}",
        json={"enabled": False, "interval_minutes": 30},
    )
    assert patched.status_code == 200
    assert patched.json()["enabled"] is False

    deleted = client.delete(f"/api/v1/information-schedules/{schedule_id}")
    assert deleted.status_code == 200
    assert client.get("/api/v1/information-schedules").json()["schedules"] == []


def test_investment_sim_flow(client):
    r = client.post(
        "/api/v1/investment-simulations",
        json={
            "ticker": "NVDA",
            "trade_date": "2026-07-01",
            "mode": "fixture",
            "initial_cash": 10000,
            "deep_model": {"provider": "deepseek", "name": "x"},
            "quick_model": {"provider": "deepseek", "name": "y"},
        },
    )
    assert r.status_code == 200
    run_id = r.json()["run_id"]
    assert "plaza" not in r.json()

    bad = client.post(
        "/api/v1/investment-simulations",
        json={"ticker": "../etc/passwd", "trade_date": "2026-07-01"},
    )
    assert bad.status_code == 400

    s = client.post(f"/api/v1/investment-simulations/{run_id}/start")
    assert s.status_code == 200

    for _ in range(100):
        g = client.get(f"/api/v1/investment-simulations/{run_id}")
        if g.json().get("status") in ("completed", "failed", "cancelled"):
            break
        time.sleep(0.05)
    g = client.get(f"/api/v1/investment-simulations/{run_id}")
    assert g.json()["status"] == "completed", g.json()
    ev = client.get(f"/api/v1/investment-simulations/{run_id}/events")
    assert len(ev.json()["events"]) > 0
    pf = client.get(f"/api/v1/investment-simulations/{run_id}/portfolio")
    assert pf.status_code == 200
    reports = client.get(f"/api/v1/investment-simulations/{run_id}/reports")
    assert reports.status_code == 200


def test_ssrf_blocked_on_assert():
    from domain.information_sources.ssrf import SSRFBlockedError, assert_url_safe

    with pytest.raises(SSRFBlockedError):
        assert_url_safe("http://127.0.0.1/x", resolve_dns=False)


def test_new_pages_exist():
    root = Path(__file__).resolve().parents[3]
    assert (root / "src/frontend/data-intelligence.html").is_file()
    assert (root / "src/frontend/investment-engine.html").is_file()
    assert not (root / "src/frontend/sources.html").exists()
    assert not (root / "src/frontend/ai-brief.html").exists()
    assert not (root / "src/frontend/world-trends.html").exists()


def test_nav_appends_two_entries_only():
    nav = (Path(__file__).resolve().parents[3] / "src/frontend/js/nav.js").read_text(
        encoding="utf-8"
    )
    assert "data-intelligence.html" in nav
    assert "investment-engine.html" in nav
    assert "智能体团队" in nav
    assert "议事广场" in nav
