# -*- coding: utf-8 -*-
"""T004 — Core / information / trading layered health diagnostics."""

from __future__ import annotations

import pytest

from agents.models import AgentProfile, AgentTeam
from agents.startup_health import (
    CORE_TEAM_IDS,
    INFORMATION_TEAM_IDS,
    assess_core_system,
    assess_information_teams,
    assess_startup_layers,
    assess_trading_runtime,
)
from agents.teams.ai_coding_team import create_ai_coding_team
from agents.teams.ai_news_60s_team import create_ai_news_60s_team
from agents.teams.build_team import create_build_team
from agents.teams.dufu_world_intel_team import create_dufu_world_intel_team


class _Mgr:
    def __init__(self, teams):
        self._teams = {t.team_id: t for t in teams}

    def list_teams(self):
        return list(self._teams.values())

    def get_team(self, team_id):
        return self._teams.get(team_id)


def test_core_system_ok_when_build_and_coding_present():
    mgr = _Mgr([create_build_team(), create_ai_coding_team()])
    result = assess_core_system(mgr)
    assert result["status"] == "ok"
    assert result["missing"] == []
    assert result["layer"] == "core_system"


def test_core_system_diagnostic_when_missing():
    mgr = _Mgr([create_build_team()])
    result = assess_core_system(mgr)
    assert result["status"] == "degraded"
    assert "ai_coding" in result["missing"]
    assert result["diagnostic"]


def test_information_teams_missing_has_clear_diagnostic():
    mgr = _Mgr([create_build_team(), create_ai_coding_team()])
    result = assess_information_teams(mgr)
    assert result["status"] == "missing"
    assert set(result["missing"]) == INFORMATION_TEAM_IDS
    assert "ai_news_60s" in result["diagnostic"]
    assert "dufu_world_intel" in result["diagnostic"]


def test_information_teams_ok_when_seeded():
    mgr = _Mgr(
        [
            create_build_team(),
            create_ai_coding_team(),
            create_ai_news_60s_team(),
            create_dufu_world_intel_team(),
        ]
    )
    result = assess_information_teams(mgr)
    assert result["status"] == "ok"
    assert result["missing"] == []


def test_trading_runtime_does_not_raise_when_missing():
    result = assess_trading_runtime()
    assert result["layer"] == "trading_runtime"
    assert result["status"] in ("ready", "unavailable")
    # Without optional extra, typically unavailable — still a valid diagnostic.
    if result["status"] == "unavailable":
        assert result["diagnostic"]


def test_layers_bundle_three_keys():
    mgr = _Mgr(
        [
            create_build_team(),
            create_ai_coding_team(),
            create_ai_news_60s_team(),
            create_dufu_world_intel_team(),
        ]
    )
    layers = assess_startup_layers(mgr)
    assert "core_system" in layers
    assert "information_teams" in layers
    assert "trading_runtime" in layers
    assert layers["core_system"]["status"] == "ok"
    assert layers["information_teams"]["status"] == "ok"
    assert layers["overall"] in ("ok", "ok_without_trading", "partial", "degraded")


@pytest.mark.asyncio
async def test_health_endpoint_exposes_three_layers(monkeypatch):
    import main as main_module
    from channels import marine_base as marine_base_module
    from sandbox import python_runner as runner_module

    class _FakeRegistry:
        def get(self, name):
            return object()

    mgr = _Mgr(
        [
            create_build_team(),
            create_ai_coding_team(),
            create_ai_news_60s_team(),
            create_dufu_world_intel_team(),
        ]
    )
    monkeypatch.setattr(marine_base_module, "get_default_registry", lambda: _FakeRegistry())
    monkeypatch.setattr(
        runner_module,
        "describe_sandbox_runtime",
        lambda: {"mode": "lite", "ready": True},
    )
    monkeypatch.setattr(main_module, "_team_manager", mgr)

    payload = await main_module.health()
    assert "core_system" in payload.services
    assert "information_teams" in payload.services
    assert "trading_runtime" in payload.services
    assert payload.details.get("core_system") is not None
    assert payload.details.get("information_teams") is not None
    assert payload.details.get("trading_runtime") is not None
    assert payload.details["layers"]["core_system"]["layer"] == "core_system"
