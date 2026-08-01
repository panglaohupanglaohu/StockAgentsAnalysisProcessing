# -*- coding: utf-8 -*-
"""T302 — Map Agent Config models → TradingAgents config dict."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from .runtime import PINNED_COMMIT, PINNED_TAG

# Supported provider aliases → TradingAgents-style provider ids
PROVIDER_MAP = {
    "openai": "openai",
    "openai-compatible": "openai",
    "openai_compatible": "openai",
    "anthropic": "anthropic",
    "claude": "anthropic",
    "google": "google",
    "gemini": "google",
    "xai": "xai",
    "grok": "xai",
    "deepseek": "deepseek",
    "qwen": "qwen",
    "dashscope": "qwen",
    "ollama": "ollama",
    "azure": "openai",
}


def normalize_provider(provider: str) -> str:
    key = (provider or "").strip().lower()
    return PROVIDER_MAP.get(key, key or "openai")


def _resolve_api_key(raw: str) -> str:
    if not raw:
        return ""
    if raw.startswith("env:"):
        return os.environ.get(raw[4:], "")
    # Never accept browser-supplied raw keys in mapper from untrusted paths;
    # allow server-side ModelConfig that already stores env refs.
    if raw.startswith("****"):
        return ""
    return raw


def _model_fields(model: Any) -> Dict[str, Any]:
    if model is None:
        return {}
    if isinstance(model, dict):
        return model
    return {
        "model_id": getattr(model, "model_id", ""),
        "provider": getattr(model, "provider", ""),
        "name": getattr(model, "name", ""),
        "api_base_url": getattr(model, "api_base_url", ""),
        "api_key": getattr(model, "api_key", ""),
        "max_tokens": getattr(model, "max_tokens", 4096),
        "temperature": getattr(model, "temperature", 0.3),
    }


def map_agent_config(
    *,
    quick_model: Any = None,
    deep_model: Any = None,
    output_language: str = "zh-CN",
    debate_rounds: int = 1,
    risk_rounds: int = 1,
    checkpoint_enabled: bool = True,
    retry: int = 1,
    analysts: Optional[List[str]] = None,
    data_vendor: str = "yfinance",
    storage_root: Optional[Path] = None,
) -> Dict[str, Any]:
    """Build TradingAgents-compatible config from Agent Config models.

    Covers OpenAI-compatible, OpenAI, Anthropic, Google, xAI/Grok, DeepSeek,
    Qwen, and Ollama via provider normalization.
    """
    quick = _model_fields(quick_model)
    deep = _model_fields(deep_model) or quick
    provider = normalize_provider(deep.get("provider") or quick.get("provider") or "openai")
    root = Path(storage_root) if storage_root else (
        Path(__file__).resolve().parents[4] / "storage" / "tradingagents"
    )
    cfg = {
        "llm_provider": provider,
        "deep_think_llm": deep.get("name") or "gpt-4o",
        "quick_think_llm": quick.get("name") or deep.get("name") or "gpt-4o-mini",
        "backend_url": deep.get("api_base_url") or quick.get("api_base_url") or "",
        "output_language": output_language,
        "max_debate_rounds": int(debate_rounds),
        "max_risk_discuss_rounds": int(risk_rounds),
        "checkpoint_enabled": bool(checkpoint_enabled),
        "retry": int(retry),
        "selected_analysts": analysts
        or ["market", "social", "news", "fundamentals"],
        "data_vendor": data_vendor,
        "data_cache_dir": str(root / "cache"),
        "results_dir": str(root / "results"),
        "checkpoint_dir": str(root / "checkpoints"),
        "stockagents_pin": {"tag": PINNED_TAG, "commit": PINNED_COMMIT},
        # Keys resolved server-side only — never serialize raw secrets to browser
        "api_key_env_resolved": bool(
            _resolve_api_key(deep.get("api_key") or "")
            or _resolve_api_key(quick.get("api_key") or "")
            or os.environ.get("OPENAI_API_KEY")
            or os.environ.get("DEEPSEEK_API_KEY")
            or os.environ.get("ANTHROPIC_API_KEY")
        ),
        "quick_model_id": quick.get("model_id"),
        "deep_model_id": deep.get("model_id"),
    }
    return cfg


def validate_mapped_config(cfg: Dict[str, Any]) -> Dict[str, Any]:
    errors: List[str] = []
    if not cfg.get("deep_think_llm"):
        errors.append("deep_think_llm required")
    if not cfg.get("quick_think_llm"):
        errors.append("quick_think_llm required")
    if cfg.get("max_debate_rounds", 0) < 0:
        errors.append("max_debate_rounds must be >= 0")
    if cfg.get("max_risk_discuss_rounds", 0) < 0:
        errors.append("max_risk_discuss_rounds must be >= 0")
    provider = cfg.get("llm_provider") or ""
    if provider and provider not in set(PROVIDER_MAP.values()) | set(PROVIDER_MAP.keys()):
        # allow unknown providers with warning only
        pass
    return {"ok": not errors, "errors": errors, "config": cfg}
