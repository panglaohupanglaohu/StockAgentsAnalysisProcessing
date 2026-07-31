# 架构设计 — architect

任务: 生成 ElasticSearch 伸缩 Terraform/运维脚本
步骤: architecture
Agent: build_architect

---

📋 任务: 0631db49-55a
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
  
  
  ## 📁 工作区产物清单（MANIFEST）
  上游步骤产物已落盘到工作区，请用 `read_file` / `list_files` 按需读取：
  
  ### pm_decompose — PM分解
  - `steps/pm_decompose/output.md` (LLM 输出主文档)
  - `steps/pm_decompose/self_report.json` (步骤自报告)
  
  ### research — 研究分析
  - `steps/research/output.md` (LLM 输出主文档)
  - `steps/research/self_report.json` (步骤自报告)
  
  提示：直接读取上述文件获取完整内容，避免上下文过载。
  
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

# 技术方案：ElasticSearch 伸缩 Terraform/运维脚本

## 1. 概述

本方案为 `AgentsGroup2026` 系统设计一套可复用的 ElasticSearch 集群伸缩基础设施脚本，支持 **plan / dry-run / apply / rollback** 全生命周期操作，并配套完整的 README 文档。脚本基于 Terraform 实现基础设施即代码，适用于 AWS 环境（可扩展至其他云），满足以下核心需求：

- 水平伸缩：增加/减少数据节点数
- 垂直伸缩：调整节点实例类型（CPU/内存）
- 安全回滚：保留历史状态快照，支持一键回退
- 预检机制：dry-run 模式验证变更影响，避免误操作

## 2. 目录结构

在项目根目录下新建 `infra/elasticsearch/` 目录，结构如下：

```
infra/elasticsearch/
├── modules/
│   └── es_cluster/               # 可复用的 ES 集群模块
│       ├── main.tf               # 核心资源定义
│       ├── variables.tf          # 输入变量
│       ├── outputs.tf            # 输出
│       └── versions.tf           # provider 版本约束
├── environments/
│   ├── dev/
│   │   ├── main.tf               # 环境级配置
│   │   ├── terraform.tfvars      # 变量值
│   │   └── backend.tf            # 状态后端配置
│   ├── staging/
│   └── prod/
├── scripts/
│   ├── plan.sh                   # 生成执行计划
│   ├── dry-run.sh                # 模拟执行（只读检查）
│   ├── apply.sh                  # 应用变更
│   ├── rollback.sh               # 回滚到上一个稳定版本
│   └── common.sh                 # 公共函数库
├── README.md                     # 使用说明
└── Makefile                      # 快捷命令
```

## 3. Terraform 模块设计

### 3.1 模块 `es_cluster` 变量定义 (`modules/es_cluster/variables.tf`)

```hcl
variable "cluster_name" {
  description = "ElasticSearch 集群名称"
  type        = string
}

variable "region" {
  description = "AWS 区域"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "数据节点 EC2 实例类型"
  type        = string
  default     = "r5.large.elasticsearch"
}

variable "instance_count" {
  description = "数据节点数量"
  type        = number
  default     = 3
}

variable "dedicated_master_enabled" {
  description = "是否启用专用主节点"
  type        = bool
  default     = true
}

variable "dedicated_master_type" {
  description = "专用主节点实例类型"
  type        = string
  default     = "c5.large.elasticsearch"
}

variable "dedicated_master_count" {
  description = "专用主节点数量（建议 3）"
  type        = number
  default     = 3
}

variable "ebs_volume_size" {
  description = "每个数据节点的 EBS 卷大小（GB）"
  type        = number
  default     = 100
}

variable "ebs_volume_type" {
  description = "EBS 卷类型"
  type        = string
  default     = "gp3"
}

variable "snapshot_bucket" {
  description = "快照存储 S3 桶名称"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "subnet_ids" {
  description = "子网 ID 列表"
  type        = list(string)
}

variable "security_group_ids" {
  description = "安全组 ID 列表"
  type        = list(string)
  default     = []
}

variable "tags" {
  description = "资源标签"
  type        = map(string)
  default     = {}
}
```

### 3.2 核心资源 (`modules/es_cluster/main.tf`)

使用 AWS OpenSearch Service（兼容 ElasticSearch）作为托管服务，避免自建集群的运维复杂度。

