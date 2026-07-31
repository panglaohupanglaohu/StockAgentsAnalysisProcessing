# 研究分析 — researcher

任务: 建立基于混沌工程的稳定性测试集，验证Spot实例、缓存及数据分层策略下的SLO达标情况
步骤: research
Agent: build_researcher

---

📋 任务: e0c257fa-606
🤖 Agent: Researcher (researcher)
📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
🔧 执行方式: DeepSeek API (直连)
⏱️ 超时: 1200s
────────────────────────────────────────────────────────────
📝 提示词:
  你是 AgentsGroup2026 系统的 Researcher (researcher)。
  请执行以下开发任务:
  
  你是技术研究员。请对以下任务进行技术调研:
  
  ## 任务
  建立基于混沌工程的稳定性测试集，验证Spot实例、缓存及数据分层策略下的SLO达标情况
  负责角色: 测试工程师
  依赖: 任务1、3完成
  预期产出: 自动化测试报告，包含成本-质量双维度验收标准
  负责角色: 测试工程师
  依赖: 任务1、3完成
  预期产出: 自动化测试报告，包含成本-质量双维度验收标准
  
  ## 📂 项目上下文 (系统自动预加载)
  
  ### 项目文件结构 (src/ 目录)
  ```
  src/frontend/agent-team-config.html
  src/frontend/datacenter-ratchet-evolution.html
  src/frontend/digital-twin-cli.html
  src/frontend/extraction-pipeline.html
  src/frontend/index.html
  src/frontend/login.html
  src/frontend/plaza.html
  src/frontend/sandbox-twin.html
  src/frontend/skill-extract.html
  src/frontend/system-evolution.html
  src/frontend/tasks.html
  src/frontend/css/agent-team-config.css
  src/frontend/css/openbridge-theme.css
  src/frontend/css/skill-extract-timeline.css
  src/frontend/css/skill-extract.css
  src/frontend/css/variables.css
  src/frontend/css/ws-theme-bridge.css
  src/frontend/js/agent-detail.js
  src/frontend/js/agent-team-config.js
  src/frontend/js/api.js
  src/frontend/js/digital-twin-cli-3d.js
  src/frontend/js/digital-twin-cli.js
  src/frontend/js/global-nav.js
  src/frontend/js/i18n.js
  src/frontend/js/nav-sidebar.js
  src/frontend/js/plaza.js
  src/frontend/js/sandbox-twin.js
  src/frontend/js/sessions-runtime.js
  src/frontend/js/skill-extract-timeline.js
  src/frontend/js/skill-extract.js
  src/frontend/js/system-evolution.js
  src/frontend/js/tasks-view.js
  src/frontend/js/token-factory.js
  src/frontend/js/tools-skills.js
  src/frontend/js/utils.js
  src/frontend/js/wizard.js
  src/backend/__init__.py
  src/backend/agent_team_api.py
  src/backend/config.py
  src/backend/main.py
  src/backend/main.py.bak
  src/backend/server.log
  src/backend/startup_check.py
  src/backend/startup_validator.py
  src/backend/tests/__init__.py
  src/backend/tests/conftest.py
  src/backend/tests/conftest.py.bak
  src/backend/tests/test_ab_testing.py
  src/backend/tests/test_agent_skill_binding.py
  src/backend/tests/test_agent_toolbox.py
  src/backend/tests/test_evolution_race.py
  src/backend/tests/test_evolution_race.py.bak
  src/backend/tests/test_fingerprint.py
  src/backend/tests/test_fingerprint.py.bak
  src/backend/tests/test_gate_evaluator.py
  src/backend/tests/test_gate_evaluator.py.bak
  src/backend/tests/test_main_health.py
  src/backend/tests/test_merge_plugin.py
  src/backend/tests/test_merge_plugin.py.bak
  src/backend/tests/test_models.py
  src/backend/tests/test_models.py.bak
  src/backend/tests/test_operation_store.py
  src/backend/tests/test_permissions_and_secrets.py
  src/backend/tests/test_plan_loop_runtime.py
  src/backend/tests/test_plaza_dispatch.py
  src/backend/tests/test_plaza_evolution_bridge.py
  src/backend/tests/test_plaza_task_artifact_bridge.py
  src/backend/tests/test_qa_gate_pipeline.py
  src/backend/tests/test_qa_gate_pipeline.py.bak
  src/backend/tests/test_review_integration.py
  src/backend/tests/test_review_integration.py.bak
  src/backend/tests/test_sandbox_security.py
  src/backend/tests/test_task_engine.py
  src/backend/tests/test_task_engine.py.bak
  src/backend/tests/test_team_manager.py
  src/backend/tests/test_team_manager.py.bak
  src/backend/tests/test_template_variants.py
  src/backend/tests/test_template_variants.py.bak
  src/backend/tests/test_token_budget.py
  src/backend/tests/test_unified_tool_loop.py
  src/backend/agents/__init__.py
  src/backend/agents/ab_testing.py
  src/backend/agents/agent_loop.py
  src/backend/agents/agent_toolbox.py
  src/backend/agents/api.py
  src/backend/agents/api.py.bak
  src/backend/agents/audit_store.py
  src/backend/agents/chat_harness.py
  src/backend/agents/domain_events.py
  src/backend/agents/domain_events.py.bak
  src/backend/agents/event_bus.py
  src/backend/agents/execution_registry.py
  src/backend/agents/extraction_models.py
  src/backend/agents/extraction_pipeline.py
  src/backend/agents/extraction_pipeline.py.bak
  src/backend/agents/extraction_routes.py
  src/backend/agents/extraction_store.py
  src/backend/agents/fingerprint.py
  src/backend/agents/fingerprint.py.bak
  src/backend/agents/gate_evaluator.py
  src/backend/agents/hermes_research.py
  src/backend/agents/knowledge_base.py
  src/backend/agents/merge_engine.py
  src/backend/agents/merge_models.py
  src/backend/agents/models.py
  src/backend/agents/models.py.bak
  src/backend/agents/operation_api.py
  src/backend/agents/operation_models.py
  src/backend/agents/operation_store.py
  src/backend/agents/plaza.py
  src/backend/agents/plaza.py.bak
  src/backend/agents/plaza_engine.py
  src/backend/agents/plaza_routes.py
  src/backend/agents/plaza_routes.py.bak
  src/backend/agents/plaza_store.py
  src/backend/agents/review_models.py
  src/backend/agents/review_routes.py
  src/backend/agents/review_service.py
  src/backend/agents/secret_store.py
  src/backend/agents/session_store.py
  src/backend/agents/similarity_engine.py
  src/backend/agents/skill_evolver.py
  src/backend/agents/skill_extract_ws.py
  src/backend/agents/skill_extractor.py
  src/backend/agents/skill_indexer.py
  src/backend/agents/skill_library.py
  src/backend/agents/skill_querier.py
  src/backend/agents/skill_registry.py
  src/backend/agents/skill_router.py
  src/backend/agents/skill_router_routes.py
  src/backend/agents/skill_store.py
  src/backend/agents/skill_tracker.py
  src/backend/agents/skill_verifier.py
  src/backend/agents/task_engine.py
  src/backend/agents/task_engine.py.bak
  src/backend/agents/task_store.py
  src/backend/agents/team_manager.py
  src/backend/agents/team_manager.py.bak
  src/backend/agents/team_store.py
  src/backend/agents/tool_executor.py
  src/backend/agents/tool_registry.py
  src/backend/agents/trajectory_analyzer.py
  src/backend/agents/tts_routes.py
  src/backend/agents/security/__init__.py
  src/backend/agents/security/permission_resolver.py
  src/backend/agents/runtime/__init__.py
  src/backend/agents/runtime/events.py
  src/backend/agents/runtime/plan_loop.py
  src/backend/agents/runtime/tool_loop.py
  src/backend/agents/evolution/__init__.py
  ... (共 969 个 src/ 文件)
  
  ```
  
  ### 文件: `src/backend/agent_team_api.py`
  ```py
  # -*- coding: utf-8 -*-
  """
  Agent Team API Routes - 双团队管理 REST API
  
  提供构建团队 & 执行团队的状态查询、KPI 考核、
  任务分配、报告查询等端点。挂载至 FastAPI 的 router。
  """
  
  from __future__ import annotations
  
  from fastapi import APIRouter, HTTPException, Query
  from pydantic import BaseModel
  from typing import Any, Dict, List, Optional
  
  router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
  
  
  # ---------------------------------------------------------------------------
  # 全局引用（在 main.py startup 时注入）
  # ---------------------------------------------------------------------------
  _build_team = None
  _execution_team = None
  _scheduler = None
  _evolution_engine = None
  
  
  def set_teams(build_team, execution_team, scheduler, evolution_engine=None):
      """在应用启动时由 main.py 调用，注入团队实例."""
      global _build_team, _execution_team, _scheduler, _evolution_engine
      _build_team = build_team
      _execution_team = execution_team
      _scheduler = scheduler
      _evolution_engine = evolution_engine
  
  
  # ---------------------------------------------------------------------------
  # Request / Response Models
  # ---------------------------------------------------------------------------
  
  class TaskAssignment(BaseModel):
      agent_id: str
      task: str
  
  class FeedbackSubmission(BaseModel):
      category: str = "optimization"
      severity: str = "medium"
      title: str
      detail: str
  
  
  # ---------------------------------------------------------------------------
  # Scheduler
  # ---------------------------------------------------------------------------
  
  @router.get("/scheduler/status")
  async def scheduler_status():
      if not _scheduler:
          raise HTTPException(503, "Scheduler not initialized")
      return _scheduler.get_status()
  
  
  @router.post("/scheduler/report")
  async def scheduler_generate_report():
      if not _scheduler:
          raise HTTPException(503, "Scheduler not initialized")
      return _scheduler.generate_report_now()
  
  
  @router.post("/scheduler/tick")
  async def scheduler_tick_once():
      """手动触发一次调度 tick (调试用)."""
      if not _scheduler:
          raise HTTPException(503, "Scheduler not initialized")
      return _scheduler.tick_once()
  
  
  # ---------------------------------------------------------------------------
  # Build Team
  # ---------------------------------------------------------------------------
  
  @router.get("/build/status")
  async def build_team_status():
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      return _build_team.get_status()
  
  
  @router.get("/build/kpis")
  async def build_team_kpis():
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      return _build_team.get_agent_kpis()
  
  
  @router.get("/build/agents/{agent_id}")
  async def build_agent_detail(agent_id: str):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      agent = _build_team.agents.get(agent_id)
      if not agent:
          raise HTTPException(404, f"Agent '{agent_id}' not found")
      return agent.to_dict()
  
  
  @router.post("/build/assign")
  async def build_assign_task(body: TaskAssignment):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      ok = _build_team.assign_task(body.agent_id, body.task)
      if not ok:
          raise HTTPException(404, f"Agent '{body.agent_id}' not found")
      return {"status": "assigned", "agent_id": body.agent_id, "task": body.task}
  
  
  @router.get("/build/reports")
  async def build_reports(limit: int = 10):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      reports = _build_team.hourly_reports[-limit:]
      return [r.to_dict() for r in reports]
  
  
  @router.get("/build/issues")
  async def build_issues():
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      return _build_team.issue_backlog
  
  
  # ---------------------------------------------------------------------------
  # Execution Team
  # ---------------------------------------------------------------------------
  
  @router.get("/execution/status")
  async def execution_team_status():
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      return _execution_team.get_status()
  
  
  @router.get("/execution/agents/{agent_id}")
  async def execution_agent_detail(agent_id: str):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      agent = _execution_team.agents.get(agent_id)
      if not agent:
          raise HTTPException(404, f"Agent '{agent_id}' not found")
      return agent.to_dict()
  
  
  @router.get("/execution/reports")
  async def execution_reports(limit: int = 10):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      reports = _execution_team.execution_reports[-limit:]
      return [r.to_dict() for r in reports]
  
  
  @router.get("/execution/feedback")
  async def execution_feedback():
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      return [item.to_dict() for item in _execution_team.feedback_queue]
  
  
  @router.post("/execution/feedback")
  async def submit_feedback(body: FeedbackSubmission):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      item = _execution_team.submit_feedback(
          category=body.category,
          severity=body.severity,
          title=body.title,
          detail=body.detail,
      )
      return item.to_dict()
  
  
  # ---------------------------------------------------------------------------
  # Combined
  # ---------------------------------------------------------------------------
  
  @router.get("/overview")
  async def teams_overview(team_id: Optional[str] = None):
      """一站式获取双团队全局概览."""
      result: Dict[str, Any] = {}
      if _build_team:
          bs = _build_team.get_status()
          result["build_team"] = {
              "health": bs["health"],
              "agent_count": bs["agent_count"],
              "metrics": bs["metrics"],
          }
      if _execution_team:
          es = _execution_team.get_status()
          result["execution_team"] = {
              "health": es["health"],
              "agent_count": es["agent_count"],
              "metrics": es["metrics"],
          }
      if _scheduler:
          result["scheduler"] = _scheduler.get_status()
      if _evolution_engine:
          result["evolution"] = {
              **_evolution_engine.get_status(),
              "compliance_rating": _serialize_compliance_rating(),
          }
      if team_id:
          result["current_team"] = _serialize_current_team(team_id)
      return result
  
  
  def _serialize_current_team(team_id: str) -> Optional[Dict[str, Any]]:
      try:
          from .agents.api import _summarize_team_tasks, _team_manager
      except ImportError:
          from agents.api import _summarize_team_tasks, _team_manager
  
      if _team_manager is None:
          return None
  
      team = _team_manager.get_team(team_id)
      if team is None:
          return None
  
      return {
          **team.to_dict(),
          "tasks": _summarize_team_tasks(team_id),
      }
  
  
  # ---------------------------------------------------------------------------
  # System Evolution (自我演进引擎)
  # ---------------------------------------------------------------------------
  
  @router.get("/evolution/status")
  async def evolution_status():
      """获取自我演进引擎状态。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      status = _evolution_engine.get_status()
      return {
          "status": "initialized" if status.get("initialized") else "not_initialized",
          **status,
      }
  
  
  @router.get("/evolution/summary")
  async def evolution_summary():
      """获取演进项汇总。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_evolution_summary()
  
  
  @router.get("/evolution/items")
  async def evolution_items(status: Optional[str] = None, limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
      """获取演进项列表，可按状态过滤、分页。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      items = _evolution_engine.get_evolution_items(status=status)
      total = len(items)
      sliced = items[offset:offset + limit]
      return {
          "items": sliced,
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  @router.get("/evolution/rules")
  async def evolution_rules(limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
      """获取审查规则列表（分页）。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      items = [r.to_dict() for r in _evolution_engine.audit_rules]
      total = len(items)
      sliced = items[offset:offset + limit]
      return {
          "items": sliced,
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  @router.post("/evolution/audit")
  async def evolution_run_audit():
      """手动触发一次审查。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.run_full_audit()
  
  
  @router.post("/evolution/cycle")
  async def evolution_run_cycle():
      """运行完整演进周期（审查→派发→验证→关闭）。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.run_evolution_cycle()
  
  
  @router.post("/evolution/dispatch")
  async def evolution_dispatch():
      """派发所有待处理演进项给 Build 团队。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.dispatch_all_pending()
  
  
  @router.post("/evolution/verify")
  async def evolution_verify():
      """验证所有待验证项。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.verify_all_pending()
  
  
  @router.get("/evolution/items/{item_id}")
  async def evolution_item_detail(item_id: str):
      """获取单个演进项详情。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      item = _evolution_engine.evolution_items.get(item_id)
      if not item:
          raise HTTPException(404, f"Item '{item_id}' not found")
      return item.to_dict()
  
  
  @router.post("/evolution/items/{item_id}/progress")
  async def evolution_mark_progress(item_id: str):
      """标记演进项为进行中。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      ok = _evolution_engine.mark_in_progress(item_id)
      if not ok:
          raise HTTPException(404, f"Item '{item_id}' not found")
      return {"status": "ok", "item_id": item_id, "new_status": "in_progress"}
  
  
  @router.post("/evolution/items/{item_id}/complete")
  async def evolution_mark_complete(item_id: str):
      """标记演进项构建完成，进入待验证。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      ok = _evolution_engine.mark_build_complete(item_id)
      if not ok:
          raise HTTPException(404, f"Item '{item_id}' not found")
      return {"status": "ok", "item_id": item_id, "new_status": "verify_pending"}
  
  
  @router.post("/evolution/close-verified")
  async def evolution_close_verified():
      """关闭所有已验证通过的演进项。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      closed = _evolution_engine.close_verified()
      return {"closed": closed, "count": len(closed)}
  
  
  @router.post("/evolution/close")
  async def evolution_close():
      """关闭所有已验证通过的演进项 (close-verified 别名)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      closed = _evolution_engine.close_verified()
      return {"closed": closed, "count": len(closed)}
  
  
  @router.get("/evolution/history")
  async def evolution_audit_history(limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
      """获取审查历史记录（分页）。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      raw = _evolution_engine.get_audit_history()
      # Normalize field names for frontend (expects timestamp, total)
      result = []
      for h in raw:
          entry = dict(h)
          entry.setdefault("timestamp", entry.pop("time", None))
          entry.setdefault("total", (entry.get("passed") or 0) + (entry.get("failed") or 0) + (entry.get("skipped") or 0))
          result.append(entry)
      total = len(result)
      sliced = result[offset:offset + limit]
      return {
          "items": sliced,
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  @router.get("/evolution/analytics")
  async def evolution_analytics():
      """获取演进分析数据 (域覆盖、严重度分布、趋势)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      summary = _evolution_engine.get_evolution_summary()
      history = _evolution_engine.get_audit_history()
      status = _evolution_engine.get_status()
  
      return {
          "summary": summary,
          "history": history,
          "stats": status.get("stats", {}),
          "items_by_status": status.get("items_by_status", {}),
          "rules_count": status.get("audit_rules_count", 0),
      }
  
  
  # ---------------------------------------------------------------------------
  # Phase 3: 业界标准化改进 API
  # ---------------------------------------------------------------------------
  
  @router.get("/evolution/compliance-rating")
  async def evolution_compliance_rating():
      """获取 DNV CII 风格 A~E 合规评级。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _serialize_compliance_rating()
  
  
  def _serialize_compliance_rating() -> Dict[str, Any]:
      data = _evolution_engine.get_compliance_rating()
      data["grade"] = data.get("rating", "?")
      data["description"] = data.get("rating_label", "")
      escalation = _evolution_engine.get_escalation_status()
      data["escalation_tier"] = "corrective" if escalation.get("escalated_count", 0) > 0 else "normal"
      return data
  
  
  @router.post("/evolution/compliance-rating/calculate")
  async def evolution_calculate_rating():
      """重新计算合规评级 (运行快速审查)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.calculate_compliance_rating()
  
  
  @router.get("/evolution/checklist")
  async def evolution_checklist(level: Optional[str] = None):
      """获取 ClassNK 双层自查清单 (company/ship)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_checklist(level=level)
  
  
  @router.get("/evolution/zones")
  async def evolution_zones():
      """获取所有合规区域。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_all_zones()
  
  
  @router.get("/evolution/zones/active")
  async def evolution_active_zones():
      """获取当前激活的合规区域
  ```
  
  ### 文件: `src/backend/tests/conftest.py`
  ```py
  # -*- coding: utf-8 -*-
  """pytest 共享 Fixtures — 测试流水线基础设施."""
  
  from __future__ import annotations
  
  import json
  import os
  import sys
  import tempfile
  from pathlib import Path
  from typing import Any, Dict
  from unittest.mock import AsyncMock, MagicMock, patch
  
  import pytest
  from fastapi.testclient import TestClient
  
  # Ensure src/backend is in path
  _backend_root = Path(__file__).resolve().parent.parent
  if str(_backend_root) not in sys.path:
      sys.path.insert(0, str(_backend_root))
  
  
  @pytest.fixture
  def sample_lamport_clock():
      """提供一个标准的 Lamport 时钟实例."""
      from agents.ab_testing import LamportClock
      return LamportClock(node_id="test-node-1")
  
  
  @pytest.fixture
  def default_ewma_config():
      """提供默认 EWMA 配置."""
      from agents.ab_testing import EWMAConfig
      return EWMAConfig()
  
  
  @pytest.fixture
  def default_ewma_engine(default_ewma_config):
      """提供默认 EWMA 阈值引擎."""
      from agents.ab_testing import EWMAThresholdEngine
      return EWMAThresholdEngine(config=default_ewma_config)
  
  
  @pytest.fixture
  def sample_ab_metrics():
      """提供示例 A/B 测试指标."""
      from agents.ab_testing import ABTestMetrics
      return ABTestMetrics(
          false_upgrade_rate=0.05,
          resource_increase_pct=12.0,
          behavior_fingerprint_mutation_rate=0.02,
          anomaly_propagation_depth=1.5,
          prediction_error_rate=0.08,
          energy_increase_pct=3.0,
          temperature_slope=0.01,
          policy_evaluation_latency_ms=45.0,
          evolution_stagnation_rate=0.03,
      )
  
  
  @pytest.fixture
  def temp_team_store():
      """使用临时文件的 TeamStore (测试后自动清理)."""
      from agents.team_store import TeamStore
  
      with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
          f.write("{}")
          tmp_path = Path(f.name)
  
      store = TeamStore(path=tmp_path)
      yield store
  
      # 清理
      if tmp_path.exists():
          tmp_path.unlink(missing_ok=True)
  
  
  @pytest.fixture
  def temp_task_store():
      """使用临时目录的 TaskStore."""
      from agents.task_store import TaskStore
  
      with tempfile.TemporaryDirectory() as tmpdir:
          store = TaskStore(base_dir=Path(tmpdir))
          yield store
  
  
  @pytest.fixture
  def team_manager(temp_team_store):
      """提供 TeamManager 实例 (使用临时存储)."""
      from agents.team_manager import TeamManager
      return TeamManager(store=temp_team_store)
  
  
  @pytest.fixture
  def sample_team_dict():
      """示例团队字典."""
      return {
          "team_id": "test-team-001",
          "name": "测试团队",
          "description": "自动化测试团队",
      }
  
  
  @pytest.fixture
  def sample_agent_dict():
      """示例 AgentProfile 字典."""
      return {
          "agent_id": "agent-001",
          "name": "TestAgent",
          "role": "developer",
          "state": "idle",
      }
  
  
  @pytest.fixture
  def sample_model_dict():
      """示例 ModelConfig 字典."""
      return {
          "model_id": "model-001",
          "name": "deepseek-v4-test",
          "provider": "deepseek",
          "max_tokens": 65536,
          "temperature": 0.7,
          "is_default": True,
      }
  
  
  @pytest.fixture
  def task_engine():
      """提供 TaskEngine 实例."""
      from agents.task_engine import TaskEngine
      from agents.task_store import TaskStore
      with tempfile.TemporaryDirectory() as tmpdir:
          yield TaskEngine(max_concurrency=4, store=TaskStore(base_dir=Path(tmpdir)))
  
  
  @pytest.fixture
  def fastapi_client() -> TestClient:
      """提供 FastAPI TestClient (自动设置环境变量)."""
      # 确保测试时不连真实 LLM
      os.environ.setdefault("DEEPSEEK_API_KEY", "test-key-not-real")
      os.environ.setdefault("OPENAI_API_KEY", "test-key-not-real")
  
      # Mock 掉 LLM 相关依赖，避免真实请求
      from main import app
      return TestClient(app)
  
  
  @pytest.fixture
  def mock_llm_call():
      """Mock LLM 调用，返回固定响应."""
      with patch("agents.chat_harness.call_llm", new_callable=AsyncMock) as mock:
          mock.return_value = "这是模拟的 LLM 回复"
          yield mock
  
  
  @pytest.fixture
  def sample_task_dict():
      """示例任务字典."""
      return {
          "task_id": "task-001",
          "title": "测试任务",
          "description": "一个用于测试的任务",
          "agent_id": "agent-001",
          "priority": 2,
          "dependencies": [],
      }
  
  
  # ── pytest 配置 ─────────────────────────────────────────────
  
  pytest_plugins = []  # 可在此添加 pytest 插件
  
  ```
  
  ### 文件: `src/backend/tests/test_evolution_race.py`
  ```py
  # -*- coding: utf-8 -*-
  """审核流竞态与断网场景测试 — EvolutionExecutor / Audit 并发 & 网络容错.
  
  覆盖:
  - EvolutionExecutor 并发执行 (Semaphore 控制)
  - 审核流竞态: 同时对同一演进项发起多次审核
  - 断网恢复: 模拟 API 不可达 / 超时
  - 回调竞态: on_complete 同时触发时的状态一致性
  - 事件日志完整性: 并发下事件无丢失/乱序
  
  注意: 所有 async 测试通过 asyncio.run() 包装，无需 pytest-asyncio。
  """
  
  from __future__ import annotations
  
  import asyncio
  import sys
  import time
  from pathlib import Path
  from typing import Any, Dict, List
  from unittest.mock import patch
  
  import pytest
  
  # Ensure src/backend is in path
  _backend_root = Path(__file__).resolve().parent.parent
  if str(_backend_root) not in sys.path:
      sys.path.insert(0, str(_backend_root))
  
  
  # ── Helper: 创建模拟演化项 ────────────────────────────────────────────────
  
  def _make_item_dict(
      item_id: str = "ev-test-001",
      title: str = "测试演化项",
      description: str = "用于竞态测试的演化项",
      current_behavior: str = "当前无此功能",
      expected_behavior: str = "期望添加此功能",
      reference_standard: str = "业界标准 X",
  ) -> Dict[str, Any]:
      return {
          "item_id": item_id,
          "title": title,
          "description": description,
          "current_behavior": current_behavior,
          "expected_behavior": expected_behavior,
          "reference_standard": reference_standard,
      }
  
  
  # ── Fixtures ───────────────────────────────────────────────────────────────
  
  @pytest.fixture
  def executor():
      """提供 EvolutionExecutor 实例."""
      from channels.evolution_executor import EvolutionExecutor
      return EvolutionExecutor()
  
  
  @pytest.fixture
  def sample_item():
      """标准测试演化项."""
      return _make_item_dict()
  
  
  # ── 1. 并发执行测试 ────────────────────────────────────────────────────────
  
  class TestEvolutionExecutorConcurrency:
      """EvolutionExecutor 并发执行测试."""
  
      def test_single_execution(self, executor, sample_item):
          """单次执行基础流程."""
          completed = []
  
          def on_complete(item_id, result):
              completed.append((item_id, result))
  
          executor.set_on_complete(on_complete)
  
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.return_value = {
                      "ok": True,
                      "summary": "所有修改已完成",
                      "files_changed": ["src/backend/test_file.py"],
                      "iterations": 3,
                  }
                  await executor.execute("ev-test-001", sample_item)
                  await asyncio.sleep(0.2)
  
          asyncio.run(_run())
  
          assert executor.get_result("ev-test-001") is not None
          result = executor.get_result("ev-test-001")
          assert result["ok"] is True
          assert len(result["files_changed"]) == 1
          assert len(completed) == 1
  
      def test_concurrent_executions_respect_semaphore(self, executor):
          """并发执行应受 Semaphore 限制."""
          from channels.evolution_executor import MAX_CONCURRENT_EXECUTIONS
  
          active_count = 0
          max_active = 0
  
          original_run = executor._run_agent_loop
  
          def counting_run(*args, **kwargs):
              nonlocal active_count, max_active
              active_count += 1
              max_active = max(max_active, active_count)
              time.sleep(0.05)
              active_count -= 1
              return {"ok": True, "summary": "done", "files_changed": [], "iterations": 1}
  
          async def _run():
              with patch.object(executor, '_run_agent_loop', wraps=counting_run):
                  task_count = MAX_CONCURRENT_EXECUTIONS * 3
                  for i in range(task_count):
                      item = _make_item_dict(f"ev-conc-{i:03d}", f"并发任务 {i}")
                      await executor.execute(f"ev-conc-{i:03d}", item)
                  await asyncio.sleep(0.5)
  
          asyncio.run(_run())
  
          assert max_active <= MAX_CONCURRENT_EXECUTIONS, (
              f"并发数 {max_active} 超过上限 {MAX_CONCURRENT_EXECUTIONS}"
          )
  
      def test_duplicate_execution_prevented(self, executor):
          """重复执行同一演进项应被阻止."""
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.return_value = {
                      "ok": True, "summary": "done", "files_changed": [], "iterations": 1,
                  }
                  await executor.execute("ev-dup", _make_item_dict("ev-dup"))
                  await executor.execute("ev-dup", _make_item_dict("ev-dup"))
                  await asyncio.sleep(0.2)
              return mock_run.call_count
  
          call_count = asyncio.run(_run())
          assert call_count == 1, f"预期调用 1 次, 实际 {call_count} 次"
  
      def test_callback_race_condition(self, executor):
          """并发回调不应导致状态不一致."""
          results_received = []
          lock = asyncio.Lock()
  
          async def on_complete(item_id, result):
              async with lock:
                  results_received.append((item_id, result.get("ok")))
  
          executor.set_on_complete(on_complete)
  
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.return_value = {
                      "ok": True, "summary": "done", "files_changed": [], "iterations": 1,
                  }
                  for i in range(10):
                      await executor.execute(f"ev-cb-{i:03d}", _make_item_dict(f"ev-cb-{i:03d}"))
                  await asyncio.sleep(0.3)
  
          asyncio.run(_run())
  
          assert len(results_received) == 10, f"预期 10 个回调, 实际 {len(results_received)}"
          assert all(ok for _, ok in results_received)
  
  
  # ── 2. 断网/超时恢复测试 ──────────────────────────────────────────────────
  
  class TestNetworkResilience:
      """网络中断与超时容错测试."""
  
      def test_executor_handles_agent_loop_timeout(self, executor):
          """AgentLoop 超时时执行器应优雅降级."""
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.side_effect = TimeoutError("LLM API timeout after 30s")
                  await executor.execute("ev-timeout", _make_item_dict("ev-timeout"))
                  await asyncio.sleep(0.2)
  
          asyncio.run(_run())
  
          result = executor.get_result("ev-timeout")
          assert result is not None
          assert result["ok"] is False
          assert "error" in result
  
      def test_executor_handles_connection_error(self, executor):
          """连接中断时执行器应正确报告错误."""
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.side_effect = ConnectionError("Connection refused")
                  await executor.execute("ev-conn-err", _make_item_dict("ev-conn-err"))
                  await asyncio.sleep(0.2)
  
          asyncio.run(_run())
  
          result = executor.get_result("ev-conn-err")
          assert result is not None
          assert result["ok"] is False
  
      def test_executor_handles_os_error(self, executor):
          """系统级错误 (OSError) 时应正确报告."""
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.side_effect = OSError("Too many open files")
                  await executor.execute("ev-os-err", _make_item_dict("ev-os-err"))
                  await asyncio.sleep(0.2)
  
          asyncio.run(_run())
  
          result = executor.get_result("ev-os-err")
          assert result is not None
          assert result["ok"] is False
  
      def test_concurrent_with_one_failure(self, executor):
          """混合成功/失败并发: 成功的任务不受失败任务影响."""
          call_count = 0
  
          def mixed_run(*args, **kwargs):
              nonlocal call_count
              call_count += 1
              if call_count % 3 == 0:
                  raise TimeoutError("Simulated timeout")
              return {"ok": True, "summary": "done", "files_changed": [], "iterations": 1}
  
          async def _run():
              with patch.object(executor, '_run_agent_loop', wraps=mixed_run):
                  for i in range(9):
                      await executor.execute(f"ev-mix-{i:03d}", _make_item_dict(f"ev-mix-{i:03d}"))
                  await asyncio.sleep(0.3)
  
          asyncio.run(_run())
  
          success = 0
          failed = 0
          for i in range(9):
              r = executor.get_result(f"ev-mix-{i:03d}")
              assert r is not None, f"任务 ev-mix-{i:03d} 无结果"
              if r["ok"]:
                  success += 1
              else:
                  failed += 1
  
          assert success == 6, f"预期 6 成功, 实际 {success}"
          assert failed == 3, f"预期 3 失败, 实际 {failed}"
  
  
  # ── 3. 审核流竞态测试 ──────────────────────────────────────────────────────
  
  class TestAuditRaceConditions:
      """审核流并发竞态场景测试."""
  
      def test_concurrent_audit_same_target(self):
          """多个审核同时对不同规则执行."""
          from channels.system_evolution import SystemEvolutionChannel
  
          async def _run():
              channel = SystemEvolutionChannel()
              channel.initialize()
  
              async def run_audit(rule):
                  try:
                      return await channel.audit_single_rule(rule.id, target_channel="bridge_chat")
                  except Exception as e:
                      return f"error: {e}"
  
              rules = channel.audit_rules[:5]
              tasks = [run_audit(r) for r in rules]
              results = await asyncio.gather(*tasks, return_exceptions=True)
  
              for r in results:
                  if isinstance(r, Exception):
                      pytest.fail(f"审核异常: {r}")
              assert len(results) == 5
  
          asyncio.run(_run())
  
      def test_concurrent_discovery_dispatch(self):
          """并发发现与派发不应产生重复演化项."""
          from channels.system_evolution import SystemEvolutionChannel
  
          async def _run():
              channel = SystemEvolutionChannel()
              channel.initialize()
  
              await channel.run_full_audit()
              initial_count = len(channel.discovered_items)
  
              async def audit_once():
                  await channel.run_full_audit()
  
              await asyncio.gather(audit_once(), audit_once(), audit_once())
  
              final_count = len(channel.discovered_items)
              assert final_count <= initial_count * 2, (
                  f"演化项从 {initial_count} 膨胀到 {final_count}，疑似竞态重复"
              )
  
          asyncio.run(_run())
  
      def test_evolution_item_status_transition_race(self):
          """演化项状态转换的并发安全性."""
          from channels.system_evolution import (
              SystemEvolutionChannel,
              EvolutionItem,
              EvolutionStatus,
          )
  
          async def _run():
              channel = SystemEvolutionChannel()
              channel.initialize()
  
              item = EvolutionItem(
                  id="ev-race-status-test",
                  title="竞态状态测试",
                  description="测试并发状态转换",
                  domain="general",
                  severity="low",
              )
              channel.discovered_items.append(item)
  
              async def dispatch():
                  await asyncio.sleep(0.01)
                  item.status = EvolutionStatus.DISPATCHED
  
              async def verify():
                  await asyncio.sleep(0.02)
                  item.status = EvolutionStatus.VERIFIED
  
              await asyncio.gather(dispatch(), verify())
              assert item.status in (EvolutionStatus.DISPATCHED, EvolutionStatus.VERIFIED)
  
          asyncio.run(_run())
  
  
  # ── 4. 事件日志完整性测试 ──────────────────────────────────────────────────
  
  class TestEventLogIntegrity:
      """并发下事件日志完整性与顺序."""
  
      def test_event_log_no_loss(self, executor):
          """并发执行时事件日志不应丢失."""
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.return_value = {
                      "ok": True, "summary": "done", "files_changed": [], "iterations": 1,
                  }
                  for i in range(5):
                      await executor.execute(f"ev-log-{i:03d}", _make_item_dict(f"ev-log-{i:03d}"))
                  await asyncio.sleep(0.3)
  
          asyncio.run(_run())
  
          for i in range(5):
              log = executor.get_event_log(f"ev-log-{i:03d}")
              event_types = [e.get("type") for e in log]
              assert "execution_start" in event_types, f"ev-log-{i:03d} 缺少 execution_start"
              assert "execution_end" in event_types, f"ev-log-{i:03d} 缺少 execution_end"
  
      def test_executor_status_accurate(self, executor):
          """执行器状态报告在并发下保持准确."""
          async def _run():
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  def slow_run(*args, **kwargs):
                      time.sleep(0.1)
                      return {"ok": True, "summary": "slow", "files_changed": [], "iterations": 1}
                  mock_run.side_effect = slow_run
  
                  for i in range(5):
                      await executor.execute(f"ev-status-{i:03d}", _make_item_dict(f"ev-status-{i:03d}"))
  
                  status = executor.get_status()
                  assert status["completed_count"] >= 0
                  assert status["running_count"] <= 5
                  await asyncio.sleep(0.8)
  
          asyncio.run(_run())
  
          final_status = executor.get_status()
          assert final_status["completed_count"] == 5, (
              f"预期 5 完成, 实际 {final_status['completed_count']}"
          )
          assert final_status["running_count"] == 0
  
  
  # ── 5. 综合场景 ────────────────────────────────────────────────────────────
  
  class TestIntegrationScenarios:
      """端到端集成场景."""
  
      def test_full_pipeline_concurrent(self):
          """完整流水线: 审计→发现→派发→执行 (并发版)."""
          from channels.system_evolution import SystemEvolutionChannel
          from channels.evolution_executor import EvolutionExecutor
  
          async def _run():
              channel = SystemEvolutionChannel()
              channel.initialize()
  
              executor = EvolutionExecutor()
  
              await channel.run_full_audit()
              discovered = len(channel.discovered_items)
              assert discovered > 0, "审计未发现任何演化项"
  
              for item in channel.discovered_items:
                  await channel.dispatch_item(item.id)
  
              completed_ids = []
              lock = asyncio.Lock()
  
              async def on_complete(item_id, result):
                  async with lock:
                      completed_ids.append(item_id)
  
              executor.set_on_complete(on_complete)
  
              with patch.object(executor, '_run_agent_loop') as mock_run:
                  mock_run.return_value = {
                      "ok": True, "summary": "completed", "files_changed": ["test.py"], "iterations": 2,
                  }
                  for item in channel.discovered_items[:5]:
                      await executor.execute(item.id, item.to_dict())
                  await asyncio.sleep(0.3)
  
              assert len(completed_ids) == min(5, discovered), (
                  f"预期完成 {min(5, discovered)} 个, 实际 {len(completed_ids)}"
              )
  
          asyncio.run(_run())
  
      def test_audit_engine_self_check(self):
          """审计引擎自检 — 验证内置规则可用."""
          from channels.system_evolution import SystemEvolutionChannel
  
          channel = SystemEvolutionChannel()
          channel.initialize()
  
          assert len(channel.audit_rules) >= 5, "至少应加载 5 条内置规则"
  
          for rule in channel.audit_rules:
              assert 
  ```
  
  ### 文件: `src/backend/tests/test_plaza_dispatch.py`
  ```py
  # -*- coding: utf-8 -*-
  """Plaza discussion dispatch tests."""
  
  from __future__ import annotations
  
  from pathlib import Path
  from tempfile import TemporaryDirectory
  
  import pytest
  
  from agents import api as api_module
  from agents import plaza_engine as plaza_engine_module
  from agents import plaza_routes
  from agents import task_engine as task_engine_module
  from agents.plaza_engine import PlazaEngine
  from agents.plaza_store import PlazaStore
  from agents.task_engine import AgentTask, TaskEngine
  from agents.task_store import TaskStore
  
  
  @pytest.fixture
  def isolated_plaza_engine(monkeypatch):
      with TemporaryDirectory() as tmpdir:
          engine = PlazaEngine()
          engine._store = PlazaStore(base_dir=Path(tmpdir))
          engine._plazas = {}
          monkeypatch.setattr(plaza_engine_module, "_engine", engine)
          yield engine
  
  
  @pytest.fixture
  def isolated_task_engine(monkeypatch):
      with TemporaryDirectory() as tmpdir:
          engine = TaskEngine(store=TaskStore(base_dir=Path(tmpdir)))
          monkeypatch.setattr(task_engine_module, "_engine", engine)
          yield engine
  
  
  def _build_plan_text() -> str:
      return (
          "## 执行计划\n"
          "| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
          "|---|---|---|---|---|---|\n"
          "| 1 | 修复启动链路 | developer | P0 | 无 | 启动补丁 |\n"
          "| 2 | 补回归测试 | qa | P1 | 1 | pytest 报告 |\n"
      )
  
  
  def _seed_discussion(engine: PlazaEngine):
      plaza = engine.create_plaza("测试广场", "dispatch")
      disc = engine.create_discussion(plaza.id, "让 Plaza 真的能派发任务", "dispatch", "", 3)
      disc.plan = {
          "revision": 3,
          "revision_reason": "测试计划",
          "revised_at": "2026-05-29T00:00:00+00:00",
          "content": _build_plan_text(),
      }
      engine._store.save_plaza(plaza)
      return plaza, disc
  
  
  class TestPlanParsing:
      def test_parse_markdown_plan_table(self):
          tasks = plaza_routes._parse_plan_table(_build_plan_text())
          assert len(tasks) == 2
          assert tasks[0]["title"] == "修复启动链路"
          assert tasks[0]["priority"] == 1
          assert tasks[0]["responsible"] == "developer"
          assert tasks[0]["expected_artifact"] == "启动补丁"
          assert tasks[1]["dependencies"] == "1"
  
  
  class TestDiscussionDispatch:
      @pytest.mark.asyncio
      async def test_dispatch_tasks_updates_discussion_plan(self, isolated_plaza_engine, monkeypatch):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          submitted = []
  
          async def fake_submit_internal_task(team_id: str, **kwargs):
              task = AgentTask(
                  task_id=f"task-{len(submitted) + 1}",
                  team_id=team_id,
                  title=kwargs["title"],
                  description=kwargs["description"],
                  priority=kwargs["priority"],
                  metadata=kwargs["metadata"],
              )
              submitted.append(task)
              return task
  
          monkeypatch.setattr(api_module, "_submit_internal_task", fake_submit_internal_task)
  
          result = await plaza_routes.dispatch_tasks_from_discussion(
              plaza.id,
              disc.id,
              plaza_routes.DispatchTasksRequest(team_id="team-build"),
          )
  
          assert result["status"] == "dispatched"
          assert result["task_count"] == 2
          assert [task["task_id"] for task in result["tasks"]] == ["task-1", "task-2"]
  
          updated_disc = isolated_plaza_engine.get_discussion(plaza.id, disc.id)
          assert updated_disc.assigned_team_id == "team-build"
          assert updated_disc.plan["task_ids"] == ["task-1", "task-2"]
          assert updated_disc.plan["task_count"] == 2
          assert updated_disc.plan["team_id"] == "team-build"
  
          first_metadata = result["tasks"][0]["metadata"]
          assert first_metadata["source"] == "plaza"
          assert first_metadata["discussion_id"] == disc.id
          assert first_metadata["plan_revision"] == 3
          assert first_metadata["plan_item_index"] == 0
          assert first_metadata["responsible_role"] == "developer"
          assert first_metadata["skills_used"] == ["code_implementation", "debugging"]
          assert first_metadata["trace_context"]["discussion_id"] == disc.id
          assert first_metadata["trace_context"]["plaza_id"] == plaza.id
          assert first_metadata["trace_context"]["plan_revision"] == 3
  
          second_metadata = result["tasks"][1]["metadata"]
          assert second_metadata["responsible_role"] == "qa"
          assert second_metadata["skills_used"] == ["testing", "test_execution", "regression_testing"]
  
          summary = await plaza_routes.get_discussion_summary(plaza.id, disc.id)
          assert summary["plan_revision"] == 3
          assert summary["task_ids"] == ["task-1", "task-2"]
          assert summary["task_count"] == 2
  
      @pytest.mark.asyncio
      async def test_get_discussion_tasks_returns_only_linked_tasks(
          self,
          isolated_plaza_engine,
          isolated_task_engine,
      ):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
  
          await isolated_task_engine.submit_task(
              AgentTask(
                  task_id="task-2",
                  team_id="team-build",
                  title="第二个任务",
                  metadata={
                      "source": "plaza",
                      "plaza_id": plaza.id,
                      "discussion_id": disc.id,
                      "plan_item_index": 1,
                  },
              )
          )
          await isolated_task_engine.submit_task(
              AgentTask(
                  task_id="task-1",
                  team_id="team-build",
                  title="第一个任务",
                  metadata={
                      "source": "plaza",
                      "plaza_id": plaza.id,
                      "discussion_id": disc.id,
                      "plan_item_index": 0,
                  },
              )
          )
          await isolated_task_engine.submit_task(
              AgentTask(
                  task_id="task-x",
                  team_id="other",
                  title="无关任务",
                  metadata={
                      "source": "plaza",
                      "plaza_id": plaza.id,
                      "discussion_id": "other-discussion",
                      "plan_item_index": 0,
                  },
              )
          )
  
          result = await plaza_routes.get_discussion_tasks(plaza.id, disc.id)
          assert result["task_count"] == 2
          assert [task["task_id"] for task in result["tasks"]] == ["task-1", "task-2"]
  
  ```
  
  ### 文件: `src/backend/tests/test_plaza_evolution_bridge.py`
  ```py
  # -*- coding: utf-8 -*-
  """Plaza to evolution bridge tests."""
  
  from __future__ import annotations
  
  from pathlib import Path
  from tempfile import TemporaryDirectory
  
  import pytest
  
  import agent_team_api as agent_team_api_module
  from agents import api as api_module
  from agents import plaza_engine as plaza_engine_module
  from agents import task_engine as task_engine_module
  from channels.system_evolution import (
      EvolutionItem,
      EvolutionStatus,
      SystemEvolutionChannel,
  )
  from agents.plaza_engine import PlazaEngine
  from agents.plaza_routes import (
      EvolveRequest,
      evolve_from_discussion,
      get_discussion_verification_alerts,
      get_discussion_verification_queue,
      run_discussion_verification_queue,
  )
  from agents.plaza_store import PlazaStore
  from agents.task_engine import AgentTask, TaskEngine
  from agents.task_store import TaskStore
  
  
  @pytest.fixture
  def isolated_plaza_engine(monkeypatch):
      with TemporaryDirectory() as tmpdir:
          engine = PlazaEngine()
          engine._store = PlazaStore(base_dir=Path(tmpdir))
          engine._plazas = {}
          monkeypatch.setattr(plaza_engine_module, "_engine", engine)
          yield engine
  
  
  @pytest.fixture
  def isolated_task_engine(monkeypatch):
      with TemporaryDirectory() as tmpdir:
          engine = TaskEngine(store=TaskStore(base_dir=Path(tmpdir) / "tasks"))
          monkeypatch.setattr(task_engine_module, "_engine", engine)
          yield engine
  
  
  def _seed_discussion(engine: PlazaEngine):
      plaza = engine.create_plaza("演化广场", "evolution")
      disc = engine.create_discussion(plaza.id, "让 Plaza 接进 Evolution", "evolution", "", 3)
      disc.plan = {
          "revision": 2,
          "revision_reason": "测试演化桥接",
          "revised_at": "2026-05-29T00:00:00+00:00",
          "content": (
              "## 执行计划\n"
              "| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
              "|---|---|---|---|---|---|\n"
              "| 1 | 打通演化派发 | developer | P0 | 无 | 任务桥接补丁 |\n"
              "| 2 | 补充桥接测试 | qa | P1 | 1 | 回归测试报告 |\n"
          ),
      }
      engine._store.save_plaza(plaza)
      return plaza, disc
  
  
  class TestEvolutionCycleGuards:
      def test_run_evolution_cycle_does_not_auto_verify_dispatched_items(self):
          channel = SystemEvolutionChannel()
          channel.initialize()
          channel.audit_rules = []
  
          item = EvolutionItem(
              id="ev-dispatch-only",
              title="仅派发",
              description="不应自动进入验证",
          )
          channel.evolution_items[item.id] = item
  
          result = channel.run_evolution_cycle()
  
          assert result["dispatch"]["count"] == 1
          assert result["verify"]["count"] == 0
          assert channel.evolution_items[item.id].status == EvolutionStatus.DISPATCHED.value
  
      def test_mark_build_complete_requires_artifacts(self):
          channel = SystemEvolutionChannel()
          channel.initialize()
  
          item = EvolutionItem(
              id="ev-build-guard",
              title="需要真实产物",
              description="无产物不允许进入验证",
              status=EvolutionStatus.IN_PROGRESS.value,
          )
          channel.evolution_items[item.id] = item
  
          assert channel.mark_build_complete(item.id) is False
          assert channel.evolution_items[item.id].status == EvolutionStatus.IN_PROGRESS.value
  
          assert channel.mark_build_complete(item.id, code_changes=["src/backend/main.py"]) is True
          assert channel.evolution_items[item.id].status == EvolutionStatus.VERIFY_PENDING.value
  
  
  class TestPlazaEvolutionBridge:
      @pytest.mark.asyncio
      async def test_evolve_from_discussion_creates_traceable_items(
          self,
          isolated_plaza_engine,
          isolated_task_engine,
          monkeypatch,
      ):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          evolution_engine = SystemEvolutionChannel()
          evolution_engine.initialize()
          evolution_engine.audit_rules = []
          monkeypatch.setattr(agent_team_api_module, "_evolution_engine", evolution_engine)
          broadcast_events = []
  
          async def fake_broadcast(discussion_id, event):
              broadcast_events.append((discussion_id, event))
  
          monkeypatch.setattr(isolated_plaza_engine, "_broadcast", fake_broadcast)
  
          created_tasks = []
  
          async def fake_submit_internal_task(team_id: str, **kwargs):
              task = AgentTask(
                  task_id=f"plaza-task-{len(created_tasks) + 1}",
                  team_id=team_id,
                  title=kwargs["title"],
                  description=kwargs["description"],
                  priority=kwargs["priority"],
                  metadata=kwargs["metadata"],
              )
              created_tasks.append(task)
              await isolated_task_engine.submit_task(task)
              return task
  
          monkeypatch.setattr(api_module, "_submit_internal_task", fake_submit_internal_task)
  
          result = await evolve_from_discussion(plaza.id, disc.id, EvolveRequest(team_id="team-build"))
  
          assert result["status"] == "evolving"
          assert result["task_count"] == 2
          assert len(result["items"]) == 2
  
          for item in result["items"]:
              assert item["source_discussion_id"] == disc.id
              assert item["source_task_ids"] == ["plaza-task-1", "plaza-task-2"]
              assert item["trace_context"]["discussion_id"] == disc.id
  
          stored_items = list(evolution_engine.evolution_items.values())
          assert len(stored_items) == 2
          assert all(item.source_plaza_id == plaza.id for item in stored_items)
          assert all(item.source_discussion_id == disc.id for item in stored_items)
          assert all(item.source_task_ids == ["plaza-task-1", "plaza-task-2"] for item in stored_items)
          assert all(item.status == EvolutionStatus.DISPATCHED.value for item in stored_items)
          assert all(item.trace_context["plaza_id"] == plaza.id for item in stored_items)
          assert broadcast_events
          assert broadcast_events[-1][0] == disc.id
          assert broadcast_events[-1][1]["type"] == "verification_state_updated"
          assert broadcast_events[-1][1]["trigger"] == "discussion_evolved"
          assert broadcast_events[-1][1]["synced_item_ids"] == [item["id"] for item in result["items"]]
  
          for task in result["tasks"]:
              metadata = task["metadata"]
              assert len(metadata["evolution_item_ids"]) == 2
              assert metadata["trace_context"]["task_id"] == task["task_id"]
              assert metadata["trace_context"]["evolution_item_ids"] == metadata["evolution_item_ids"]
  
          linked_task = isolated_task_engine.get_task("plaza-task-1")
          assert linked_task is not None
          assert len(linked_task.metadata["evolution_item_ids"]) == 2
  
      @pytest.mark.asyncio
      async def test_discussion_verification_queue_surfaces_manual_verify_items(
          self,
          isolated_plaza_engine,
          monkeypatch,
      ):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          evolution_engine = SystemEvolutionChannel()
          evolution_engine.initialize()
          evolution_engine.evolution_items["evo-manual"] = EvolutionItem(
              id="evo-manual",
              title="人工验证项",
              status=EvolutionStatus.VERIFY_PENDING.value,
              verify_test_name="manual-check",
              verify_result="pending",
              verify_detail="Awaiting verify test: manual-check",
              source_plaza_id=plaza.id,
              source_discussion_id=disc.id,
              source_task_ids=["plaza-task-1"],
          )
          evolution_engine.evolution_items["evo-other"] = EvolutionItem(
              id="evo-other",
              title="其他讨论",
              status=EvolutionStatus.VERIFY_PENDING.value,
              verify_test_name="other-check",
              source_plaza_id=plaza.id,
              source_discussion_id="other-disc",
              source_task_ids=["task-x"],
          )
          monkeypatch.setattr(agent_team_api_module, "_evolution_engine", evolution_engine)
  
          payload = await get_discussion_verification_queue(plaza.id, disc.id)
  
          assert payload["count"] == 1
          assert payload["items"][0]["id"] == "evo-manual"
          assert payload["items"][0]["requires_manual_verify"] is True
          assert payload["items"][0]["verify_detail"] == "Awaiting verify test: manual-check"
  
      @pytest.mark.asyncio
      async def test_discussion_verification_alerts_surface_retry_and_manual_verify(
          self,
          isolated_plaza_engine,
          monkeypatch,
      ):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          evolution_engine = SystemEvolutionChannel()
          evolution_engine.initialize()
          evolution_engine.evolution_items["evo-manual"] = EvolutionItem(
              id="evo-manual",
              title="人工验证项",
              status=EvolutionStatus.VERIFY_PENDING.value,
              verify_test_name="manual-check",
              verify_result="pending",
              verify_detail="Awaiting verify test: manual-check",
              source_plaza_id=plaza.id,
              source_discussion_id=disc.id,
          )
          evolution_engine.evolution_items["evo-retry"] = EvolutionItem(
              id="evo-retry",
              title="重试项",
              status=EvolutionStatus.DISPATCHED.value,
              verify_result="failed",
              verify_detail="回归失败 (retry queued 1/3)",
              retry_count=1,
              source_plaza_id=plaza.id,
              source_discussion_id=disc.id,
          )
          monkeypatch.setattr(agent_team_api_module, "_evolution_engine", evolution_engine)
  
          payload = await get_discussion_verification_alerts(plaza.id, disc.id)
  
          assert payload["count"] == 2
          assert payload["alerts"][0]["item_id"] == "evo-manual"
          assert payload["alerts"][0]["alert_level"] == "warning"
          assert payload["alerts"][0]["next_action"] == "run_verify_test:manual-check"
          assert payload["alerts"][1]["item_id"] == "evo-retry"
          assert payload["alerts"][1]["next_action"] == "redispatch_build"
  
      @pytest.mark.asyncio
      async def test_run_discussion_verification_queue_only_affects_current_discussion(
          self,
          isolated_plaza_engine,
          monkeypatch,
      ):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          evolution_engine = SystemEvolutionChannel()
          evolution_engine.initialize()
          broadcast_events = []
  
          async def fake_broadcast(discussion_id, event):
              broadcast_events.append((discussion_id, event))
  
          monkeypatch.setattr(isolated_plaza_engine, "_broadcast", fake_broadcast)
          evolution_engine.evolution_items["evo-pass"] = EvolutionItem(
              id="evo-pass",
              title="当前讨论通过项",
              status=EvolutionStatus.VERIFY_PENDING.value,
              verify_test_name="verify-pass",
              source_plaza_id=plaza.id,
              source_discussion_id=disc.id,
          )
          evolution_engine.evolution_items["evo-other"] = EvolutionItem(
              id="evo-other",
              title="其他讨论待验证",
              status=EvolutionStatus.VERIFY_PENDING.value,
              verify_test_name="verify-other",
              source_plaza_id=plaza.id,
              source_discussion_id="other-disc",
          )
          evolution_engine.register_verify_test("verify-pass", lambda: (True, "当前讨论验证通过"))
          evolution_engine.register_verify_test("verify-other", lambda: (True, "不应被触发"))
          monkeypatch.setattr(agent_team_api_module, "_evolution_engine", evolution_engine)
  
          payload = await run_discussion_verification_queue(plaza.id, disc.id)
  
          assert payload["verify"]["count"] == 1
          assert payload["verify"]["verified"][0]["item_id"] == "evo-pass"
          assert payload["closed"] == ["evo-pass"]
          assert payload["alerts"] == []
          assert evolution_engine.evolution_items["evo-pass"].status == EvolutionStatus.CLOSED.value
          assert evolution_engine.evolution_items["evo-other"].status == EvolutionStatus.VERIFY_PENDING.value
          assert broadcast_events
          assert broadcast_events[-1][0] == disc.id
          assert broadcast_events[-1][1]["type"] == "verification_state_updated"
          assert broadcast_events[-1][1]["trigger"] == "verification_queue_run"
          assert broadcast_events[-1][1]["status_counts"][EvolutionStatus.CLOSED.value] == 1
          assert broadcast_events[-1][1]["alert_count"] == 0
  
  ```
  
  ### 文件: `src/backend/agents/plaza_engine.py`
  ```py
  # -*- coding: utf-8 -*-
  """智能体广场引擎 — 讨论编排与多 Agent 协同.
  
  核心编排逻辑:
  1. Moderator（主持人壁龛）提出子话题，引导讨论方向
  2. 每轮: 各参与者按座席层级依次发言（内圈→中圈→外圈）
  3. Moderator 总结本轮关键观点
  4. 最终轮: Moderator 生成全局总结 + 关键结论
  
  消息通过 asyncio.Queue 实时推送给 SSE 订阅者。
  """
  
  from __future__ import annotations
  
  import asyncio
  import json
  import logging
  import re
  from datetime import datetime, timezone
  from typing import Any, AsyncIterator, Callable, Dict, List, Optional
  from uuid import uuid4
  
  from .plaza import (
      Discussion, DiscussionStatus, NicheRole, Participant,
      Plaza, PlazaMessage, SeatTier, PRESET_TOPICS,
  )
  from .plaza_store import PlazaStore
  
  logger = logging.getLogger(__name__)
  
  _ROUND_SPEAKER_LIMIT = 5
  _EXCHANGES_PER_ROUND = 2  # 每轮内交锋次数
  _SPEAKERS_PER_EXCHANGE = 3  # 每次交锋参与人数
  _CORE_ROLE_PRIORITY = {
      "architect": 0,
      "researcher": 1,
      "developer": 2,
      "qa_engineer": 3,
      "qa": 3,
      "tester": 3,
      "devops": 4,
      "project_manager": 5,
      "documentation": 6,
  }
  
  
  class PlazaEngine:
      """广场引擎 — 管理广场、参与者和讨论编排."""
  
      def __init__(self):
          self._store = PlazaStore()
          self._plazas: Dict[str, Plaza] = self._store.load_all()
          self._sse_queue
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose (完整产出)
  
  # PM分解 — project_manager
  
  任务: 建立基于混沌工程的稳定性测试集，验证Spot实例、缓存及数据分层策略下的SLO达标情况
  步骤: pm_decompose
  Agent: build_pm
  
  ---
  
  📋 任务: e0c257fa-606
  🤖 Agent: PM (project_manager)
  📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
  🔧 执行方式: DeepSeek API (直连)
  ⏱️ 超时: 1200s
  ────────────────────────────────────────────────────────────
  📝 提示词:
    你是 AgentsGroup2026 系统的 PM (project_manager)。
    请执行以下开发任务:
    
    你是项目经理 (PM)。请对以下任务进行分解和规划:
    
    ## 任务
    建立基于混沌工程的稳定性测试集，验证Spot实例、缓存及数据分层策略下的SLO达标情况
    负责角色: 测试工程师
    依赖: 任务1、3完成
    预期产出: 自动化测试报告，包含成本-质量双维度验收标准
    负责角色: 测试工程师
    依赖: 任务1、3完成
    预期产出: 自动化测试报告，包含成本-质量双维度验收标准
    
    ## 📂 项目上下文 (系统自动预加载)
    
    ### 项目文件结构 (src/ 目录)
    ```
    src/frontend/agent-team-config.html
    src/frontend/datacenter-ratchet-evolution.html
    src/frontend/digital-twin-cli.html
    src/frontend/extraction-pipeline.html
    src/frontend/index.html
    src/frontend/login.html
    src/frontend/plaza.html
    src/frontend/sandbox-twin.html
    src/frontend/skill-extract.html
    src/frontend/system-evolution.html
    src/frontend/tasks.html
    src/frontend/css/agent-team-config.css
    src/frontend/css/openbridge-theme.css
    src/frontend/css/skill-extract-timeline.css
    src/frontend/css/skill-extract.css
    src/frontend/css/variables.css
    src/frontend/css/ws-theme-bridge.css
    src/frontend/js/agent-detail.js
    src/frontend/js/agent-team-config.js
    src/frontend/js/api.js
    src/frontend/js/digital-twin-cli-3d.js
    src/frontend/js/digital-twin-cli.js
    src/frontend/js/global-nav.js
    src/frontend/js/i18n.js
    src/frontend/js/nav-sidebar.js
    src/frontend/js/plaza.js
    src/frontend/js/sandbox-twin.js
    src/frontend/js/sessions-runtime.js
    src/frontend/js/skill-extract-timeline.js
    src/frontend/js/skill-extract.js
    src/frontend/js/system-evolution.js
    src/frontend/js/tasks-view.js
    src/frontend/js/token-factory.js
    src/frontend/js/tools-skills.js
    src/frontend/js/utils.js
    src/frontend/js/wizard.js
    src/backend/__init__.py
    src/backend/agent_team_api.py
    src/backend/config.py
    src/backend/main.py
    src/backend/main.py.bak
    src/backend/server.log
    src/backend/startup_check.py
    src/backend/startup_validator.py
    src/backend/tests/__init__.py
    src/backend/tests/conftest.py
    src/backend/tests/conftest.py.bak
    src/backend/tests/test_ab_testing.py
    src/backend/tests/test_agent_skill_binding.py
    src/backend/tests/test_agent_toolbox.py
    src/backend/tests/test_evolution_race.py
    src/backend/tests/test_evolution_race.py.bak
    src/backend/tests/test_fingerprint.py
    src/backend/tests/test_fingerprint.py.bak
    src/backend/tests/test_gate_evaluator.py
    src/backend/tests/test_gate_evaluator.py.bak
    src/backend/tests/test_main_health.py
    src/backend/tests/test_merge_plugin.py
    src/backend/tests/test_merge_plugin.py.bak
    src/backend/tests/test_models.py
    src/backend/tests/test_models.py.bak
    src/backend/tests/test_operation_store.py
    src/backend/tests/test_permissions_and_secrets.py
    src/backend/tests/test_plan_loop_runtime.py
    src/backend/tests/test_plaza_dispatch.py
    src/backend/tests/test_plaza_evolution_bridge.py
    src/backend/tests/test_plaza_task_artifact_bridge.py
    src/backend/tests/test_qa_gate_pipeline.py
    src/backend/tests/test_qa_gate_pipeline.py.bak
    src/backend/tests/test_review_integration.py
    src/backend/tests/test_review_integration.py.bak
    src/backend/tests/test_sandbox_security.py
    src/backend/tests/test_task_engine.py
    src/backend/tests/test_task_engine.py.bak
    src/backend/tests/test_team_manager.py
    src/backend/tests/test_team_manager.py.bak
    src/backend/tests/test_template_variants.py
    src/backend/tests/test_template_variants.py.bak
    src/backend/tests/test_token_budget.py
    src/backend/tests/test_unified_tool_loop.py
    src/backend/agents/__init__.py
    src/backend/agents/ab_testing.py
    src/backend/agents/agent_loop.py
    src/backend/agents/agent_toolbox.py
    src/backend/agents/api.py
    src/backend/agents/api.py.bak
    src/backend/agents/audit_store.py
    src/backend/agents/chat_harness.py
    src/backend/agents/domain_events.py
    src/backend/agents/domain_events.py.bak
    src/backend/agents/event_bus.py
    src/backend/agents/execution_registry.py
    src/backend/agents/extraction_models.py
    src/backend/agents/extraction_pipeline.py
    src/backend/agents/extraction_pipeline.py.bak
    src/backend/agents/extraction_routes.py
    src/backend/agents/extraction_store.py
    src/backend/agents/fingerprint.py
    src/backend/agents/fingerprint.py.bak
    src/backend/agents/gate_evaluator.py
    src/backend/agents/hermes_research.py
    src/backend/agents/knowledge_base.py
    src/backend/agents/merge_engine.py
    src/backend/agents/merge_models.py
    src/backend/agents/models.py
    src/backend/agents/models.py.bak
    src/backend/agents/operation_api.py
    src/backend/agents/operation_models.py
    src/backend/agents/operation_store.py
    src/backend/agents/plaza.py
    src/backend/agents/plaza.py.bak
    src/backend/agents/plaza_engine.py
    src/backend/agents/plaza_routes.py
    src/backend/agents/plaza_routes.py.bak
    src/backend/agents/plaza_store.py
    src/backend/agents/review_models.py
    src/backend/agents/review_routes.py
    src/backend/agents/review_service.py
    src/backend/agents/secret_store.py
    src/backend/agents/session_store.py
    src/backend/agents/similarity_engine.py
    src/backend/agents/skill_evolver.py
    src/backend/agents/skill_extract_ws.py
    src/backend/agents/skill_extractor.py
    src/backend/agents/skill_indexer.py
    src/backend/agents/skill_library.py
    src/backend/agents/skill_querier.py
    src/backend/agents/skill_registry.py
    src/backend/agents/skill_router.py
    src/backend/agents/skill_router_routes.py
    src/backend/agents/skill_store.py
    src/backend/agents/skill_tracker.py
    src/backend/agents/skill_verifier.py
    src/backend/agents/task_engine.py
    src/backend/agents/task_engine.py.bak
    src/backend/agents/task_store.py
    src/backend/agents/team_manager.py
    src/backend/agents/team_manager.py.bak
    src/backend/agents/team_store.py
    src/backend/agents/tool_executor.py
    src/backend/agents/tool_registry.py
    src/backend/agents/trajectory_analyzer.py
    src/backend/agents/tts_routes.py
    src/backend/agents/security/__init__.py
    src/backend/agents/security/permission_resolver.py
    src/backend/agents/runtime/__init__.py
    src/backend/agents/runtime/events.py
    src/backend/agents/runtime/plan_loop.py
    src/backend/agents/runtime/tool_loop.py
    src/backend/agents/evolution/__init__.py
    ... (共 969 个 src/ 文件)
    
    ```
    
    ### 文件: `src/backend/agent_team_api.py`
    ```py
    # -*- coding: utf-8 -*-
    """
    Agent Team API Routes - 双团队管理 REST API
    
    提供构建团队 & 执行团队的状态查询、KPI 考核、
    任务分配、报告查询等端点。挂载至 FastAPI 的 router。
    """
    
    from __future__ import annotations
    
    from fastapi import APIRouter, HTTPException, Query
    from pydantic import BaseModel
    from typing import Any, Dict, List, Optional
    
    router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
    
    
    # ---------------------------------------------------------------------------
    # 全局引用（在 main.py startup 时注入）
    # ---------------------------------------------------------------------------
    _build_team = None
    _execution_team = None
    _scheduler = None
    _evolution_engine = None
    
    
    def set_teams(build_team, execution_team, scheduler, evolution_engine=None):
        """在应用启动时由 main.py 调用，注入团队实例."""
        global _build_team, _execution_team, _scheduler, _evolution_engine
        _build_team = build_team
        _execution_team = execution_team
        _scheduler = scheduler
        _evolution_engine = evolution_engine
    
    
    # ---------------------------------------------------------------------------
    # Request / Response Models
    # ---------------------------------------------------------------------------
    
    class TaskAssignment(BaseModel):
        agent_id: str
        task: str
    
    class FeedbackSubmission(BaseModel):
        category: str = "optimization"
        severity: str = "medium"
        title: str
        detail: str
    
    
    # ---------------------------------------------------------------------------
    # Scheduler
    # ---------------------------------------------------------------------------
    
    @router.get("/scheduler/status")
    async def scheduler_status():
        if not _scheduler:
            raise HTTPException(503, "Scheduler not initialized")
        return _scheduler.get_status()
    
    
    @router.post("/scheduler/report")
    async def scheduler_generate_report():
        if not _scheduler:
            raise HTTPException(503, "Scheduler not initialized")
        return _scheduler.generate_report_now()
    
    
    @router.post("/scheduler/tick")
    async def scheduler_tick_once():
        """手动触发一次调度 tick (调试用)."""
        if not _scheduler:
            raise HTTPException(503, "Scheduler not initialized")
        return _scheduler.tick_once()
    
    
    # ---------------------------------------------------------------------------
    # Build Team
    # ---------------------------------------------------------------------------
    
    @router.get("/build/status")
    async def build_team_status():
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        return _build_team.get_status()
    
    
    @router.get("/build/kpis")
    async def build_team_kpis():
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        return _build_team.get_agent_kpis()
    
    
    @router.get("/build/agents/{agent_id}")
    async def build_agent_detail(agent_id: str):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        agent = _build_team.agents.get(agent_id)
        if not agent:
            raise HTTPException(404, f"Agent '{agent_id}' not found")
        return agent.to_dict()
    
    
    @router.post("/build/assign")
    async def build_assign_task(body: TaskAssignment):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        ok = _build_team.assign_task(body.agent_id, body.task)
        if not ok:
            raise HTTPException(404, f"Agent '{body.agent_id}' not found")
        return {"status": "assigned", "agent_id": body.agent_id, "task": body.task}
    
    
    @router.get("/build/reports")
    async def build_reports(limit: int = 10):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        reports = _build_team.hourly_reports[-limit:]
        return [r.to_dict() for r in reports]
    
    
    @router.get("/build/issues")
    async def build_issues():
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        return _build_team.issue_backlog
    
    
    # ---------------------------------------------------------------------------
    # Execution Team
    # ---------------------------------------------------------------------------
    
    @router.get("/execution/status")
    async def execution_team_status():
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        return _execution_team.get_status()
    
    
    @router.get("/execution/agents/{agent_id}")
    async def execution_agent_detail(agent_id: str):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        agent = _execution_team.agents.get(agent_id)
        if not agent:
            raise HTTPException(404, f"Agent '{agent_id}' not found")
        return agent.to_dict()
    
    
    @router.get("/execution/reports")
    async def execution_reports(limit: int = 10):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        reports = _execution_team.execution_reports[-limit:]
        return [r.to_dict() for r in reports]
    
    
    @router.get("/execution/feedback")
    async def execution_feedback():
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        return [item.to_dict() for item in _execution_team.feedback_queue]
    
    
    @router.post("/execution/feedback")
    async def submit_feedback(body: FeedbackSubmission):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        item = _execution_team.submit_feedback(
            category=body.category,
            severity=body.severity,
            title=body.title,
            detail=body.detail,
        )
        return item.to_dict()
    
    
    # ---------------------------------------------------------------------------
    # Combined
    # ---------------------------------------------------------------------------
    
    @router.get("/overview")
    async def teams_overview(team_id: Optional[str] = None):
        """一站式获取双团队全局概览."""
        result: Dict[str, Any] = {}
        if _build_team:
            bs = _build_team.get_status()
            result["build_team"] = {
                "health": bs["health"],
                "agent_count": bs["agent_count"],
                "metrics": bs["metrics"],
            }
        if _execution_team:
            es = _execution_team.get_status()
            result["execution_team"] = {
                "health": es["health"],
                "agent_count": es["agent_count"],
                "metrics": es["metrics"],
            }
        if _scheduler:
            result["scheduler"] = _scheduler.get_status()
        if _evolution_engine:
            result["evolution"] = {
                **_evolution_engine.get_status(),
                "compliance_rating": _serialize_compliance_rating(),
            }
        if team_id:
            result["current_team"] = _serialize_current_team(team_id)
        return result
    
    
    def _serialize_current_team(team_id: str) -> Optional[Dict[str, Any]]:
        try:
            from .agents.api import _summarize_team_tasks, _team_manager
        except ImportError:
            from agents.api import _summarize_team_tasks, _team_manager
    
        if _team_manager is None:
            return None
    
        team = _team_manager.get_team(team_id)
        if team is None:
            return None
    
        return {
            **team.to_dict(),
            "tasks": _summarize_team_tasks(team_id),
        }
    
    
    # ---------------------------------------------------------------------------
    # System Evolution (自我演进引擎)
    # ---------------------------------------------------------------------------
    
    @router.get("/evolution/status")
    async def evolution_status():
        """获取自我演进引擎状态。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        status = _evolution_engine.get_status()
        return {
            "status": "initialized" if status.get("initialized") else "not_initialized",
            **status,
        }
    
    
    @router.get("/evolution/summary")
    async def evolution_summary():
        """获取演进项汇总。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_evolution_summary()
    
    
    @router.get("/evolution/items")
    async def evolution_items(status: Optional[str] = None, limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
        """获取演进项列表，可按状态过滤、分页。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        items = _evolution_engine.get_evolution_items(status=status)
        total = len(items)
        sliced = items[offset:offset + limit]
        return {
            "items": sliced,
            "total": total,
            "limit": limit,
            "offset": offset,
            "has_more": offset + limit < total,
        }
    
    
    @router.get("/evolution/rules")
    async def evolution_rules(limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
        """获取审查规则列表（分页）。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        items = [r.to_dict() for r in _evolution_engine.audit_rules]
        total = len(items)
        sliced = items[offset:offset + limit]
        return {
            "items": sliced,
            "total": total,
            "limit": limit,
            "offset": offset,
            "has_more": offset + limit < total,
        }
    
    
    @router.post("/evolution/audit")
    async def evolution_run_audit():
        """手动触发一次审查。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.run_full_audit()
    
    
    @router.post("/evolution/cycle")
    async def evolution_run_cycle():
        """运行完整演进周期（审查→派发→验证→关闭）。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.run_evolution_cycle()
    
    
    @router.post("/evolution/dispatch")
    async def evolution_dispatch():
        """派发所有待处理演进项给 Build 团队。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.dispatch_all_pending()
    
    
    @router.post("/evolution/verify")
    async def evolution_verify():
        """验证所有待验证项。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.verify_all_pending()
    
    
    @router.get("/evolution/items/{item_id}")
    async def evolution_item_detail(item_id: str):
        """获取单个演进项详情。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        item = _evolution_engine.evolution_items.get(item_id)
        if not item:
            raise HTTPException(404, f"Item '{item_id}' not found")
        return item.to_dict()
    
    
    @router.post("/evolution/items/{item_id}/progress")
    async def evolution_mark_progress(item_id: str):
        """标记演进项为进行中。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        ok = _evolution_engine.mark_in_progress(item_id)
        if not ok:
            raise HTTPException(404, f"Item '{item_id}' not found")
        return {"status": "ok", "item_id": item_id, "new_status": "in_progress"}
    
    
    @router.post("/evolution/items/{item_id}/complete")
    async def evolution_mark_complete(item_id: str):
        """标记演进项构建完成，进入待验证。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        ok = _evolution_engine.mark_build_complete(item_id)
        if not ok:
            raise HTTPException(404, f"Item '{item_id}' not found")
        return {"status": "ok", "item_id": item_id, "new_status": "verify_pending"}
    
    
    @router.post("/evolution/close-verified")
    async def evolution_close_verified():
        """关闭所有已验证通过的演进项。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        closed = _evolution_engine.close_verified()
        return {"closed": closed, "count": len(closed)}
    
    
    @router.post("/evolution/close")
    async def evolution_close():
        """关闭所有已验证通过的演进项 (close-verified 别名)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        closed = _evolution_engine.close_verified()
        return {"closed": closed, "count": len(closed)}
    
    
    @router.get("/evolution/history")
    async def evolution_audit_history(limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
        """获取审查历史记录（分页）。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        raw = _evolution_engine.get_audit_history()
        # Normalize field names for frontend (expects timestamp, total)
        result = []
        for h in raw:
            entry = dict(h)
            entry.setdefault("timestamp", entry.pop("time", None))
            entry.setdefault("total", (entry.get("passed") or 0) + (entry.get("failed") or 0) + (entry.get("skipped") or 0))
            result.append(entry)
        total = len(result)
        sliced = result[offset:offset + limit]
        return {
            "items": sliced,
            "total": total,
            "limit": limit,
            "offset": offset,
            "has_more": offset + limit < total,
        }
    
    
    @router.get("/evolution/analytics")
    async def evolution_analytics():
        """获取演进分析数据 (域覆盖、严重度分布、趋势)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        summary = _evolution_engine.get_evolution_summary()
        history = _evolution_engine.get_audit_history()
        status = _evolution_engine.get_status()
    
        return {
            "summary": summary,
            "history": history,
            "stats": status.get("stats", {}),
            "items_by_status": status.get("items_by_status", {}),
            "rules_count": status.get("audit_rules_count", 0),
        }
    
    
    # ---------------------------------------------------------------------------
    # Phase 3: 业界标准化改进 API
    # ---------------------------------------------------------------------------
    
    @router.get("/evolution/compliance-rating")
    async def evolution_compliance_rating():
        """获取 DNV CII 风格 A~E 合规评级。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _serialize_compliance_rating()
    
    
    def _serialize_compliance_rating() -> Dict[str, Any]:
        data = _evolution_engine.get_compliance_rating()
        data["grade"] = data.get("rating", "?")
        data["description"] = data.get("rating_label", "")
        escalation = _evolution_engine.get_escalation_status()
        data["escalation_tier"] = "corrective" if escalation.get("escalated_count", 0) > 0 else "normal"
        return data
    
    
    @router.post("/evolution/compliance-rating/calculate")
    async def evolution_calculate_rating():
        """重新计算合规评级 (运行快速审查)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.calculate_compliance_rating()
    
    
    @router.get("/evolution/checklist")
    async def evolution_checklist(level: Optional[str] = None):
        """获取 ClassNK 双层自查清单 (company/ship)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_checklist(level=level)
    
    
    @router.get("/evolution/zones")
    async def evolution_zones():
        """获取所有合规区域。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_all_zones()
    
    
    @router.get("/evolution/zones/active")
    async def evolution_active_zones():
        """获取当前激活的合规区域
    ```
    
    ### 文件: `src/backend/tests/conftest.py`
    ```py
    # -*- coding: utf-8 -*-
    """pytest 共享 Fixtures — 测试流水线基础设施."""
    
    from __future__ import annotations
    
    import json
    import os
    import sys
    import tempfile
    from pathlib import Path
    from typing import Any, Dict
    from unittest.mock import AsyncMock, MagicMock, patch
    
    import pytest
    from fastapi.testclient import TestClient
    
    # Ensure src/backend is in path
    _backend_root = Path(__file__).resolve().parent.parent
    if str(_backend_root) not in sys.path:
        sys.path.insert(0, str(_backend_root))
    
    
    @pytest.fixture
    def sample_lamport_clock():
        """提供一个标准的 Lamport 时钟实例."""
        from agents.ab_testing import LamportClock
        return LamportClock(node_id="test-node-1")
    
    
    @pytest.fixture
    def default_ewma_config():
        """提供默认 EWMA 配置."""
        from agents.ab_testing import EWMAConfig
        return EWMAConfig()
    
    
    @pytest.fixture
    def default_ewma_engine(default_ewma_config):
        """提供默认 EWMA 阈值引擎."""
        from agents.ab_testing import EWMAThresholdEngine
        return EWMAThresholdEngine(config=default_ewma_config)
    
    
    @pytest.fixture
    def sample_ab_metrics():
        """提供示例 A/B 测试指标."""
        from agents.ab_testing import ABTestMetrics
        return ABTestMetrics(
            false_upgrade_rate=0.05,
            resource_increase_pct=12.0,
            behavior_fingerprint_mutation_rate=0.02,
            anomaly_propagation_depth=1.5,
            prediction_error_rate=0.08,
            energy_increase_pct=3.0,
            temperature_slope=0.01,
            policy_evaluation_latency_ms=45.0,
            evolution_stagnation_rate=0.03,
        )
    
    
    @pytest.fixture
    def temp_team_store():
        """使用临时文件的 TeamStore (测试后自动清理)."""
        from agents.team_store import TeamStore
    
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{}")
            tmp_path = Path(f.name)
    
        store = TeamStore(path=tmp_path)
        yield store
    
        # 清理
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)
    
    
    @pytest.fixture
    def temp_task_store():
        """使用临时目录的 TaskStore."""
        from agents.task_store import TaskStore
    
        with tempfile.TemporaryDirectory() as tmpdir:
            store = TaskStore(base_dir=Path(tmpdir))
            yield store
    
    
    @pytest.fixture
    def team_manager(temp_team_store):
        """提供 TeamManager 实例 (使用临时存储)."""
        from agents.team_manager import TeamManager
        return TeamManager(store=temp_team_store)
    
    
    @pytest.fixture
    def sample_team_dict():
        """示例团队字典."""
        return {
            "team_id": "test-team-001",
            "name": "测试团队",
            "description": "自动化测试团队",
        }
    
    
    @pytest.fixture
    def sample_agent_dict():
        """示例 AgentProfile 字典."""
        return {
            "agent_id": "agent-001",
            "name": "TestAgent",
            "role": "developer",
            "state": "idle",
        }
    
    
    @pytest.fixture
    def sample_model_dict():
        """示例 ModelConfig 字典."""
        return {
            "model_id": "model-001",
            "name": "deepseek-v4-test",
            "provider": "deepseek",
            "max_tokens": 65536,
            "temperature": 0.7,
            "is_default": True,
        }
    
    
    @pytest.fixture
    def task_engine():
        """提供 TaskEngine 实例."""
        from agents.task_engine import TaskEngine
        from agents.task_store import TaskStore
        with tempfile.TemporaryDirectory() as tmpdir:
            yield TaskEngine(max_concurrency=4, store=TaskStore(base_dir=Path(tmpdir)))
    
    
    @pytest.fixture
    def fastapi_client() -> TestClient:
        """提供 FastAPI TestClient (自动设置环境变量)."""
        # 确保测试时不连真实 LLM
        os.environ.setdefault("DEEPSEEK_API_KEY", "test-key-not-real")
        os.environ.setdefault("OPENAI_API_KEY", "test-key-not-real")
    
        # Mock 掉 LLM 相关依赖，避免真实请求
        from main import app
        return TestClient(app)
    
    
    @pytest.fixture
    def mock_llm_call():
        """Mock LLM 调用，返回固定响应."""
        with patch("agents.chat_harness.call_llm", new_callable=AsyncMock) as mock:
            mock.return_value = "这是模拟的 LLM 回复"
            yield mock
    
    
    @pytest.fixture
    def sample_task_dict():
        """示例任务字典."""
        return {
            "task_id": "task-001",
            "title": "测试任务",
            "description": "一个用于测试的任务",
            "agent_id": "agent-001",
            "priority": 2,
            "dependencies": [],
        }
    
    
    # ── pytest 配置 ─────────────────────────────────────────────
    
    pytest_plugins = []  # 可在此添加 pytest 插件
    
    ```
    
    ### 文件: `src/backend/tests/test_evolution_race.py`
    ```py
    # -*- coding: utf-8 -*-
    """审核流竞态与断网场景测试 — EvolutionExecutor / Audit 并发 & 网络容错.
    
    覆盖:
    - EvolutionExecutor 并发执行 (Semaphore 控制)
    - 审核流竞态: 同时对同一演进项发起多次审核
    - 断网恢复: 模拟 API 不可达 / 超时
    - 回调竞态: on_complete 同时触发时的状态一致性
    - 事件日志完整性: 并发下事件无丢失/乱序
    
    注意: 所有 async 测试通过 asyncio.run() 包装，无需 pytest-asyncio。
    """
    
    from __future__ import annotations
    
    import asyncio
    import sys
    import time
    from pathlib import Path
    from typing import Any, Dict, List
    from unittest.mock import patch
    
    import pytest
    
    # Ensure src/backend is in path
    _backend_root = Path(__file__).resolve().parent.parent
    if str(_backend_root) not in sys.path:
        sys.path.insert(0, str(_backend_root))
    
    
    # ── Helper: 创建模拟演化项 ────────────────────────────────────────────────
    
    def _make_item_dict(
        item_id: str = "ev-test-001",
        title: str = "测试演化项",
        description: str = "用于竞态测试的演化项",
        current_behavior: str = "当前无此功能",
        expected_behavior: str = "期望添加此功能",
        reference_standard: str = "业界标准 X",
    ) -> Dict[str, Any]:
        return {
            "item_id": item_id,
            "title": title,
            "description": description,
            "current_behavior": current_behavior,
            "expected_behavior": expected_behavior,
            "reference_standard": reference_standard,
        }
    
    
    # ── Fixtures ───────────────────────────────────────────────────────────────
    
    @pytest.fixture
    def executor():
        """提供 EvolutionExecutor 实例."""
        from channels.evolution_executor import EvolutionExecutor
        return EvolutionExecutor()
    
    
    @pytest.fixture
    def sample_item():
        """标准测试演化项."""
        return _make_item_dict()
    
    
    # ── 1. 并发执行测试 ────────────────────────────────────────────────────────
    
    class TestEvolutionExecutorConcurrency:
        """EvolutionExecutor 并发执行测试."""
    
        def test_single_execution(self, executor, sample_item):
            """单次执行基础流程."""
            completed = []
    
            def on_complete(item_id, result):
                completed.append((item_id, result))
    
            executor.set_on_complete(on_complete)
    
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.return_value = {
                        "ok": True,
                        "summary": "所有修改已完成",
                        "files_changed": ["src/backend/test_file.py"],
                        "iterations": 3,
                    }
                    await executor.execute("ev-test-001", sample_item)
                    await asyncio.sleep(0.2)
    
            asyncio.run(_run())
    
            assert executor.get_result("ev-test-001") is not None
            result = executor.get_result("ev-test-001")
            assert result["ok"] is True
            assert len(result["files_changed"]) == 1
            assert len(completed) == 1
    
        def test_concurrent_executions_respect_semaphore(self, executor):
            """并发执行应受 Semaphore 限制."""
            from channels.evolution_executor import MAX_CONCURRENT_EXECUTIONS
    
            active_count = 0
            max_active = 0
    
            original_run = executor._run_agent_loop
    
            def counting_run(*args, **kwargs):
                nonlocal active_count, max_active
                active_count += 1
                max_active = max(max_active, active_count)
                time.sleep(0.05)
                active_count -= 1
                return {"ok": True, "summary": "done", "files_changed": [], "iterations": 1}
    
            async def _run():
                with patch.object(executor, '_run_agent_loop', wraps=counting_run):
                    task_count = MAX_CONCURRENT_EXECUTIONS * 3
                    for i in range(task_count):
                        item = _make_item_dict(f"ev-conc-{i:03d}", f"并发任务 {i}")
                        await executor.execute(f"ev-conc-{i:03d}", item)
                    await asyncio.sleep(0.5)
    
            asyncio.run(_run())
    
            assert max_active <= MAX_CONCURRENT_EXECUTIONS, (
                f"并发数 {max_active} 超过上限 {MAX_CONCURRENT_EXECUTIONS}"
            )
    
        def test_duplicate_execution_prevented(self, executor):
            """重复执行同一演进项应被阻止."""
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.return_value = {
                        "ok": True, "summary": "done", "files_changed": [], "iterations": 1,
                    }
                    await executor.execute("ev-dup", _make_item_dict("ev-dup"))
                    await executor.execute("ev-dup", _make_item_dict("ev-dup"))
                    await asyncio.sleep(0.2)
                return mock_run.call_count
    
            call_count = asyncio.run(_run())
            assert call_count == 1, f"预期调用 1 次, 实际 {call_count} 次"
    
        def test_callback_race_condition(self, executor):
            """并发回调不应导致状态不一致."""
            results_received = []
            lock = asyncio.Lock()
    
            async def on_complete(item_id, result):
                async with lock:
                    results_received.append((item_id, result.get("ok")))
    
            executor.set_on_complete(on_complete)
    
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.return_value = {
                        "ok": True, "summary": "done", "files_changed": [], "iterations": 1,
                    }
                    for i in range(10):
                        await executor.execute(f"ev-cb-{i:03d}", _make_item_dict(f"ev-cb-{i:03d}"))
                    await asyncio.sleep(0.3)
    
            asyncio.run(_run())
    
            assert len(results_received) == 10, f"预期 10 个回调, 实际 {len(results_received)}"
            assert all(ok for _, ok in results_received)
    
    
    # ── 2. 断网/超时恢复测试 ──────────────────────────────────────────────────
    
    class TestNetworkResilience:
        """网络中断与超时容错测试."""
    
        def test_executor_handles_agent_loop_timeout(self, executor):
            """AgentLoop 超时时执行器应优雅降级."""
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.side_effect = TimeoutError("LLM API timeout after 30s")
                    await executor.execute("ev-timeout", _make_item_dict("ev-timeout"))
                    await asyncio.sleep(0.2)
    
            asyncio.run(_run())
    
            result = executor.get_result("ev-timeout")
            assert result is not None
            assert result["ok"] is False
            assert "error" in result
    
        def test_executor_handles_connection_error(self, executor):
            """连接中断时执行器应正确报告错误."""
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.side_effect = ConnectionError("Connection refused")
                    await executor.execute("ev-conn-err", _make_item_dict("ev-conn-err"))
                    await asyncio.sleep(0.2)
    
            asyncio.run(_run())
    
            result = executor.get_result("ev-conn-err")
            assert result is not None
            assert result["ok"] is False
    
        def test_executor_handles_os_error(self, executor):
            """系统级错误 (OSError) 时应正确报告."""
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.side_effect = OSError("Too many open files")
                    await executor.execute("ev-os-err", _make_item_dict("ev-os-err"))
                    await asyncio.sleep(0.2)
    
            asyncio.run(_run())
    
            result = executor.get_result("ev-os-err")
            assert result is not None
            assert result["ok"] is False
    
        def test_concurrent_with_one_failure(self, executor):
            """混合成功/失败并发: 成功的任务不受失败任务影响."""
            call_count = 0
    
            def mixed_run(*args, **kwargs):
                nonlocal call_count
                call_count += 1
                if call_count % 3 == 0:
                    raise TimeoutError("Simulated timeout")
                return {"ok": True, "summary": "done", "files_changed": [], "iterations": 1}
    
            async def _run():
                with patch.object(executor, '_run_agent_loop', wraps=mixed_run):
                    for i in range(9):
                        await executor.execute(f"ev-mix-{i:03d}", _make_item_dict(f"ev-mix-{i:03d}"))
                    await asyncio.sleep(0.3)
    
            asyncio.run(_run())
    
            success = 0
            failed = 0
            for i in range(9):
                r = executor.get_result(f"ev-mix-{i:03d}")
                assert r is not None, f"任务 ev-mix-{i:03d} 无结果"
                if r["ok"]:
                    success += 1
                else:
                    failed += 1
    
            assert success == 6, f"预期 6 成功, 实际 {success}"
            assert failed == 3, f"预期 3 失败, 实际 {failed}"
    
    
    # ── 3. 审核流竞态测试 ──────────────────────────────────────────────────────
    
    class TestAuditRaceConditions:
        """审核流并发竞态场景测试."""
    
        def test_concurrent_audit_same_target(self):
            """多个审核同时对不同规则执行."""
            from channels.system_evolution import SystemEvolutionChannel
    
            async def _run():
                channel = SystemEvolutionChannel()
                channel.initialize()
    
                async def run_audit(rule):
                    try:
                        return await channel.audit_single_rule(rule.id, target_channel="bridge_chat")
                    except Exception as e:
                        return f"error: {e}"
    
                rules = channel.audit_rules[:5]
                tasks = [run_audit(r) for r in rules]
                results = await asyncio.gather(*tasks, return_exceptions=True)
    
                for r in results:
                    if isinstance(r, Exception):
                        pytest.fail(f"审核异常: {r}")
                assert len(results) == 5
    
            asyncio.run(_run())
    
        def test_concurrent_discovery_dispatch(self):
            """并发发现与派发不应产生重复演化项."""
            from channels.system_evolution import SystemEvolutionChannel
    
            async def _run():
                channel = SystemEvolutionChannel()
                channel.initialize()
    
                await channel.run_full_audit()
                initial_count = len(channel.discovered_items)
    
                async def audit_once():
                    await channel.run_full_audit()
    
                await asyncio.gather(audit_once(), audit_once(), audit_once())
    
                final_count = len(channel.discovered_items)
                assert final_count <= initial_count * 2, (
                    f"演化项从 {initial_count} 膨胀到 {final_count}，疑似竞态重复"
                )
    
            asyncio.run(_run())
    
        def test_evolution_item_status_transition_race(self):
            """演化项状态转换的并发安全性."""
            from channels.system_evolution import (
                SystemEvolutionChannel,
                EvolutionItem,
                EvolutionStatus,
            )
    
            async def _run():
                channel = SystemEvolutionChannel()
                channel.initialize()
    
                item = EvolutionItem(
                    id="ev-race-status-test",
                    title="竞态状态测试",
                    description="测试并发状态转换",
                    domain="general",
                    severity="low",
                )
                channel.discovered_items.append(item)
    
                async def dispatch():
                    await asyncio.sleep(0.01)
                    item.status = EvolutionStatus.DISPATCHED
    
                async def verify():
                    await asyncio.sleep(0.02)
                    item.status = EvolutionStatus.VERIFIED
    
                await asyncio.gather(dispatch(), verify())
                assert item.status in (EvolutionStatus.DISPATCHED, EvolutionStatus.VERIFIED)
    
            asyncio.run(_run())
    
    
    # ── 4. 事件日志完整性测试 ──────────────────────────────────────────────────
    
    class TestEventLogIntegrity:
        """并发下事件日志完整性与顺序."""
    
        def test_event_log_no_loss(self, executor):
            """并发执行时事件日志不应丢失."""
            async def _run():
                with patch.object(executor, '_run_agent_loop') as mock_run:
                    mock_run.return_value = {
                        "ok": True, "summary": "done", "files_changed": [], "iterations": 1,
                    }
                    for i in range(5):
                        await executor.execute(f"ev-log-{i:03d}", _make_item_dict(f"ev-log-{i:03d}"))
                    await asyncio.sleep(0.3)
    
            asyncio.run(_run())
    
            for i in range(5):
                log = executor.get_event_log(f"ev-log-{i:03d}")
                event_types = [e.get("type") for e in log]
                assert "execution_start" in event_types, f"ev-log-{i:03d} 缺少 execution_start"
                assert "execution_end" in event_types, f"ev-log-{i:03d} 缺少 execution_end"
    
        def test_executor_status_accurate(self, executor):
            """执行器状态报告在并发下保持准确."""
            async def _run():
                with patch.object(executor, '_run_agent_loop') as moc
  ...(截断)
  
  ## ⚠️ 最重要的规则
  系统已自动预加载项目文件结构和相关源文件（见上方 📂 项目上下文）。
  **你必须只引用上方提供的实际文件**，严禁凭想象编造文件名或路径。
  如果上下文中没有某个文件，说明该文件不存在。
  
  ## 要求
  1. 仔细阅读上方提供的项目文件结构和源文件内容
  2. 根据**实际存在的文件**分析哪些需要修改
  3. 列出需要修改的文件的**完整路径** (必须是项目上下文中出现的路径)
  4. 分析实现方案的可行性
  5. 引用具体代码行号说明修改点
  
  项目根目录: /Users/panglaohu/Downloads/DoubleBoatClawSystem
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
  
  项目根目录: /Users/panglaohu/Downloads/AgentsGroup2026
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
────────────────────────────────────────────────────────────
⚡ 使用 DeepSeek V4 直连 (64K 输出, 流式)...

