# 部署上线 — devops

任务: 执行代码 review、单步变更和彩排回滚
步骤: deploy
Agent: build_deployer

---

📋 任务: bdf59329-cf4
🤖 Agent: Deployer (devops)
📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
🔧 执行方式: Claude Code CLI
⏱️ 超时: 1800s
────────────────────────────────────────────────────────────
📝 提示词:
  你是 AgentsGroup2026 系统的 Deployer (devops)。
  请执行以下开发任务:
  
  你是 DevOps 部署工程师。
  开发者的代码交付物已自动保存到管线共享工作区。
  部署步骤完成后，系统会自动将代码文件应用到项目代码库。
  
  ## 任务
  执行代码 review、单步变更和彩排回滚
  负责角色: 运维操作员
  依赖: 任务2
  预期产出: 审核记录、执行日志、回滚验证结果
  负责角色: 运维操作员
  执行智能体: build_deploy
  依赖: 任务2
  预期产出: 审核记录、执行日志、回滚验证结果
  
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
  src/backend/tests/test_core_api_smoke.py
  src/backend/tests/test_cost_aggregator.py
  src/backend/tests/test_cost_gate.py
  src/backend/tests/test_cost_gate_routes.py
  src/backend/tests/test_cost_monitor.py
  src/backend/tests/test_cost_report.py
  src/backend/tests/test_cost_target_tracker.py
  src/backend/tests/test_datacenter_api.py
  src/backend/tests/test_eco_drill.py
  src/backend/tests/test_eco_drill_engine.py
  src/backend/tests/test_eco_drill_routing.py
  src/backend/tests/test_eco_loop.py
  src/backend/tests/test_eco_runtime_config.py
  src/backend/tests/test_evidence_store.py
  ... (共 1796 个 src/ 文件)
  
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
  
  ### 文件: `src/backend/tests/test_review_integration.py`
  ```py
  # -*- coding: utf-8 -*-
  """审核集成测试 — 覆盖4阶段状态流转、异常跳转、交叉复核越权、带偏差标注数据下的复核准确率验证.
  
  测试结构:
    Test4StageStateFlow          — 4阶段状态流转 (PENDING→CHANGES_REQUESTED→APPROVED→CLOSED)
    TestAbnormalJumps            — 异常跳转 (非法状态转换)
    TestCrossReviewAuthorization — 交叉复核越权测试
    TestBiasedAnnotationAccuracy — 带偏差标注数据下的复核准确率验证
  """
  
  from __future__ import annotations
  
  import asyncio
  import math
  
  import pytest
  
  from agents.gate_evaluator import (
      evaluate,
      evaluate_from_dict,
      _compute_weighted_score,
  )
  from agents.review_models import (
      GateEvaluationContext,
      GateLevel,
      GateEvaluationResult,
      ReviewAction,
      ReviewStatus,
      ReviewEntry,
  )
  from agents.review_service import ReviewService
  
  
  # ══════════════════════════════════════════════════════════════════════
  # Helper fixtures
  # ══════════════════════════════════════════════════════════════════════
  
  @pytest.fixture
  def review_service():
      """创建隔离的 ReviewService 实例 (使用内存存储)."""
      svc = ReviewService()
      # 使用内存模式以避免文件系统依赖
      svc._store = None  # 强制使用内存 store
      svc._store_factory = None
      return svc
  
  
  @pytest.fixture
  def pending_entry(review_service):
      """创建一个 PENDING 状态的审核条目."""
      ctx = GateEvaluationContext(
          entity_id="EVO-TEST-001",
          compliance_score=85.0,
          test_pass_rate=90.0,
          code_quality_score=80.0,
          security_issues=1,
          documentation_level=75.0,
          evolution_impact=0.8,
          breaking_changes=False,
          critical_test_failures=0.0,
      )
      result = evaluate(ctx)
      entry = asyncio.run(
          review_service.submit("EVO-TEST-001", result, context=ctx.model_dump(), reviewer="submitter_alice")
      )
      return entry
  
  
  def _run(coro):
      """Helper to run async coroutines in sync tests."""
      return asyncio.run(coro)
  
  
  # ══════════════════════════════════════════════════════════════════════
  # Test 1: 4阶段状态流转
  # ══════════════════════════════════════════════════════════════════════
  
  class Test4StageStateFlow:
      """验证完整 4 阶段状态流转: PENDING → CHANGES_REQUESTED → APPROVED → CLOSED."""
  
      def test_full_4stage_flow_pending_to_changes_requested(self, review_service, pending_entry):
          """阶段1→2: PENDING → CHANGES_REQUESTED."""
          entry = pending_entry
          assert entry.status == ReviewStatus.PENDING
          assert entry.version == 1
  
          updated = _run(review_service.perform_action(
              entry_id=entry.id,
              action=ReviewAction.REQUEST_CHANGES,
              reviewer="reviewer_bob",
              comment="需要补充文档",
              idempotency_key="stage1-2",
          ))
          assert updated.status == ReviewStatus.CHANGES_REQUESTED
          assert updated.version == 2
          assert updated.current_action == ReviewAction.REQUEST_CHANGES
  
      def test_full_4stage_flow_changes_to_approved(self, review_service, pending_entry):
          """阶段2→3: CHANGES_REQUESTED → APPROVED."""
          entry = pending_entry
          # 先转到 CHANGES_REQUESTED
          _run(review_service.perform_action(
              entry_id=entry.id,
              action=ReviewAction.REQUEST_CHANGES,
              reviewer="reviewer_bob",
              comment="需要修改",
              idempotency_key="s2-a",
          ))
          # 再批准
          updated = _run(review_service.perform_action(
              entry_id=entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              comment="修改已确认",
              idempotency_key="s2-b",
          ))
          assert updated.status == ReviewStatus.APPROVED
          assert updated.version == 3
  
      def test_full_4stage_flow_approved_to_closed(self, review_service, pending_entry):
          """阶段3→4: APPROVED → CLOSED."""
          entry = pending_entry
          # PENDING → CHANGES_REQUESTED
          _run(review_service.perform_action(
              entry_id=entry.id,
              action=ReviewAction.REQUEST_CHANGES,
              reviewer="reviewer_bob",
              comment="需要修改",
              idempotency_key="s3-a",
          ))
          # CHANGES_REQUESTED → APPROVED
          _run(review_service.perform_action(
              entry_id=entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              comment="修改已确认",
              idempotency_key="s3-b",
          ))
          # APPROVED → CLOSED
          updated = _run(review_service.perform_action(
              entry_id=entry.id,
              action=ReviewAction.CLOSE,
              reviewer="reviewer_bob",
              comment="审核完成，关闭",
              idempotency_key="s3-c",
          ))
          assert updated.status == ReviewStatus.CLOSED
          assert updated.version == 4
          assert updated.resolved_at is not None
  
      def test_complete_4stage_flow_all_steps(self, review_service, pending_entry):
          """完整4阶段: PENDING → CHANGES_REQUESTED → APPROVED → CLOSED."""
          entry = pending_entry
          assert entry.status == ReviewStatus.PENDING, "Stage 1: PENDING"
  
          # Stage 1→2
          e = _run(review_service.perform_action(
              entry_id=entry.id, action=ReviewAction.REQUEST_CHANGES,
              reviewer="reviewer_bob", comment="需要修改",
              idempotency_key="full-1",
          ))
          assert e.status == ReviewStatus.CHANGES_REQUESTED, "Stage 2: CHANGES_REQUESTED"
          assert e.version == 2
  
          # Stage 2→3
          e = _run(review_service.perform_action(
              entry_id=entry.id, action=ReviewAction.APPROVE,
              reviewer="reviewer_bob", comment="已修改",
              idempotency_key="full-2",
          ))
          assert e.status == ReviewStatus.APPROVED, "Stage 3: APPROVED"
          assert e.version == 3
  
          # Stage 3→4
          e = _run(review_service.perform_action(
              entry_id=entry.id, action=ReviewAction.CLOSE,
              reviewer="reviewer_bob", comment="关闭",
              idempotency_key="full-3",
          ))
          assert e.status == ReviewStatus.CLOSED, "Stage 4: CLOSED"
          assert e.version == 4
  
      # ── Alternative paths ────────────────────────────────────────
  
      def test_short_flow_pending_to_approved(self, review_service, pending_entry):
          """快速通道: PENDING → APPROVED (跳过 CHANGES_REQUESTED)."""
          updated = _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              comment="直接通过",
              idempotency_key="short-1",
          ))
          assert updated.status == ReviewStatus.APPROVED
          assert updated.version == 2
  
      def test_short_flow_pending_to_rejected(self, review_service, pending_entry):
          """拒绝通道: PENDING → REJECTED."""
          updated = _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.REJECT,
              reviewer="reviewer_bob",
              comment="不符合要求",
              idempotency_key="reject-1",
          ))
          assert updated.status == ReviewStatus.REJECTED
          assert updated.version == 2
  
      def test_rejected_to_closed(self, review_service, pending_entry):
          """REJECTED → CLOSED."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.REJECT,
              reviewer="reviewer_bob",
              comment="不符合要求",
              idempotency_key="rej-close-a",
          ))
          updated = _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.CLOSE,
              reviewer="reviewer_bob",
              comment="关闭拒绝条目",
              idempotency_key="rej-close-b",
          ))
          assert updated.status == ReviewStatus.CLOSED
  
      def test_idempotency_prevents_duplicate(self, review_service, pending_entry):
          """幂等性: 相同 idempotency_key 不会重复处理."""
          key = "idempotent-001"
          e1 = _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              comment="首次批准",
              idempotency_key=key,
          ))
          assert e1.status == ReviewStatus.APPROVED
          assert e1.version == 2
  
          # 重复调用应返回已有结果
          e2 = _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.REJECT,  # 不同的 action，但相同 key
              reviewer="reviewer_charlie",
              comment="尝试重复",
              idempotency_key=key,
          ))
          assert e2.status == ReviewStatus.APPROVED  # 保持首次结果
          assert e2.version == 2  # 版本未变
  
      def test_version_increments_on_each_transition(self, review_service, pending_entry):
          """每次状态变更版本号递增."""
          entry = pending_entry
          assert entry.version == 1
  
          e = _run(review_service.perform_action(
              entry_id=entry.id, action=ReviewAction.APPROVE,
              reviewer="bob", idempotency_key="ver-1",
          ))
          assert e.version == 2
  
          e = _run(review_service.perform_action(
              entry_id=entry.id, action=ReviewAction.CLOSE,
              reviewer="bob", idempotency_key="ver-2",
          ))
          assert e.version == 3
  
  
  # ══════════════════════════════════════════════════════════════════════
  # Test 2: 异常跳转
  # ══════════════════════════════════════════════════════════════════════
  
  class TestAbnormalJumps:
      """验证非法状态转换被正确拒绝."""
  
      def test_cannot_approve_an_already_approved(self, review_service, pending_entry):
          """已 APPROVED 的条目不能再次 APPROVE."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              idempotency_key="abn-1",
          ))
          with pytest.raises(ValueError, match="状态转换"):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAction.APPROVE,
                  reviewer="reviewer_bob",
                  idempotency_key="abn-1-dup",
              ))
  
      def test_cannot_approve_closed_entry(self, review_service, pending_entry):
          """已 CLOSED 的条目不能再 APPROVE."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              idempotency_key="abn-2a",
          ))
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.CLOSE,
              reviewer="reviewer_bob",
              idempotency_key="abn-2b",
          ))
          with pytest.raises(ValueError, match="状态转换"):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAction.APPROVE,
                  reviewer="reviewer_bob",
                  idempotency_key="abn-2c",
              ))
  
      def test_cannot_reject_closed_entry(self, review_service, pending_entry):
          """已 CLOSED 的条目不能再 REJECT."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.REJECT,
              reviewer="reviewer_bob",
              idempotency_key="abn-3a",
          ))
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.CLOSE,
              reviewer="reviewer_bob",
              idempotency_key="abn-3b",
          ))
          with pytest.raises(ValueError, match="状态转换"):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAction.REJECT,
                  reviewer="reviewer_bob",
                  idempotency_key="abn-3c",
              ))
  
      def test_cannot_request_changes_on_closed(self, review_service, pending_entry):
          """已 CLOSED 的条目不能请求修改."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              idempotency_key="abn-4a",
          ))
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.CLOSE,
              reviewer="reviewer_bob",
              idempotency_key="abn-4b",
          ))
          with pytest.raises(ValueError, match="状态转换"):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAction.REQUEST_CHANGES,
                  reviewer="reviewer_bob",
                  idempotency_key="abn-4c",
              ))
  
      def test_cannot_request_changes_on_approved(self, review_service, pending_entry):
          """已 APPROVED 的条目不能请求修改."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              idempotency_key="abn-5a",
          ))
          with pytest.raises(ValueError, match="状态转换"):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAction.REQUEST_CHANGES,
                  reviewer="reviewer_bob",
                  idempotency_key="abn-5b",
              ))
  
      def test_cannot_approve_rejected_entry(self, review_service, pending_entry):
          """已 REJECTED 的条目不能 APPROVE (应先 REQUEST_CHANGES?)."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.REJECT,
              reviewer="reviewer_bob",
              idempotency_key="abn-6a",
          ))
          with pytest.raises(ValueError, match="状态转换"):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAction.APPROVE,
                  reviewer="reviewer_bob",
                  idempotency_key="abn-6b",
              ))
  
      def test_can_close_pending_entry_directly(self, review_service, pending_entry):
          """可以直接关闭 PENDING 条目 (当前系统允许 PENDING → CLOSED)."""
          # 当前系统允许从 PENDING 直接 CLOSE
          updated = _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.CLOSE,
              reviewer="reviewer_bob",
              idempotency_key="abn-7",
          ))
          assert updated.status == ReviewStatus.CLOSED
          assert updated.version == 2
  
      def test_nonexistent_entry_returns_error(self, review_service):
          """操作不存在的条目返回错误."""
          with pytest.raises(ValueError, match="未找到"):
              _run(review_service.perform_action(
                  entry_id="NONEXISTENT-001",
                  action=ReviewAction.APPROVE,
                  reviewer="reviewer_bob",
              ))
  
      def test_cannot_jump_backward_from_approved_to_pending(self, review_service, pending_entry):
          """已 APPROVED 的条目不能回退到 PENDING (不可逆)."""
          _run(review_service.perform_action(
              entry_id=pending_entry.id,
              action=ReviewAction.APPROVE,
              reviewer="reviewer_bob",
              idempotency_key="back-1a",
          ))
          # 没有从 APPROVED → PENDING 的转换，任何操作都会触发 ValueError
          with pytest.raises(ValueError):
              _run(review_service.perform_action(
                  entry_id=pending_entry.id,
                  action=ReviewAc
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
  
  
  def parse_plan_table(plan_text: str) -> List[Dict[str, Any]]:
   
  ```
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 04: develop
  任务: 执行代码 review、单步变更和彩排回滚
  Agent: build_developer
  📋 任务: bdf59329-cf4
  🤖 Agent: Developer (developer)
  📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
  🔧 执行方式: Claude Code CLI
  ────────────────────────────────────────────────────────────
  你是 AgentsGroup2026 系统的 Developer (developer)。
  你是开发工程师 (DeepSeek V4 + 工具循环模式)。
  你**已经被赋予真正的工具能力**: read_file / grep / list_files / write_file / patch_file / run_python。
  禁止凭空想象 — 所有写代码前必须先用工具读真实代码。
  执行代码 review、单步变更和彩排回滚
  预期产出: 审核记录、执行日志、回滚验证结果
  执行智能体: build_deploy
  预期产出: 审核记录、执行日志、回滚验证结果
  
  ### 步骤 05: test (完整产出)
  
  # 测试验证 — qa_engineer
  
  任务: 执行代码 review、单步变更和彩排回滚
  步骤: test
  Agent: build_tester
  
  ---
  
  📋 任务: bdf59329-cf4
  🤖 Agent: Tester (qa_engineer)
  📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
  🔧 执行方式: Claude Code CLI
  ⏱️ 超时: 1800s
  ────────────────────────────────────────────────────────────
  📝 提示词:
    你是 AgentsGroup2026 系统的 Tester (qa_engineer)。
    请执行以下开发任务:
    
    你是 QA 测试工程师 (DeepSeek V4 + 工具循环模式)。
    你**已经被赋予真正的测试工具能力**: read_file / grep / run_python / run_pytest。
    禁止凭空判定 — 所有结论必须来自工具的真实输出。
    
    ## 任务
    执行代码 review、单步变更和彩排回滚
    负责角色: 运维操作员
    依赖: 任务2
    预期产出: 审核记录、执行日志、回滚验证结果
    负责角色: 运维操作员
    执行智能体: build_deploy
    依赖: 任务2
    预期产出: 审核记录、执行日志、回滚验证结果
    
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
    src/backend/tests/test_core_api_smoke.py
    src/backend/tests/test_cost_aggregator.py
    src/backend/tests/test_cost_gate.py
    src/backend/tests/test_cost_gate_routes.py
    src/backend/tests/test_cost_monitor.py
    src/backend/tests/test_cost_report.py
    src/backend/tests/test_cost_target_tracker.py
    src/backend/tests/test_datacenter_api.py
    src/backend/tests/test_eco_drill.py
    src/backend/tests/test_eco_drill_engine.py
    src/backend/tests/test_eco_drill_routing.py
    src/backend/tests/test_eco_loop.py
    src/backend/tests/test_eco_runtime_config.py
    src/backend/tests/test_evidence_store.py
    ... (共 1796 个 src/ 文件)
    
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
  
  ...(截断)
  
  ## 自动部署机制
  - 开发步骤的代码块已提取到: `storage/pipeline_runs/<task_id>/04_develop/code/`
  - 本步骤完成时系统自动执行: 开发文件 → 项目代码库 (含 .bak 备份)
  - 你只需审查变更合理性并输出部署报告
  
  ## 部署策略要求
  1. **变更分析**: 分析代码变更的范围和影响
     - 小改动 (hotfix/patch): 就地更新
     - 较大功能变更: 蓝绿部署
  2. **蓝绿部署判断**: 新增/大幅修改 HTML 页面、API 签名变更、核心 Channel 逻辑变更
  3. **⚠️ Captain 安全拒绝规则**:
     如果 Captain/PM 在前序步骤中拒绝了删除/移除操作:
     - **不得直接修改原始页面**
     - **创建新版本**: `<文件名>-v2.<ext>` (如 cms-health-v2.html)
     - 新版本包含所请求的修改内容，用代码块格式输出:
       ```html // src/frontend/cms-health-v2.html
       <!-- 完整文件内容 -->
       ```
  4. **产出**: 输出部署清单 (Markdown 格式) 包含: 部署类型, 影响文件, 回滚方案
  
  项目根目录: /Users/panglaohu/Downloads/DoubleBoatClawSystem
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  
  
  项目根目录: /Users/panglaohu/Downloads/AgentsGroup2026
  后端: src/backend/ (Python FastAPI)
  前端: src/frontend/ (HTML + JS)
  完成后运行: PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest tests/ -q --tb=short
  
────────────────────────────────────────────────────────────
⏳ 正在启动 Claude Code CLI...

🔗 Claude Code → default | 模型: deepseek-chat
⏳ DeepSeek 正在思考中...

⏳ 等待 DeepSeek 响应... (10s)
⏳ 等待 DeepSeek 响应... (20s)
⏳ 等待 DeepSeek 响应... (30s)
⏳ 等待 DeepSeek 响应... (40s)
⏳ 等待 DeepSeek 响应... (50s)
⏳ 等待 DeepSeek 响应... (60s)
⏳ 等待 DeepSeek 响应... (70s)
⏳ 等待 DeepSeek 响应... (80s)
⏳ 等待 DeepSeek 响应... (90s)
⏳ 等待 DeepSeek 响应... (100s)
⏳ 等待 DeepSeek 响应... (110s)
⏳ 等待 DeepSeek 响应... (120s)
⏳ 等待 DeepSeek 响应... (130s)
⏳ 等待 DeepSeek 响应... (140s)
⏳ 等待 DeepSeek 响应... (150s)
⏳ 等待 DeepSeek 响应... (160s)
⏳ 等待 DeepSeek 响应... (170s)
API Error: Unable to connect to API (ConnectionRefused)


⚠️ Claude Code 退出码: 1
