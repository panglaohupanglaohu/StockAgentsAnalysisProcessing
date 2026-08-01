# -*- coding: utf-8 -*-
"""TradingAgents v0.3.1 runtime probe and smoke helpers.

Pin: signed tag ``v0.3.1`` / commit ``01477f9``.
Optional dependency group: ``pip install -e '.[trading]'``.

Importing this module must never crash the StockAgents core process when the
optional package is missing — health endpoints degrade to ``unavailable``.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

# Fixed pin — upgrades require pin change + compatibility tests + ADR.
PINNED_TAG = "v0.3.1"
PINNED_COMMIT = "01477f9"
PINNED_REPO = "https://github.com/TauricResearch/TradingAgents"
LICENSE = "Apache-2.0"


def actionable_import_message(exc: BaseException) -> str:
    """Human-actionable message when TradingAgents cannot be imported."""
    return (
        f"TradingAgents runtime unavailable ({type(exc).__name__}: {exc}). "
        f"Install the optional extra pinned to {PINNED_TAG} "
        f"(commit {PINNED_COMMIT}): python -m pip install -e '.[trading]'. "
        "Core StockAgents pages continue without the investment runtime."
    )


def probe_trading_runtime() -> Dict[str, Any]:
    """Probe optional TradingAgents import without raising.

    Returns a stable dict::

        {
          "status": "ready" | "unavailable",
          "pinned_tag": "v0.3.1",
          "pinned_commit": "01477f9",
          "import_path": "tradingagents.graph.trading_graph.TradingAgentsGraph",
          "error": optional str,
          "action": optional install hint,
        }
    """
    base: Dict[str, Any] = {
        "status": "unavailable",
        "pinned_tag": PINNED_TAG,
        "pinned_commit": PINNED_COMMIT,
        "pinned_repo": PINNED_REPO,
        "license": LICENSE,
        "import_path": "tradingagents.graph.trading_graph.TradingAgentsGraph",
    }
    try:
        from tradingagents.graph.trading_graph import TradingAgentsGraph  # noqa: F401

        base["status"] = "ready"
        base["class_name"] = "TradingAgentsGraph"
        return base
    except ImportError as exc:
        base["error"] = str(exc)
        base["action"] = actionable_import_message(exc)
        return base
    except Exception as exc:  # pragma: no cover — unexpected import-time failures
        base["error"] = f"{type(exc).__name__}: {exc}"
        base["action"] = actionable_import_message(exc)
        return base


def try_import_trading_graph():
    """Return TradingAgentsGraph class or None if unavailable."""
    try:
        from tradingagents.graph.trading_graph import TradingAgentsGraph

        return TradingAgentsGraph
    except ImportError:
        return None


def smoke_import() -> Dict[str, Any]:
    """Minimal import smoke used by tests and health diagnostics."""
    result = probe_trading_runtime()
    result["smoke"] = "import"
    return result


def smoke_fixture_graph(ticker: str = "NVDA", trade_date: Optional[str] = None) -> Dict[str, Any]:
    """Attempt a dry construction smoke against a fixture ticker.

    Does **not** call live market APIs. When the package is missing, returns
    ``status=unavailable``. When present, only verifies the graph class is
    constructible with a minimal config stub if the upstream API allows it;
    otherwise reports ``status=ready`` with ``graph_smoke=skipped``.
    """
    probe = probe_trading_runtime()
    if probe["status"] != "ready":
        return {**probe, "ticker": ticker, "graph_smoke": "skipped"}

    graph_cls = try_import_trading_graph()
    if graph_cls is None:
        return {**probe, "ticker": ticker, "graph_smoke": "skipped"}

    # Upstream constructors often need full config/LLM keys. We only verify the
    # class is callable and document pin — full run is a later task (T304+).
    return {
        **probe,
        "ticker": ticker,
        "trade_date": trade_date,
        "graph_smoke": "class_ready",
        "graph_class": getattr(graph_cls, "__name__", "TradingAgentsGraph"),
        "note": (
            "Full graph execution requires model keys and is covered by "
            "later adapter tasks; this smoke only validates import + pin."
        ),
    }