🔗 API: api.deepseek.com | 模型: deepseek-v4-pro
────────────────────────────────────────────────────────────

我会以 **Researcher** 身份，基于项目上下文和你给出的 PM 分解结果，对“基于混沌工程的稳定性测试集”进行技术调研。重点放在：**可落地的文件清单、混沌策略/SLO 验证点与现有代码的衔接方式**。

---

## 一、任务拆解与技术目标

| 项目 | 说明 |
|------|------|
| 目标 | 建立 **混沌工程** 风格的自动化稳定性测试集 |
| 范围 | **Spot 实例回收、缓存失效、数据分层/冷热策略** |
| 验收维度 | **SLO 达标率** + **成本-质量双维度** |
| 依赖 | 任务 1（基础设施/API 就绪）、任务 3（缓存 & 分层策略已实现） |
| 产物形式 | 自动化测试报告（HTML / JSON）+ pytest 测试套件 |

---

## 二、技术调研结论（可行性 & 落点）

### 2.1 现有代码中与混沌/容灾相关的能力

| 能力 | 位置 | 作用 |
|------|------|------|
| EvolutionExecutor 竞态/断网测试 | `src/backend/tests/test_evolution_race.py` | 已验证异步并发、网络超时与 OSError 优雅降级 |
| 异步 Semaphore 控制 | 同上 `TestEvolutionExecutorConcurrency` | 可直接复用并发控制模式 |
| 任务引擎测试 | `src/backend/tests/test_task_engine.py` | 任务发布/状态机可被混沌策略驱动 |
| Plaza dispatch 测试 | `src/backend/tests/test_plaza_dispatch.py` | 可用于验证下游链路对混沌的容忍性 |
| `conftest.py` 中临时存储 & mock | `src/backend/tests/conftest.py` | 提供隔离的缓存/存储/网络模拟基座 |
| `test_evolution_race.py` 中 Semaphore + lock 模式 | 已给出并发安全样板 | 可直接用于缓存/分层策略边界并发测试 |

