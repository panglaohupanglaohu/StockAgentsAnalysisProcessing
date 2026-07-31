# -*- coding: utf-8 -*-
"""Utility estimation and version comparison — Eqs. 16-20.

Six-factor utility vector: Q, U, R, C, E, A → weighted composite F.
Version comparison with paired trials, LCB, and non-regression gating.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


@dataclass
class UsageRecord:
    """Eq.16: ξ_{i,t} = (y, r, l, e, ι, f, v)."""

    skill_id: str
    success: bool
    reward: float = 0.0
    latency_ms: float = 0.0
    resource_cost: float = 0.0
    human_intervention: bool = False
    failure_type: int = 0
    env_version: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "success": self.success,
            "reward": self.reward,
            "latency_ms": self.latency_ms,
            "resource_cost": self.resource_cost,
            "human_intervention": self.human_intervention,
            "failure_type": self.failure_type,
            "env_version": self.env_version,
        }


@dataclass
class UtilityEstimate:
    skill_id: str
    Q: float = 0.0  # data completeness + provenance fidelity
    U: float = 0.0  # success rate
    R: float = 0.0  # mean reward
    C: float = 0.0  # cross-task reuse
    E: float = 0.0  # latency + resource cost (reversed)
    A: float = 0.0  # aging sensitivity (reversed)
    composite: float = 0.0
    n_trials: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "Q": round(self.Q, 4),
            "U": round(self.U, 4),
            "R": round(self.R, 4),
            "C": round(self.C, 4),
            "E": round(self.E, 4),
            "A": round(self.A, 4),
            "composite": round(self.composite, 4),
            "n_trials": self.n_trials,
        }


class UtilityEstimator:
    """Estimates skill utility from usage records and validation data.

    Eq.17: F(D,i) = w^T x(D,i), where x = (Q, U, R, C, -E, -A)^T.
    Costs E and aging A are negative contributions.
    """

    def __init__(self, weights: Optional[Dict[str, float]] = None):
        self.weights = weights or {
            "Q": 0.20,
            "U": 0.25,
            "R": 0.20,
            "C": 0.15,
            "E": 0.10,
            "A": 0.10,
        }
        self._validate_weights()

    def _validate_weights(self):
        total = sum(self.weights.values())
        if abs(total - 1.0) > 0.01:
            for k in self.weights:
                self.weights[k] /= total

    def estimate(
        self,
        skill_id: str,
        usage_records: List[UsageRecord],
        validation_metadata: Optional[Dict[str, Any]] = None,
    ) -> UtilityEstimate:
        """Compute six-factor utility from usage evidence."""
        if not usage_records:
            return UtilityEstimate(skill_id=skill_id)

        n = len(usage_records)
        successes = sum(1 for r in usage_records if r.success)
        interventions = sum(1 for r in usage_records if r.human_intervention)

        Q = self._estimate_Q(validation_metadata or {})
        U = successes / n if n > 0 else 0.0
        R = np.mean([r.reward for r in usage_records]) if n > 0 else 0.0
        C = self._estimate_C(usage_records)
        E = self._estimate_E(usage_records)
        A = self._estimate_A(usage_records)

        x = np.array([Q, U, R, C, -E, -A])
        w = np.array([self.weights[k] for k in ("Q", "U", "R", "C", "E", "A")])
        composite = float(np.clip(np.dot(w, x) / (np.sum(w) + 1e-8), 0.0, 1.0))

        return UtilityEstimate(
            skill_id=skill_id,
            Q=Q,
            U=U,
            R=R,
            C=C,
            E=E,
            A=A,
            composite=composite,
            n_trials=n,
        )

    @staticmethod
    def _estimate_Q(meta: Dict[str, Any]) -> float:
        completeness = meta.get("field_completeness", 0.0)
        provenance_score = meta.get("provenance_score", 0.0)
        return (completeness + provenance_score) / 2.0

    @staticmethod
    def _estimate_C(records: List[UsageRecord]) -> float:
        if not records:
            return 0.0
        unique_tasks = len(set(r.skill_id for r in records))
        return min(unique_tasks / max(len(records), 1), 1.0)

    @staticmethod
    def _estimate_E(records: List[UsageRecord]) -> float:
        if not records:
            return 0.0
        avg_latency = np.mean([r.latency_ms for r in records])
        avg_cost = np.mean([r.resource_cost for r in records])
        latency_norm = 1.0 / (1.0 + avg_latency / 1000.0)
        cost_norm = 1.0 / (1.0 + avg_cost)
        return float((latency_norm + cost_norm) / 2.0)

    @staticmethod
    def _estimate_A(records: List[UsageRecord]) -> float:
        if not records:
            return 0.0
        env_changes = sum(1 for r in records if r.env_version != records[0].env_version)
        return min(env_changes / max(len(records), 1), 1.0)


class VersionComparator:
    """Paired utility comparison with confidence lower bound.

    Eq.18: Δf_t = f(c;x) - f(s;x), ΔF = (1/N) Σ Δf_t
    Eq.19: LCB_{1-α} = ΔF - t_{1-α,N-1} * s_Δ / √N
    Eq.20: G_r = 1[LCB ≥ δ_min] ∧ C ∧ H
    """

    def __init__(
        self,
        alpha: float = 0.05,
        delta_min: float = 0.0,
        hard_constraints: Optional[Dict[str, Tuple[str, float]]] = None,
    ):
        self.alpha = alpha
        self.delta_min = delta_min
        self.hard_constraints = hard_constraints or {}

    def compare(
        self,
        incumbent: UtilityEstimate,
        challenger: UtilityEstimate,
        paired_diffs: List[float],
    ) -> Dict[str, Any]:
        """Perform paired comparison and return accept/reject decision."""
        if not paired_diffs:
            return {"accepted": False, "reason": "no paired trial data", "LCB": None}

        n = len(paired_diffs)
        mean_diff = np.mean(paired_diffs)
        std_diff = np.std(paired_diffs, ddof=1) if n > 1 else 0.0

        # t-based LCB
        lcb = self._compute_lcb(mean_diff, std_diff, n)

        # Hard constraints
        C_ok, C_reasons = self._check_constraints(incumbent, challenger)

        accepted = lcb >= self.delta_min and C_ok

        return {
            "accepted": accepted,
            "mean_diff": round(float(mean_diff), 4),
            "std_diff": round(float(std_diff), 4),
            "LCB": round(lcb, 4),
            "delta_min": self.delta_min,
            "n_trials": n,
            "constraints_ok": C_ok,
            "constraint_reasons": C_reasons,
        }

    def _compute_lcb(self, mean_diff: float, std_diff: float, n: int) -> float:
        if n <= 1 or std_diff == 0.0:
            return mean_diff
        try:
            t_val = _t_inv_cdf(1.0 - self.alpha, n - 1)
        except Exception:
            t_val = 1.96
        se = std_diff / math.sqrt(n)
        return mean_diff - t_val * se

    def _check_constraints(
        self, incumbent: UtilityEstimate, challenger: UtilityEstimate
    ) -> Tuple[bool, List[str]]:
        reasons = []
        for metric, (direction, epsilon) in self.hard_constraints.items():
            inc_val = getattr(incumbent, metric, 0.0)
            chal_val = getattr(challenger, metric, 0.0)
            if direction == "≥" and chal_val < inc_val - epsilon:
                reasons.append(f"{metric}: {chal_val:.3f} < {inc_val:.3f} - {epsilon}")
            elif direction == "≤" and chal_val > inc_val + epsilon:
                reasons.append(f"{metric}: {chal_val:.3f} > {inc_val:.3f} + {epsilon}")
        return len(reasons) == 0, reasons


def _t_inv_cdf(p: float, df: int) -> float:
    """Approximate t-distribution inverse CDF for given p and df."""
    if df < 1:
        return 1.96
    if df > 30:
        import scipy.stats as stats

        return float(stats.norm.ppf(p))
    import scipy.stats as stats

    return float(stats.t.ppf(p, df))


def compute_paired_diffs(
    incumbent_records: List[UsageRecord], challenger_records: List[UsageRecord]
) -> List[float]:
    """Compute per-trial utility differences for paired comparison (Eq.18)."""
    diffs = []
    for inc, chal in zip(incumbent_records, challenger_records):
        inc_util = _simple_utility(inc)
        chal_util = _simple_utility(chal)
        diffs.append(chal_util - inc_util)
    return diffs


def _simple_utility(r: UsageRecord) -> float:
    score = 0.0
    if r.success:
        score += r.reward * 0.5 + 0.5
    else:
        score -= 0.3
    if not r.human_intervention:
        score += 0.1
    return max(-1.0, min(1.0, score))
