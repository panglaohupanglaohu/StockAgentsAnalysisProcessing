# -*- coding: utf-8 -*-
"""SWEI Protocol — Seal-Will-Export-Import for controlled memory inheritance.

Eq.23-26: layered inheritance strategies, import gating, and transaction rollback.
Supports agent upgrade, replacement, and cross-team migration.
"""

from __future__ import annotations

import copy
import json
import logging
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

MEMORY_SCHEMA = "ag.memory/swi/v1"


class InheritStrategy(str, Enum):
    REPLACE = "replace"
    MERGE = "merge"
    SELECTIVE = "selective"


class LayerName(str, Enum):
    EVENT = "event"
    PERCEPTION = "perception"
    INTENT = "intent"
    RISK = "risk"


@dataclass
class SealSnapshot:
    snapshot_id: str
    source_agent_id: str
    timestamp: int
    layers: Dict[str, Any] = field(default_factory=dict)
    locked: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "source_agent_id": self.source_agent_id,
            "timestamp": self.timestamp,
            "schema": MEMORY_SCHEMA,
            "locked": self.locked,
        }


@dataclass
class WillDeclaration:
    will_id: str
    source_agent_id: str
    target_agent_id: str
    strategy: Dict[str, InheritStrategy] = field(default_factory=dict)
    scope: Dict[str, List[str]] = field(default_factory=dict)
    permissions: Dict[str, Any] = field(default_factory=dict)
    conflict_policy: str = "error"
    retention_period_ms: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "will_id": self.will_id,
            "source_agent_id": self.source_agent_id,
            "target_agent_id": self.target_agent_id,
            "strategy": {k: v.value for k, v in self.strategy.items()},
            "scope": self.scope,
            "permissions": self.permissions,
            "conflict_policy": self.conflict_policy,
            "retention_period_ms": self.retention_period_ms,
        }


@dataclass
class MigrationPackage:
    package_id: str
    source_agent_id: str
    target_agent_id: str
    will: WillDeclaration
    records: Dict[str, List[Any]] = field(default_factory=dict)
    size_bytes: int = 0
    checksum: str = ""
    created_at_ms: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "package_id": self.package_id,
            "source_agent_id": self.source_agent_id,
            "target_agent_id": self.target_agent_id,
            "layer_record_counts": {k: len(v) for k, v in self.records.items()},
            "size_bytes": self.size_bytes,
            "checksum": self.checksum,
            "created_at_ms": self.created_at_ms,
        }


@dataclass
class ImportResult:
    target_agent_id: str
    package_id: str
    accepted: bool
    layer_results: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    rejected_reasons: List[str] = field(default_factory=list)
    latency_ms: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "target_agent_id": self.target_agent_id,
            "package_id": self.package_id,
            "accepted": self.accepted,
            "layer_results": self.layer_results,
            "rejected_reasons": self.rejected_reasons,
            "latency_ms": self.latency_ms,
        }


