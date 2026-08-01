# -*- coding: utf-8 -*-
"""Layered startup health for core teams, information teams, and trading runtime.

Three independent layers (missing lower layers must not take down the app):

* ``core_system`` — build_system + ai_coding (and legacy page contracts)
* ``information_teams`` — ai_news_60s + dufu_world_intel
* ``trading_runtime`` — optional TradingAgents v0.3.1 pin

Missing information teams yield an explicit diagnostic. TradingAgents missing
degrades to unavailable and never blocks original system startup.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional, Set

CORE_TEAM_IDS: Set[str] = {"build_system", "ai_coding"}
INFORMATION_TEAM_IDS: Set[str] = {"ai_news_60s", "dufu_world_intel"}
ALL_CORE_IDS: Set[str] = CORE_TEAM_IDS | INFORMATION_TEAM_IDS


def _team_ids_from_manager(team_manager: Any) -> Set[str]:
    if team_manager is None:
        return set()
    if hasattr(team_manager, "list_teams"):
        try:
            teams = team_manager.list_teams()
            return {getattr(t, "team_id", None) or t.get("team_id") for t in teams if t}
        except Exception:
            pass
    teams_map = getattr(team_manager, "_teams", None) or {}
    return set(teams_map.keys())


def _agents_present(team_manager: Any, team_id: str) -> bool:
    if team_manager is None:
        return False
    team = None
    if hasattr(team_manager, "get_team"):
        try:
            team = team_manager.get_team(team_id)
        except Exception:
            team = None
    if team is None:
        teams_map = getattr(team_manager, "_teams", None) or {}
        team = teams_map.get(team_id)
    if team is None:
        return False
    agents = getattr(team, "agents", None) or {}
    return len(agents) > 0


def assess_core_system(team_manager: Any) -> Dict[str, Any]:
    present = _team_ids_from_manager(team_manager)
    missing = sorted(CORE_TEAM_IDS - present)
    empty = [tid for tid in sorted(CORE_TEAM_IDS & present) if not _agents_present(team_manager, tid)]
    ok = not missing and not empty
    return {
        "layer": "core_system",
        "status": "ok" if ok else "degraded",
        "required": sorted(CORE_TEAM_IDS),
        "missing": missing,
        "empty_agents": empty,
        "diagnostic": (
            None
            if ok
            else (
                "Core system teams missing or empty: "
                + ", ".join(missing + [f"{t}(no agents)" for t in empty])
                + ". Original Agent Config / Build / AI Coding may be incomplete."
            )
        ),
    }


def assess_information_teams(team_manager: Any) -> Dict[str, Any]:
    present = _team_ids_from_manager(team_manager)
    missing = sorted(INFORMATION_TEAM_IDS - present)
    empty = [
        tid
        for tid in sorted(INFORMATION_TEAM_IDS & present)
        if not _agents_present(team_manager, tid)
    ]
    ok = not missing and not empty
    return {
        "layer": "information_teams",
        "status": "ok" if ok else "missing",
        "required": sorted(INFORMATION_TEAM_IDS),
        "missing": missing,
        "empty_agents": empty,
        "diagnostic": (
            None
            if ok
            else (
                "Information teams not loaded: "
                + ", ".join(missing + [f"{t}(no agents)" for t in empty])
                + ". Seed factories ai_news_60s_team / dufu_world_intel_team "
                "or clear AG_TEAM_ID filter. Data-intelligence pipelines unavailable."
            )
        ),
    }


def assess_trading_runtime() -> Dict[str, Any]:
    try:
        from integrations.tradingagents import probe_trading_runtime

        probe = probe_trading_runtime()
    except Exception as exc:
        probe = {
            "status": "unavailable",
            "error": str(exc),
            "action": "Trading runtime probe failed; investment engine disabled.",
        }
    status = probe.get("status") or "unavailable"
    return {
        "layer": "trading_runtime",
        "status": status,
        "probe": probe,
        "diagnostic": (
            None
            if status == "ready"
            else (probe.get("action") or probe.get("error") or "TradingAgents unavailable")
        ),
    }


def assess_startup_layers(team_manager: Any = None) -> Dict[str, Any]:
    """Return the three-layer startup health snapshot."""
    core = assess_core_system(team_manager)
    info = assess_information_teams(team_manager)
    trading = assess_trading_runtime()
    # Overall: core failure is the only thing that makes system non-ok for legacy.
    if core["status"] != "ok":
        overall = "degraded"
    elif info["status"] != "ok":
        overall = "partial"
    elif trading["status"] != "ready":
        overall = "ok_without_trading"
    else:
        overall = "ok"
    return {
        "overall": overall,
        "core_system": core,
        "information_teams": info,
        "trading_runtime": trading,
    }


def missing_core_team_ids(team_manager: Any, required: Optional[Iterable[str]] = None) -> Set[str]:
    req = set(required or ALL_CORE_IDS)
    return req - _team_ids_from_manager(team_manager)
