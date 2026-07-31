# 架构设计 — architect

任务: 建立 ES 当前容量、索引、分片和 SLO 基线
步骤: architecture
Agent: build_architect

---

📋 任务: 620f6ecd-a38
🤖 Agent: Architect (architect)
📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
🔧 执行方式: 配置模型 (codebuddy / glm-5.1)
⏱️ 超时: 1200s
────────────────────────────────────────────────────────────
📝 提示词:
  你是 AgentsGroup2026 系统的 Architect (architect)。
  请执行以下开发任务:
  
  你是系统架构师。请为以下任务设计技术方案:
  
  ## 任务
  建立 ES 当前容量、索引、分片和 SLO 基线
  负责角色: 上云架构师
  依赖: 无
  预期产出: 容量评估表、扩容选型建议、风险清单
  负责角色: 上云架构师
  执行智能体: build_archit
  依赖: 无
  预期产出: 容量评估表、扩容选型建议、风险清单
  
  ## 📂 项目上下文 (系统自动预加载)
  
  ### 项目文件结构 (src/ 目录)
  ```
  src/frontend/Agent-digital-twin.html
  src/frontend/agent-team-config-new.html
  src/frontend/agent-team-config.html
  src/frontend/cost-dashboard.html
  src/frontend/datacenter-ratchet-evolution.html
  src/frontend/digital-twin-cli.html
  src/frontend/extraction-pipeline.html
  src/frontend/index.html
  src/frontend/login.html
  src/frontend/pet-config.html
  src/frontend/plaza.html
  src/frontend/sandbox-twin.html
  src/frontend/skill-extract.html
  src/frontend/system-evolution.html
  src/frontend/tasks.html
  src/frontend/css/agent-team-config.css
  src/frontend/css/base.css
  src/frontend/css/components.css
  src/frontend/css/cost-dashboard.css
  src/frontend/css/openbridge-theme.css
  src/frontend/css/sandbox-twin.css
  src/frontend/css/skill-extract-timeline.css
  src/frontend/css/skill-extract.css
  src/frontend/css/tasks-ws.css
  src/frontend/css/theme.css
  src/frontend/css/topbar-ws.css
  src/frontend/css/variables.css
  src/frontend/css/ws-theme-bridge.css
  src/frontend/js/ag-context.js
  src/frontend/js/agent-detail.js
  src/frontend/js/agent-team-config.js
  src/frontend/js/api.js
  src/frontend/js/cost-dashboard.js
  src/frontend/js/digital-twin-cli-3d.js
  src/frontend/js/digital-twin-cli.js
  src/frontend/js/evidence-runs.js
  src/frontend/js/extract-routing.js
  src/frontend/js/global-nav.js
  src/frontend/js/i18n.js
  src/frontend/js/nav-sidebar.js
  src/frontend/js/nav.js
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
  src/frontend/js/office/eco-replay.js
  src/frontend/js/office/office-boot.js
  src/frontend/js/office/office-scene.js
  src/frontend/js/office/office-state.js
  src/frontend/js/office/pet-behavior.js
  src/frontend/js/office/pet-ecosystem.js
  src/frontend/js/office/pet-factory.js
  src/frontend/js/office/voice-config-validator.js
  src/frontend/js/office/__checks__/pet-behavior.check.mjs
  src/frontend/js/office/__checks__/voice-config-validator.check.mjs
  src/frontend/js/digital-twin/director.js
  src/frontend/js/digital-twin/eco-console.js
  src/frontend/js/digital-twin/eco-curves.js
  src/frontend/js/digital-twin/eco-genetics.js
  src/frontend/js/digital-twin/eco-matchup.js
  src/frontend/js/digital-twin/secs-core.js
  src/frontend/js/digital-twin/v4-evolution.js
  src/frontend/js/digital-twin/v4-scenario-evolution.js
  src/frontend/js/digital-twin/v4-scenarios.js
  src/frontend/node_modules/.vite/vitest/da39a3ee5e6b4b0d3255bfef95601890afd80709/results.json
  src/frontend/__tests__/ag-context.test.js
  src/frontend/__tests__/agent-config.test.js
  src/frontend/__tests__/agent-detail-digital-employee.test.js
  src/frontend/__tests__/agent-detail-pagination.test.js
  src/frontend/__tests__/agent-team-config-delete.test.js
  src/frontend/__tests__/agent-team-config-pagination.test.js
  src/frontend/__tests__/agent-team-config-state.test.js
  src/frontend/__tests__/api.test.js
  src/frontend/__tests__/close-form.test.js
  src/frontend/__tests__/cost-dashboard.test.js
  src/frontend/__tests__/csrf-pages.test.js
  src/frontend/__tests__/digital-twin-cli-pagination.test.js
  src/frontend/__tests__/digital-twin-move-state-machine.test.js
  src/frontend/__tests__/digital-twin-move-vm.test.js
  src/frontend/__tests__/digital-twin-ratchet.test.js
  src/frontend/__tests__/digital-twin-state.test.js
  src/frontend/__tests__/eco-genetics-v4.test.js
  src/frontend/__tests__/evidence-runs.test.js
  src/frontend/__tests__/extract-routing.test.js
  src/frontend/__tests__/frontend-big-change-smoke.test.js
  src/frontend/__tests__/global-nav.test.js
  src/frontend/__tests__/login-page-flow.test.js
  src/frontend/__tests__/office-state.test.js
  src/frontend/__tests__/plaza-action-paths.test.js
  src/frontend/__tests__/plaza-modal-input.test.js
  src/frontend/__tests__/plaza-pagination.test.js
  src/frontend/__tests__/plaza-runtime-helpers.test.js
  src/frontend/__tests__/plaza-vitest-new.test.js
  src/frontend/__tests__/scenario-cards.test.js
  src/frontend/__tests__/skill-extract-action-paths.test.js
  src/frontend/__tests__/skill-extract-modal-flow.test.js
  src/frontend/__tests__/skill-extract-smoke.test.js
  src/frontend/__tests__/skill-extract-verification.test.js
  src/frontend/__tests__/skill-publish-gate.test.js
  src/frontend/__tests__/system-evolution.test.js
  src/frontend/__tests__/tasks-pagination.test.js
  src/frontend/__tests__/team-unified.test.js
  src/frontend/__tests__/toast-robustness.test.js
  src/frontend/__tests__/tools-skills.test.js
  src/frontend/__tests__/utils-surface.test.js
  src/frontend/__tests__/utils.test.js
  src/frontend/__tests__/wizard-pagination.test.js
  src/backend/__init__.py
  src/backend/agent_team_api.py
  src/backend/ci_cost_gate.py
  src/backend/config.py
  src/backend/datacenter_api.py
  src/backend/main.py
  src/backend/mypy.ini
  src/backend/server.log
  src/backend/startup_check.py
  src/backend/startup_validator.py
  src/backend/token_factory.py
  src/backend/tests/__init__.py
  src/backend/tests/conftest.py
  src/backend/tests/test_ab_testing.py
  src/backend/tests/test_agent_skill_binding.py
  src/backend/tests/test_agent_toolbox.py
  src/backend/tests/test_agent_triggers.py
  src/backend/tests/test_api_handler_integration.py
  src/backend/tests/test_api_integration_extended.py
  src/backend/tests/test_api_pagination.py
  src/backend/tests/test_api_rate_limit.py
  src/backend/tests/test_api_session_message.py
  src/backend/tests/test_auth_csrf.py
  src/backend/tests/test_aws_ops_costdown.py
  src/backend/tests/test_budget_models.py
  src/backend/tests/test_channel_event_bridge.py
  src/backend/tests/test_chaos_stability.py
  src/backend/tests/test_cli_deprecation.py
  src/backend/tests/test_core_api_smoke.py
  src/backend/tests/test_cost_aggregator.py
  src/backend/tests/test_cost_gate.py
  src/backend/tests/test_cost_gate_routes.py
  src/backend/tests/test_cost_monitor.py
  src/backend/tests/test_cost_report.py
  src/backend/tests/test_cost_target_tracker.py
  ... (共 2069 个 src/ 文件)
  
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
  
  
  @pytest.fixture(autouse=True)
  def _reset_shared_singletons():
      """根治测试数据污染 (bug-041): 每个用例前后重置共享 ABTestManager 单例的 EWMA 状态，
      避免前序用例改动共享阈值/决策历史污染后序用例。conftest 层统一，覆盖后端全部测试。"""
      def _reset():
          try:
              from agents.ab_testing import reset_ab_test_manager
              reset_ab_test_manager()
          except Exception:
              pass
      _reset()
      yield
      _reset()
  
  
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
  
  ### 文件: `src/backend/tests/test_execution_plan.py`
  ```py
  # -*- coding: utf-8 -*-
  """P5-1/P6-2/P5-2: 结构化执行计划契约 + 落地性审查 + 派发闭环 测试."""
  
  from __future__ import annotations
  
  from pathlib import Path
  from tempfile import TemporaryDirectory
  
  import pytest
  
  from agents import plaza_engine as plaza_engine_module
  from agents import plaza_routes
  from agents.execution_plan import (
      ExecutionPlan,
      PlanStep,
      build_plan_from_text,
      load_plan_from_discussion,
      save_plan_to_discussion,
      validate_plan,
  )
  from agents.plaza_engine import PlazaEngine
  from agents.plaza_store import PlazaStore
  
  
  GOOD_PLAN = (
      "## 执行计划\n"
      "| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
      "|---|---|---|---|---|---|\n"
      "| 1 | 调研现状并整理约束 | researcher | P0 | 无 | 调研报告 |\n"
      "| 2 | 设计并实现方案 | developer | P1 | 1 | 可运行补丁 |\n"
      "| 3 | 回归验证 | qa | P1 | 2 | pytest 报告 |\n"
  )
  
  BAD_PLAN = (
      "## 执行计划\n"
      "| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
      "|---|---|---|---|---|---|\n"
      "| 1 | 做点什么 |  | P0 | 9 |  |\n"
  )
  
  
  @pytest.fixture
  def isolated_plaza_engine(monkeypatch):
      with TemporaryDirectory() as tmpdir:
          engine = PlazaEngine()
          engine._store = PlazaStore(base_dir=Path(tmpdir))
          engine._plazas = {}
          monkeypatch.setattr(plaza_engine_module, "_engine", engine)
          yield engine
  
  
  def _seed(engine, plan_text=GOOD_PLAN):
      plaza = engine.create_plaza("契约广场", "plan")
      disc = engine.create_discussion(plaza.id, "把计划变成任务", "plan", "", 3)
      disc.plan = {"revision": 2, "content": plan_text}
      engine._store.save_plaza(plaza)
      return plaza, disc
  
  
  class TestPlanContract:
      def test_build_from_text_produces_structured_steps(self):
          plan = build_plan_from_text(GOOD_PLAN, topic="t", goal="g")
          assert len(plan.steps) == 3
          s2 = plan.steps[1]
          assert s2.title == "设计并实现方案"
          assert s2.responsible_role == "developer"
          assert s2.acceptance == "可运行补丁"
          assert s2.dependencies == ["1"]
          assert plan.status == "draft"
  
      def test_validate_good_plan_passes(self):
          assert validate_plan(build_plan_from_text(GOOD_PLAN)) == []
  
      def test_validate_flags_missing_fields_and_bad_deps(self):
          issues = validate_plan(build_plan_from_text(BAD_PLAN))
          fields = {i["field"] for i in issues}
          assert "responsible_role" in fields
          assert "acceptance" in fields
          assert "dependencies" in fields  # 依赖 9 无法解析
  
      def test_validate_empty_plan(self):
          issues = validate_plan(ExecutionPlan())
          assert issues and issues[0]["field"] == "steps"
  
      def test_roundtrip_serialization(self):
          plan = build_plan_from_text(GOOD_PLAN, plaza_id="p", discussion_id="d")
          clone = ExecutionPlan.from_dict(plan.to_dict())
          assert clone.to_dict() == plan.to_dict()
  
      def test_refresh_status_completes_when_all_steps_done(self):
          plan = build_plan_from_text(GOOD_PLAN)
          plan.status = "dispatched"
          for s in plan.steps:
              s.status = "completed"
          plan.refresh_status()
          assert plan.status == "completed"
  
  
  class TestPlanEndpoints:
      @pytest.mark.asyncio
      async def test_get_builds_and_persists_structured_plan(self, isolated_plaza_engine):
          plaza, disc = _seed(isolated_plaza_engine)
          resp = await plaza_routes.get_execution_plan(plaza.id, disc.id)
          assert resp["issues"] == []
          assert len(resp["plan"]["steps"]) == 3
          assert resp["dispatchable"] is False  # 未批准
          assert load_plan_from_discussion(disc) is not None
  
      @pytest.mark.asyncio
      async def test_approve_rejects_infeasible_plan(self, isolated_plaza_engine):
          plaza, disc = _seed(isolated_plaza_engine, BAD_PLAN)
          await plaza_routes.get_execution_plan(plaza.id, disc.id)
          from fastapi import HTTPException
          with pytest.raises(HTTPException) as exc:
              await plaza_routes.approve_execution_plan(
                  plaza.id, disc.id, plaza_routes.ApprovePlanRequest(),
              )
          assert exc.value.status_code == 422
          assert exc.value.detail["issues"]
  
      @pytest.mark.asyncio
      async def test_dispatch_requires_approval_then_binds_tasks(
          self, isolated_plaza_engine, monkeypatch,
      ):
          plaza, disc = _seed(isolated_plaza_engine)
          await plaza_routes.get_execution_plan(plaza.id, disc.id)
  
          created = []
  
          async def fake_submit_internal_task(team_id, **kwargs):
              from agents.task_engine import AgentTask
              task = AgentTask(team_id=team_id, title=kwargs.get("title", ""))
              created.append(task)
              return task
  
          from agents import api as api_module
          monkeypatch.setattr(api_module, "_submit_internal_task", fake_submit_internal_task)
  
          # 未批准 → 派发被落地性关卡拦下
          from fastapi import HTTPException
          with pytest.raises(HTTPException) as exc:
              await plaza_routes._dispatch_discussion_tasks(
                  plaza.id, disc, "team-x", auto_start=False,
              )
          assert "尚未批准" in str(exc.value.detail)
  
          # 批准 → 派发成功，步骤↔任务绑定，计划进入 dispatched
          await plaza_routes.approve_execution_plan(
              plaza.id, disc.id, plaza_routes.ApprovePlanRequest(approved_by="owner"),
          )
          tasks = await plaza_routes._dispatch_discussion_tasks(
              plaza.id, disc, "team-x", auto_start=False,
          )
          assert len(tasks) == 3
          plan = load_plan_from_discussion(disc)
          assert plan.status == "dispatched"
          assert all(s.status == "dispatched" and s.task_id for s in plan.steps)
  
      @pytest.mark.asyncio
      async def test_step_status_feedback_completes_plan(self, isolated_plaza_engine):
          plaza, disc = _seed(isolated_plaza_engine)
          resp = await plaza_routes.get_execution_plan(plaza.id, disc.id)
          plan = load_plan_from_discussion(disc)
          plan.status = "dispatched"
          for s in plan.steps:
              s.status = "dispatched"
          save_plan_to_discussion(disc, plan)
  
          step_ids = [s["step_id"] for s in resp["plan"]["steps"]]
          for sid in step_ids[:-1]:
              out = await plaza_routes.update_plan_step_status(
                  plaza.id, disc.id, sid,
                  plaza_routes.PlanStepStatusRequest(status="completed"),
              )
              assert out["plan_status"] == "dispatched"
          out = await plaza_routes.update_plan_step_status(
              plaza.id, disc.id, step_ids[-1],
              plaza_routes.PlanStepStatusRequest(status="completed", task_id="t-9"),
          )
          assert out["plan_status"] == "completed"
  
      @pytest.mark.asyncio
      async def test_step_status_rejects_illegal_value(self, isolated_plaza_engine):
          plaza, disc = _seed(isolated_plaza_engine)
          resp = await plaza_routes.get_execution_plan(plaza.id, disc.id)
          sid = resp["plan"]["steps"][0]["step_id"]
          from fastapi import HTTPException
          with pytest.raises(HTTPException) as exc:
              await plaza_routes.update_plan_step_status(
                  plaza.id, disc.id, sid,
                  plaza_routes.PlanStepStatusRequest(status="doing"),
              )
          assert exc.value.status_code == 400
  
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
  from agents import plaza_stream
  from agents import task_engine as task_engine_module
  from agents.plaza import DiscussionStatus, PlazaMessage
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
      async def test_list_discussions_supports_optional_pagination(self, isolated_plaza_engine):
          plaza, _ = _seed_discussion(isolated_plaza_engine)
          isolated_plaza_engine.create_discussion(plaza.id, "第二个议题", "dispatch", "", 3)
  
          payload = await plaza_routes.list_discussions(plaza.id, limit=1, offset=1)
  
          assert payload["total"] == 2
          assert payload["limit"] == 1
          assert payload["offset"] == 1
          assert len(payload["items"]) == 1
  
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
  
          paged = await plaza_routes.get_discussion_tasks(plaza.id, disc.id, limit=1, offset=1)
          assert paged["task_count"] == 2
          assert paged["limit"] == 1
          assert paged["offset"] == 1
          assert paged["has_more"] is False
          assert [task["task_id"] for task in paged["tasks"]] == ["task-2"]
  
  
  class TestDiscussionLifecycle:
      @pytest.mark.asyncio
      async def test_create_discussion_persists_goal_and_metadata(self, isolated_plaza_engine):
          plaza = isolated_plaza_engine.create_plaza("生命周期广场", "lifecycle")
  
          payload = await plaza_routes.create_discussion(
              plaza.id,
              plaza_routes.CreateDiscussionRequest(
                  topic="验证 Plaza 生命周期",
                  description="从创建到启动的主路径",
                  goal="确保讨论能被稳定创建",
                  moderator_agent_id="pm-1",
                  max_rounds=4,
              ),
          )
  
          stored = isolated_plaza_engine.get_discussion(plaza.id, payload["id"])
          assert payload["topic"] == "验证 Plaza 生命周期"
          assert payload["status"] == DiscussionStatus.OPEN.value
          assert stored is not None
          assert stored.goal == "确保讨论能被稳定创建"
          assert stored.moderator_agent_id == "pm-1"
          assert stored.max_rounds == 4
  
      @pytest.mark.asyncio
      async def test_start_discussion_resets_closed_discussion_before_scheduling(
          self,
          isolated_plaza_engine,
          monkeypatch,
      ):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          disc.status = DiscussionStatus.CLOSED
          disc.current_round = 2
          disc.messages.append(
              PlazaMessage(
                  discussion_id=disc.id,
                  agent_id="agent-1",
                  agent_name="Agent 1",
                  content="旧消息",
                  round_number=2,
              )
          )
          disc.summary = "旧总结"
          disc.plan["task_ids"] = ["task-old"]
          disc.assigned_team_id = "team-old"
          isolated_plaza_engine._store.save_plaza(plaza)
  
          scheduled = []
  
          def fake_create_task(coro):
              scheduled.append(coro)
              coro.close()
              return object()
  
          monkeypatch.setattr(plaza_routes.asyncio, "create_task", fake_create_task)
  
          result = await plaza_routes.start_discussion(plaza.id, disc.id)
  
          refreshed = isolated_plaza_engine.get_discussion(plaza.id, disc.id)
          assert result["status"] == "started"
          assert scheduled, "discussion run coroutine should be scheduled"
          assert refreshed is not None
          assert refreshed.status == DiscussionStatus.OPEN
          assert refreshed.current_round == 0
          assert refreshed.messages == []
          assert refreshed.summary == ""
          assert refreshed.plan == {}
          assert refreshed.assigned_team_id == ""
  
      @pytest.mark.asyncio
      async def test_start_discussion_rejects_non_open_non_closed_state(self, isolated_plaza_engine):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          disc.status = DiscussionStatus.IN_PROGRESS
          isolated_plaza_engine._store.save_plaza(plaza)
  
          with pytest.raises(plaza_routes.HTTPException) as exc_info:
              await plaza_routes.start_discussion(plaza.id, disc.id)
  
          assert exc_info.value.status_code == 400
          assert "无法启动" in str(exc_info.value.detail)
  
      def test_resolve_startable_discussion_resets_closed_state(self, isolated_plaza_engine):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          disc.status = DiscussionStatus.CLOSED
          disc.current_round = 2
          disc.messages.append(PlazaMessage(discussion_id=disc.id, agent_id="a-1", content="旧消息"))
          disc.summary = "旧总结"
          disc.assigned_team_id = "team-old"
          isolated_plaza_engine._store.save_plaza(plaza)
  
          refreshed = plaza_routes._resolve_startable_discussion(
              isolated_plaza_engine,
              plaza.id,
              disc.id,
          )
  
          assert refreshed.status == DiscussionStatus.OPEN
          assert refreshed.current_round == 0
          assert refreshed.messages == []
          assert refreshed.summary == ""
          assert refreshed.assigned_team_id == ""
  
      def test_schedule_discussion_run_uses_background_task(self, isolated_plaza_engine, monkeypatch):
          plaza, disc = _seed_discussion(isolated_plaza_engine)
          scheduled = []
  
          def fake_create_task(coro):
              scheduled.append(coro)
              coro.close()
              return object()
  
          monkeypatch.setattr(plaza_routes.asyncio, "create_task", fake_create_task)
  
          plaza_routes._schedule_discussion_run(isolated_plaza_engine, plaza.id, disc.id)
  
          assert len(scheduled) == 1
  
      def test_format_sse_event_preserves_optional_id_and_unicode_payload(self):
          assert plaza_stream.format_sse_event({"type": "heartbeat"}) == (
              'data: {"type": "heartbeat"}\n\n'
          )
          assert plaza_stream.format_sse_event({"type": "message", "text": "议事"}, "7") == (
              'id: 7\ndata: {"type": "message", "text": "议事"}\n\n'
          )
  
      def test_parse_last_event_id_matches_existing_digit_only_behavior(self):
          assert plaza_stream.parse_last_event_id("") == -1
          assert plaza_stream.parse_last_event_id("abc") == -1
          assert plaza_stream.parse_last_event_id("-1") == -1
          assert plaza_stream.parse_last_event_id("12") == 12
  
      def test_iter_replay_message_events_skips_received_non_negative_seq(self, isolated_plaza_engine):
          _, disc = _seed_discussion(isolated_plaza_engine)
          disc.messages = []
          for seq, agent_id in [(-1, "pending"), (0, "old"), (1, "next")]:
              msg = PlazaMessage(discussion_id=disc.id, agent_id=agent_id, content=agent_id)
              msg.seq = seq
              disc.messages.append(msg)
  
          events = list(plaza_stream.iter_replay_message_events(disc, 0))
  
          assert len(events) == 2
          assert '"agent_id": "pending"' in events[0]
          assert '"agent_id": "next"' in events[1]
          assert '"agent_id": "old"' not in "".join(events)
  
      def test_build_stream_status_event_uses_next_message_sequence(self, isolated_plaza_engine):
          _, disc = _seed_discussion(isolated_plaza_engine)
          disc.messages = []
          assert plaza_stream.build_stream_status_event(disc) == (
              0,
              'id: 0\ndata: {"type": "status", "status": "open"}\n\n',
          )
  
          msg = PlazaMessage(discussion_id=disc.id, agent_id="a-1", content="消息")
          msg.seq = 4
          disc.messages.append(msg)
  
          assert plaza_stream.build_stream_status_event(disc) == (
              5,
              'id: 5\ndata: {"type": "status", "status": "open"}\n\n',
          )
  
      def test_iter_closed_discussion_events_emits_end_after_status(self, isolated_plaza_engine):
          _, disc = _seed_discussion(isolated_plaza_engine)
          disc.status = plaza_routes.DiscussionStatus.CLOSED
          disc.summary = "结论"
          disc.plan = {}
  
          assert list(plaza_stream.iter_closed_discussion_events(disc, 7)) == [
              'id: 8\ndata: {"type": "discussion_end", "summary": "结论"}\n\n',
          ]
  
      def test_iter_closed_discussion_events_emits_plan_before_end(self, isolated_plaza_engine):
          _, disc = _seed_discussion(isolated_plaza_engine)
          disc.status = plaza_routes.DiscussionStatus.CLOSED
          disc.summary = "结论"
          disc.plan = {"content": "执行计划"}
  
          assert list(plaza_stream.iter_closed_discussion_events(disc, 7)) == [
              'id: 8\ndata: {"type": "plan_updated", "plan": {"content": "执行计划"}}\n\n',
              'id: 9\ndata: {"type": "discussion_end", "summary": "结论"}\n\n',
          ]
  
      def test_format_live_stream_event_uses_non_negative_message_sequence(self, isolated_plaza_engine):
          _, disc = _seed_discussion(isolated_plaza_engine)
          msg = PlazaMessage(discussion_id=disc.id, agent_id="live", content="实时")
          msg.seq = 3
  
          event = plaza_stream.format_live_stream_event({"type": "mes
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
  
  
  def _build_success_workflow(artifact_dir: str) -> list:
      return [
          {
              "key": "develop",
              "status": "completed",
              "artifact": f"{artifact_dir}/04_develop/summary.md",
              "deliverable_paths": ["src/backend/main.py"],
              "_summary": {
                  "files_changed": ["src/backend/main.py"],
                  "verify_checklist": ["import check: `src/backend/main.py`"],
              },
          },
          {
              "key": "test",
              "status": "completed",
              "artifact": f"{artifact_dir}/05_test.md",
              "_summary": {
                  "verdict": "PASS",
                  "checklist": [],
              },
          },
          {
              "key": "deploy",
              "status": "completed",
              "artifact": f"{artifact_dir}/06_deploy/summary.md",
              "deploy_result": {
                  "developer": {"applied": [{"path": "src/backend/main.py"}], "skipped": [], "failed": []},
                  "deployer": {"applied": [], "skipped": [], "failed": []},
              },
          },
      ]
  
  
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
  
          assert list(result.keys()) == ["cycle", "audit", "dispatch", "verify", "closed", "summary"]
          assert result["cycle"] == 1
          assert result["dispatch"]["count"] == 1
          assert result["verify"]["count"] == 0
          assert result["closed"] == []
          assert result["summary"]["total_items"] >= 1
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
  
      @pytest.mark.asyncio
      async def test_plaza_end_to_end_discussion_to_verification_close(
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
              index = len(created_tasks) + 1
              pipeline_dir = Path(isolated_task_engine._store._dir) / f"pipeline-{index}"
              task = AgentTask(
                  task_id=f"plaza-task-{index}",
                  team_id=team_id,
                  title=kwargs["title"],
                  description=kwargs["description"],
                  priority=kwargs["priority"],
                  metadata={
                      **kwargs["metadata"],
                      "pipeline_dir": str(pipeline_dir),
                      "workflow": _build_success_workflow(str(pipeline_dir)),
     
  ```
  
  ### 文件: `src/backend/agents/execution_plan.py`
  ```py
  # -*- coding: utf-8 -*-
  """ExecutionPlan — Plaza 集体智慧的结构化产出契约 (Todos P5-1) + 落地性审查 (P6-2).
  
  两阶段经济学的分界物:
  - 讨论阶段产出本结构（不计成本，只求落地）；
  - 本结构经人批准(approve)后进入执行阶段（派发/孪生竞标/生产），成本纪律从此开始。
  
  每个步骤必须具备: 标题、负责角色、预期产出(验收依据)；依赖必须可解析。
  审查不过 → 不允许派发（除非显式 force）。
  """
  
  from __future__ import annotations
  
  import re
  import uuid
  from dataclasses import dataclass, field
  from datetime import datetime, timezone
  from typing import Any, Dict, List, Optional
  
  # ── 计划文本解析（自 plaza_routes 迁移，成为唯一实现） ──────────
  
  _PRIORITY_MAP = {"P0": 1, "P1": 1, "P2": 2, "P3": 3, "1": 1, "2": 2, "3": 3}
  
  _GARBAGE_TITLE_PATTERNS = [
      re.compile(r"^```"),
      re.compile(r"我的定位[:：]"),
      re.compile(r"你是议事长"),
      re.compile(r"^⚠️"),
      re.compile(r"^💡"),
      re.compile(r"我是 AgentsGroup"),
      re.compile(r"当前系统功能正常"),
      re.compile(r"^[#]{1,6}\s"),
      re.compile(r"[{}]"),
      re.compile(r"Authentication\s+Fails"),
      re.compile(r"api key"),
      re.compile(r"^{.*}$"),
  ]
  
  
  def is_valid_task_title(title: str) -> bool:
      """检查任务标题是否为有效的人类任务描述，排除代码块/系统提示/错误等."""
      if not title or len(title.strip()) < 3:
          return False
      if len(title) > 150:
          return False
      t = title.strip()
      for pattern in _GARBAGE_TITLE_PATTERNS:
          if pattern.search(t):
              return False
      return True
  
  
  # 角色 → 默认技能（计划表无技能列时的推断源，v4 XG-1）
  ROLE_DEFAULT_SKILLS: Dict[str, List[str]] = {
      "开发": ["coding", "code_review"],
      "developer": ["coding", "code_review"],
      "engineer": ["coding", "testing"],
      "工程师": ["coding", "testing"],
      "测试": ["testing", "qa"],
      "qa": ["testing", "qa"],
      "tester": ["testing", "qa"],
      "运维": ["deployment", "ops"],
      "ops": ["deployment", "ops"],
      "sre": ["deployment", "ops", "monitoring"],
      "架构": ["architecture", "analysis"],
      "architect": ["architecture", "analysis"],
      "产品": ["analysis", "planning"],
      "pm": ["analysis", "planning"],
      "分析": ["analysis", "research"],
      "researcher": ["analysis", "research"],
      "安全": ["security", "code_review"],
      "security": ["security", "code_review"],
  }
  
  # title/description 关键词 → 技能（最后兜底）
  _SKILL_HINTS: Dict[str, List[str]] = {
      "coding": ["代码", "开发", "实现", "编程", "code", "implement", "develop"],
      "code_review": ["审查", "评审", "review"],
      "testing": ["测试", "test", "qa", "单测"],
      "deployment": ["部署", "发布", "deploy", "上线"],
      "terraform": ["terraform", "基础设施", "iac"],
      "analysis": ["分析", "调研", "research", "评估"],
      "ops": ["运维", "ops", "监控", "monitor"],
      "security": ["安全", "security", "漏洞"],
      "planning": ["规划", "计划", "拆解", "plan"],
  }
  
  
  def _parse_skills_cell(raw: str) -> List[str]:
      """解析技能单元格：逗号/顿号/斜杠分隔."""
      if not raw or raw.strip() in ("-", "无", "none", "None", "—", "–"):
          return []
      parts = re.split(r"[,，、;/|]+", raw)
      return [p.strip() for p in parts if p.strip()]
  
  
  def _header_index(headers: List[str], *needles: str) -> Optional[int]:
      for i, h in enumerate(headers):
          hl = h.lower()
          for n in needles:
              if n.lower() in hl or n in h:
                  return i
      return None
  
  
  def infer_skills_for_step(
      *,
      title: str = "",
      description: str = "",
      responsible_role: str = "",
      explicit: Optional[List[str]] = None,
  ) -> tuple[List[str], bool]:
      """返回 (skills, inferred). explicit 非空则 inferred=False."""
      if explicit:
          return list(explicit), False
      role = (responsible_role or "").strip().lower()
      if role:
          for key, skills in ROLE_DEFAULT_SKILLS.items():
              kl = key.lower()
              if kl in role or role in kl:
                  return list(skills), True
      blob = f"{title} {description}".lower()
      found: List[str] = []
      for skill, kws in _SKILL_HINTS.items():
          if any(kw.lower() in blob for kw in kws):
              if skill not in found:
                  found.append(skill)
      if found:
          return found, True
      return ["generic"], True
  
  
  def parse_plan_table(plan_text: str) -> List[Dict[str, Any]]:
      """从 markdown 表格或列表格式中提取任务项.
  
      只接受结构化格式（表格/列表），拒绝按行分割兜底。
      返回空列表时，调用方应回退到 LLM 拆解或单任务兜底。
      支持可选「所需技能/技能」列（v4 XG-1）。
      """
      tasks: List[Dict[str, Any]] = []
  
      # ── 策略 1: Markdown 表格 ──
      table_lines = [
          line.strip()
          for line in plan_text.splitlines()
          if line.strip().startswith("|") and line.strip().endswith("|")
      ]
      if len(table_lines) >= 3:
          header_cells = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
          if any("任务" in cell for cell in header_cells):
              # 兼容固定 6 列布局 + 按表头定位
              idx_title = _header_index(header_cells, "任务", "title") or 1
              idx_resp = _header_index(header_cells, "负责", "角色", "responsible") or 2
              idx_pri = _header_index(header_cells, "优先级", "priority") or 3
              idx_dep = _header_index(header_cells, "依赖", "depend") or 4
              idx_art = _header_index(header_cells, "预期", "产出", "验收", "artifact") or 5
              idx_sk = _header_index(header_cells, "技能", "skill", "所需技能")
              for row_line in table_lines[2:]:
                  cells = [cell.strip() for cell in row_line.strip("|").split("|")]
                  if len(cells) < 6:
                      continue
                  if not cells[0] or re.fullmatch(r"-{3,}", cells[0].replace(" ", "")):
                      continue
                  title = cells[idx_title] if idx_title < len(cells) else cells[1]
                  responsible = cells[idx_resp] if idx_resp < len(cells) else cells[2]
                  priority = cells[idx_pri] if idx_pri < len(cells) else cells[3]
                  dependencies = cells[idx_dep] if idx_dep < len(cells) else cells[4]
                  expected_artifact = cells[idx_art] if idx_art < len(cells) else cells[5]
                  skills_raw = cells[idx_sk] if idx_sk is not None and idx_sk < len(cells) else ""
                  if not is_valid_task_title(title):
                      continue
                  description = "\n".join(
                      line for line in [
                          f"负责角色: {responsible}" if responsible else "",
                          f"依赖: {dependencies}" if dependencies and dependencies != "-" else "",
                          f"预期产出: {expected_artifact}" if expected_artifact else "",
                      ] if line
                  )
                  tasks.append({
                      "title": title,
                      "description": description or title,
                      "priority": _PRIORITY_MAP.get(priority.strip(), 2),
                      "responsible": responsible,
                      "dependencies": dependencies,
                      "expected_artifact": expected_artifact,
                      "required_skills": _parse_skills_cell(skills_raw),
                  })
              if tasks:
                  return tasks
  
      # ── 策略 2: 列表格式 ( - 标题: 描述 ) ──
      list_items = re.findall(r'[-*]\s+(.+?)[:：]\s*(.+)', plan_text)
      if list_items:
          for title, desc in list_items:
              clean_title = title.strip()
              if not is_valid_task_title(clean_title):
                  continue
              tasks.append({
                  "title": clean_title,
                  "description": desc.strip(),
                  "priority": 2,
                  "responsible": "",
                  "dependencies": "",
                  "expected_artifact": "",
                  "required_skills": [],
              })
          if tasks:
              return tasks
  
      return []
  
  
  # ── 结构化契约 ─────────────────────────────────────────────
  
  STEP_STATUSES = ("pending", "dispatched", "completed", "failed")
  PLAN_STATUSES = ("draft", "approved", "dispatched", "completed")
  
  
  @dataclass
  class PlanStep:
      """执行计划的一个步骤 — 派发后 1 步骤 ↔ 1 任务."""
  
      step_id: str = ""
      index: int = 0
      title: str = ""
      description: str = ""
      responsible_role: str = ""
      acceptance: str = ""            # 验收依据 = 预期产出
      dependencies: List[str] = field(default_factory=list)   # 引用其他 step 的序号/标题
      required_skills: List[str] = field(default_factory=list)
      priority: int = 2
      status: str = "pending"
      task_id: str = ""               # 派发后回填
  
      def to_dict(self) -> Dict[str, Any]:
          return {
              "step_id": self.step_id, "index": self.index, "title": self.title,
              "description": self.description, "responsible_role": self.responsible_role,
              "acceptance": self.acceptance, "dependencies": list(self.dependencies),
              "required_skills": list(self.required_skills), "priority": self.priority,
              "status": self.status, "task_id": self.task_id,
          }
  
      @classmethod
      def from_dict(cls, d: Dict[str, Any]) -> "PlanStep":
          return cls(
              step_id=d.get("step_id", ""), index=int(d.get("index", 0)),
              title=d.get("title", ""), description=d.get("description", ""),
              responsible_role=d.get("responsible_role", ""),
              acceptance=d.get("acceptance", ""),
              dependencies=list(d.get("dependencies", [])),
              required_skills=list(d.get("required_skills", [])),
              priority=int(d.get("priority", 2)),
              status=d.get("status", "pending"), task_id=d.get("task_id", ""),
          )
  
  
  @dataclass
  class ExecutionPlan:
      """Plaza 讨论收敛出的结构化执行计划."""
  
      plan_id: str = ""
      plaza_id: str = ""
      discussion_id: str = ""
      topic: str = ""
      goal: str = ""
      revision: int = 1
      status: str = "draft"
      approved_by: str = ""
      steps: List[PlanStep] = field(default_factory=list)
      created_at: str = ""
      updated_at: str = ""
  
      def __post_init__(self) -> None:
          if not self.plan_id:
              self.plan_id = f"plan-{uuid.uuid4().hex[:8]}"
          now = datetime.now(timezone.utc).isoformat()
          if not self.created_at:
              self.created_at = now
          if not self.updated_at:
              self.updated_at = now
  
      def touch(self) -> None:
          self.updated_at = datetime.now(timezone.utc).isoformat()
  
      def get_step(self, step_id: str) -> Optional[PlanStep]:
          for s in self.steps:
              if s.step_id == step_id:
                  return s
          return None
  
      def refresh_status(self) -> None:
          """步骤状态汇总 → 计划状态（全完成→completed）."""
          if not self.steps:
              return
          if all(s.status == "completed" for s in self.steps):
              self.status = "completed"
          elif any(s.status in ("dispatched", "completed", "failed") for s in self.steps):
              if self.status in ("approved", "dispatched"):
                  self.status = "dispatched"
          self.touch()
  
      def to_dict(self) -> Dict[str, Any]:
          return {
              "plan_id": self.plan_id, "plaza_id": self.plaza_id,
              "discussion_id": self.discussion_id, "topic": self.topic,
              "goal": self.goal, "revision": self.revision, "status": self.status,
              "approved_by": self.approved_by,
              "steps": [s.to_dict() for s in self.steps],
              "created_at": self.created_at, "updated_at": self.updated_at,
          }
  
      @classmethod
      def from_dict(cls, d: Dict[str, Any]) -> "ExecutionPlan":
          plan = cls(
              plan_id=d.get("plan_id", ""), plaza_id=d.get("plaza_id", ""),
              discussion_id=d.get("discussion_id", ""), topic=d.get("topic", ""),
              goal=d.get("goal", ""), revision=int(d.get("revision", 1)),
              status=d.get("status", "draft"), approved_by=d.get("approved_by", ""),
              created_at=d.get("created_at", ""), updated_at=d.get("updated_at", ""),
          )
          plan.steps = [PlanStep.from_dict(s) for s in d.get("steps", [])]
          return plan
  
  
  def build_plan_from_text(
      plan_text: str,
      *,
      plaza_id: str = "",
      discussion_id: str = "",
      topic: str = "",
      goal: str = "",
      revision: int = 1,
  ) -> ExecutionPlan:
      """把议事长的计划文本编译为结构化 ExecutionPlan."""
      i
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  ## ⚠️ 重要提示
  上方 📂 项目上下文 包含了任务相关的实际源文件。
  请基于这些文件设计方案，不要引用不存在的文件。
  
  ## 要求
  1. 基于调研结果和实际源码，设计详细技术方案
  2. 明确指出需要修改的文件和具体修改内容
  3. 定义接口规范（如有新增 API）
  4. 为开发工程师提供逐步实施指南
  
  项目根目录: /Users/panglaohu/Downloads/DoubleBoatClawSystem
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
  
  项目根目录: /Users/panglaohu/Downloads/AgentsGroup2026
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
────────────────────────────────────────────────────────────
⚡ 正在调用配置模型 (glm-5.1)...

🔗 API: models.sjtu.edu.cn | 模型: glm-5.1
────────────────────────────────────────────────────────────

# 技术方案：ES 当前容量、索引、分片和 SLO 基线评估

## 1. 概述

本方案为 **AgentsGroup2026** 系统提供 Elasticsearch 集群容量评估、索引/分片分析及 SLO 基线建立的技术设计。方案由 `build_archit` 智能体执行，产出容量评估表、扩容选型建议和风险清单。评估结果将作为上云架构决策的输入。

## 2. 数据采集方案

### 2.1 采集目标
- 集群健康状态（green/yellow/red）
- 节点资源（CPU、内存、磁盘、JVM heap）
- 索引元数据（名称、文档数、存储大小、分片数、副本数）
- 分片分配详情（节点分布、未分配分片、迁移状态）
- 查询/写入吞吐量（QPS、TPS、延迟百分位）
- 索引生命周期管理（ILM）策略及执行状态

### 2.2 采集方式
通过 Elasticsearch REST API 获取，无需安装额外代理。使用 Python `requests` 库封装采集器。

**核心 API 调用：**
```python
# 集群健康
GET /_cluster/health

# 节点统计
GET /_nodes/stats

# 索引统计
GET /_stats

# 索引分片分配
GET /_cat/shards?v&h=index,shard,prirep,state,node,store,ip

# 索引设置
GET /_all/_settings

# 索引生命周期管理
GET /_ilm/status
GET /_ilm/policy
```

### 2.3 采集频率
- 基线评估：一次性全量采集
- 持续监控（可选）：每 5 分钟采集一次，保留 7 天数据用于趋势分析

## 3. 容量评估模型

### 3.1 评估维度

| 维度 | 指标 | 阈值参考 | 风险等级 |
|------|------|----------|----------|
| 磁盘使用率 | 节点磁盘使用率 / 索引存储总量 | >75% 警告，>85% 严重 | 高/中/低 |
| 分片数量 | 每个节点分片数 / 索引分片数 | 单节点 <1000，单索引 <50 | 高/中/低 |
| 分片大小 | 平均分片大小 / 最大分片大小 | 10-50GB 最佳，>100GB 需拆分 | 高/中/低 |
| JVM Heap | 堆使用率 / GC 频率 | >75% 警告，>90% 严重 | 高/中/低 |
| CPU 使用率 | 节点 CPU 平均/峰值 | >70% 持续警告 | 高/中/低 |
| 查询延迟 | p99 查询延迟 | >500ms 警告，>2s 严重 | 高/中/低 |
| 写入吞吐 | 索引速率 vs 节点写入能力 | 接近节点瓶颈 | 高/中/低 |
| 未分配分片 | 数量 | >0 需关注 | 高/中/低 |
| ILM 合规 | 索引是否遵循生命周期策略 | 未配置 ILM 的索引 | 中 |

### 3.2 容量计算公式

**当前容量利用率：**
```
磁盘利用率 = sum(索引主分片大小 + 副本分片大小) / sum(节点可用磁盘)
```

**分片密度：**
```
分片密度 = 总分片数 / 数据节点数
```

**写入容量瓶颈：**
```
节点写入瓶颈 = 节点写入速率 / (节点磁盘 IOPS * 分片副本数)
```

**SLO 基线：**
- 可用性：集群状态 green ≥ 99.9%
- 延迟：p99 查询延迟 ≤ 200ms（业务关键索引）
- 数据持久性：副本数 ≥ 1，快照策略已配置

## 4. 输出格式

### 4.1 容量评估表（JSON / Markdown）

```json
{
  "cluster_name": "production-es",
  "assessment_time": "2026-06-01T00:00:00Z",
  "overall_status": "warning",
  "nodes": [
    {
      "node_id": "node-1",
      "ip": "10.0.0.1",
      "roles": ["data", "master"],
      "disk_usage_pct": 78.5,
      "heap_usage_pct": 72.3,
      "cpu_usage_pct": 65.0,
      "shard_count": 245,
      "risk_level": "medium",
      "risks": ["磁盘使用率接近阈值"]
    }
  ],
  "indices": [
    {
      "index_name": "logs-2026.05",
      "docs_count": 12500000,
      "size_gb": 450.2,
      "shards": 30,
      "replicas": 1,
      "avg_shard_size_gb": 15.0,
      "max_shard_size_gb": 22.3,
      "ilm_policy": "hot-warm-delete",
      "risk_level": "low"
    }
  ],
  "slo_compliance": {
    "availability": "green (100%)",
    "p99_latency_ms": 180,
    "replication_factor": 1,
    "snapshot_enabled": true,
    "violations": []
  },
  "capacity_summary": {
    "total_disk_tb": 10.0,
    "used_disk_tb": 7.8,
    "free_disk_tb": 2.2,
    "projected_growth_monthly_pct": 8.5,
    "estimated_exhaustion_days": 95
  }
}
```

### 4.2 扩容选型建议

| 建议类型 | 描述 | 优先级 | 预估成本 |
|----------|------|--------|----------|
| 增加数据节点 | 添加 2 个 2TB SSD 节点，降低分片密度 | P0 | $X |
| 升级磁盘 | 将现有节点磁盘从 1TB 升级至 2TB | P1 | $Y |
| 调整分片策略 | 对 `logs-*` 索引按天滚动，分片数从 30 降至 10 | P1 | 无 |
| 启用 ILM | 为未配置 ILM 的索引设置 hot-warm-cold 策略 | P2 | 无 |
| 优化查询 | 对慢查询添加 routing 或调整 mapping | P2 | 无 |

### 4.3 风险清单

| 风险 ID | 风险描述 | 影响 | 可能性 | 缓解措施 |
|---------|----------|------|--------|----------|
| RISK-001 | 磁盘使用率 >85% 导致节点只读 | 写入失败 | 高 | 立即扩容或清理历史索引 |
| RISK-002 | 单节点分片数 >1000 导致集群不稳定 | 查询延迟升高 | 中 | 增加节点或合并小分片 |
| RISK-003 | 未配置 ILM 的索引持续增长 | 存储爆炸 | 中 | 配置 ILM 策略 |
| RISK-004 | 副本数不足导致数据丢失风险 | 数据丢失 | 低 | 设置 min_replicas=1 |

## 5. 实施步骤

### 5.1 新增后端模块

**文件：`src/backend/es_capacity_planner.py`**

```python
"""
ES 容量评估与规划模块
负责：采集 ES 集群指标，计算容量利用率，生成评估报告
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

import requests
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# ---------- 数据模型 ----------

class NodeInfo(BaseModel):
    node_id: str
    ip: str
    roles: List[str]
    disk_usage_pct: float
    heap_usage_pct: float
    cpu_usage_pct: float
    shard_count: int
    risk_level: str = "low"
    risks: List[str] = []

class IndexInfo(BaseModel):
    index_name: str
    docs_count: int
    size_gb: float
    shards: int
    replicas: int
    avg_shard_size_gb: float
    max_shard_size_gb: float
    ilm_policy: Optional[str]
    risk_level: str = "low"

class CapacityReport(BaseModel):
    cluster_name: str
    assessment_time: str
    overall_status: str
    nodes: List[NodeInfo]
    indices: List[IndexInfo]
    slo_compliance: Dict
    capacity_summary: Dict

# ---------- 采集器 ----------

class ESCollector:
    def __init__(self, hosts: List[str], username: str = "", password: str = ""):
        self.hosts = hosts
        self.auth = (username, password) if username else None

    def _request(self, path: str) -> dict:
        for host in self.hosts:
            url = f"{host}/{path}"
            try:
                resp = requests.get(url, auth=self.auth, timeout=10)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:
                logger.warning(f"Failed to fetch {url}: {e}")
                continue
        raise ConnectionError("All ES hosts unreachable")

    def collect_cluster_health(self) -> dict:
        return self._request("_cluster/health")

    def collect_nodes_stats(self) -> dict:
        return self._request("_nodes/stats")

    def collect_indices_stats(self) -> dict:
        return self._request("_stats")

    def collect_shard_allocation(self) -> List[dict]:
        raw = self._request("_cat/shards?v&h=index,shard,prirep,state,node,store,ip&format=json")
        return raw if isinstance(raw, list) else []

    def collect_index_settings(self) -> dict:
        return self._request("_all/_settings")

    def collect_ilm_status(self) -> dict:
        return self._request("_ilm/status")

# ---------- 评估引擎 ----------

class CapacityAssessor:
    def __init__(self, collector: ESCollector):
        self.collector = collector

    def assess(self) -> CapacityReport:
        health = self.collector.collect_cluster_health()
        nodes_stats = self.collector.collect_nodes_stats()
        indices_stats = self.collector.collect_indices_stats()
        shards = self.collector.collect_shard_allocation()
        settings = self.collector.collect_index_settings()
        ilm_status = self.collector.collect_ilm_status()

        # 解析节点信息
        nodes = self._parse_nodes(nodes_stats, shards)
        # 解析索引信息
        indices = self._parse_indices(indices_stats, settings, ilm_status)
        # 计算 SLO 合规
        slo = self._calc_slo(health, indices_stats)
        # 容量汇总
        summary = self._calc_summary(nodes, indices)

        overall = "green"
        if any(n.risk_level == "high" for n in nodes):
            overall = "red"
        elif any(n.risk_level == "medium" for n in nodes):
            overall = "yellow"

        return CapacityReport(
            cluster_name=health.get("cluster_name", "unknown"),
            assessment_time=datetime.utcnow().isoformat() + "Z",
            overall_status=overall,
            nodes=nodes,
            indices=indices,
            slo_compliance=slo,
            capacity_summary=summary,
        )

    def _parse_nodes(self, nodes_stats: dict, shards: List[dict]) -> List[NodeInfo]:
        # 实现节点解析逻辑
        pass

    def _parse_indices(self, indices_stats: dict, settings: dict, ilm_status: dict) -> List[IndexInfo]:
        # 实现索引解析逻辑
        pass

    def _calc_slo(self, health: dict, indices_stats: dict) -> dict:
        # 实现 SLO 计算
        pass

    def _calc_summary(self, nodes: List[NodeInfo], indices: List[IndexInfo]) -> dict:
        # 实现容量汇总
        pass
```

### 5.2 新增 API 端点

**文件：`src/backend/main.py`**（追加路由）

```python
from fastapi import APIRouter, HTTPException
from es_capacity_planner import ESCollector, CapacityAssessor

router = APIRouter(prefix="/api/es-capacity", tags=["ES Capacity"])

@router.post("/assess")
async def assess_es_capacity(
    hosts: List[str] = Query(...),
    username: str = Query(None),
    password: str = Query(None),
):
    """
    触发 ES 容量评估
    返回容量评估报告（JSON）
    """
    try:
        collector = ESCollector(hosts, username, password)
        assessor = CapacityAssessor(collector)
        report = assessor.assess()
        return report.dict()
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Assessment failed: {e}")

@router.get("/report/{cluster_name}")
async def get_report(cluster_name: str):
    """
    获取已缓存的评估报告（需实现持久化）
    """
    # 从数据库或文件读取
    pass
```

### 5.3 前端展示（可选）

**文件：`src/frontend/es-capacity-dashboard.html`**（新增）

- 使用 Chart.js 展示节点资源使用率、索引大小趋势
- 表格展示风险清单
- 导出 PDF 功能

### 5.4 智能体集成

**文件：`src/backend/agents/build_archit.py`**（新增）

```python
"""
build_archit 智能体：执行 ES 容量评估任务
"""
from es_capacity_planner import ESCollector, CapacityAssessor

async def execute_es_capacity_assessment(hosts: List[str], credentials: dict) -> dict:
    collector = ESCollector(hosts, **credentials)
    assessor = CapacityAssessor(collector)
    report = assessor.assess()
    # 生成扩容选型建议和风险清单
    suggestions = generate_scaling_suggestions(report)
    risks = generate_risk_list(report)
    return {
        "capacity_report": report.dict(),
        "scaling_suggestions": suggestions,
        "risk_list": risks,
    }
```

## 6. 依赖与配置

### 6.1 Python 依赖
```
requests>=2.28
pydantic>=2.0
```

### 6.2 环境变量
```
ES_HOSTS=http://es1:9200,http://es2:9200
ES_USERNAME=admin
ES_PASSWORD=secret
```

## 7. 风险与注意事项

1. **ES 版本兼容性**：采集 API 在 ES 7.x/8.x 有差异，需适配。
2. **认证方式**：支持 Basic Auth、API Key、无认证。
3. **大规模集群**：采集 `_stats` 可能产生性能影响，建议在低峰期执行。
4. **数据持久化**：评估报告应存储至数据库或文件，支持历史对比。

## 8. 实施路线图

| 阶段 | 任务 | 负责人 | 预计工时 |
|------|------|--------|----------|
| 1 | 实现 ESCollector 数据采集 | 后端开发 | 2d |
| 2 | 实现 CapacityAssessor 评估逻辑 | 后端开发 | 3d |
| 3 | 实现 API 端点与智能体集成 | 后端开发 | 1d |
| 4 | 前端展示（可选） | 前端开发 | 2d |
| 5 | 测试与文档 | QA | 1d |

---

**附件：** 容量评估表模板（Markdown）、扩容选型建议模板、风险清单模板（见 4.1-4.3）。

────────────────────────────────────────────────────────────
✅ glm-5.1 完成
