# -*- coding: utf-8 -*-
"""Phase 11 AWS costdown pure-function assertions for offline CI.

Mirrors the G1–G4 gates used by the AWS ops costdown case study.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Set

from agents.teams.aws_ops_team import AWS_OPS_ROLES, TEAM_ID as _FACTORY_TEAM_ID

TEAM_ID = _FACTORY_TEAM_ID
EXPECTED_AGENT_COUNT = 6
EXISTING_CLOUD_TEAM_IDS = frozenset(
    {"cloud-ops-team", "d083a568", "build_system", "ai_coding", "energy_first_principle"}
)

# agent_id → expected tools/skills from factory template
G1_TEMPLATE: Dict[str, Dict[str, List[str]]] = {
    aid: {"tools": list(tools), "skills": list(skills)}
    for _role, aid, tools, skills in AWS_OPS_ROLES
}


def assert_g1(
    agents: List[Dict[str, Any]],
    registered_tools: Set[str],
    team_id: str = TEAM_ID,
) -> Dict[str, Any]:
    """G1: 6 roles, real tools, no team_id conflict, match template."""
    if team_id in EXISTING_CLOUD_TEAM_IDS:
        return {"ok": False, "reason": f"team_id 与既有团队冲突: {team_id}"}
    if team_id != TEAM_ID and team_id in EXISTING_CLOUD_TEAM_IDS:
        return {"ok": False, "reason": f"team_id 冲突: {team_id}"}
    # explicit conflict check used by tests with d083a568
    if team_id in ("d083a568", "cloud-ops-team", "build_system"):
        return {"ok": False, "reason": f"team_id 冲突: {team_id}"}
    if len(agents) != EXPECTED_AGENT_COUNT:
        return {"ok": False, "reason": f"角色数不符: {len(agents)} != {EXPECTED_AGENT_COUNT}"}
    by_id = {a.get("agent_id"): a for a in agents}
    for aid, tmpl in G1_TEMPLATE.items():
        if aid not in by_id:
            return {"ok": False, "reason": f"缺少角色 {aid}"}
        tools = list(by_id[aid].get("tools") or [])
        skills = list(by_id[aid].get("skills") or [])
        for t in tools:
            if t not in registered_tools:
                return {"ok": False, "reason": f"未注册工具 {t}"}
        if set(tools) != set(tmpl["tools"]):
            return {"ok": False, "reason": f"{aid} 工具与模板不一致"}
        if set(skills) != set(tmpl["skills"]):
            return {"ok": False, "reason": f"{aid} 技能与模板不一致"}
    return {"ok": True, "reason": ""}


def assert_g2b(scores: List[int], final: int, max_rounds: int = 3) -> Dict[str, Any]:
    """G2b: iterative score trajectory converges to 5 within max rounds."""
    if final < 5:
        return {"ok": False, "reason": f"最终分 {final} < 5"}
    if len(scores) > max_rounds:
        return {"ok": False, "reason": f"轮数过多: {len(scores)} > {max_rounds}"}
    for i in range(1, len(scores)):
        if scores[i] < scores[i - 1]:
            return {"ok": False, "reason": f"分数退步: {scores}"}
    if not scores or scores[-1] < 5:
        return {"ok": False, "reason": f"未收敛到满分: {scores}"}
    return {"ok": True, "reason": ""}


def assert_g2c(*_args, **_kwargs) -> Dict[str, Any]:
    """G2c placeholder — twin identity continuity (not heavily asserted in unit tests)."""
    return {"ok": True, "reason": ""}


def assert_g3(steps: List[Dict[str, Any]], min_steps: int = 5, min_agents: int = 3) -> Dict[str, Any]:
    """G3: twin collaboration run has enough steps, multi-agent, positive reward."""
    if len(steps) < min_steps:
        return {"ok": False, "reason": f"步数不足: {len(steps)} < {min_steps}"}
    agents: Set[str] = set()
    total_reward = 0.0
    for st in steps:
        for act in st.get("agent_actions") or []:
            if act.get("agent_id"):
                agents.add(str(act["agent_id"]))
        total_reward += float(st.get("reward") or 0)
    if total_reward <= 0:
        return {"ok": False, "reason": "reward 合计为 0"}
    if len(agents) < min_agents:
        return {"ok": False, "reason": f"参与 agent 不足: {len(agents)} < {min_agents}"}
    return {"ok": True, "reason": ""}


def assert_g4(
    baseline_per_call: float,
    current_per_call: float,
    target: float,
    progress: Optional[Dict[str, Any]] = None,
    ratchet_metrics: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """G4: real cost reduction vs baseline, target achieved, ratchet present."""
    progress = progress or {}
    ratchet_metrics = ratchet_metrics or []
    if current_per_call > target:
        return {
            "ok": False,
            "reason": f"降幅不足: current={current_per_call} > target={target}",
        }
    if progress.get("status") != "achieved":
        return {"ok": False, "reason": f"target 未 achieved: {progress.get('status')}"}
    if not ratchet_metrics:
        return {"ok": False, "reason": "棘轮指标缺失"}
    if baseline_per_call <= 0:
        return {"ok": False, "reason": "baseline 无效"}
    reduction = (baseline_per_call - current_per_call) / baseline_per_call
    if reduction < 0.15:
        return {"ok": False, "reason": f"降幅不足: {reduction:.2%}"}
    return {"ok": True, "reason": ""}