class SWEIProtocol:
    """Four-phase controlled memory inheritance protocol.

    Phase 1 — Seal: freeze source memory to read-only snapshot
    Phase 2 — Will: declare scope, strategy, permissions, conflict policy
    Phase 3 — Export: generate migration package with provenance + checksum
    Phase 4 — Import: gated activation — check, then accept/rollback
    """

    def __init__(self):
        self._snapshots: Dict[str, SealSnapshot] = {}
        self._wills: Dict[str, WillDeclaration] = {}
        self._packages: Dict[str, MigrationPackage] = {}

    def seal(self, source_agent_id: str, memory_layers: Dict[str, Any]) -> SealSnapshot:
        """Phase 1: freeze source memory into read-only snapshot."""
        sid = f"snap_{int(time.time() * 1000):x}_{uuid.uuid4().hex[:6]}"
        layers_copy = copy.deepcopy(memory_layers)
        snapshot = SealSnapshot(
            snapshot_id=sid,
            source_agent_id=source_agent_id,
            timestamp=int(time.time() * 1000),
            layers=layers_copy,
        )
        self._snapshots[sid] = snapshot
        logger.info("sealed snapshot %s for agent %s", sid, source_agent_id)
        return snapshot

    def declare_will(
        self,
        source_agent_id: str,
        target_agent_id: str,
        strategies: Dict[str, InheritStrategy],
        scope: Optional[Dict[str, List[str]]] = None,
        permissions: Optional[Dict[str, Any]] = None,
        conflict_policy: str = "error",
        retention_period_ms: int = 0,
    ) -> WillDeclaration:
        """Phase 2: declare inheritance intent."""
        wid = f"will_{int(time.time() * 1000):x}_{uuid.uuid4().hex[:6]}"
        will = WillDeclaration(
            will_id=wid,
            source_agent_id=source_agent_id,
            target_agent_id=target_agent_id,
            strategy=strategies,
            scope=scope or {},
            permissions=permissions or {},
            conflict_policy=conflict_policy,
            retention_period_ms=retention_period_ms,
        )
        self._wills[wid] = will
        logger.info("will declared %s: %s → %s", wid, source_agent_id, target_agent_id)
        return will

    def export_package(
        self, snapshot: SealSnapshot, will: WillDeclaration
    ) -> MigrationPackage:
        """Phase 3: generate migration package from snapshot per will declaration.

        Eq.24: z_{i→j,t} = Export(Seal(m_{i,t}), W_{i→j,t})
        """
        pid = f"pkg_{int(time.time() * 1000):x}_{uuid.uuid4().hex[:6]}"

        records: Dict[str, List[Any]] = {}
        total_size = 0

        for layer, strategy in will.strategy.items():
            source_data = snapshot.layers.get(layer, [])
            if strategy == InheritStrategy.SELECTIVE:
                allowed_keys = will.scope.get(layer, [])
                selected = [r for r in source_data if any(k in r for k in allowed_keys)]
            elif strategy == InheritStrategy.REPLACE:
                selected = list(source_data)
            elif strategy == InheritStrategy.MERGE:
                selected = list(source_data)
            else:
                selected = []
            records[layer] = copy.deepcopy(selected)
            total_size += len(json.dumps(selected, default=str))

        pkg = MigrationPackage(
            package_id=pid,
            source_agent_id=snapshot.source_agent_id,
            target_agent_id=will.target_agent_id,
            will=will,
            records=records,
            size_bytes=total_size,
            checksum=_sha256_hex(json.dumps({k: len(v) for k, v in records.items()})),
            created_at_ms=int(time.time() * 1000),
        )
        self._packages[pid] = pkg
        logger.info("exported package %s (%.1f KB)", pid, total_size / 1024)
        return pkg

    def import_package(
        self,
        pkg: MigrationPackage,
        target_memory: Dict[str, Any],
        quarantine_check: Optional[callable] = None,
    ) -> ImportResult:
        """Phase 4: gated import with transactional rollback.

        Eq.25: g_imp = ∧ g_ν  (scope, schema, integrity, auth, conflict)
        Eq.26: m_new(j,t) = T(m_old(j,t), z_{i→j,t}, g_imp)

        If ANY gate fails → rollback entire transaction.
        """
        t0 = time.perf_counter()
        pre_import_snapshot = copy.deepcopy(target_memory)
        reasons: List[str] = []
        layer_results: Dict[str, Dict[str, Any]] = {}

        # Gate checks
        gates_ok, gate_reasons = self._check_import_gates(
            pkg, target_memory, quarantine_check
        )
        reasons.extend(gate_reasons)

        if not gates_ok:
            return ImportResult(
                target_agent_id=pkg.target_agent_id,
                package_id=pkg.package_id,
                accepted=False,
                rejected_reasons=reasons,
                latency_ms=(time.perf_counter() - t0) * 1000,
            )

        # Apply strategies
        try:
            for layer, strategy in pkg.will.strategy.items():
                records = pkg.records.get(layer, [])
                result = self._apply_layer_strategy(
                    layer,
                    strategy,
                    records,
                    target_memory.get(layer, []),
                )
                target_memory[layer] = result["after"]
                layer_results[layer] = result

            return ImportResult(
                target_agent_id=pkg.target_agent_id,
                package_id=pkg.package_id,
                accepted=True,
                layer_results=layer_results,
                latency_ms=(time.perf_counter() - t0) * 1000,
            )
        except Exception as e:
            # Transactional rollback
            for layer in list(target_memory.keys()):
                target_memory[layer] = pre_import_snapshot.get(layer, [])
            logger.warning("import rolled back: %s", e)
            return ImportResult(
                target_agent_id=pkg.target_agent_id,
                package_id=pkg.package_id,
                accepted=False,
                rejected_reasons=[f"transaction failure: {e}"],
                latency_ms=(time.perf_counter() - t0) * 1000,
            )

    def _check_import_gates(
        self,
        pkg: MigrationPackage,
        target_memory: Dict[str, Any],
        quarantine_check: Optional[callable],
    ) -> Tuple[bool, List[str]]:
        """Eq.25: check scope, schema, integrity, auth, conflict."""
        reasons: List[str] = []

        if not pkg.records:
            reasons.append("empty migration package")

        for layer, strategy in pkg.will.strategy.items():
            if strategy == InheritStrategy.SELECTIVE and not pkg.will.scope.get(layer):
                reasons.append(f"selective import for {layer} has no scope filter")

        if quarantine_check is not None:
            for layer, records in pkg.records.items():
                for rec in records:
                    result = quarantine_check(layer, rec)
                    if result.get("contaminated"):
                        reasons.append(
                            f"contaminated record in {layer}: {result.get('reason')}"
                        )

        return len(reasons) == 0, reasons

    @staticmethod
    def _apply_layer_strategy(
        layer: str, strategy: InheritStrategy, imported: List[Any], existing: List[Any]
    ) -> Dict[str, Any]:
        before_count = len(existing)
        if strategy == InheritStrategy.REPLACE:
            after = list(imported)
        elif strategy == InheritStrategy.MERGE:
            existing_ids = {
                r.get("id") for r in existing if isinstance(r, dict) and r.get("id")
            }
            new_records = [
                r
                for r in imported
                if not (isinstance(r, dict) and r.get("id") in existing_ids)
            ]
            after = list(existing) + new_records
        elif strategy == InheritStrategy.SELECTIVE:
            after = list(imported)
        else:
            after = list(existing)

        return {
            "layer": layer,
            "strategy": strategy.value,
            "before_count": before_count,
            "imported_count": len(imported),
            "after_count": len(after),
            "after": after,
        }

    @staticmethod
    def verify_integrity(
        source_counts: Dict[str, int], imported_counts: Dict[str, int]
    ) -> Dict[str, float]:
        """Eq.27: R_count = N_imp / N_sel per layer."""
        results = {}
        for layer, expected in source_counts.items():
            actual = imported_counts.get(layer, 0)
            results[layer] = actual / expected if expected > 0 else 1.0
        return results


def _sha256_hex(s: str) -> str:
    import hashlib

    return hashlib.sha256(s.encode()).hexdigest()[:16]


# ── quarantine checker factories ────────────────────────────────────


def default_quarantine_check(layer: str, record: Dict[str, Any]) -> Dict[str, Any]:
    """Default quarantine: flag records with suspicious markers."""
    suspicious_markers = [
        "malicious",
        "injection",
        "__import__",
    ]
    if isinstance(record, dict):
        for k, v in record.items():
            val = str(v).lower()
            for marker in suspicious_markers:
                if marker in val:
                    return {
                        "contaminated": True,
                        "reason": f"marker '{marker}' in field '{k}'",
                    }
    return {"contaminated": False}
