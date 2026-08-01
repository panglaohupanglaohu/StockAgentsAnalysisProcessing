# -*- coding: utf-8 -*-
"""AWS ES costdown script scoring criteria (Phase 11 offline helpers).

Used by ``test_aws_ops_costdown.py``. Pure functions — no LLM / network.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

# (criterion_id, substring that must appear in the script)
CRITERIA: List[Tuple[str, str]] = [
    ("instance_spec", "describe-elasticsearch-domain"),
    ("apply_change", "update-elasticsearch-domain-config"),
    ("wait_active", "Processing"),
    ("monitor_alarm", "put-metric-alarm"),
    ("cost_or_rollback", "pricing"),
]


def score_script(script: Optional[str]) -> Dict[str, Any]:
    """Score a shell script against the five costdown criteria.

    Returns ``{"score": int, "hit": list[str], "missing": list[str]}``.
    """
    text = script or ""
    if not isinstance(text, str):
        text = ""
    hit: List[str] = []
    missing: List[str] = []
    for key, needle in CRITERIA:
        if needle in text:
            hit.append(key)
        else:
            missing.append(key)
    return {"score": len(hit), "hit": hit, "missing": missing}