```hcl
resource "aws_opensearch_domain" "this" {
  domain_name           = var.cluster_name
  engine_version        = "Elasticsearch_7.10"  # 或 OpenSearch_2.x
  cluster_config {
    instance_type          = var.instance_type
    instance_count         = var.instance_count
    dedicated_master_enabled = var.dedicated_master_enabled
    dedicated_master_type    = var.dedicated_master_type
    dedicated_master_count   = var.dedicated_master_count
    zone_awareness_enabled   = length(var.subnet_ids) >= 2
    zone_awareness_config {
      availability_zone_count = length(var.subnet_ids) >= 2 ? 2 : 1
    }
  }
  ebs_options {
    ebs_enabled = true
    volume_size = var.ebs_volume_size
    volume_type = var.ebs_volume_type
  }
  snapshot_options {
    automated_snapshot_start_hour = 23
  }
  vpc_options {
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_group_ids
  }
  encrypt_at_rest {
    enabled = true
  }
  node_to_node_encryption {
    enabled = true
  }
  domain_endpoint_options {
    enforce_https       = true
    tls_security_policy = "Policy-Min-TLS-1-2-2019-07"
  }
  log_publishing_options {
    cloudwatch_log_group_arn = aws_cloudwatch_log_group.this.arn
    log_type                 = "INDEX_SLOW_LOGS"
  }
  tags = var.tags
}

resource "aws_cloudwatch_log_group" "this" {
  name              = "/aws/opensearch/${var.cluster_name}/slow-logs"
  retention_in_days = 30
  tags              = var.tags
}
```

### 3.3 输出 (`modules/es_cluster/outputs.tf`)

```hcl
output "domain_arn" {
  value = aws_opensearch_domain.this.arn
}

output "domain_endpoint" {
  value = aws_opensearch_domain.this.endpoint
}

output "kibana_endpoint" {
  value = aws_opensearch_domain.this.kibana_endpoint
}

output "cluster_config" {
  value = aws_opensearch_domain.this.cluster_config
}
```

## 4. 运维脚本设计

### 4.1 公共函数库 (`scripts/common.sh`)

```bash
#!/bin/bash
set -euo pipefail

# 环境变量
ENV=${1:-dev}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TF_DIR="${SCRIPT_DIR}/../environments/${ENV}"
STATE_BACKUP_DIR="${SCRIPT_DIR}/../state_backups/${ENV}"

# 颜色输出
info()  { echo -e "\033[1;34m[INFO]\033[0m $*"; }
warn()  { echo -e "\033[1;33m[WARN]\033[0m $*"; }
error() { echo -e "\033[1;31m[ERROR]\033[0m $*" >&2; exit 1; }

# 检查 Terraform 是否安装
check_terraform() {
  command -v terraform >/dev/null 2>&1 || error "Terraform 未安装，请先安装 https://www.terraform.io/downloads"
}

# 初始化 Terraform
init_terraform() {
  cd "$TF_DIR"
  terraform init -reconfigure -upgrade
}

# 备份当前状态（用于回滚）
backup_state() {
  mkdir -p "$STATE_BACKUP_DIR"
  local backup_file="${STATE_BACKUP_DIR}/terraform.tfstate.$(date +%Y%m%d%H%M%S)"
  cp terraform.tfstate "$backup_file" 2>/dev/null || warn "无现有状态文件可备份"
  info "状态已备份至: $backup_file"
}
```

### 4.2 `plan.sh` — 生成执行计划

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh" "$@"

check_terraform
init_terraform

info "生成 Terraform 执行计划..."
terraform plan -out=tfplan -detailed-exitcode
PLAN_EXIT=$?

if [ $PLAN_EXIT -eq 0 ]; then
  info "无变更，集群已处于期望状态。"
elif [ $PLAN_EXIT -eq 1 ]; then
  error "计划生成失败，请检查错误信息。"
elif [ $PLAN_EXIT -eq 2 ]; then
  info "计划生成成功，存在变更。使用 dry-run.sh 进行模拟执行，或 apply.sh 应用。"
fi
```

### 4.3 `dry-run.sh` — 模拟执行（只读检查）

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh" "$@"

check_terraform
init_terraform

info "执行 dry-run 模拟（只读检查）..."
# 生成计划并解析变更摘要
terraform plan -out=tfplan -detailed-exitcode > /dev/null 2>&1
terraform show -json tfplan > /tmp/tfplan.json

# 提取关键变更信息
echo "========== 变更摘要 =========="
echo "数据节点数变化:"
jq -r '.resource_changes[] | select(.type == "aws_opensearch_domain") | .change.before.cluster_config.instance_count, .change.after.cluster_config.instance_count' /tmp/tfplan.json | paste - -
echo "实例类型变化:"
jq -r '.resource_changes[] | select(.type == "aws_opensearch_domain") | .change.before.cluster_config.instance_type, .change.after.cluster_config.instance_type' /tmp/tfplan.json | paste - -
echo "EBS 容量变化:"
jq -r '.resource_changes[] | select(.type == "aws_opensearch_domain") | .change.before.ebs_options[0].volume_size, .change.after.ebs_options[0].volume_size' /tmp/tfplan.json | paste - -
echo "=============================="

# 询问确认
read -p "以上变更是预期的吗？(yes/no) " confirm
if [ "$confirm" != "yes" ]; then
  info "dry-run 取消，未执行任何变更。"
  rm -f tfplan
  exit 0
fi

info "dry-run 通过，可执行 apply.sh 应用变更。"
rm -f tfplan
```

### 4.4 `apply.sh` — 应用变更

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh" "$@"

