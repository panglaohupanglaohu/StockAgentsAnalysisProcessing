# -*- coding: utf-8 -*-
"""Optional TradingAgents v0.3.1 integration boundary.

Importing StockAgents core modules must not require the optional ``trading``
dependency. Use :func:`probe_trading_runtime` for health/status.
"""

from .config_mapper import map_agent_config, normalize_provider, validate_mapped_config
from .graph_adapter import StockAgentsTradingGraph
from .runtime import (
    LICENSE,
    PINNED_COMMIT,
    PINNED_REPO,
    PINNED_TAG,
    actionable_import_message,
    probe_trading_runtime,
    smoke_fixture_graph,
    smoke_import,
    try_import_trading_graph,
)

__all__ = [
    "LICENSE",
    "PINNED_COMMIT",
    "PINNED_REPO",
    "PINNED_TAG",
    "StockAgentsTradingGraph",
    "actionable_import_message",
    "map_agent_config",
    "normalize_provider",
    "probe_trading_runtime",
    "smoke_fixture_graph",
    "smoke_import",
    "try_import_trading_graph",
    "validate_mapped_config",
]
