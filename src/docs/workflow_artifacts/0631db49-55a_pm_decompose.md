# PM分解 — project_manager

任务: 生成 ElasticSearch 伸缩 Terraform/运维脚本
步骤: pm_decompose
Agent: build_pm

---

📋 任务: 0631db49-55a
🤖 Agent: PM (project_manager)
📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
🔧 执行方式: 配置模型 (codebuddy / glm-5.1)
⏱️ 超时: 1200s
────────────────────────────────────────────────────────────
📝 提示词:
  你是 AgentsGroup2026 系统的 PM (project_manager)。
  请执行以下开发任务:
  
  你是项目经理 (PM)。请对以下任务进行分解和规划:
  
  ## 任务
  生成 ElasticSearch 伸缩 Terraform/运维脚本
  负责角色: Build System
  依赖: 任务1
  预期产出: plan/dry-run/apply/rollback 脚本与 README
  负责角色: Build System
  执行智能体: build_pm
  依赖: 任务1
  预期产出: plan/dry-run/apply/rollback 脚本与 README
  
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
  
  ### 文件: `src/backend/tests/test_plan_loop_runtime.py`
  ```py
  # -*- coding: utf-8 -*-
  """Regression tests for the shared plan-loop runtime."""
  
  from __future__ import annotations
  
  import pytest
  
  from agents.chat_harness import ExecutionPlan, ProviderConfig
  from agents.runtime import plan_loop as plan_loop_module
  
  
  class _FakeToolResult:
      def __init__(self, success: bool = True, output: str = "", error: str = ""):
          self.success = success
          self.output = output
          self.error = error
  
  
  class _FakeExecutor:
      def __init__(self, result: _FakeToolResult):
          self.result = result
          self.calls = []
  
      async def execute(self, tool_name, tool_args, **kwargs):
          self.calls.append(
              {
                  "tool_name": tool_name,
                  "tool_args": tool_args,
                  "kwargs": kwargs,
              }
          )
          return self.result
  
  
  class _FakeHarness:
      def __init__(self):
          self.chat_calls = []
          self.stream_calls = []
  
      async def chat(self, prompt, **kwargs):
          self.chat_calls.append({"prompt": prompt, **kwargs})
          return type("Turn", (), {"response": "总结完成"})()
  
      async def stream_chat(self, prompt, **kwargs):
          self.stream_calls.append({"prompt": prompt, **kwargs})
          yield {"type": "message_delta", "text": "总结"}
          yield {"type": "message_stop", "stop_reason": "completed"}
  
  
  @pytest.mark.asyncio
  async def test_run_plan_loop_executes_steps_and_uses_synthesis_prompt(monkeypatch):
      executor = _FakeExecutor(_FakeToolResult(success=True, output="file contents"))
      harness = _FakeHarness()
      events = []
  
      monkeypatch.setattr("agents.tool_executor.get_tool_executor", lambda: executor)
  
      def build_plan(prompt, available_tools=None):
          plan = ExecutionPlan(goal=prompt)
          plan.add_step(
              "tool_call",
              "读取文件",
              tool_name="read_file",
              tool_args={"path": "README.md"},
          )
          plan.add_step("respond", "回复用户")
          return plan
  
      result = await plan_loop_module.run_plan_loop(
          harness,
          prompt="请读取 README",
          plan_builder=build_plan,
          agent_id="agent-1",
          team_id="team-1",
          session_id="sess-1",
          system_prompt="system",
          tools=[{"type": "function", "function": {"name": "read_file"}}],
          on_event=lambda event_type, payload: events.append((event_type, payload)),
      )
  
      assert executor.calls[0]["tool_name"] == "read_file"
      assert result.observations[0]["tool"] == "read_file"
      assert result.final_response == "总结完成"
      assert "[read_file] ✅: file contents" in harness.chat_calls[0]["prompt"]
      assert harness.chat_calls[0]["session_id"] == "sess-1"
      assert [event[0] for event in events[:3]] == ["plan_start", "step_start", "tool_result"]
      assert events[-1][0] == "loop_end"
      assert all(payload["runtime_id"] == "sess-1" for _, payload in events)
      assert [payload["sequence"] for _, payload in events] == list(range(1, len(events) + 1))
      assert events[0][1]["loop_kind"] == "plan_loop"
  
  
  @pytest.mark.asyncio
  async def test_stream_plan_loop_skips_after_iteration_cap_and_streams_synthesis(monkeypatch):
      executor = _FakeExecutor(_FakeToolResult(success=True, output="first tool ok"))
      harness = _FakeHarness()
      callback_events = []
  
      monkeypatch.setattr("agents.tool_executor.get_tool_executor", lambda: executor)
  
      def build_plan(prompt, available_tools=None):
          plan = ExecutionPlan(goal=prompt)
          plan.add_step(
              "tool_call",
              "第一步",
              tool_name="read_file",
              tool_args={"path": "README.md"},
          )
          plan.add_step(
              "tool_call",
              "第二步",
              tool_name="write_file",
              tool_args={"path": "tmp.txt", "content": "x"},
          )
          return plan
  
      events = [
          event
          async for event in plan_loop_module.stream_plan_loop(
              harness,
              prompt="请执行计划",
              plan_builder=build_plan,
              agent_id="agent-2",
              team_id="team-2",
              session_id="sess-2",
              system_prompt="system",
              max_iterations=1,
              on_event=lambda event_type, payload: callback_events.append((event_type, payload)),
          )
      ]
  
      skipped = [
          event for event in events
          if event["type"] == "step_complete"
          and event["step"]["status"] == "skipped"
      ]
  
      assert skipped
      assert skipped[0]["step"]["error"] == "Iteration cap reached"
      assert harness.stream_calls
      assert "[read_file] ✅: first tool ok" in harness.stream_calls[0]["prompt"]
      assert events[-1]["type"] == "message_stop"
      assert callback_events[0][0] == "plan_start"
      assert callback_events[-1][0] == "loop_end"
      runtime_events = [event for event in events if event["type"] in {"plan_start", "step_start", "tool_result", "step_complete", "plan_complete"}]
      assert runtime_events
      assert all(event["runtime_id"] == "sess-2" for event in runtime_events)
      assert [event["sequence"] for event in runtime_events] == list(range(1, len(runtime_events) + 1))
  
  
  @pytest.mark.asyncio
  async def test_chat_harness_agent_loop_methods_delegate_to_shared_plan_runtime(monkeypatch):
      from agents.chat_harness import ChatHarness
  
      captured = {"run": None, "stream": None}
  
      async def fake_run_plan_loop(harness, **kwargs):
          captured["run"] = kwargs
          return type("LoopResult", (), {"iterations": 2})()
  
      async def fake_stream_plan_loop(harness, **kwargs):
          captured["stream"] = kwargs
          yield {"type": "message_stop", "stop_reason": "completed"}
  
      monkeypatch.setattr("agents.runtime.run_plan_loop", fake_run_plan_loop)
      monkeypatch.setattr("agents.runtime.stream_plan_loop", fake_stream_plan_loop)
  
      harness = ChatHarness(default_config=ProviderConfig())
      result = await harness.agent_loop(
          "做个计划",
          tools=[{"type": "function", "function": {"name": "read_file"}}],
          max_iterations=3,
          on_event=lambda *_args: None,
      )
      chunks = [
          chunk
          async for chunk in harness.agent_loop_stream(
              "做个流式计划",
              max_iterations=4,
              on_event=lambda *_args: None,
          )
      ]
  
      assert result.iterations == 2
      assert captured["run"]["max_iterations"] == 3
      assert captured["run"]["tools"][0]["function"]["name"] == "read_file"
      assert callable(captured["run"]["on_event"])
      assert captured["stream"]["max_iterations"] == 4
      assert callable(captured["stream"]["on_event"])
      assert chunks[-1]["type"] == "message_stop"
  
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
              self.created_at = n
  ```
  
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
⚡ 正在调用配置模型 (glm-5.1)...

