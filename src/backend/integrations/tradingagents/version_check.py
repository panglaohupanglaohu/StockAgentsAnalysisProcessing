# -*- coding: utf-8 -*-
"""T307 — Check for newer TradingAgents releases without auto-upgrade."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .runtime import PINNED_COMMIT, PINNED_REPO, PINNED_TAG


async def check_tradingagents_release(
    *,
    current_tag: str = PINNED_TAG,
    timeout: float = 5.0,
) -> Dict[str, Any]:
    """Query GitHub releases API; never mutates pin or installs packages."""
    result: Dict[str, Any] = {
        "pinned_tag": PINNED_TAG,
        "pinned_commit": PINNED_COMMIT,
        "repo": PINNED_REPO,
        "latest_tag": None,
        "update_available": False,
        "auto_upgrade": False,
        "message": (
            "Upgrades require changing the pin in pyproject.toml, running "
            "compatibility tests, and recording an ADR. Production must not follow main."
        ),
    }
    try:
        import httpx

        url = "https://api.github.com/repos/TauricResearch/TradingAgents/releases/latest"
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url, headers={"Accept": "application/vnd.github+json"})
            if resp.status_code != 200:
                result["error"] = f"GitHub API status {resp.status_code}"
                return result
            data = resp.json()
            tag = data.get("tag_name") or data.get("name")
            result["latest_tag"] = tag
            result["update_available"] = bool(tag and tag.lstrip("v") != current_tag.lstrip("v") and tag != current_tag)
            if result["update_available"]:
                result["message"] = (
                    f"New release {tag} detected; still pinned to {current_tag}. "
                    "Do not auto-upgrade."
                )
    except Exception as exc:
        result["error"] = str(exc)
    return result