**结论：现有项目已具备混沌测试所需的基础设施（异步并发、网络故障模拟、资源隔离夹具）** ✅

---

### 2.2 需要新增/修改的文件清单（仅列出实际存在的路径）

以下全部基于你提供的项目文件结构，不存在臆造文件名。

**🔧 新增测试文件**
```
src/backend/tests/test_stability_chaos_slo.py
```
（完全新建，不修改已有文件）

**🔧 需要修改的文件（最少侵入性）**
```
src/backend/tests/conftest.py
```
（补充 **Spot 实例回收、缓存层、数据分层** 的模拟夹具）

**📊 可选前端报告（如需可视化）**
```
src/frontend/index.html
```
（若需嵌入测试报告链接入口，但非必须）

---

### 2.3 混沌策略方案（4 个核心能力 + SLO 验证点）

| 策略编号 | 混沌场景 | 模拟方式 | 验证 SLO |
|----------|----------|-----------|-----------|
| **CS-01** | Spot 实例突然终止（graceful shutdown） | 参数化注入 `asyncio.CancelledError` / `SystemExit` | 任务重调度延迟 < 5s（SLO） |
| **CS-02** | Spot 实例网络分区 → 恢复 | `mock` 注入 `TimeoutError` / `ConnectionError` 后释放 | 恢复后缓存一致性验证 |
| **CS-03** | 缓存节点不可用（Redis/Mem 模拟） | 通过 mock 使 `skill_store` / `task_store` 返回 `ConnectionError` | 缓存未命中回源时间 < 200ms |
| **CS-04** | 数据分层冷热切换风暴 | 并发修改分层策略同时触发大量迁移任务 | 任务引擎不出现死锁 / 并发写入串行化错误 |