🔗 API: models.sjtu.edu.cn | 模型: glm-5.1
────────────────────────────────────────────────────────────

# 任务分解与规划：ElasticSearch 伸缩 Terraform/运维脚本

## 1. 任务概述

**目标**：为 ElasticSearch 集群生成一套可重复使用的 Terraform 伸缩脚本，支持 `plan`、`dry-run`、`apply`、`rollback` 四种操作模式，并附带完整的 README 文档。

**负责角色**：Build System（构建系统）  
**依赖**：任务1（假设为基础设施预置、IAM 权限、Terraform 后端配置等前置条件）  
**预期产出**：
- `plan.sh` / `dry-run.sh` / `apply.sh` / `rollback.sh` 四个可执行脚本
- `README.md` 说明文档

**项目根目录**：`/Users/panglaohu/Downloads/AgentsGroup2026`  
**后端**：`src/backend/` (Python FastAPI)  
**前端**：`src/frontend/` (HTML + JS)  
**注意**：当前项目上下文未包含 ElasticSearch 相关配置，需从零构建。

---

## 2. 子任务分解

### 2.1 调研与设计阶段

| 子任务 | 描述 | 负责角色 | 预估工时 | 依赖 |
|--------|------|----------|----------|------|
| 2.1.1 调研现有 ElasticSearch 集群架构 | 确认集群版本、节点角色（master/data/ingest）、存储类型、网络拓扑、现有 Terraform 状态 | 研究员 | 2h | 任务1（权限） |
| 2.1.2 确定伸缩策略 | 选择水平伸缩（增加/减少节点数）还是垂直伸缩（调整实例规格）；定义伸缩触发条件（CPU/内存/存储水位） | 架构师 | 3h | 2.1.1 |
| 2.1.3 设计 Terraform 模块结构 | 规划模块目录、变量、输出；确定如何管理 state（S3/DynamoDB） | 架构师 | 2h | 2.1.2 |
| 2.1.4 定义 rollback 机制 | 伸缩前快照、保留旧配置、回滚步骤（恢复节点数/规格） | 架构师 | 1h | 2.1.2 |

