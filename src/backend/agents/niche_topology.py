# -*- coding: utf-8 -*-
"""12-Niche topology and cross-role CHALLENGE routing — Eq.4.

Inner ring: direct execution knowledge (target, tools, steps, preconditions)
Middle ring: inspection & safety (detection, failure modes, risk, rollback)
Outer ring: provenance & governance (source, version, audit, changelog)
Host: agenda control (not occupying any Niche)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple


class ORIDStage(str, Enum):
    OBJECTIVE = "O"  # facts, environment, tools
    REFLECTIVE = "R"  # risks, unknowns, failure modes
    INTERPRETIVE = "I"  # alternative interpretations, causal chains
    DECISIONAL = "D"  # candidate plans, consensus


class NicheRing(str, Enum):
    INNER = "inner"
    MIDDLE = "middle"
    OUTER = "outer"


@dataclass
class NicheDefinition:
    niche_id: str
    name: str
    ring: NicheRing
    knowledge_function: str
    supports_fields: List[str] = field(default_factory=list)
    challenge_target: Optional[ORIDStage] = None


class RitualSignal(str, Enum):
    SUPPLEMENT = "SUPPLEMENT"
    CHALLENGE = "CHALLENGE"
    AGREE = "AGREE"
    COURT = "COURT"
    DIGRESS = "DIGRESS"


TWELVE_NICHE: Dict[str, NicheDefinition] = {
    "N_TARGET": NicheDefinition(
        "N_TARGET",
        "target_objective",
        NicheRing.INNER,
        "task goal definition",
        ["name", "description"],
    ),
    "N_TOOLS": NicheDefinition(
        "N_TOOLS",
        "tool_inventory",
        NicheRing.INNER,
        "available tools & APIs",
        ["tools"],
    ),
    "N_STEPS": NicheDefinition(
        "N_STEPS",
        "step_sequence",
        NicheRing.INNER,
        "execution step order",
        ["instructions"],
    ),
    "N_PRECOND": NicheDefinition(
        "N_PRECOND",
        "precondition_gate",
        NicheRing.INNER,
        "preconditions for execution",
        ["preconditions"],
        challenge_target=ORIDStage.OBJECTIVE,
    ),
    "N_DETECT": NicheDefinition(
        "N_DETECT",
        "failure_detection",
        NicheRing.MIDDLE,
        "detection conditions & monitoring",
        ["postconditions"],
        challenge_target=ORIDStage.REFLECTIVE,
    ),
    "N_FAILMODES": NicheDefinition(
        "N_FAILMODES",
        "failure_modes",
        NicheRing.MIDDLE,
        "known failure modes",
        [],
        challenge_target=ORIDStage.REFLECTIVE,
    ),
    "N_RISK": NicheDefinition(
        "N_RISK",
        "risk_constraints",
        NicheRing.MIDDLE,
        "risk boundaries & constraints",
        [],
        challenge_target=ORIDStage.REFLECTIVE,
    ),
    "N_ROLLBACK": NicheDefinition(
        "N_ROLLBACK",
        "rollback_rules",
        NicheRing.MIDDLE,
        "rollback procedures",
        [],
        challenge_target=ORIDStage.REFLECTIVE,
    ),
    "N_SOURCE": NicheDefinition(
        "N_SOURCE",
        "source_origin",
        NicheRing.OUTER,
        "provenance & evidence",
        ["provenance", "evidence_spans"],
        challenge_target=ORIDStage.OBJECTIVE,
    ),
    "N_VERSION": NicheDefinition(
        "N_VERSION",
        "version_control",
        NicheRing.OUTER,
        "version tracking",
        ["version", "lineage"],
    ),
    "N_AUDIT": NicheDefinition(
        "N_AUDIT",
        "audit_log",
        NicheRing.OUTER,
        "change audit trail",
        [],
    ),
    "N_CHANGELOG": NicheDefinition(
        "N_CHANGELOG",
        "change_log",
        NicheRing.OUTER,
        "revision history",
        [],
    ),
}


@dataclass
class NicheMapping:
    agent_id: str
    role: str
    niches: Set[str] = field(default_factory=set)


class NicheRouter:
    """Eq.4: η_k ⊆ A_k × R_k × N_k, challenge routing Γ_k.

    Maps agents to Niche knowledge-function positions and routes
    CHALLENGE signals back to the appropriate ORID stage.
    """

    def __init__(self):
        self._mappings: Dict[str, NicheMapping] = {}

    def assign_niches(
        self, agent_id: str, role: str, niche_ids: List[str]
    ) -> NicheMapping:
        mapping = NicheMapping(agent_id=agent_id, role=role, niches=set(niche_ids))
        self._mappings[agent_id] = mapping
        return mapping

    def route_challenge(
        self, niche_id: str, current_stage: ORIDStage
    ) -> Optional[ORIDStage]:
        """Route CHALLENGE from a Niche back to the target ORID stage.

        Eq.4: (target_niche, current_stage, CHALLENGE, target_stage) ∈ Γ_k
        """
        niche = TWELVE_NICHE.get(niche_id)
        if niche is None:
            return None
        return niche.challenge_target or current_stage

    def get_agent_niches(self, agent_id: str) -> Set[str]:
        mapping = self._mappings.get(agent_id)
        return mapping.niches if mapping else set()

    def get_niche_agents(self, niche_id: str) -> List[str]:
        return [aid for aid, m in self._mappings.items() if niche_id in m.niches]

    def compute_source_role_entropy(
        self, field_assignments: List[Dict[str, Any]]
    ) -> float:
        """Compute entropy of role contributions to field sources.

        Higher entropy → more diverse role participation.
        """
        role_counts: Dict[str, int] = {}
        for fa in field_assignments:
            role = fa.get("role", "unknown")
            role_counts[role] = role_counts.get(role, 0) + 1

        total = sum(role_counts.values())
        if total == 0:
            return 0.0

        entropy = 0.0
        for count in role_counts.values():
            p = count / total
            if p > 0:
                entropy -= p * (p**0.5)
        return entropy

    def compute_single_role_dominance(
        self, field_assignments: List[Dict[str, Any]]
    ) -> float:
        """Fraction of fields dominated by a single role."""
        role_counts: Dict[str, int] = {}
        for fa in field_assignments:
            role = fa.get("role", "unknown")
            role_counts[role] = role_counts.get(role, 0) + 1
        if not role_counts:
            return 0.0
        return max(role_counts.values()) / sum(role_counts.values())


NICHE_FIELD_MAP: Dict[str, List[str]] = {
    niche.niche_id: niche.supports_fields for niche in TWELVE_NICHE.values()
}


def get_field_niches(field_name: str) -> List[str]:
    """Which Niche positions typically inform a given skill field."""
    return [nid for nid, fields in NICHE_FIELD_MAP.items() if field_name in fields]