**成本-质量双维度验收标准**：
- **质量维**：SLO 达成率 ≥ 95%，无数据不一致
- **成本维**：混沌注入期间额外的 **LLM token / API 调用次数 / 资源重试数** 不超过基线 * 1.3

---

### 2.4 实现方案（具体到文件与代码）

**1) 新建 `test_stability_chaos_slo.py`**
- 结构基于 `test_evolution_race.py` 的模式（`asyncio.run()` 包装 async 测试，无需 pytest-asyncio）
- 复用 `conftest.py` 中的 `task_engine`、`team_manager`、`mock_llm_call` 夹具
- 实现 4 个测试类：
  - `TestSpotInstanceResilience`
  - `TestCacheFailureDegradation`
  - `TestDataTieringChaos`
  - `TestSLOComplianceReporting`

**2) 修改 `conftest.py`**
- 增加 fixture `mock_spot_instance_killer()`：模拟 Spot 回收信号
- 增加 fixture `mock_cache_failure_engine()`：模拟缓存可恢复/不可恢复错误
- 增加 fixture `mock_tier_migration_worker()`：模拟数据分层迁移任务

**3) 报告生成**
- 利用 pytest `--json-report` 或 `pytest-json-report` 插件生成结构化报告
- 或编写一个 `SLOReportCollector` 聚合器，在测试中累积各场景 SLO 达标/成本数据，由 `test_stability_chaos_slo.py` 的 `teardown` 输出 JSON 报告。