### 2.2 开发阶段

| 子任务 | 描述 | 负责角色 | 预估工时 | 依赖 |
|--------|------|----------|----------|------|
| 2.2.1 编写 Terraform 主模块 | 实现 `main.tf`、`variables.tf`、`outputs.tf`，支持节点数、实例类型、磁盘大小等参数 | 开发者 | 4h | 2.1.3 |
| 2.2.2 编写伸缩脚本 | 实现 `plan.sh`（仅显示变更）、`dry-run.sh`（模拟 apply 但不实际执行）、`apply.sh`（执行伸缩）、`rollback.sh`（回滚到上一个稳定状态） | 开发者 | 4h | 2.2.1 |
| 2.2.3 集成 Terraform 后端与状态锁定 | 配置 S3 后端和 DynamoDB 锁表，确保并发安全 | 开发者 | 1h | 2.2.1 |
| 2.2.4 编写 README | 包含使用前提、环境变量、脚本用法、示例、回滚说明、注意事项 | 开发者 | 2h | 2.2.2 |

### 2.3 测试与验证阶段

| 子任务 | 描述 | 负责角色 | 预估工时 | 依赖 |
|--------|------|----------|----------|------|
| 2.3.1 单元测试 Terraform 模块 | 使用 `terraform validate`、`terraform fmt`、`tflint` 检查语法和最佳实践 | QA | 1h | 2.2.1 |
| 2.3.2 集成测试（沙箱环境） | 在非生产环境执行 `plan` → `dry-run` → `apply` → 验证集群健康 → `rollback` | QA | 3h | 2.2.2 |
| 2.3.3 压力测试与回滚验证 | 模拟伸缩过程中断，验证 rollback 脚本能正确恢复 | QA | 2h | 2.3.2 |
| 2.3.4 安全审计 | 检查 IAM 权限最小化、密钥管理（避免硬编码）、网络策略 | 安全工程师 | 1h | 2.2.1 |

### 2.4 文档与交付

| 子任务 | 描述 | 负责角色 | 预估工时 | 依赖 |
|--------|------|----------|----------|------|
| 2.4.1 ��善 README | 补充故障排查、常见问题、变更日志 | 开发者 | 1h | 2.3.4 |
| 2.4.2 代码审查与合并 | 提交 PR，邀请架构师/运维审查 | 开发者 | 1h | 2.4.1 |
| 2.4.3 最终交付 | 将脚本和 README 放入 `src/backend/scripts/es-scaling/` 目录 | Build System | 0.5h | 2.4.2 |

