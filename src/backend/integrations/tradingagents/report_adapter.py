# -*- coding: utf-8 -*-
"""T305 — Index TradingAgents reports into StockAgents storage."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from .graph_adapter import GraphResult

_DEFAULT = Path(__file__).resolve().parents[4] / "storage" / "tradingagents" / "reports"


def _atomic_write(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        tmp.write_text(data, encoding="utf-8")
        os.replace(tmp, path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def save_reports(result: GraphResult, root: Optional[Path] = None) -> Dict[str, Any]:
    """Persist market/sentiment/news/fundamentals, debates, plan, decision."""
    base = Path(root) if root else _DEFAULT
    run_dir = base / result.run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    index = {
        "run_id": result.run_id,
        "ticker": result.ticker,
        "trade_date": result.trade_date,
        "mode": result.mode,
        "sections": {},
        "final_decision": result.final_decision,
        "context_versions": result.context_versions,
        "graph_shape": result.graph_shape,
        "adapter_version": result.adapter_version,
        "pin": result.pin,
    }
    section_map = {
        "market": "market_analyst",
        "sentiment": "sentiment_analyst",
        "news": "news_analyst",
        "fundamentals": "fundamentals_analyst",
        "bull_bear_debate": ["bull_researcher", "bear_researcher", "research_manager"],
        "trade_plan": "trader",
        "risk_debate": ["aggressive_risk", "neutral_risk", "conservative_risk"],
        "final_decision": "portfolio_manager",
    }
    for name, key in section_map.items():
        if isinstance(key, list):
            content = "\n\n".join(f"## {k}\n{result.reports.get(k, '')}" for k in key)
        else:
            content = result.reports.get(key, "")
        path = run_dir / f"{name}.md"
        _atomic_write(path, content or "(empty)")
        index["sections"][name] = str(path)
    _atomic_write(run_dir / "index.json", json.dumps(index, ensure_ascii=False, indent=2))
    _atomic_write(
        run_dir / "raw_state.json",
        json.dumps(result.to_dict(), ensure_ascii=False, indent=2),
    )
    return index


def load_report_index(run_id: str, root: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    base = Path(root) if root else _DEFAULT
    path = base / run_id / "index.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
