# -*- coding: utf-8 -*-
"""T003 — Lock the active teams and 7 legacy business pages.

The product exposes exactly four teams: Build System, AI Coding, 60-second AI
news, and Dufu world intelligence. Any other historical team record is pruned
at startup. Removing one of the active teams, unmounting Plaza, or deleting a
legacy page surface must fail CI immediately.
"""

from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
FRONTEND = ROOT / "src" / "frontend"
BACKEND = ROOT / "src" / "backend"

LEGACY_PAGES = [
    "agent-team-config.html",
    "plaza.html",
    "skill-extract.html",
    "agent-memory.html",
    "Agent-digital-twin.html",
    "cost-dashboard.html",
    "pet-config.html",
]

LEGACY_ROUTES = {
    "agent-team-config": "/agent-team-config.html",
    "plaza": "/plaza.html",
    "skill-extract": "/skill-extract.html",
    "agent-memory": "/agent-memory.html",
    "digital-twin-office": "/Agent-digital-twin.html",
    "cost-dashboard": "/cost-dashboard.html",
    "pet-config": "/pet-config.html",
}


def test_build_system_team_has_agents():
    from agents.teams.build_team import create_build_team

    team = create_build_team()
    assert team.team_id == "build_system"
    assert team.agents
    assert len(team.agents) >= 1


def test_ai_coding_team_has_agents():
    from agents.teams.ai_coding_team import create_ai_coding_team

    team = create_ai_coding_team()
    assert team.team_id == "ai_coding"
    assert team.agents
    assert len(team.agents) >= 1


def test_active_team_policy_prunes_historical_teams():
    from agents.team_policy import ACTIVE_TEAM_IDS, prune_teams

    kept, removed = prune_teams(
        {team_id: object() for team_id in (
            "build_system",
            "ai_coding",
            "ai_news_60s",
            "dufu_world_intel",
            "energy_first_principle",
            "d083a568",
            "cloud-ops-team",
            "aws-ops",
            "pet_squad",
        )}
    )
    assert set(kept) == set(ACTIVE_TEAM_IDS)
    assert removed == ("aws-ops", "cloud-ops-team", "d083a568", "energy_first_principle", "pet_squad")


def test_runtime_team_storage_contains_only_active_teams():
    import json

    storage = ROOT / "storage" / "teams" / "teams.json"
    if not storage.exists():
        pytest.skip("runtime team storage is created on first startup")
    payload = json.loads(storage.read_text(encoding="utf-8"))
    assert set(payload) == {
        "build_system",
        "ai_coding",
        "ai_news_60s",
        "dufu_world_intel",
    }


def test_all_legacy_pages_exist_on_disk():
    for name in LEGACY_PAGES:
        path = FRONTEND / name
        assert path.is_file(), f"Legacy page missing: {name}"
        text = path.read_text(encoding="utf-8")
        assert len(text) > 100, f"Legacy page unexpectedly empty: {name}"


def test_legacy_routes_documented_and_present():
    for key, route in LEGACY_ROUTES.items():
        filename = route.lstrip("/")
        if "?" in filename:
            filename = filename.split("?", 1)[0]
        assert (FRONTEND / filename).is_file(), f"Missing page for {key}: {route}"


def test_plaza_router_module_and_engine_chat_harness():
    from agents import plaza_routes, plaza_engine

    assert hasattr(plaza_routes, "router"), "plaza_router must remain exportable"
    assert plaza_routes.router is not None

    engine = plaza_engine.get_plaza_engine()
    assert engine is not None
    # Chat harness wiring surface — set_chat_fn used by main startup.
    assert hasattr(engine, "set_chat_fn")
    assert callable(engine.set_chat_fn)


def test_main_mounts_plaza_and_static_legacy_routes():
    main_src = (BACKEND / "main.py").read_text(encoding="utf-8")
    assert "include_router(plaza_router" in main_src
    assert "from agents.plaza_engine import get_plaza_engine" in main_src
    assert "set_chat_fn" in main_src
    # Static frontend mount must remain (legacy pages served from src/frontend).
    assert "StaticFiles" in main_src


def test_disk_team_priority_over_factory_semantics():
    """Persisted team must not be overwritten by factory seed pattern in main."""
    main_src = (BACKEND / "main.py").read_text(encoding="utf-8")
    # Seed pattern: only create when team_id not already in manager.
    assert '"build_system" not in _team_manager._teams' in main_src
    assert '"ai_coding" not in _team_manager._teams' in main_src
    assert '"ai_news_60s" not in _team_manager._teams' in main_src
    assert '"dufu_world_intel" not in _team_manager._teams' in main_src


def test_team_manager_does_not_replace_existing_on_manual_seed(tmp_path, monkeypatch):
    """Simulate disk-first: if team already present, factory output is ignored."""
    from agents.models import AgentProfile, AgentTeam
    from agents.team_manager import TeamManager
    from agents.teams.build_team import create_build_team

    mgr = TeamManager()
    # Inject a "disk" team with a distinctive agent.
    disk = AgentTeam(team_id="build_system", name="Disk Build", description="persisted")
    disk.add_agent(AgentProfile(agent_id="disk_only", name="Disk Agent", role="keeper"))
    mgr._teams["build_system"] = disk

    if "build_system" not in mgr._teams:
        mgr._teams["build_system"] = create_build_team()

    assert mgr.get_team("build_system").name == "Disk Build"
    assert "disk_only" in mgr.get_team("build_system").agents
    assert "build_pm" not in mgr.get_team("build_system").agents