---

## 3. 技术风险与缓解措施

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|----------|
| ElasticSearch 集群在伸缩期间不可用 | 业务中断 | 中 | 使用滚动更新（`rolling_update`），设置 `minimum_master_nodes`；在 apply 前强制 `plan` 检查 |
| Terraform state 锁冲突 | 并发操作导致状态损坏 | 低 | 使用 DynamoDB 锁表，脚本中增加 `-lock=true` 参数 |
| 回滚失败（如新节点数据未同步） | 数据丢失或集群不稳定 | 中 | 伸缩前强制创建快照（snapshot），回滚脚本先恢复快照再恢复节点数 |
| 权限不足（IAM 角色未授权） | 脚本执行失败 | 低 | 在 README 中明确所需权限列表，并在脚本开头做预检查 |
| 脚本中硬编码敏感信息 | 安全泄露 | 低 | 所有敏感参数通过环境变量或 Terraform 变量传入，禁止硬编码 |

---

## 4. 依赖关系说明

- **任务1**（前置依赖）：假设已完成以下内容：
  - Terraform 后端（S3 bucket + DynamoDB 表）已创建
  - AWS 凭证（或云厂商凭证）已配置
  - ElasticSearch 集群的基础 Terraform 模块（创建集群）已存在
  - 目标集群的 `terraform state` 可访问

- **内部依赖**：严格按照 2.1 → 2.2 → 2.3 → 2.4 顺序执行，其中 2.2.2 依赖 2.2.1，2.3 依赖 2.2。

---

## 5. 输出目录结构建议

```
src/backend/scripts/es-scaling/
├── README.md
├── modules/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
├── scripts/
│   ├── plan.sh
│   ├── dry-run.sh
│   ├── apply.sh
│   └── rollback.sh
└── examples/
    └── scaling-example.tfvars
```

---

## 6. 后续角色指导

### 6.1 研究员（2.1.1）
- 查看现有 `src/backend/` 下是否有 ElasticSearch 相关配置（如 `config.py` 中的 ES 连接信息）
- 与运维团队确认当前集群版本、节点数、实例类型、存储类型（EBS/本地 SSD）
- 确认 Terraform 状态文件位置（S3 bucket 名称、key 前缀）

### 6.2 架构师（2.1.2 ~ 2.1.4）
- 优先采用水平伸缩（增加/减少 data 节点），避免垂直伸缩导致的长时间重启
- 设计变量：`node_count`、`instance_type`、`volume_size`、`volume_type`
- 回滚策略：每次 apply 前自动备份当前 state 到 `backups/` 目录，并记录变更时间戳

### 6.3 开发者（2.2）
- 使用 Terraform `count` 或 `for_each` 管理节点数，避免硬编码
- 脚本中统一使用 `set -euo pipefail` 确保错误退出
- `dry-run.sh` 实现：`terraform plan -out=tfplan && terraform show tfplan`，但不执行 `apply`
- `rollback.sh` 实现：从备份目录恢复上一个 state 文件，然后 `terraform apply` 恢复到旧配置

### 6.4 QA（2.3）
- 测试环境使用独立的 Terraform workspace，避免影响生产
- 验证 `plan` 输出中节点数变化正确
- 模拟 `apply` 过程中断（如 `Ctrl+C`），然后执行 `rollback`，确认集群恢复

---

## 7. 时间估算与里程碑

| 里程碑 | 截止时间 | 关键交付物 |
|--------|----------|------------|
| M1: 设计完成 | Day 2 | 伸缩策略文档、Terraform 模块设计 |
| M2: 开发完成 | Day 5 | 所有脚本与模块代码 |
| M3: 测试通过 | Day 7 | 测试报告、回滚验证记录 |
| M4: 交付 | Day 8 | 最终脚本、README、合并到主分支 |

---

**备注**：本分解基于通用 ElasticSearch 伸缩场景，具体实现需根据实际云厂商（AWS/GCP/Azure）调整 Terraform provider。建议在 `README.md` 中明确支持的云平台和版本要求。

────────────────────────────────────────────────────────────
✅ glm-5.1 完成
