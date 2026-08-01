# -*- coding: utf-8 -*-
"""Validate agent tool bindings against the real tool registry catalog."""

from __future__ import annotations

from typing import Iterable, Set

from ..tool_registry import get_default_tools


def known_tool_names() -> Set[str]:
    """Return the set of tool *names* registered in the default catalog."""
    return {t.name for t in get_default_tools() if t.name}


def validate_real_tools(tools: Iterable[str]) -> None:
    """Raise ValueError if any tool name is missing from the default catalog.

    Agents bind tools by name (not auto-generated tool_id). Binding a name that
    is not in the registry would leave the agent with a dead capability.
    """
    known = known_tool_names()
    missing = sorted({name for name in tools if name and name not in known})
    if missing:
        raise ValueError(
            "Agent binds unknown tools (not in tool_registry): "
            + ", ".join(missing)
        )
