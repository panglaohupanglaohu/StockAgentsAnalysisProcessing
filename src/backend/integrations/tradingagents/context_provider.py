# -*- coding: utf-8 -*-
"""Context provider: inject versioned information docs without future leakage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from domain.information_sources.documents import DocumentStore, get_document_store


@dataclass
class SourceContext:
    docs: List[Dict[str, Any]] = field(default_factory=list)
    as_of: str = ""
    channels: List[str] = field(default_factory=list)

    def to_prompt(self, max_tokens: int = 2000) -> str:
        # Rough char budget ~ 4 chars/token
        budget = max(200, max_tokens * 4)
        parts = [
            f"[StockAgents context as_of={self.as_of} channels={','.join(self.channels)}]"
        ]
        used = len(parts[0])
        for d in self.docs:
            block = (
                f"\n--- doc {d.get('document_id')} v{d.get('version')} "
                f"as_of={d.get('as_of')} channel={d.get('channel')} ---\n"
                f"{d.get('title', '')}\n"
                f"{(d.get('summary') or d.get('headline') or '')[:800]}\n"
                f"citations: {', '.join((d.get('evidence_urls') or [])[:5])}\n"
            )
            if used + len(block) > budget:
                break
            parts.append(block)
            used += len(block)
        return "".join(parts)


class SourceContextProvider:
    def __init__(self, document_store: Optional[DocumentStore] = None) -> None:
        self.docs = document_store or get_document_store()

    def for_ticker(
        self,
        *,
        ticker: str,
        before: str,
        channels: Optional[List[str]] = None,
        limit: int = 8,
    ) -> SourceContext:
        channels = channels or ["ai_news_60s", "dufu_world_intel"]
        found = self.docs.documents_for_context(before=before, channels=channels, limit=limit)
        payload = []
        ticker_u = (ticker or "").upper()
        for doc in found:
            report = doc.report or {}
            # Prefer docs that mention ticker; still include others as macro context
            blob = json_safe_text(report) + " " + (doc.title or "")
            score = 2 if ticker_u and ticker_u in blob.upper() else 1
            payload.append(
                {
                    "document_id": doc.document_id,
                    "version": doc.version,
                    "channel": doc.channel,
                    "as_of": doc.as_of,
                    "title": doc.title,
                    "summary": report.get("headline")
                    or (report.get("what_happened") or {}).get("text")
                    or doc.title,
                    "evidence_urls": doc.evidence_urls,
                    "score": score,
                }
            )
        payload.sort(key=lambda x: (x["score"], x["as_of"]), reverse=True)
        return SourceContext(docs=payload, as_of=before, channels=channels)


def json_safe_text(obj: Any) -> str:
    import json

    try:
        return json.dumps(obj, ensure_ascii=False)
    except Exception:
        return str(obj)
