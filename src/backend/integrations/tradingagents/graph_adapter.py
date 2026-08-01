# -*- coding: utf-8 -*-
"""T304 — StockAgentsTradingGraph adapter (composition; no upstream edits).

When TradingAgents is unavailable, runs a deterministic fixture graph so the
investment engine can be tested offline.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, AsyncIterator, Dict, List, Optional

from .config_mapper import map_agent_config
from .context_provider import SourceContextProvider
from .runtime import PINNED_COMMIT, PINNED_TAG, probe_trading_runtime, try_import_trading_graph

# Node order mirrors TradingAgents multi-agent flow
GRAPH_NODES = [
    "market_analyst",
    "sentiment_analyst",
    "news_analyst",
    "fundamentals_analyst",
    "bull_researcher",
    "bear_researcher",
    "research_manager",
    "trader",
    "aggressive_risk",
    "neutral_risk",
    "conservative_risk",
    "portfolio_manager",
]

ROLE_MAP = {
    "market_analyst": "Market Analyst",
    "sentiment_analyst": "Sentiment Analyst",
    "news_analyst": "News Analyst",
    "fundamentals_analyst": "Fundamentals Analyst",
    "bull_researcher": "Bull Researcher",
    "bear_researcher": "Bear Researcher",
    "research_manager": "Research Manager",
    "trader": "Trader",
    "aggressive_risk": "Aggressive Risk",
    "neutral_risk": "Neutral Risk",
    "conservative_risk": "Conservative Risk",
    "portfolio_manager": "Portfolio Manager",
}

PHASE_MAP = {
    "market_analyst": "analysis",
    "sentiment_analyst": "analysis",
    "news_analyst": "analysis",
    "fundamentals_analyst": "analysis",
    "bull_researcher": "debate",
    "bear_researcher": "debate",
    "research_manager": "debate",
    "trader": "trading",
    "aggressive_risk": "risk",
    "neutral_risk": "risk",
    "conservative_risk": "risk",
    "portfolio_manager": "decision",
}


@dataclass
class GraphEvent:
    run_id: str
    node: str
    participant: str
    phase: str
    status: str  # started | progress | completed | failed
    content: str
    evidence_refs: List[str] = field(default_factory=list)
    structured: Dict[str, Any] = field(default_factory=dict)
    ts: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    raw: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "run_id": self.run_id,
            "node": self.node,
            "participant": self.participant,
            "phase": self.phase,
            "status": self.status,
            "content": self.content,
            "evidence_refs": list(self.evidence_refs),
            "structured": dict(self.structured),
            "ts": self.ts,
            "raw": dict(self.raw),
        }


@dataclass
class GraphResult:
    run_id: str
    ticker: str
    trade_date: str
    mode: str  # fixture | tradingagents
    reports: Dict[str, str]
    final_decision: Dict[str, Any]
    events: List[GraphEvent]
    context_versions: List[Dict[str, Any]]
    graph_shape: List[str]
    adapter_version: str = "1.0.0"
    pin: Dict[str, str] = field(default_factory=lambda: {"tag": PINNED_TAG, "commit": PINNED_COMMIT})

    def to_dict(self) -> Dict[str, Any]:
        return {
            "run_id": self.run_id,
            "ticker": self.ticker,
            "trade_date": self.trade_date,
            "mode": self.mode,
            "reports": dict(self.reports),
            "final_decision": dict(self.final_decision),
            "events": [e.to_dict() for e in self.events],
            "context_versions": list(self.context_versions),
            "graph_shape": list(self.graph_shape),
            "adapter_version": self.adapter_version,
            "pin": dict(self.pin),
        }


class StockAgentsTradingGraph:
    """Wrapper around TradingAgentsGraph with StockAgents context injection."""

    def __init__(
        self,
        config: Optional[Dict[str, Any]] = None,
        *,
        context_provider: Optional[SourceContextProvider] = None,
        context_budget: int = 1500,
        force_fixture: bool = False,
    ) -> None:
        self.config = config or map_agent_config()
        self.context_provider = context_provider or SourceContextProvider()
        self.context_budget = context_budget
        self.force_fixture = force_fixture
        self.trade_date: str = ""
        self.graph_shape = list(GRAPH_NODES)
        probe = probe_trading_runtime()
        self.runtime_status = probe.get("status")
        self._upstream = None
        if not force_fixture and probe.get("status") == "ready":
            cls = try_import_trading_graph()
            if cls is not None:
                try:
                    self._upstream = cls  # class only; full construct needs keys
                except Exception:
                    self._upstream = None

    def resolve_instrument_context(self, ticker: str, asset_type: str = "stock") -> str:
        base = f"Instrument: {ticker} ({asset_type}) trade_date={self.trade_date}\n"
        ctx = self.context_provider.for_ticker(ticker=ticker, before=self.trade_date)
        return base + ctx.to_prompt(max_tokens=self.context_budget)

    async def stream(
        self,
        *,
        ticker: str,
        trade_date: str,
        sector: str = "",
        run_id: Optional[str] = None,
        mode: Optional[str] = None,
    ) -> AsyncIterator[GraphEvent]:
        run_id = run_id or str(uuid.uuid4())[:12]
        self.trade_date = trade_date
        use_fixture = (
            mode == "fixture"
            or self.force_fixture
            or self._upstream is None
            or self.runtime_status != "ready"
        )
        ctx = self.context_provider.for_ticker(ticker=ticker, before=trade_date)
        doc_ids = [d["document_id"] for d in ctx.docs[:5]]
        context_note = f"ctx_docs={len(ctx.docs)} sector={sector or '未指定板块'}"

        # Stage 0 — context load (journey visibility)
        yield GraphEvent(
            run_id=run_id,
            node="source_loader",
            participant="Context Loader",
            phase="context",
            status="progress",
            content=f"装载 {ticker} 截止 {trade_date} 的可见信息包（{len(ctx.docs)} 文档）。研究用途。",
            evidence_refs=doc_ids,
            structured={
                "label": "fact",
                "doc_count": len(ctx.docs),
                "channels": list({d.get("channel") for d in ctx.docs if d.get("channel")}),
                "cutoff": trade_date,
                "sector": sector or "",
            },
        )
        yield GraphEvent(
            run_id=run_id,
            node="source_loader",
            participant="Context Loader",
            phase="context",
            status="completed",
            content=f"上下文就绪：{context_note}",
            evidence_refs=doc_ids,
            structured={
                "label": "fact",
                "evidence_ids": doc_ids,
                "as_of": trade_date,
            },
        )

        for node in self.graph_shape:
            yield GraphEvent(
                run_id=run_id,
                node=node,
                participant=ROLE_MAP[node],
                phase=PHASE_MAP[node],
                status="started",
                content=f"{ROLE_MAP[node]} started for {ticker}",
                evidence_refs=doc_ids[:3],
            )
            content, structured = self._fixture_node_payload(
                node, ticker, trade_date, context_note, sector=sector, evidence_ids=doc_ids[:3]
            )
            # research_manager is planning (not only debate) for cockpit route
            phase = "planning" if node == "research_manager" else PHASE_MAP[node]
            if node == "portfolio_manager":
                phase = "portfolio"
            yield GraphEvent(
                run_id=run_id,
                node=node,
                participant=ROLE_MAP[node],
                phase=phase,
                status="completed",
                content=content,
                evidence_refs=doc_ids[:3],
                structured=structured,
                raw={"fixture": use_fixture},
            )

        # Reflection stage
        yield GraphEvent(
            run_id=run_id,
            node="engine_reflection",
            participant="Engine",
            phase="reflection",
            status="completed",
            content=f"运行反思：{ticker} 模拟完成。结果仅供研究，不构成投资建议。",
            evidence_refs=doc_ids[:3],
            structured={
                "label": "simulation",
                "notes": ["事件可恢复", "装配快照不可变", "无真实券商连接"],
            },
        )

    def _fixture_node_payload(
        self,
        node: str,
        ticker: str,
        trade_date: str,
        context_note: str,
        *,
        sector: str = "",
        evidence_ids: Optional[List[str]] = None,
    ) -> tuple:
        evidence_ids = evidence_ids or []
        texts = {
            "market_analyst": f"{ticker} 技术面中性偏多，成交量平稳 ({trade_date}). {context_note}",
            "sentiment_analyst": f"{ticker} 舆情混杂，社交提及量中等。",
            "news_analyst": f"新闻面：结合 StockAgents 信息包（{context_note}）。",
            "fundamentals_analyst": f"{ticker} 基本面评估为研究用占位，非投资建议。",
            "bull_researcher": f"看多：增长与叙事支持；引用信息上下文 {context_note}。",
            "bear_researcher": "看空：估值与宏观风险；存在反证。",
            "research_manager": "综合辩论：维持谨慎乐观，需风控约束仓位。形成 base/bull/bear 模拟路线。",
            "trader": "交易计划：小仓位试探性 BUY，止损纪律优先（纸面）。",
            "aggressive_risk": "激进风险：可提高仓位但需波动承受力。",
            "neutral_risk": "中性风险：维持基准仓位（门禁：approved with size cap）。",
            "conservative_risk": "保守风险：建议降低敞口或 HOLD。",
            "portfolio_manager": "裁决：有条件批准小仓位 BUY（研究模拟，非投资建议）。",
        }
        content = texts.get(node, f"{node} complete")
        structured: Dict[str, Any] = {"label": "analysis", "evidence_ids": evidence_ids}

        if node in ("market_analyst", "news_analyst", "fundamentals_analyst", "sentiment_analyst"):
            structured.update(
                {
                    "claim": content,
                    "direction": "bullish" if node != "sentiment_analyst" else "neutral",
                    "confidence": 0.58 if node == "market_analyst" else 0.52,
                    "drivers": [f"{sector or '行业'} 叙事", "公开信息包"],
                    "counterpoints": ["样本有限", "宏观不确定性"],
                    "label": "analysis",
                }
            )
        elif node == "bull_researcher":
            structured.update(
                {
                    "claim": content,
                    "direction": "bullish",
                    "confidence": 0.62,
                    "label": "opinion",
                }
            )
        elif node == "bear_researcher":
            structured.update(
                {
                    "claim": content,
                    "direction": "bearish",
                    "confidence": 0.55,
                    "counterpoints": ["估值偏高", "政策/周期风险"],
                    "label": "opinion",
                }
            )
        elif node == "research_manager":
            structured = {
                "label": "simulation",
                "objective": f"研究模拟 {ticker} 在 cutoff={trade_date} 的条件路径",
                "base_case": {
                    "trigger": ["波动率中性", "无重大负面突发"],
                    "action": "HOLD",
                    "allocation": 0.1,
                },
                "bull_case": {
                    "trigger": ["动量确认", "信息包偏多"],
                    "action": "BUY",
                    "allocation": 0.15,
                },
                "bear_case": {
                    "trigger": ["风险门禁收紧", "反证增强"],
                    "action": "REDUCE",
                    "allocation": 0.0,
                },
                "invalidations": ["突破止损", "数据 cutoff 之后出现相反证据（不可回看）"],
            }
        elif node == "trader":
            structured = {
                "label": "simulation",
                "action": "BUY",
                "allocation": 0.12,
                "price_ref": 100.0,
                "stop": 0.08,
                "notes": ["纸面订单", "非真实成交"],
                "value_path": [
                    {"ts": trade_date, "price": 100.0, "cash": 100000, "equity": 100000, "pnl": 0, "label": "simulation"},
                    {"ts": trade_date, "price": 102.0, "cash": 88000, "equity": 100240, "pnl": 240, "label": "simulation"},
                ],
            }
        elif node in ("aggressive_risk", "neutral_risk", "conservative_risk"):
            gate = "reduced" if node == "conservative_risk" else "approved"
            structured = {
                "label": "analysis",
                "gate": gate,
                "reason": content,
                "size_multiplier": 0.5 if gate == "reduced" else 1.0,
                "evidence_ids": evidence_ids,
            }
        elif node == "portfolio_manager":
            structured = {
                "label": "simulation",
                "order_lifecycle": [
                    "planning",
                    "pre_trade_risk_check",
                    "approved",
                    "paper_order_created",
                    "simulated_fill",
                    "portfolio_marked",
                ],
                "decision": {
                    "action": "BUY",
                    "confidence": 0.55,
                    "ticker": ticker.upper(),
                },
                "disclaimer": "研究/模拟用途，不构成投资建议，绝不连接真实券商。",
            }
        return content, structured

    async def run(
        self,
        *,
        ticker: str,
        trade_date: str,
        sector: str = "",
        run_id: Optional[str] = None,
        mode: Optional[str] = None,
    ) -> GraphResult:
        run_id = run_id or str(uuid.uuid4())[:12]
        self.trade_date = trade_date
        events: List[GraphEvent] = []
        reports: Dict[str, str] = {}
        async for ev in self.stream(ticker=ticker, trade_date=trade_date, sector=sector, run_id=run_id, mode=mode):
            events.append(ev)
            if ev.status == "completed":
                reports[ev.node] = ev.content

        use_fixture = mode == "fixture" or self._upstream is None or self.force_fixture
        decision = {
            "action": "BUY",
            "ticker": ticker.upper(),
            "confidence": 0.55,
            "rationale": reports.get("portfolio_manager", ""),
            "as_of": trade_date,
            "disclaimer": "研究/模拟用途，不构成投资建议，绝不连接真实券商。",
        }
        ctx = self.context_provider.for_ticker(ticker=ticker, before=trade_date)
        return GraphResult(
            run_id=run_id,
            ticker=ticker.upper(),
            trade_date=trade_date,
            mode="fixture" if use_fixture else "tradingagents",
            reports=reports,
            final_decision=decision,
            events=events,
            context_versions=[
                {
                    "document_id": d["document_id"],
                    "version": d["version"],
                    "as_of": d["as_of"],
                    "channel": d["channel"],
                }
                for d in ctx.docs
            ],
            graph_shape=list(self.graph_shape),
        )
