# -*- coding: utf-8 -*-
"""Active team policy for the StockAgents product surface.

The product intentionally exposes four teams only.  Legacy team factories and
historical JSON records may remain in the repository for compatibility tests,
but they must not be seeded into the running application or shown in Agent
Config.
"""

from __future__ import annotations

from typing import Any, Dict, Iterable, Tuple


ACTIVE_TEAM_IDS = frozenset(
    {
        "build_system",
        "ai_coding",
        "ai_news_60s",
        "dufu_world_intel",
    }
)


def prune_teams(teams: Dict[str, Any]) -> Tuple[Dict[str, Any], Tuple[str, ...]]:
    """Return only active teams and the removed team ids.

    The input mapping is not mutated so callers can decide when to persist the
    controlled cleanup.  Sorting makes startup logs and tests deterministic.
    """

    kept = {team_id: team for team_id, team in teams.items() if team_id in ACTIVE_TEAM_IDS}
    removed = tuple(sorted(set(teams) - ACTIVE_TEAM_IDS))
    return kept, removed


def is_active_team(team_id: str) -> bool:
    return team_id in ACTIVE_TEAM_IDS