---

## 三、下一步动作建议

1. **由 Architect 确认**：
   - Spot 实例终止时预期的任务重调度流程入口（调用哪个 API / 状态��）
   - 缓存/分层策略的具体实现文件路径（不在当前上下文中，但如果是任务 3 产出，需届时接入）
2. **由 Developer 实现**：
   - 在上方新增测试文件中按 CS-01 ~ CS-04 顺序实现测试用例
3. **由 QA/测试工程师**：
   - 跑完测试套件后根据 `SLOReportCollector` 产出自动报告

---

## 四、技术风险

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| 任务 3 的缓存/分层实现与混沌策略假设不一致 | 测试无法对接到真实实现 | 在任务 3 完成后二次校准 fixture 接口 |
| Spot 实例终止行为在本地环境难以完全模拟 | 部分场景仅 mock，缺乏生产级真实性 | 增加混沌工程基线指标（如 error injection coverage） |
| `asyncio.CancelledError` 会中断整个 event loop | 测试本身可能抛出未捕获异常 | 使用 `asyncio.wait_for` + `try/except` 严格控制作用域 |

---

## 五、总结

| 项 | 结论 |
|------|------|
| 是否有现成基础设施 | ✅ 有（`test_evolution_race.py`、`conftest.py`） |
| 是否需要引入新依赖 | 可以不需要（pytest + mock + asyncio），报告可引入 `pytest-json-report` |
| 工程量评估 | 中低：新增 1 个测试文件 + 修改 1 个夹具文件 |
| 是否符合成本-质量验收 | ✅ 可通过自定义 collector 和 SLO 阈值判断生成报告 |

---

如果你需要我 **直接生成 `test_stability_chaos_slo.py` 的初版伪代码框架** 或 **更详细的 Spot/Cache 注入模型定义**，我可以在下一步继续交付。

────────────────────────────────────────────────────────────
✅ deepseek-v4-pro 完成
