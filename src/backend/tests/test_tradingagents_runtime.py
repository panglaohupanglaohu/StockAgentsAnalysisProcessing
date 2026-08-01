# -*- coding: utf-8 -*-
"""T301 — TradingAgents v0.3.1 pin, import smoke, health degradation."""

from __future__ import annotations

from integrations.tradingagents import (
    LICENSE,
    PINNED_COMMIT,
    PINNED_TAG,
    probe_trading_runtime,
    smoke_fixture_graph,
    smoke_import,
)


def test_pin_is_v031_commit_01477f9():
    assert PINNED_TAG == "v0.3.1"
    assert PINNED_COMMIT == "01477f9"
    assert LICENSE == "Apache-2.0"


def test_probe_never_raises():
    result = probe_trading_runtime()
    assert result["pinned_tag"] == "v0.3.1"
    assert result["pinned_commit"] == "01477f9"
    assert result["status"] in ("ready", "unavailable")
    if result["status"] == "unavailable":
        assert result.get("action") or result.get("error")


def test_smoke_import_stable_shape():
    result = smoke_import()
    assert result["smoke"] == "import"
    assert result["status"] in ("ready", "unavailable")


def test_smoke_fixture_ticker_does_not_crash():
    result = smoke_fixture_graph(ticker="NVDA")
    assert result["ticker"] == "NVDA"
    assert result["status"] in ("ready", "unavailable")
    assert "graph_smoke" in result


def test_pyproject_pins_trading_extra():
    from pathlib import Path

    root = Path(__file__).resolve().parents[3]
    text = (root / "pyproject.toml").read_text(encoding="utf-8")
    assert "tradingagents" in text
    assert "01477f9" in text