check_terraform
init_terraform

# 先备份当前状态
backup_state

info "应用 Terraform 变更..."
terraform apply -auto-approve tfplan 2>&1 | tee /tmp/terraform_apply.log
APPLY_EXIT=$?

if [ $APPLY_EXIT -eq 0 ]; then
  info "变更已成功应用。"
  # 清理计划文件
  rm -f tfplan
else
  error "应用失败，请检查日志 /tmp/terraform_apply.log。可执行 rollback.sh 回滚。"
fi
```

### 4.5 `rollback.sh` — 回滚到上一个稳定版本

```bash
#!/bin/bash
source "$(dirname "$0")/common.sh" "$@"

check_terraform
init_terraform

# 查找最新的状态备份
LATEST_BACKUP=$(ls -t "${STATE_BACKUP_DIR}/terraform.tfstate."* 2>/dev/null | head -1)
if [ -z "$LATEST_BACKUP" ]; then
  error "未找到状态备份，无法回滚。"
fi

info "将回滚到备份: $LATEST_BACKUP"
read -p "确认回滚？此操作不可逆！(yes/no) " confirm
if [ "$confirm" != "yes" ]; then
  info "回滚取消。"
  exit 0
fi

# 恢复状态文件
cp "$LATEST_BACKUP" terraform.tfstate

# 重新生成计划并应用（恢复到备份时的状态）
info "生成回滚计划..."
terraform plan -out=rollback_plan
info "应用回滚..."
terraform apply -auto-approve rollback_plan
ROLLBACK_EXIT=$?

if [ $ROLLBACK_EXIT -eq 0 ]; then
  info "回滚成功。"
  rm -f rollback_plan
else
  error "回滚失败，请手动干预。"
fi
```

## 5. 使用说明（README 核心内容）

### 5.1 前置条件

- Terraform >= 1.5
- AWS CLI 已配置凭证（或使用 IAM Role）
- 目标环境 VPC、子网、安全组已就绪
- S3 桶用于快照存储（需提前创建）

### 5.2 快速开始

```bash
# 1. 进入环境目录
cd infra/elasticsearch/environments/dev

# 2. 编辑 terraform.tfvars 设置变量
vim terraform.tfvars

# 3. 生成执行计划
../../scripts/plan.sh dev

# 4. 模拟执行（dry-run）
../../scripts/dry-run.sh dev

# 5. 应用变更
../../scripts/apply.sh dev

# 6. 回滚（如需）
../../scripts/rollback.sh dev
```

### 5.3 伸缩操作示例

**水平扩展（增加节点数）**：修改 `terraform.tfvars` 中的 `instance_count` 为 5，然后执行 `plan.sh` → `dry-run.sh` → `apply.sh`。

**垂直扩展（升级实例类型）**：修改 `instance_type` 为 `r5.xlarge.elasticsearch`，执行相同流程。

**缩容**：减少 `instance_count` 或降级 `instance_type`，注意缩容可能导致数据重分布，建议在低峰期操作。

### 5.4 安全注意事项

- 所有脚本默认使用 `-auto-approve`，生产环境建议手动确认
- 回滚脚本依赖状态备份，请确保 `state_backups/` 目录持久化（建议使用 S3 远程状态）
- 修改集群配置后，ES 会自动进行滚动重启，期间服务可能短暂不可用

## 6. 与现有系统的集成

当前 `AgentsGroup2026` 系统未直接使用 ElasticSearch，但未来可能用于：

- 日志聚合（后端日志）
- 全文搜索（前端知识库）
- 指标存储（成本仪表盘）

建议在 `src/backend/config.py` 中添加 ES 连接配置项，并在 `main.py` 中初始化客户端。本 Terraform 脚本输出的 `domain_endpoint` 可作为配置值注入。

## 7. 后续扩展

- 支持多集群（读写分离、冷热架构）
- 集成 CI/CD（GitHub Actions 自动 plan/apply）
- 添加监控告警（CloudWatch + PagerDuty）
- 支持 OpenSearch 最新版本

## 8. 实施指南

1. **创建目录结构**：按第 2 节创建所有文件和目录。
2. **编写 Terraform 模块**：将第 3 节代码写入对应文件。
3. **编写运维脚本**：将第 4 节脚本写入 `scripts/` 目录，并赋予执行权限 (`chmod +x scripts/*.sh`)。
4. **配置环境变量**：为每个环境创建 `terraform.tfvars`，填写实际 VPC、子网等参数。
5. **初始化并测试**：在 dev 环境执行 `plan.sh` 验证语法，然后 `apply.sh` 创建测试集群。
6. **编写 README**：基于第 5 节内容完善文档。
7. **集成到 CI**：在 `.github/workflows/` 中添加 Terraform 工作流，自动执行 plan 和 apply。

---

**方案设计人**：Architect (AgentsGroup2026)  
**日期**：2026-05-29  
**版本**：v1.0

────────────────────────────────────────────────────────────
✅ glm-5.1 完成
