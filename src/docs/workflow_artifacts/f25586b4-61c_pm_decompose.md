# PM分解 — project_manager

任务: 基于实际监控数据，评估当前方案对Agent推理延迟的影响，决定是否引入更复杂的状态同步机制
步骤: pm_decompose
Agent: build_pm

---

📋 任务: f25586b4-61c
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
  基于实际监控数据，评估当前方案对Agent推理延迟的影响，决定是否引入更复杂的状态同步机制
  负责角色: 全体
  依赖: 任务3
  预期产出: POC阶段性能评估报告
  负责角色: 全体
  依赖: 任务3
  预期产出: POC阶段性能评估报告
  
  ## 📂 项目上下文 (系统自动预加载)
  
  ### 项目文件结构 (src/ 目录)
  ```
  src/frontend/Agent-digital-twin.html
  src/frontend/agent-team-config.html
  src/frontend/cost-dashboard.html
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
  src/frontend/css/cost-dashboard.css
  src/frontend/css/openbridge-theme.css
  src/frontend/css/sandbox-twin.css
  src/frontend/css/skill-extract-timeline.css
  src/frontend/css/skill-extract.css
  src/frontend/css/tasks-ws.css
  src/frontend/css/topbar-ws.css
  src/frontend/css/variables.css
  src/frontend/css/ws-theme-bridge.css
  src/frontend/js/agent-detail.js
  src/frontend/js/agent-team-config.js
  src/frontend/js/api.js
  src/frontend/js/cost-dashboard.js
  src/frontend/js/digital-twin-cli-3d.js
  src/frontend/js/digital-twin-cli.js
  src/frontend/js/evidence-runs.js
  src/frontend/js/extract-routing.js
  src/frontend/js/global-nav.js
  src/frontend/js/global-nav.js.bak
  src/frontend/js/i18n.js
  src/frontend/js/nav-sidebar.js
  src/frontend/js/plaza.js
  src/frontend/js/sandbox-twin-3d.js
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
  src/frontend/node_modules/.vite/vitest/da39a3ee5e6b4b0d3255bfef95601890afd80709/results.json
  src/frontend/__tests__/agent-config.test.js
  src/frontend/__tests__/agent-detail-pagination.test.js
  src/frontend/__tests__/agent-team-config-pagination.test.js
  src/frontend/__tests__/agent-team-config-state.test.js
  src/frontend/__tests__/api.test.js
  src/frontend/__tests__/cost-dashboard.test.js
  src/frontend/__tests__/csrf-pages.test.js
  src/frontend/__tests__/digital-twin-cli-pagination.test.js
  src/frontend/__tests__/evidence-runs.test.js
  src/frontend/__tests__/extract-routing.test.js
  src/frontend/__tests__/global-nav.test.js
  src/frontend/__tests__/login-page-flow.test.js
  src/frontend/__tests__/plaza-action-paths.test.js
  src/frontend/__tests__/plaza-modal-input.test.js
  src/frontend/__tests__/plaza-pagination.test.js
  src/frontend/__tests__/plaza-runtime-helpers.test.js
  src/frontend/__tests__/skill-extract-action-paths.test.js
  src/frontend/__tests__/skill-extract-verification.test.js
  src/frontend/__tests__/skill-publish-gate.test.js
  src/frontend/__tests__/system-evolution.test.js
  src/frontend/__tests__/tasks-pagination.test.js
  src/frontend/__tests__/tools-skills.test.js
  src/frontend/__tests__/utils-surface.test.js
  src/frontend/__tests__/utils.test.js
  src/frontend/__tests__/wizard-pagination.test.js
  src/backend/0tfuaiyp
  src/backend/__init__.py
  src/backend/agent_team_api.py
  src/backend/ci_cost_gate.py
  src/backend/config.py
  src/backend/datacenter_api.py
  src/backend/main.py
  src/backend/main.py.bak
  src/backend/server.log
  src/backend/startup_check.py
  src/backend/startup_validator.py
  src/backend/token_factory.py
  src/backend/tests/__init__.py
  src/backend/tests/conftest.py
  src/backend/tests/conftest.py.bak
  src/backend/tests/test_ab_testing.py
  src/backend/tests/test_agent_skill_binding.py
  src/backend/tests/test_agent_toolbox.py
  src/backend/tests/test_api_handler_integration.py
  src/backend/tests/test_api_integration_extended.py
  src/backend/tests/test_api_pagination.py
  src/backend/tests/test_api_rate_limit.py
  src/backend/tests/test_auth_csrf.py
  src/backend/tests/test_channel_event_bridge.py
  src/backend/tests/test_chaos_stability.py
  src/backend/tests/test_core_api_smoke.py
  src/backend/tests/test_cost_gate.py
  src/backend/tests/test_cost_monitor.py
  src/backend/tests/test_datacenter_api.py
  src/backend/tests/test_evidence_store.py
  src/backend/tests/test_evolution_evidence_detail.py
  src/backend/tests/test_evolution_race.py
  src/backend/tests/test_evolution_race.py.bak
  src/backend/tests/test_execution_evidence.py
  src/backend/tests/test_fingerprint.py
  src/backend/tests/test_fingerprint.py.bak
  src/backend/tests/test_frontend_auth_contract.py
  src/backend/tests/test_gate_evaluator.py
  src/backend/tests/test_gate_evaluator.py.bak
  src/backend/tests/test_main_health.py
  src/backend/tests/test_merge_plugin.py
  src/backend/tests/test_merge_plugin.py.bak
  src/backend/tests/test_models.py
  src/backend/tests/test_models.py.bak
  src/backend/tests/test_network_egress.py
  src/backend/tests/test_network_egress.py.bak
  src/backend/tests/test_operation_store.py
  src/backend/tests/test_permissions_and_secrets.py
  src/backend/tests/test_plan_loop_runtime.py
  src/backend/tests/test_plaza_consensus.py
  src/backend/tests/test_plaza_dispatch.py
  src/backend/tests/test_plaza_evolution_bridge.py
  src/backend/tests/test_plaza_retry_escalation.py
  src/backend/tests/test_plaza_structured_outputs.py
  src/backend/tests/test_plaza_task_artifact_bridge.py
  src/backend/tests/test_qa_gate_pipeline.py
  src/backend/tests/test_qa_gate_pipeline.py.bak
  src/backend/tests/test_request_models.py
  src/backend/tests/test_review_integration.py
  src/backend/tests/test_review_integration.py.bak
  src/backend/tests/test_sandbox_docker.py
  src/backend/tests/test_sandbox_security.py
  src/backend/tests/test_sandbox_smoke.py
  src/backend/tests/test_security_headers.py
  src/backend/tests/test_skill_publish_gate.py
  src/backend/tests/test_skill_verifier.py
  src/backend/tests/test_start_script_auth_bootstrap.py
  src/backend/tests/test_startup_validator.py
  src/backend/tests/test_state_machine.py
  src/backend/tests/test_storage_lifecycle.py
  src/backend/tests/test_storage_lifecycle.py.bak
  src/backend/tests/test_task_engine.py
  src/backend/tests/test_task_engine.py.bak
  src/backend/tests/test_team_manager.py
  src/backend/tests/test_team_manager.py.bak
  src/backend/tests/test_template_variants.py
  src/backend/tests/test_template_variants.py.bak
  ... (共 1197 个 src/ 文件)
  
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
  from pydantic import BaseModel, Field
  from typing import Any, Dict, List, Optional
  
  router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
  
  try:
      from config import DEFAULT_PAGE_SIZE as _DEFAULT_PAGE_SIZE
      from config import MAX_PAGE_SIZE as _MAX_PAGE_SIZE
  except Exception:
      _DEFAULT_PAGE_SIZE = 50
      _MAX_PAGE_SIZE = 200
  
  
  # ---------------------------------------------------------------------------
  # 全局引用（在 main.py startup 时注入）
  # ---------------------------------------------------------------------------
  _build_team = None
  _execution_team = None
  _scheduler = None
  _evolution_engine = None
  
  
  def _paginate_optional(items: List[Dict[str, Any]], *, limit: int, offset: int) -> Any:
      """Preserve old array responses by default while enabling optional pagination."""
      limit = getattr(limit, "default", limit)
      offset = getattr(offset, "default", offset)
      limit = int(limit or 0)
      offset = max(int(offset or 0), 0)
      if limit <= 0 and offset <= 0:
          return items
      if limit <= 0:
          limit = _DEFAULT_PAGE_SIZE
      limit = min(limit, _MAX_PAGE_SIZE)
      total = len(items)
      return {
          "items": items[offset:offset + limit],
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
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
  
  
  class EvolutionCloseRequest(BaseModel):
      reason: str = Field(default="", description="关闭理由")
      verify_conclusion: str = Field(default="", description="验证结论")
  
  
  class EvolutionCompleteRequest(BaseModel):
      code_changes: List[str] = Field(default_factory=list, description="构建阶段产生的代码或配置变更")
      artifact_dir: str = Field(default="", description="构建阶段产物目录")
  
  
  class FeedbackSubmission(BaseModel):
      category: str = "optimization"
      severity: str = "medium"
      title: str
      detail: str
  
  # ── 演化优化请求模型 ──────────────────────────────────────────
  
  class OptimizeRequest(BaseModel):
      target_type: str = "skill"
      target_id: str = ""
      team_id: str = "build_system"
      iterations: int = Field(default=5, ge=1, le=10)
      content: str = ""
  
  class AutoTriageRequest(BaseModel):
      team_id: str = "build_system"
      top_n: int = Field(default=5, ge=1, le=10)
  
  class DatasetGenerateRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      count: int = Field(default=15, ge=1, le=30)
  
  class ExampleItem(BaseModel):
      task_input: str
      rubric: str
  
  class DatasetManualRequest(BaseModel):
      dataset_id: str = ""
      skill_id: str = ""
      examples: List[ExampleItem] = Field(default_factory=list)
      skill_name: str = ""
  
  class DatasetImportKBRequest(BaseModel):
      skill_id: str = ""
      skill_name: str = ""
      dataset_id: str = ""
      max_examples: int = Field(default=20, ge=1, le=50)
  
  class UpdateExamplesRequest(BaseModel):
      action: str = "replace_all"
      examples: List[ExampleItem] = Field(default_factory=list)
      indices: List[int] = Field(default_factory=list)
      index: int = -1
      example: Optional[ExampleItem] = None
  
  class StepBaselineRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      dataset_id: str = ""
  
  class FailureItem(BaseModel):
      task_input: str = ""
      rubric: str = ""
      composite: float = 0.0
      reasoning: str = ""
  
  class StepReflectRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      failures: List[FailureItem] = Field(default_factory=list)
      user_hints: str = ""
  
  class StepMutateRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      reflection: Dict[str, Any] = Field(default_factory=dict)
  
  class StepEvaluateCandidateRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      dataset_id: str = ""
      instructions: str = ""
  
  class StepApplyRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      instructions: str = ""
      baseline_score: float = 0.0
      new_score: float = 0.0
  
  
  # ---------------------------------------------------------------------------
  # Minimal AgentScheduler — provides basic scheduling status & tick
  # ---------------------------------------------------------------------------
  
  import time as _time
  
  
  class AgentScheduler:
      """轻量级调度器，提供运行状态、tick 计数、报告生成等基本能力。
  
      在 main.py startup 时自动创建并注入，确保前端团队概览的
      「调度器」卡片显示「运行中」而非「已停止」。
      """
  
      def __init__(self) -> None:
          self._started_at = _time.time()
          self._tick_count: int = 0
          self._last_tick_at: float = 0.0
  
      def get_status(self) -> Dict[str, Any]:
          return {
              "running": True,
              "tick_count": self._tick_count,
              "uptime_seconds": _time.time() - self._started_at,
              "last_tick_at": self._last_tick_at if self._last_tick_at else None,
          }
  
      def tick_once(self) -> Dict[str, Any]:
          """手动触发一次 tick（供调试/手动推进）."""
          self._tick_count += 1
          self._last_tick_at = _time.time()
          # 每次 tick 尝试驱动 evolution engine 的审查周期（如果存在）
          try:
              global _evolution_engine
              if _evolution_engine is not None:
                  _evolution_engine.audit()
          except Exception:
              pass
          return {"tick": self._tick_count, "ok": True}
  
      def generate_report_now(self) -> Dict[str, Any]:
          return {
              "status": self.get_status(),
              "summary": (f"调度器已运行 {self.get_status()['uptime_seconds']:.0f} 秒，"
                          f"累计 {self._tick_count} 次 tick"),
          }
  
  
  # ---------------------------------------------------------------------------
  # Scheduler API
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
  async def build_reports(
      limit: int = Query(default=10, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      items = [r.to_dict() for r in _build_team.hourly_reports]
      if limit > 0 and offset == 0:
          items = items[-limit:]
          return items
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
  @router.get("/build/issues")
  async def build_issues(
      limit: int = Query(default=0, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      items = list(_build_team.issue_backlog)
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
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
  async def execution_reports(
      limit: int = Query(default=10, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      items = [r.to_dict() for r in _execution_team.execution_reports]
      if limit > 0 and offset == 0:
          items = items[-limit:]
          return items
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
  @router.get("/execution/feedback")
  async def execution_feedback(
      limit: int = Query(default=0, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      items = [item.to_dict() for item in _execution_team.feedback_queue]
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
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
          raise HTTPExceptio
  ```
  
  ### 文件: `src/backend/agents/operation_api.py`
  ```py
  # -*- coding: utf-8 -*-
  """操作事件 & 情境切片 API — 查询/追溯/统计 REST 端点.
  
  提供:
    - GET  /api/v1/operations           — 查询操作事件列表
    - GET  /api/v1/operations/{id}      — 获取单个操作事件
    - GET  /api/v1/operations/{id}/trace — 获取操作追溯 (操作+关联切片)
    - GET  /api/v1/operations/{id}/chain — 获取操作因果链
    - GET  /api/v1/context-slices        — 查询情境切片列表
    - GET  /api/v1/context-slices/{id}   — 获取单个情境切片
    - GET  /api/v1/operations/stats      — 存储统计
    - GET  /api/v1/operations/verify     — 完整性验证
    - POST /api/v1/operations/record     — 记录操作事件 (内部调用)
  
  设计原则:
    - 只读端点 (GET) 公开给前端审计面板
    - 写入端点 (POST /record) 供后端 Agent 内部调用
    - 所有响应包含完整性状态
  """
  
  from __future__ import annotations
  
  import logging
  from typing import Any, Dict, List, Optional
  
  from fastapi import APIRouter, HTTPException, Query
  from pydantic import BaseModel, Field
  
  from .operation_models import (
      OperationEvent,
      OperationType,
      OperationQuery,
      OperationTrace,
      ContextQuery,
      ContextSlice,
      ContextType,
  )
  from .operation_store import get_operation_store
  from .evidence_store import EvidenceRun, EvidenceQuery, get_evidence_store
  
  logger = logging.getLogger(__name__)
  
  router = APIRouter(prefix="/api/v1/operations", tags=["Operations"])
  
  # 额外的情境切片子路由
  slices_router = APIRouter(prefix="/api/v1/context-slices", tags=["Context Slices"])
  
  # 统一验证/执行证据子路由
  evidence_router = APIRouter(prefix="/api/v1/evidence-runs", tags=["Evidence Runs"])
  
  
  # ═══════════════════════════════════════════════════════════════
  # Pydantic Schemas
  # ═══════════════════════════════════════════════════════════════
  
  
  class RecordOperationRequest(BaseModel):
      """记录操作事件的请求体."""
      operation_type: str = Field(..., description="操作类型: tool_call / task_started / ...")
      agent_id: str = Field(default="system")
      team_id: str = Field(default="default")
      summary: str = Field(default="")
      detail: Optional[Dict[str, Any]] = Field(default_factory=dict)
      parent_operation_id: Optional[str] = None
      session_id: Optional[str] = None
      task_id: Optional[str] = None
      idempotency_key: Optional[str] = None
      # 可选的情境切片
      context_slices: Optional[List[Dict[str, Any]]] = None
  
  
  class OperationResponse(BaseModel):
      """操作事件响应."""
      ok: bool = True
      operation: Dict[str, Any]
  
  
  class OperationListResponse(BaseModel):
      """操作事件列表响应."""
      ok: bool = True
      operations: List[Dict[str, Any]]
      total: int
      limit: int
      offset: int
  
  
  class TraceResponse(BaseModel):
      """操作追溯响应."""
      ok: bool = True
      trace: Dict[str, Any]
  
  
  class ChainResponse(BaseModel):
      """因果链响应."""
      ok: bool = True
      chain: List[Dict[str, Any]]
      depth: int
  
  
  class SliceResponse(BaseModel):
      """情境切片响应."""
      ok: bool = True
      slice: Dict[str, Any]
  
  
  class SliceListResponse(BaseModel):
      """情境切片列表响应."""
      ok: bool = True
      slices: List[Dict[str, Any]]
      total: int
      limit: int
      offset: int
  
  
  class StatsResponse(BaseModel):
      """统计响应."""
      ok: bool = True
      stats: Dict[str, Any]
  
  
  class VerifyResponse(BaseModel):
      """完整性验证响应."""
      ok: bool = True
      verification: Dict[str, Any]
      healthy: bool
  
  
  class RecordEvidenceRunRequest(BaseModel):
      """记录统一证据的请求体."""
      evidence_type: str = Field(..., description="证据类型: skill_verify / agent_loop / evolution_verify / cost_gate")
      status: str = Field(..., description="结果状态: passed / failed / blocked / ...")
      summary: str = ""
      team_id: Optional[str] = None
      agent_id: Optional[str] = None
      skill_id: Optional[str] = None
      task_id: Optional[str] = None
      evolution_item_id: Optional[str] = None
      cost_target_id: Optional[str] = None
      plaza_topic_id: Optional[str] = None
      session_id: Optional[str] = None
      request_id: Optional[str] = None
      operation_id: Optional[str] = None
      runtime: Optional[Dict[str, Any]] = Field(default_factory=dict)
      command: str = ""
      exit_code: Optional[int] = None
      artifact_dir: str = ""
      stdout: str = ""
      stderr: str = ""
      metrics_before: Optional[Dict[str, Any]] = Field(default_factory=dict)
      metrics_after: Optional[Dict[str, Any]] = Field(default_factory=dict)
      detail: Optional[Dict[str, Any]] = Field(default_factory=dict)
  
  
  class EvidenceRunResponse(BaseModel):
      """统一证据响应."""
      ok: bool = True
      evidence: Dict[str, Any]
  
  
  class EvidenceRunListResponse(BaseModel):
      """统一证据列表响应."""
      ok: bool = True
      evidence_runs: List[Dict[str, Any]]
      total: int
      limit: int
      offset: int
  
  
  # ═══════════════════════════════════════════════════════════════
  # Operation Endpoints
  # ═══════════════════════════════════════════════════════════════
  
  
  @router.post("/record", response_model=OperationResponse)
  async def record_operation(req: RecordOperationRequest):
      """记录一条操作事件 (内部调用).
  
      支持可选的情境切片列表，原子写入。
      幂等键去重: 相同 idempotency_key 不重复写入。
      """
      store = get_operation_store()
  
      # 解析 operation_type
      try:
          op_type = OperationType(req.operation_type)
      except ValueError:
          raise HTTPException(status_code=400, detail=f"未知操作类型: {req.operation_type}")
  
      event = OperationEvent.create(
          operation_type=op_type,
          agent_id=req.agent_id,
          team_id=req.team_id,
          summary=req.summary,
          detail=req.detail or {},
          parent_operation_id=req.parent_operation_id,
          session_id=req.session_id,
          task_id=req.task_id,
          idempotency_key=req.idempotency_key,
      )
  
      # 构建情境切片
      slices: List[ContextSlice] = []
      if req.context_slices:
          for cs_data in req.context_slices:
              ctx_type_str = cs_data.get("context_type", "custom")
              try:
                  ctx_type = ContextType(ctx_type_str)
              except ValueError:
                  ctx_type = ContextType.CUSTOM
              cs = ContextSlice.create(
                  operation_id=event.operation_id,
                  context_type=ctx_type,
                  payload=cs_data.get("payload", {}),
                  summary=cs_data.get("summary", ""),
                  entity_id=cs_data.get("entity_id"),
                  entity_type=cs_data.get("entity_type"),
              )
              slices.append(cs)
  
      if slices:
          ok = await store.record_operation_with_context(event, slices)
      else:
          ok = await store.append_operation(event)
  
      if not ok:
          return OperationResponse(
              ok=True,
              operation={
                  "operation_id": event.operation_id,
                  "status": "duplicate (idempotent)",
              }
          )
  
      return OperationResponse(ok=True, operation=event.to_dict())
  
  
  @router.get("", response_model=OperationListResponse)
  async def list_operations(
      operation_type: Optional[str] = Query(None, description="按操作类型过滤"),
      agent_id: Optional[str] = Query(None, description="按 Agent ID 过滤"),
      team_id: Optional[str] = Query(None, description="按团队 ID 过滤"),
      session_id: Optional[str] = Query(None, description="按会话 ID 过滤"),
      task_id: Optional[str] = Query(None, description="按任务 ID 过滤"),
      parent_operation_id: Optional[str] = Query(None, description="按父操作 ID 过滤"),
      start_time: Optional[str] = Query(None, description="起始时间 (ISO 8601)"),
      end_time: Optional[str] = Query(None, description="结束时间 (ISO 8601)"),
      limit: int = Query(100, ge=1, le=1000, description="返回条数"),
      offset: int = Query(0, ge=0, description="偏移量"),
  ):
      """查询操作事件列表."""
      store = get_operation_store()
  
      op_type_enum = None
      if operation_type:
          try:
              op_type_enum = OperationType(operation_type)
          except ValueError:
              raise HTTPException(status_code=400, detail=f"未知操作类型: {operation_type}")
  
      q = OperationQuery(
          operation_type=op_type_enum,
          agent_id=agent_id,
          team_id=team_id,
          session_id=session_id,
          task_id=task_id,
          parent_operation_id=parent_operation_id,
          start_time=start_time,
          end_time=end_time,
          limit=limit,
          offset=offset,
      )
  
      results = await store.query_operations(q)
      return OperationListResponse(
          operations=[op.to_dict() for op in results],
          total=len(results),
          limit=limit,
          offset=offset,
      )
  
  
  @router.get("/stats", response_model=StatsResponse)
  async def get_stats():
      """获取操作存储统计."""
      store = get_operation_store()
      stats = await store.get_stats()
      return StatsResponse(ok=True, stats=stats)
  
  
  @router.get("/verify", response_model=VerifyResponse)
  async def verify_integrity():
      """验证存储数据完整性."""
      store = get_operation_store()
      v = await store.verify_all()
      healthy = v["corrupt_ops"] == 0 and v["corrupt_slices"] == 0
      return VerifyResponse(ok=True, verification=v, healthy=healthy)
  
  
  @router.get("/{operation_id}", response_model=OperationResponse)
  async def get_operation(operation_id: str):
      """获取单个操作事件."""
      store = get_operation_store()
      op = await store.get_operation(operation_id)
      if not op:
          raise HTTPException(status_code=404, detail=f"操作 {operation_id} 不存在")
      return OperationResponse(ok=True, operation=op.to_dict())
  
  
  @router.get("/{operation_id}/trace", response_model=TraceResponse)
  async def get_operation_trace(operation_id: str):
      """获取操作追溯 — 操作事件 + 关联情境切片."""
      store = get_operation_store()
      trace = await store.get_trace(operation_id)
      if not trace:
          raise HTTPException(status_code=404, detail=f"操作 {operation_id} 不存在")
      return TraceResponse(ok=True, trace=trace.to_dict())
  
  
  @router.get("/{operation_id}/chain", response_model=ChainResponse)
  async def get_causal_chain(
      operation_id: str,
      max_depth: int = Query(20, ge=1, le=100, description="最大追溯深度"),
  ):
      """获取操作因果链 — 沿 parent_operation_id 回溯."""
      store = get_operation_store()
      chain = await store.get_causal_chain(operation_id, max_depth=max_depth)
      return ChainResponse(
          ok=True,
          chain=[op.to_dict() for op in chain],
          depth=len(chain),
      )
  
  
  # ═══════════════════════════════════════════════════════════════
  # EvidenceRun Endpoints
  # ═══════════════════════════════════════════════════════════════
  
  
  @evidence_router.post("", response_model=EvidenceRunResponse)
  async def record_evidence_run(req: RecordEvidenceRunRequest):
      """记录一条统一执行/验证证据."""
      run = EvidenceRun.create(
          evidence_type=req.evidence_type,
          status=req.status,
          summary=req.summary,
          team_id=req.team_id,
          agent_id=req.agent_id,
          skill_id=req.skill_id,
          task_id=req.task_id,
          evolution_item_id=req.evolution_item_id,
          cost_target_id=req.cost_target_id,
          plaza_topic_id=req.plaza_topic_id,
          session_id=req.session_id,
          request_id=req.request_id,
          operation_id=req.operation_id,
          runtime=req.runtime or {},
          command=req.command,
          exit_code=req.exit_code,
          artifact_dir=req.artifact_dir,
          stdout=req.stdout,
          stderr=req.stderr,
          metrics_before=req.metrics_before or {},
          metrics_after=req.metrics_after or {},
          detail=req.detail or {},
      )
      await get_evidence_store().append_evidence(run)
      return EvidenceRunResponse(ok=True, evidence=run.to_dict())
  
  
  @evidence_router.get("", response_model=EvidenceRunListResponse)
  async def list_evidence_runs(
      evidence_type: Optional[str] = Query(None, description="按证据类型过滤"),
      status: Optional[str] = Query(None, description="按状态过滤"),
      team_id: Optional[str] = Query(None, description="按团队 ID 过滤"),
      agent_id: Optional[str] = Query(None, description="按 Agent ID 过滤"),
      skill_id: Optional[str] = Query(None, description="按技能 ID 过滤"),
      task_id: Optional[str] = Query(None, description="按任务 ID 过滤"),
      evolution_item_id: Optional[str] = Query(None, description="按演进项 ID 过滤"),
      cost_target_id: Optional[str] = Query(None, description="按成本目标 ID 过滤"),
      plaza_topic_id: Optional[str] = Query(None, description="按 Plaza 话题 ID 过滤"),
      request_id: Optional[str] = Query(None, description="按 request_id 过滤"),
      start_time: Optional[str] = Query(None, description="起始时间 (ISO 8601)"),
      end_time: Optional[str] = Query(None, description="结束时间 (ISO 8601)"),
      limit: int = Query(100, ge=1, le=1000),
      offset: int = Query(0, ge=0),
  ):
      """查询统一执行/验证证据."""
      q = EvidenceQuery(
          evidence_type=evidence_type,
          status=status,
          team_id=team_id,
          agent_id=agent_id,
          skill_id=skill_id,
          task_id=task_id,
          evolution_item_id=evolution_item_id,
          cost_target_id=cost_target_id,
          plaza_topic_id=plaza_topic_id,
          request_id=request_id,
          start_time=start_time,
          end_time=end_time,
          limit=limit,
          offset=offset,
      )
      results = await get_evidence_store().query_evidence(q)
      return EvidenceRunListResponse(
          evidence_runs=[run.to_dict() for run in results],
          total=len(results),
          limit=limit,
          offset=offset,
      )
  
  
  @evidence_router.get("/by-object/{entity_type}/{entity_id}", response_model=EvidenceRunListResponse)
  async def list_evidence_by_object(
      entity_type: str,
      entity_id: str,
      limit: int = Query(100, ge=1, le=1000),
      offset: int = Query(0, ge=0),
  ):
      """按关联对象查询证据，如 skill/xxx、task/xxx、evolution/xxx."""
      results = await get_evidence_store().query_for_object(
          entity_type,
          entity_id,
          limit=limit,
          offset=offset,
      )
      return EvidenceRunListResponse(
          evidence_runs=[run.to_dict() for run in results],
          total=len(results),
          limit=limit,
          offset=offset,
      )
  
  
  @evidence_router.get("/verify", response_model=VerifyResponse)
  async def verify_evidence_runs():
      """验证 EvidenceRun 存储完整性."""
      v = await get_evidence_store().verify_all()
      return VerifyResponse(ok=True, verification=v, healthy=v["corrupt"] == 0)
  
  
  @evidence_router.get("/{evidence_id}", response_model=EvidenceRunResponse)
  async def get_evidence_run(evidence_id: str):
      """获取单条统一执行/验证证据."""
      run = await get_evidence_store().get_evidence(evidence_id)
      if not run:
          raise HTTPException(status_code=404, detail=f"证据 {evidence_id} 不存在")
      return EvidenceRunResponse(ok=True, evidence=run.to_dict())
  
  
  # ═══════════════════════════════════════════════════════════════
  # Context Slice Endpoints (via slices_router)
  # ═══════════════════════════════════════════════════════════════
  
  
  @slices_router.get("", response_model=SliceListResponse)
  async def list_slices(
      operation_id: Optional[str] = Query(None, description="按操作 ID 过滤"),
      context_type: Optional[str] = Query(None, description="按情境类型过滤"),
      entity_id: Optional[str] = Query(None, description="按实体 ID 过滤"),
      entity_type: Optional[str] = Query(None, description="按实体类型过滤"),
      start_time: Optional[str] = Query(None, description="起始时间"),
      end_time: Optional[str] = Query(None, description="结束时间"),
      limit: int = Query(100, ge=1, le=1000),
      offset: int = Query(0, ge=0),
  ):
      """查询情境切片列表."""
      store = get_operation_store()
  
      ctx_type_enum = None
      if context_type:
        
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
  _MAX_RETRIES = 3  # LLM 调用最大重试次数
  _RETRY_BACKOFF_BASE = 1.5  # 退避基数（秒）
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
          self._sse_queues: Dict[str, List[asyncio.Queue]] = {}  # discussion_id → queues
          self._discussion_locks: Dict[str, asyncio.Lock] = {}
          self._chat_fn: Optional[Callable] = None  # ChatHarness.chat reference
          self._escalation_queue: List[Dict[str, Any]] = []  # failed tasks for human review
  
      def set_chat_fn(self, fn: Callable):
          """注入 ChatHarness.chat 异步函数."""
          self._chat_fn = fn
  
      def _get_agent_profile(self, agent_id: str):
          """从 TeamManager 获取完整 AgentProfile，用于注入个性."""
          try:
              from agents.api import _team_manager
              if _team_manager:
                  for team in _team_manager.list_teams():
                      agent = team.get_agent(agent_id)
                      if agent:
                          return agent
          except Exception:
              pass
          return None
  
      def _build_agent_system_prompt(self, participant: Participant) -> str:
          """根据 AgentProfile 构建有个性的 system prompt."""
          profile = self._get_agent_profile(participant.agent_id)
          if profile:
              expertise = "、".join(profile.personality.expertise_areas) if profile.personality.expertise_areas else ""
              traits = "、".join(profile.metadata.get("traits", [])) if profile.metadata else ""
              parts = [
                  f"你是 {profile.name}，职责: {profile.role}。",
                  f"专长: {expertise}。" if expertise else "",
                  f"性格特质: {traits}。" if traits else "",
                  f"你的工作方式: {profile.system_prompt}" if profile.system_prompt else "",
                  f"\n你正在一个智能体广场的讨论中发言。",
                  f"请用自然的方式说话，像一个真实的专业人士在开会讨论。",
                  f"可以表达观点、提出建议、回应他人，说话要有内容、有依据。",
                  f"不需要客套寒暄，但要说人话，不要像电报一样压缩。",
              ]
              return "".join(p for p in parts if p)
          # 回退到基础信息
          return (
              f"你是 {participant.agent_name}，职责: {participant.role}。"
              f"你正在一个智能体广场的讨论中发言。"
              f"请用自然的方式说话，像一个真实的专业人士在开会讨论。"
              f"可以表达观点、提出建议、回应他人，说话要有内容、有依据。"
          )
  
      def _next_plan_revision(self, disc: Discussion) -> int:
          """Return the next monotonically increasing plan revision number."""
          current = 0
          if disc.plan:
              try:
                  current = int(disc.plan.get("revision", 0) or 0)
              except (TypeError, ValueError):
                  current = 0
          return current + 1
  
      def _build_plan_payload(self, disc: Discussion, content: str, reason: str) -> Dict[str, Any]:
          """Normalize discussion plan metadata for downstream task dispatch."""
          previous_task_ids = []
          if disc.plan:
              previous_task_ids = list(disc.plan.get("task_ids", []) or [])
          return {
              "revision": self._next_plan_revision(disc),
              "revision_reason": reason,
              "revised_at": datetime.now(timezone.utc).isoformat(),
              "content": content,
              "task_ids": previous_task_ids,
              "task_count": len(previous_task_ids),
          }
  
      # ── 广场 CRUD ──────────────────────────────────────────
  
      def create_plaza(self, name: str, description: str = "") -> Plaza:
          plaza = Plaza(name=name, description=description)
          self._plazas[plaza.id] = plaza
          self._store.save_plaza(plaza)
          logger.info(f"🏛️ 广场创建: {name} ({plaza.id})")
          return plaza
  
      def get_plaza(self, plaza_id: str) -> Optional[Plaza]:
          return self._plazas.get(plaza_id)
  
      def list_plazas(self) -> List[Plaza]:
          return list(self._plazas.values())
  
      def delete_plaza(self, plaza_id: str) -> bool:
          if plaza_id in self._plazas:
              del self._plazas[plaza_id]
              self._store.delete_plaza(plaza_id)
              return True
          return False
  
      # ── 参与者管理 ──────────────────────────────────────────
  
      def add_participant(
          self, plaza_id: str, agent_id: str, agent_name: str = "",
          role: str = "", team_id: str = "",
          seat_tier: SeatTier = SeatTier.MIDDLE,
          niche_role: NicheRole = NicheRole.OBSERVER,
      ) -> Optional[Participant]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return None
          # 分配壁龛编号 (动态扩展)
          used_niches = {p.niche_index for p in plaza.participants.values() if p.niche_index >= 0}
          niche_index = len(used_niches)
          # 自动扩展壁龛数
          if niche_index >= plaza.niche_count:
              plaza.niche_count = niche_index + 1
          p = Participant(
              agent_id=agent_id, agent_name=agent_name, role=role,
              team_id=team_id, seat_tier=seat_tier, niche_role=niche_role,
              niche_index=niche_index,
          )
          plaza.participants[agent_id] = p
          self._store.save_plaza(plaza)
          logger.info(f"🪑 参与者加入广场 {plaza_id}: {agent_name} (壁龛 #{niche_index})")
          return p
  
      def remove_participant(self, plaza_id: str, agent_id: str) -> bool:
          plaza = self._plazas.get(plaza_id)
          if plaza and agent_id in plaza.participants:
              del plaza.participants[agent_id]
              self._store.save_plaza(plaza)
              return True
          return False
  
      # ── 讨论管理 ──────────────────────────────────────────
  
      def create_discussion(
          self, plaza_id: str, topic: str, description: str = "",
          moderator_agent_id: str = "", max_rounds: int = 5,
      ) -> Optional[Discussion]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return None
          disc = Discussion(
              plaza_id=plaza_id, topic=topic, description=description,
              moderator_agent_id=moderator_agent_id, max_rounds=max_rounds,
          )
          plaza.discussions[disc.id] = disc
          self._store.save_plaza(plaza)
          logger.info(f"💬 讨论创建: {topic[:40]} ({disc.id})")
          return disc
  
      def get_discussion(self, plaza_id: str, discussion_id: str) -> Optional[Discussion]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return None
          return plaza.discussions.get(discussion_id)
  
      def list_discussions(self, plaza_id: str) -> List[Discussion]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return []
          return list(plaza.discussions.values())
  
      def delete_discussion(self, plaza_id: str, discussion_id: str) -> bool:
          plaza = self._plazas.get(plaza_id)
          if not plaza or discussion_id not in plaza.discussions:
              return False
          del plaza.discussions[discussion_id]
          self._sse_queues.pop(discussion_id, None)
          self._store.save_plaza(plaza)
          return True
  
      def reset_discussion(self, plaza_id: str, discussion_id: str) -> Optional[Discussion]:
          """重置已结束讨论，保留话题本身以便重新讨论。"""
          disc = self.get_discussion(plaza_id, discussion_id)
          if not disc:
              return None
          disc.status = DiscussionStatus.OPEN
          disc.current_round = 0
          disc.messages.clear()
          disc.summary = ""
          disc.key_conclusions.clear()
          disc.plan.clear()
          disc.assigned_team_id = ""
          disc.started_at = None
          disc.ended_at = None
          plaza = self._plazas.get(plaza_id)
          if plaza:
              self._store.save_plaza(plaza)
          return disc
  
      # ── SSE 订阅管理 ──────────────────────────────────────
  
      def subscribe(self, discussion_id: str) -> asyncio.Queue:
          q: asyncio.Queue = asyncio.Queue()
          self._sse_queues.setdefault(discussion_id, []).append(q)
          return q
  
      def unsubscribe(self, discussion_id: str, q: asyncio.Queue):
          qs = self._sse_queues.get(discussion_id, [])
          if q in qs:
              qs.remove(q)
  
      async def _broadcast(self, discussion_id: str, event: Dict[str, Any]):
          """向所有 SSE 订阅者推送事件."""
          for q in self._sse_queues.get(discussion_id, []):
              try:
                  q.put_nowait(event)
              except asyncio.QueueFull:
                  pass
  
      # ── 核心讨论编排 ──────────────────────────────────────
  
      async def run_discussion(
          self, plaza_id: str, discussion_id: str,
      ) -> Optional[Discussion]:
          """运行一场完整的广场讨论.
  
          编排流程 (向心结构):
          1. Moderator 开场: 阐述话题，提出第一轮子问题
          2. 每轮:
             a. 各参与者按座席层级依次发言 (内→中→外)
             b. Moderator 总结本轮观点
          3. 最终轮: Moderator 生成全局总结 + 关键结论
          """
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return None
          disc = plaza.discussions.get(discussion_id)
          if not disc:
              return None
          if disc.status not in (DiscussionStatus.OPEN,):
              return disc
  
          disc.status = DiscussionStatus.IN_PROGRESS
          disc.started_at = datetime.now(timezone.utc).isoformat()
  
          # Give event loop a chance to process SSE client connections
          await asyncio.sleep(0.1)
  
          await self._broadcast(disc.id, {
              "type": "discussion_start",
              "discussion_id": disc.id,
              "topic": disc.topic,
          })
  
          participants = list(plaza.participants.values())
          moderator = None
          speakers = []
  
          moderator = self._resolve_moderator(plaza, disc, participants)
          speakers = self._sort_speakers(participants, moderator)
  
          if not self._chat_fn:
              # 无 LLM 时使用模拟回复
              await self._run_simulated(disc, moderator, speakers)
              return disc
  
          # ── 开场: Moderator 引导话题 ──
          opening_prompt = (
              f"你是本场讨论的议事长（主持人）。\n"
              f"讨论话题: 「{disc.topic}」\n"
              f"{f'话题描述: {disc.description}' if disc.description else ''}\n"
              f"{f'讨论目标: {disc.goal}' if disc.goal else ''}\n"
              f"参与者: {', '.join(p.agent_name or p.agent_id for p in speakers)}\n\n"
              f"请开场:\n"
              f"- 用 2-4 句话点明讨论的核心问题\n"
              f"- 直接围绕用户提出的话题展开，不要自行转换或重新解读话题\n"
              f"- 然后向参与者提出第一个需要讨论的具体问题\n"
              f"- 说人话，像一个项目经理在主持会议"
          )
          opening = await self._speak_with_lock(
              disc, moderator, opening_prompt, round_number=0,
              niche_role="moderator",
          )
  
          # ── 多轮讨论 (辩论式交锋) ──
          for round_num in range(1, disc.max_rounds + 1):
              disc.current_round = round_num
              await self._broadcast(disc.id, {
                  "type": "round_start", "round": round_num,
                  "max_rounds": disc.max_rounds,
              })
  
              round_speakers = self._select_round_speakers(speakers, round_num)
              # 每轮多次短交锋，模拟辩论赛节奏
              exchanges = _EXCHANGES_PER_ROUND if disc.max_rounds <= 2 else 2
              for ex_idx in range(exchanges):
                  # 轮转选人: 每次交锋选不同子集
                  ex_speakers = self._pick_exchange_speakers(
                      round_speakers, ex_idx, _SPEAKERS_PER_EXCHANGE,
                  )
                  for speaker in ex_speakers:
                      # 获取最近 5 条作为即时上下文 (短窗口促进针锋相对)
                      recent = self._format_recent(disc, limit=5)
                      context_block = f"背景描述: {disc.description}\n" if disc.description else ""
                      goal_block = f"讨论目标: {disc.goal}\n" if disc.goal else ""
                      speak_prompt = (
                          f"你正在参与关于「{disc.topic}」的团队讨论。\n"
                          f"{context_block}{goal_block}"
                          f"你是 {speaker.agent_name}（{speaker.role}）。"
                          f"第 {round_num} 轮，第 {ex_idx+1} 次发言。\n\n"
                          f"刚才的讨论:\n{recent}\n\n"
                          f"发言要求:\n"
                          f"- 结合你的专业背景，给出有实质内容的观点或建议\n"
                          f"- 回应上面讨论中你认为重要的点，然后补充你的看法\n"
                          f"- 可以提出具体的方案、步骤、注意事项\n"
                          f"- 说 3-5 句话，100-200 字左右，不要太短也不要写论文\n"
                          f"- 像在开会发言一样自然表达，不要用列表和标题"
                      )
                      await self._speak_with_lock(
                          disc, speaker, speak_prompt, round_number=round_num,
                          niche_role=speaker.niche_role.value,
                      )
  
              # Moderator 收束本轮 (非最后一轮时)
              if round_num < disc.max_rounds:
                  summary_prompt = (
                      f"你是主持人。第 {round_num} 轮讨论已结束。\n\n"
                      f"本轮讨论:\n{self._format_round_messages(disc, round_num)}\n\n"
                      f"请小结本轮要点:\n"
                      f"- 总结大家达成的共识和仍有分歧的地方\n"
                      f"- 提出下一轮需要重点讨论的问题\n"
                      f"- 用 2-3 句话，自然表达"
                  )
                  await self._speak_with_lock(
                      disc, moderator, summary_prompt, round_number=round_num,
                      niche_role="moderator",
                  )
  
          # ── 最终总结 ──
          disc.status = DiscussionStatus.SUMMARIZING
          await self._broadcast(disc.id, {"type": "summarizing"})
  
          final_prompt = (
              f"你是议事长。关于「{disc.topic}」的讨论已经完成 {disc.max_rounds} 轮。\n"
              f"{f'背景描述: {disc.description}' if disc.description else ''}\n"
              f"{f'讨论目标: {disc.goal}' if disc.goal else ''}\n\n"
              f"完整讨论记录:\n{self._format_history(disc)}\n\n"
              f"请生成可直接派发任务的技术型概要。核心原则——有取舍、有权重:\n"
              f"- build/构建/开发/架构/部署相关发言 = 权重最高(P0级)，这些人要真正动手执行\n"
              f"- 测试/QA/安全相关 = 中等权重(P1级)，是质量门禁\n"
              f"- 能耗/外围优化/观察类 = 低权重(P2级)，仅作为补充参考，绝不挤占主篇幅\n"
              f"- 如果能耗建议不影响主目标上线，就放到最后1行带过\n\n"
              f"输出结构 (严格按此格式，不要自由发挥):\n"
              f"## 技术概要\n"
              f"4-6 句写清: 主目标、核心方案、关键约束、最大风险、首要动作\n"
              f"必须是接到这份概要的人能直接开工的技术描述\n\n"
              f"## 加权结论 (P0→P1→P2)\n"
              f"- [P0] 结论 | 主要支持角色 | 为什么重要\n"
              f"- [P1] ...\n"
              f"- [P2] 仅保留 1 条最相关的低权重建议\n\n"
              f"## 执行计划\n"
              f"| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
              f"|---|---|---|---|---|---|\n"
              f"列出 3-5 个任务，按优先级排序\n\n"
              f"## 补充观察\n"
              f"1 句话带过能耗/外围建议即可\n\n"
             
  ```
  
  ### 文件: `src/backend/agents/plaza_routes.py`
  ```py
  # -*- coding: utf-8 -*-
  """智能体广场 API 路由 + SSE 实时推送."""
  
  from __future__ import annotations
  
  import asyncio
  import json
  import logging
  from datetime import datetime, timezone
  from typing import Any, Dict, List, Optional
  
  from fastapi import APIRouter, HTTPException, Query, status
  from fastapi.responses import StreamingResponse
  from pydantic import BaseModel, Field
  
  from channels.system_evolution import EvolutionStatus
  
  from .plaza import PRESET_TOPICS, SeatTier, NicheRole, DiscussionStatus
  from .plaza_engine import get_plaza_engine
  
  logger = logging.getLogger(__name__)
  router = APIRouter(prefix="/plaza", tags=["Plaza"])
  
  try:
      from config import DEFAULT_PAGE_SIZE as _DEFAULT_PAGE_SIZE
      from config import MAX_PAGE_SIZE as _MAX_PAGE_SIZE
  except Exception:
      _DEFAULT_PAGE_SIZE = 50
      _MAX_PAGE_SIZE = 200
  
  
  # ── Request Models ────────────────────────────────────────
  
  class SelectedAgent(BaseModel):
      agent_id: str
      agent_name: str = ""
      role: str = ""
      team_id: str = ""
  
  
  class CreatePlazaRequest(BaseModel):
      name: str = Field(..., min_length=1, max_length=100)
      description: str = Field(default="", max_length=500)
      selected_agents: List[SelectedAgent] = Field(default_factory=list)
      chairperson_agent_id: str = Field(default="")
  
  
  class AddParticipantRequest(BaseModel):
      agent_id: str
      agent_name: str = ""
      role: str = ""
      team_id: str = ""
      seat_tier: str = Field(default="middle")
      niche_role: str = Field(default="observer")
  
  
  class CreateDiscussionRequest(BaseModel):
      topic: str = Field(..., min_length=1, max_length=200)
      description: str = Field(default="", max_length=2000)
      goal: str = Field(default="", max_length=500)
      moderator_agent_id: str = ""
      max_rounds: int = Field(default=3, ge=1, le=10)
  
  
  class SetVisualModeRequest(BaseModel):
      mode: str = Field(default="modern")  # modern | rome_320ad | senedd
  
  
  class DiscussionOutputRequest(BaseModel):
      output_type: str = Field(..., min_length=1, max_length=50)
      target_ids: List[str] = Field(default_factory=list)
      team_id: str = Field(default="")
      status_value: str = Field(default="created")
  
  
  _ALLOWED_DISCUSSION_OUTPUT_TYPES = {
      "task",
      "task_execution",
      "evolution_item",
      "skill_candidate",
      "cost_governance",
  }
  
  
  def _paginate_optional(items: List[Dict[str, Any]], *, limit: int, offset: int) -> Any:
      """Keep old array responses by default, but support stable optional pagination."""
      limit = getattr(limit, "default", limit)
      offset = getattr(offset, "default", offset)
      limit = int(limit or 0)
      offset = max(int(offset or 0), 0)
      if limit <= 0 and offset <= 0:
          return items
      if limit <= 0:
          limit = _DEFAULT_PAGE_SIZE
      limit = min(limit, _MAX_PAGE_SIZE)
      total = len(items)
      return {
          "items": items[offset:offset + limit],
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  def _participant_team_ids(plaza) -> List[str]:
      """Return discussion participant team IDs in stable first-seen order."""
      team_ids: List[str] = []
      for participant in getattr(plaza, "participants", {}).values():
          team_id = getattr(participant, "team_id", "") or ""
          if team_id and team_id not in team_ids:
              team_ids.append(team_id)
      return team_ids
  
  
  def _discussion_summary_text(disc) -> str:
      """Pick the best short conclusion text for downstream output tracing."""
      if getattr(disc, "summary", ""):
          return str(disc.summary)[:1000]
      conclusions = getattr(disc, "key_conclusions", []) or []
      if conclusions:
          return "\n".join(str(item) for item in conclusions[:5])[:1000]
      plan = getattr(disc, "plan", {}) or {}
      if plan.get("content"):
          return str(plan["content"])[:1000]
      return str(getattr(disc, "description", "") or getattr(disc, "topic", ""))[:1000]
  
  
  def _record_discussion_output(
      plaza,
      disc,
      *,
      output_type: str,
      target_ids: List[str],
      team_id: str = "",
      status_value: str = "created",
  ) -> Dict[str, Any]:
      """Record a structured downstream object created from a Plaza discussion."""
      clean_targets = [target_id for target_id in target_ids if target_id]
      output = {
          "id": f"{disc.id}:{output_type}:{':'.join(clean_targets) or team_id or 'none'}",
          "type": output_type,
          "status": status_value,
          "target_ids": clean_targets,
          "team_id": team_id or getattr(disc, "assigned_team_id", ""),
          "source": {
              "type": "plaza_discussion",
              "plaza_id": getattr(plaza, "id", ""),
              "discussion_id": disc.id,
              "topic": disc.topic,
              "summary": _discussion_summary_text(disc),
              "participant_team_ids": _participant_team_ids(plaza),
          },
          "created_at": datetime.now(timezone.utc).isoformat(),
      }
  
      if not disc.plan:
          disc.plan = {"content": _discussion_summary_text(disc)}
      outputs = list(disc.plan.get("outputs") or [])
      outputs = [item for item in outputs if item.get("id") != output["id"]]
      outputs.append(output)
      disc.plan["outputs"] = outputs[-20:]
      return output
  
  
  def _get_plan_source(disc) -> str:
      """Return the current discussion plan text, falling back to the summary."""
      if disc.plan and disc.plan.get("content"):
          return str(disc.plan["content"])
      if disc.summary:
          return disc.summary
      return ""
  
  
  def _get_plan_revision(disc) -> int:
      """Return the discussion plan revision, defaulting to the first version."""
      if not disc.plan:
          return 1
      try:
          return int(disc.plan.get("revision", 1) or 1)
      except (TypeError, ValueError):
          return 1
  
  
  def _build_plaza_task_metadata(
      *,
      plaza_id: str,
      discussion_id: str,
      discussion_topic: str,
      team_id: str,
      plan_revision: int,
      plan_item_index: int,
      responsible_role: str = "",
      acceptance_test: str = "",
      expected_artifacts: Optional[List[str]] = None,
  ) -> Dict[str, Any]:
      """Normalize plaza-origin task metadata for tracing and later evolution."""
      inferred_skills = _infer_skills_from_role(responsible_role)
      trace_context = {
          "source": "plaza",
          "plaza_id": plaza_id,
          "discussion_id": discussion_id,
          "discussion_topic": discussion_topic,
          "team_id": team_id,
          "plan_revision": plan_revision,
          "plan_item_index": plan_item_index,
          "responsible_role": responsible_role,
      }
      return {
          "source": "plaza",
          "plaza_id": plaza_id,
          "discussion_id": discussion_id,
          "discussion_topic": discussion_topic,
          "team_id": team_id,
          "plan_revision": plan_revision,
          "plan_item_index": plan_item_index,
          "responsible_role": responsible_role,
          "acceptance_test": acceptance_test,
          "expected_artifacts": list(expected_artifacts or []),
          "skills_used": inferred_skills,
          "trace_context": trace_context,
      }
  
  
  def _infer_skills_from_role(responsible_role: str) -> List[str]:
      """Infer likely skill evidence from the role assigned in the discussion plan."""
      role = (responsible_role or "").strip().lower()
      if not role:
          return []
  
      role_skill_hints = (
          (("developer", "engineer", "开发", "实现"), ["code_implementation", "debugging"]),
          (("qa", "tester", "test", "测试"), ["testing", "test_execution", "regression_testing"]),
          (("architect", "架构"), ["architecture_design", "interface_definition"]),
          (("research", "analyst", "研究", "分析"), ["web_research", "requirements_analysis"]),
          (("pm", "manager", "协调", "项目"), ["task_decomposition", "progress_tracking"]),
          (("deploy", "ops", "devops", "运维"), ["build_automation", "deployment_orchestration"]),
      )
  
      for keywords, skills in role_skill_hints:
          if any(keyword in role for keyword in keywords):
              return list(skills)
      return []
  
  
  async def _dispatch_discussion_tasks(
      plaza_id: str,
      disc,
      team_id: str,
      *,
      auto_start: bool,
  ) -> List[Dict[str, Any]]:
      """Materialize discussion plan items into concrete tasks."""
      plan_source = _get_plan_source(disc)
      if not plan_source:
          raise HTTPException(status.HTTP_400_BAD_REQUEST, "尚无执行计划，请先完成讨论或生成计划")
  
      tasks_data = _parse_plan_table(plan_source)
      if not tasks_data or (len(tasks_data) == 1 and tasks_data[0].get("title") == "演化需求"):
          from .chat_harness import get_chat_harness
  
          harness = get_chat_harness()
          parse_prompt = (
              "你是任务拆解助
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  ## 要求
  1. 分析任务需求，拆解为可执行的子步骤
  2. 识别技术风险和依赖关系
  3. 为后续研究人员、架构师、开发者提供清晰的指导
  4. 输出一份结构化的任务分解文档 (Markdown 格式)
  
  ## ⚠️ 重要提示
  系统已自动预加载项目文件结构和相关源文件（见下方 📂 项目上下文）。
  请基于**实际存在的文件**进行分析，不要猜测文件名。
  
  项目根目录: /Users/panglaohu/Downloads/DoubleBoatClawSystem
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
  
  项目根目录: /Users/panglaohu/Downloads/AgentsGroup2026
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
────────────────────────────────────────────────────────────
⚡ 使用 DeepSeek V4 直连 (64K 输出, 流式)...

🔗 API: api.deepseek.com | 模型: deepseek-chat
────────────────────────────────────────────────────────────

⚠️ API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****AGED is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}

🔄 连接重试 (1/2)...

⚠️ API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****AGED is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}

🔄 连接重试 (2/2)...

⚠️ API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****AGED is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}

❌ 所有重试已耗尽: API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****AGED is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}
