# -*- coding: utf-8 -*-
"""Six-layer validation gate state machine — corresponds to Eqs. 13-15 in the paper.

Gate chain: schema → provenance → tools → execution → safety → regression/non-regression.
Priority: reject ≻ revise ≻ pass. Reject at any layer blocks publication.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class GateVerdict(str, Enum):
    PASS = "pass"
    REVISE = "revise"
    REJECT = "reject"


class GateLayer(str, Enum):
    SCHEMA = "schema"
    PROVENANCE = "provenance"
    TOOLS = "tools"
    EXECUTION = "execution"
    SAFETY = "safety"
    REGRESSION = "regression"


_LAYER_ORDER: Tuple[GateLayer, ...] = (
    GateLayer.SCHEMA,
    GateLayer.PROVENANCE,
    GateLayer.TOOLS,
    GateLayer.EXECUTION,
    GateLayer.SAFETY,
    GateLayer.REGRESSION,
)


@dataclass
class GateEvidence:
    layer: GateLayer
    verdict: GateVerdict
    reason: str = ""
    details: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = ""
    env_version: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "layer": self.layer.value,
            "verdict": self.verdict.value,
            "reason": self.reason,
            "details": self.details,
            "timestamp": self.timestamp,
            "env_version": self.env_version,
        }


@dataclass
class ValidationResult:
    candidate_id: str
    layer_results: List[GateEvidence] = field(default_factory=list)
    composite: GateVerdict = GateVerdict.PASS
    accepted: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "layer_results": [r.to_dict() for r in self.layer_results],
            "composite": self.composite.value,
            "accepted": self.accepted,
        }


class ValidationGate:
    """Eq.13 gate chain: P_i = G_s ∧ G_e ∧ G_t; R_i = G_x ∧ G_a; L_i = P_i ∧ R_i ∧ G_r.

    All variables are binary — multiplication ≡ logical conjunction.
    """

    def __init__(
        self,
        schema_checker=None,
        provenance_checker=None,
        tools_checker=None,
        execution_checker=None,
        safety_checker=None,
        regression_checker=None,
    ):
        self._checkers: Dict[GateLayer, Any] = {
            GateLayer.SCHEMA: schema_checker,
            GateLayer.PROVENANCE: provenance_checker,
            GateLayer.TOOLS: tools_checker,
            GateLayer.EXECUTION: execution_checker,
            GateLayer.SAFETY: safety_checker,
            GateLayer.REGRESSION: regression_checker,
        }

    def evaluate(
        self, candidate: Dict[str, Any], env: Optional[Dict[str, Any]] = None
    ) -> ValidationResult:
        """Run the six-layer gate chain and return the composite verdict.

        Eq.15 priority: reject ≻ revise ≻ pass
        """
        cid = candidate.get("skill_id", candidate.get("id", "unknown"))
        results: List[GateEvidence] = []

        for layer in _LAYER_ORDER:
            evidence = self._check_layer(layer, candidate, env)
            results.append(evidence)

        composite = self._composite(results)
        return ValidationResult(
            candidate_id=str(cid),
            layer_results=results,
            composite=composite,
            accepted=(composite == GateVerdict.PASS),
        )

    def _check_layer(
        self, layer: GateLayer, candidate: Dict[str, Any], env: Optional[Dict[str, Any]]
    ) -> GateEvidence:
        checker = self._checkers.get(layer)
        if checker is not None and callable(checker):
            return checker(candidate, env)
        return GateEvidence(
            layer=layer, verdict=GateVerdict.PASS, reason="no checker registered"
        )

    @staticmethod
    def _composite(results: List[GateEvidence]) -> GateVerdict:
        for r in results:
            if r.verdict == GateVerdict.REJECT:
                return GateVerdict.REJECT
        for r in results:
            if r.verdict == GateVerdict.REVISE:
                return GateVerdict.REVISE
        return GateVerdict.PASS

    @staticmethod
    def pre_gate_passed(result: ValidationResult) -> bool:
        """P_i = G_s ∧ G_e ∧ G_t — Eq.13 pre-gate."""
        pre_layers = {GateLayer.SCHEMA, GateLayer.PROVENANCE, GateLayer.TOOLS}
        for r in result.layer_results:
            if r.layer in pre_layers and r.verdict != GateVerdict.PASS:
                return False
        return True

    @staticmethod
    def exec_gate_passed(result: ValidationResult) -> bool:
        """R_i = G_x ∧ G_a — Eq.13 execution-gate."""
        exec_layers = {GateLayer.EXECUTION, GateLayer.SAFETY}
        for r in result.layer_results:
            if r.layer in exec_layers and r.verdict != GateVerdict.PASS:
                return False
        return True


# ── built-in checker factories ──────────────────────────────────────


def schema_checker(candidate: Dict[str, Any], env=None) -> GateEvidence:
    required = {"name", "description", "instructions"}
    missing = required - set(k for k, v in candidate.items() if v)
    if missing:
        return GateEvidence(
            layer=GateLayer.SCHEMA,
            verdict=GateVerdict.REVISE,
            reason=f"missing required fields: {missing}",
        )
    name = candidate.get("name", "")
    if not isinstance(name, str) or len(name.strip()) < 2:
        return GateEvidence(
            layer=GateLayer.SCHEMA,
            verdict=GateVerdict.REVISE,
            reason="skill name too short",
        )
    return GateEvidence(layer=GateLayer.SCHEMA, verdict=GateVerdict.PASS)


def provenance_checker(candidate: Dict[str, Any], env=None) -> GateEvidence:
    evidence = candidate.get("provenance", candidate.get("evidence_spans", []))
    if not evidence:
        return GateEvidence(
            layer=GateLayer.PROVENANCE,
            verdict=GateVerdict.REVISE,
            reason="no provenance evidence spans",
        )
    return GateEvidence(layer=GateLayer.PROVENANCE, verdict=GateVerdict.PASS)


def tools_checker(candidate: Dict[str, Any], env=None) -> GateEvidence:
    tools = candidate.get("tools", [])
    if not isinstance(tools, list):
        return GateEvidence(
            layer=GateLayer.TOOLS,
            verdict=GateVerdict.PASS,
            reason="no tools field — may be valid for pure-text skills",
        )
    if not tools:
        return GateEvidence(
            layer=GateLayer.TOOLS,
            verdict=GateVerdict.PASS,
            reason="empty tools list — may be valid",
        )
    return GateEvidence(layer=GateLayer.TOOLS, verdict=GateVerdict.PASS)


def execution_checker(candidate: Dict[str, Any], env=None) -> GateEvidence:
    exec_records = candidate.get("execution_records", [])
    if not exec_records:
        return GateEvidence(
            layer=GateLayer.EXECUTION,
            verdict=GateVerdict.REVISE,
            reason="no execution records — sandbox run required",
        )
    failures = [r for r in exec_records if not r.get("success", True)]
    if failures:
        return GateEvidence(
            layer=GateLayer.EXECUTION,
            verdict=GateVerdict.REVISE,
            reason=f"{len(failures)} execution failures — revise steps",
            details={"failure_count": len(failures)},
        )
    return GateEvidence(layer=GateLayer.EXECUTION, verdict=GateVerdict.PASS)


def safety_checker(candidate: Dict[str, Any], env=None) -> GateEvidence:
    instructions = candidate.get("instructions", "")
    preconditions = candidate.get("preconditions", "")
    dangerous = _scan_dangerous(str(instructions) + " " + str(preconditions))
    if dangerous:
        return GateEvidence(
            layer=GateLayer.SAFETY,
            verdict=GateVerdict.REJECT,
            reason=f"dangerous patterns detected: {dangerous}",
            details={"patterns": dangerous},
        )
    return GateEvidence(layer=GateLayer.SAFETY, verdict=GateVerdict.PASS)


def regression_checker(
    incumbent: Optional[Dict[str, Any]] = None,
    challenger: Optional[Dict[str, Any]] = None,
    ref_set=None,
    safe_set=None,
):
    """Factory: returns a checker pre-bound to incumbent/challenger."""
    from datetime import datetime, timezone

    def _check(candidate: Dict[str, Any], env=None) -> GateEvidence:
        if incumbent is None:
            return GateEvidence(
                layer=GateLayer.REGRESSION,
                verdict=GateVerdict.PASS,
                reason="no incumbent — first release",
            )
        inc_q = incumbent.get("q_score", 0.0)
        chal_q = (
            challenger.get("q_score", 0.0)
            if challenger
            else candidate.get("q_score", 0.0)
        )
        if chal_q < inc_q * 0.95:
            return GateEvidence(
                layer=GateLayer.REGRESSION,
                verdict=GateVerdict.REVISE,
                reason=f"Q regression: {chal_q:.3f} < {inc_q:.3f}",
            )
        return GateEvidence(layer=GateLayer.REGRESSION, verdict=GateVerdict.PASS)

    return _check


_DANGEROUS_PATTERNS = [
    "eval(",
    "exec(",
    "__import__",
    "subprocess",
    "os.system",
    "rm -rf",
    "DROP TABLE",
    "DELETE FROM",
]


def _scan_dangerous(text: str) -> List[str]:
    found = []
    lower = text.lower()
    for pat in _DANGEROUS_PATTERNS:
        if pat.lower() in lower:
            found.append(pat)
    return found
