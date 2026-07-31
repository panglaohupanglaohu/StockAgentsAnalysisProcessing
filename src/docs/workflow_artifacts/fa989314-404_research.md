# 研究分析 — researcher

任务: 将成本异常纳入SLO监控，制定成本相关的应急回滚Runbook
步骤: research
Agent: build_researcher

---

📋 任务: fa989314-404
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
  将成本异常纳入SLO监控，制定成本相关的应急回滚Runbook
  负责角色: 值班与事件指挥官
  依赖: 任务1完成
  预期产出: 成本异常告警规则，应急回滚操作手册
  负责角色: 值班与事件指挥官
  依赖: 任务1完成
  预期产出: 成本异常告警规则，应急回滚操作手册
  
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
  ... (共 970 个 src/ 文件)
  
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
  
  ### 文件: `src/backend/agents/ab_testing.py`
  ```py
  # -*- coding: utf-8 -*-
  """A/B测试框架 — 基于EWMA和Lamport时钟的因果一致性升级策略.
  
  核心功能:
  1. EWMA (Exponentially Weighted Moving Average) 阈值计算
  2. Lamport 时钟因果一致性追踪
  3. 流量染色标签 (x-sync-policy: ewma) 解析与路由
  4. 冷启动预热缓存 (预计算滑动窗口均值)
  5. ConfigMap 热更新支持
  6. 渐进式流量分配 (5% → 50% → 100%)
  """
  
  from __future__ import annotations
  
  import asyncio
  import json
  import logging
  import math
  import time
  from dataclasses import dataclass, field
  from datetime import datetime, timezone
  from enum import Enum
  from typing import Any, Callable, Dict, List, Optional, Tuple
  
  logger = logging.getLogger(__name__)
  
  
  # ══════════════════════════════════════════════════════════════════
  # 枚举与数据模型
  # ══════════════════════════════════════════════════════════════════
  
  
  class SyncPolicy(str, Enum):
      """同步策略枚举 — 用于流量染色标签."""
      FIXED_THRESHOLD = "fixed_threshold"  # 对照组: 固定阈值
      EWMA_ADAPTIVE = "ewma_adaptive"      # 实验组: EWMA动态阈值
      EWMA = EWMA_ADAPTIVE
      LAMPORT_CLOCK = "lamport_clock"
  
  
  class TrafficAllocation(float, Enum):
      """流量分配阶段."""
      PHASE_1_5PCT = 5.0
      PHASE_2_50PCT = 50.0
      PHASE_3_100PCT = 100.0
      CANARY_5PCT = PHASE_1_5PCT
      HALF_50PCT = PHASE_2_50PCT
      FULL_100PCT = PHASE_3_100PCT
      ROLLED_BACK = 0.0
  
  
  @dataclass
  class LamportClock:
      """Lamport 逻辑时钟 — 追踪因果依赖关系.
  
      Attributes:
          node_id: 节点标识
          counter: 逻辑时钟计数器
          timestamp: 物理时间戳 (毫秒)
      """
      node_id: str
      counter: int = 0
      timestamp: float = 0.0  # 物理时间戳 (毫秒)
  
      def __post_init__(self) -> None:
          if self.timestamp <= 0:
              self.timestamp = time.time() * 1000
  
      def tick(self, physical_ts: Optional[float] = None) -> int:
          """时钟滴答 — 递增计数器.
  
          Args:
              physical_ts: 物理时间戳 (毫秒), 默认使用当前时间.
  
          Returns:
              递增后的计数器值.
          """
          self.counter += 1
          self.timestamp = physical_ts or (time.time() * 1000)
          return self.counter
  
      def merge(self, other: LamportClock) -> int:
          """合并另一个时钟 — 取 max(counter, other.counter) + 1.
  
          Args:
              other: 另一个 Lamport 时钟.
  
          Returns:
              合并后的计数器值.
          """
          self.counter = max(self.counter, other.counter) + 1
          self.timestamp = max(self.timestamp, other.timestamp)
          return self.counter
  
      def update(self, other_timestamp: float) -> float:
          """兼容旧 API: 用对端时间戳推进本地时钟."""
          self.counter += 1
          self.timestamp = max(self.timestamp, other_timestamp) + 1
          return self.timestamp
  
      def is_concurrent_with(self, other: LamportClock) -> bool:
          return self.node_id != other.node_id and self.timestamp == other.timestamp
  
      def happened_before(self, other: LamportClock) -> bool:
          return self.timestamp < other.timestamp
  
      def to_dict(self) -> Dict[str, Any]:
          return {
              "node_id": self.node_id,
              "counter": self.counter,
              "timestamp": self.timestamp,
          }
  
      @classmethod
      def from_dict(cls, data: Dict[str, Any]) -> LamportClock:
          return cls(
              node_id=data["node_id"],
              counter=data.get("counter", 0),
              timestamp=data.get("timestamp", 0.0),
          )
  
  
  @dataclass
  class CausalDependency:
      """因果依赖关系 — 追踪事件之间的因果关系.
  
      Attributes:
          source_node: 源节点 ID
          target_node: 目标节点 ID
          clock: 依赖发生时的 Lamport 时钟
          depth: 依赖深度 (级联层数)
      """
      source_node: str
      target_node: str
      clock: LamportClock
      depth: int = 1
  
  
  @dataclass
  class EWMAConfig:
      """EWMA 策略配置 — 支持 ConfigMap 热更新.
  
      Attributes:
          alpha: EWMA 平滑因子 (0 < alpha <= 1), 默认 0.3
          base_threshold_ms: 基础阈值 (毫秒), 默认 100ms
          threshold_multiplier: 阈值乘数, 默认 3.0 (3-sigma)
          cooling_period_seconds: 冷却期 (秒), 默认 60s
          min_samples: 最小样本数, 默认 10
          max_dependency_depth: 最大因果依赖深度, 默认 3
          clock_skew_tolerance_ms: 时钟偏差容忍度 (毫秒), 默认 100ms
          enable_warm_cache: 是否启用预热缓存, 默认 True
          warm_cache_window_size: 预热缓存窗口大小, 默认 100
      """
      alpha: float = 0.3
      beta: float = 0.1
      base_threshold_ms: float = 100.0
      min_threshold_ms: float = 50.0
      max_threshold_ms: float = 500.0
      threshold_multiplier: float = 3.0
      cooldown_seconds: float = 30.0
      cooling_extension_seconds: float = 15.0
      min_samples: int = 10
      max_causal_depth: int = 5
      clock_skew_tolerance_ms: float = 100.0
      enable_warm_cache: bool = True
      warm_cache_window_size: int = 100
  
      @property
      def cooling_period_seconds(self) -> float:
          return self.cooldown_seconds
  
      @cooling_period_seconds.setter
      def cooling_period_seconds(self, value: float) -> None:
          self.cooldown_seconds = value
  
      @property
      def max_dependency_depth(self) -> int:
          return self.max_causal_depth
  
      @max_dependency_depth.setter
      def max_dependency_depth(self, value: int) -> None:
          self.max_causal_depth = value
  
      def to_dict(self) -> Dict[str, Any]:
          return {
              "alpha": self.alpha,
              "beta": self.beta,
              "base_threshold_ms": self.base_threshold_ms,
              "min_threshold_ms": self.min_threshold_ms,
              "max_threshold_ms": self.max_threshold_ms,
              "threshold_multiplier": self.threshold_multiplier,
              "cooldown_seconds": self.cooldown_seconds,
              "cooling_period_seconds": self.cooling_period_seconds,
              "cooling_extension_seconds": self.cooling_extension_seconds,
              "min_samples": self.min_samples,
              "max_causal_depth": self.max_causal_depth,
              "max_dependency_depth": self.max_dependency_depth,
              "clock_skew_tolerance_ms": self.clock_skew_tolerance_ms,
              "enable_warm_cache": self.enable_warm_cache,
              "warm_cache_window_size": self.warm_cache_window_size,
          }
  
      @classmethod
      def from_dict(cls, data: Dict[str, Any]) -> EWMAConfig:
          return cls(
              alpha=data.get("alpha", 0.3),
              beta=data.get("beta", 0.1),
              base_threshold_ms=data.get("base_threshold_ms", 100.0),
              min_threshold_ms=data.get("min_threshold_ms", 50.0),
              max_threshold_ms=data.get("max_threshold_ms", 500.0),
              threshold_multiplier=data.get("threshold_multiplier", 3.0),
              cooldown_seconds=data.get(
                  "cooldown_seconds",
                  data.get("cooling_period_seconds", 30.0),
              ),
              cooling_extension_seconds=data.get("cooling_extension_seconds", 15.0),
              min_samples=data.get("min_samples", 10),
              max_causal_depth=data.get(
                  "max_causal_depth",
                  data.get("max_dependency_depth", 5),
              ),
              clock_skew_tolerance_ms=data.get("clock_skew_tolerance_ms", 100.0),
              enable_warm_cache=data.get("enable_warm_cache", True),
              warm_cache_window_size=data.get("warm_cache_window_size", 100),
          )
  
  
  @dataclass
  class ABTestMetrics:
      """A/B测试指标 — 核心验证指标 + 辅助监控指标.
  
      Attributes:
          false_upgrade_rate: 误升级率 (核心指标)
          resource_increase_pct: 资源增幅百分比 (核心指标)
          behavior_fingerprint_mutation_rate: 行为指纹变异率
          anomaly_propagation_depth: 异常传播深度
          prediction_error_rate: 预测误差率
          energy_increase_pct: 能耗增幅百分比
          temperature_slope: 温度斜率
          policy_evaluation_latency_ms: 策略评估延迟 (毫秒)
          evolution_stagnation_rate: 演化僵化率
      """
      false_upgrade_rate: float = 0.0
      resource_increase_pct: float = 0.0
      behavior_fingerprint_mutation_rate: float = 0.0
      anomaly_propagation_depth: float = 0.0
      prediction_error_rate: float = 0.0
      energy_increase_pct: float = 0.0
      temperature_slope: float = 0.0
      policy_evaluation_latency_ms: float = 0.0
      evolution_stagnation_rate: float = 0.0
      experiment_traffic_pct: float = 0.0
  
      def to_dict(self) -> Dict[str, float]:
          return {
              "false_upgrade_rate": self.false_upgrade_rate,
              "resource_increase_pct": self.resource_increase_pct,
              "behavior_fingerprint_mutation_rate": self.behavior_fingerprint_mutation_rate,
              "anomaly_propagation_depth": self.anomaly_propagation_depth,
              "prediction_error_rate": self.prediction_error_rate,
              "energy_increase_pct": self.energy_increase_pct,
              "temperature_slope": self.temperature_slope,
              "policy_evaluation_latency_ms": self.policy_evaluation_latency_ms,
              "evolution_stagnation_rate": self.evolution_stagnation_rate,
          }
  
  
  # ══════════════════════════════════════════════════════════════════
  # EWMA 阈值计算引擎
  # ══════════════════════════════════════════════════════════════════
  
  
  class EWMAThresholdEngine:
      """EWMA 阈值计算引擎 — 动态计算强同步触发阈值.
  
      基于指数加权移动平均 (EWMA) 和标准差动态调整阈值，
      实现自适应因果一致性升级策略。
  
      Attributes:
          config: EWMA 策略配置
          _ewma: 当前 EWMA 值
          _ewmvar: 当前 EWMA 方差
          _sample_count: 样本计数
          _last_update_ts: 上次更新时间戳
          _cooling_until: 冷却期截止时间
      """
  
      def __init__(self, config: Optional[EWMAConfig] = None):
          self.config = config or EWMAConfig()
          self._ewma: float = self.config.base_threshold_ms
          self._ewmvar: float = 0.0
          self._sample_count: int = 0
          self._last_update_ts: float = 0.0
          self._cooling_until: float = 0.0
          self._warm_cache: WarmCache = WarmCache(
              window_size=self.config.warm_cache_window_size
          ) if self.config.enable_warm_cache else None
  
      def update(self, latency_ms: float, timestamp: Optional[float] = None) -> float:
          """更新 EWMA 统计量并返回当前阈值.
  
          Args:
              latency_ms: 本次同步延迟 (毫秒).
  
          Returns:
              当前动态阈值 (毫秒).
          """
          now = timestamp if timestamp is not None else time.time()
  
          # 检查冷却期
          if now < self._cooling_until:
              return self._compute_threshold()
  
          self._sample_count += 1
          alpha = self.config.alpha
  
          previous_ewma = self._ewma
          self._ewma = alpha * latency_ms + (1 - alpha) * self._ewma
          diff = latency_ms - previous_ewma
          self._ewmvar = (1 - alpha) * (self._ewmvar + alpha * diff * diff)
  
          self._last_update_ts = now
  
          # 更新预热缓存
          if self._warm_cache:
              self._warm_cache.add(latency_ms)
  
          return self._compute_threshold()
  
      def _compute_threshold(self) -> float:
          """计算当前动态阈值.
  
          Returns:
              阈值 (毫秒).
          """
          if self._sample_count < self.config.min_samples:
              threshold = max(self.config.base_threshold_ms, self._ewma)
              return min(self.config.max_threshold_ms, max(self.config.min_threshold_ms, threshold))
  
          std_dev = math.sqrt(self._ewmvar) if self._ewmvar > 0 else 0.0
          threshold = self._ewma + self.config.threshold_multiplier * std_dev
          threshold = max(threshold, self.config.base_threshold_ms)
          threshold = max(self.config.min_threshold_ms, threshold)
          threshold = min(self.config.max_threshold_ms, threshold)
          return threshold
  
      def get_ewma(self) -> float:
          return self._ewma
  
      def get_current_threshold(self) -> float:
          """获取当前阈值 (不更新统计量).
  
          Returns:
              当前阈值 (毫秒).
          """
          return self._compute_threshold()
  
      def get_ewma_stats(self) -> Dict[str, Any]:
          """获取 EWMA 统计信息.
  
          Returns:
              统计字典.
          """
          return {
              "ewma": self._ewma,
              "ewmvar": self._ewmvar,
              "std_dev": math.sqrt(self._ewmvar) if self._ewmvar > 0 else 0.0,
              "sample_count": self._sample_count,
              "update_count": self._sample_count,
              "alpha": self.config.alpha,
              "current_threshold": self._compute_threshold(),
              "cooling_active": time.time() < self._cooling_until,
              "cooling_remaining_seconds": max(0, self._cooling_until - time.time()),
          }
  
      def enter_cooling(self, reason: str = "") -> None:
          """进入冷却期 — 暂停策略切换.
  
          Args:
              reason: 冷却原因.
          """
          self._cooling_until = time.time() + self.config.cooldown_seconds
          logger.warning(f"❄️ EWMA 进入冷却期 {self.config.cooldown_seconds}s: {reason}")
  
      def is_cooling(self) -> bool:
          """是否处于冷却期.
  
          Returns:
              True 如果处于冷却期.
          """
          return time.time() < self._cooling_until
  
      def reset(self) -> None:
          """重置所有统计量."""
          self._ewma = self.config.base_threshold_ms
          self._ewmvar = 0.0
          self._sample_count = 0
          self._last_update_ts = 0.0
          self._cooling_until = 0.0
          if self._warm_cache:
              self._warm_cache.reset()
          logger.info("🔄 EWMA 引擎已重置")
  
      def warm_up(self, precomputed_values: Optional[List[float]] = None) -> float:
          """预热 — 使用预计算值初始化 EWMA 统计量.
  
          确保首次计算延迟 < 1秒.
  
          Args:
              precomputed_values: 预计算的延迟样本列表.
  
          Returns:
              预热后的阈值 (毫秒).
          """
          if not precomputed_values:
              # 使用预热缓存中的数据
              if self._warm_cache and self._warm_cache.size() > 0:
                  precomputed_values = self._warm_cache.get_all()
              else:
                  # 使用默认预估值
                  precomputed_values = [self.config.base_threshold_ms] * 5
  
          for val in precomputed_values:
              self.update(val)
  
          threshold = self._compute_threshold()
          logger.info(f"🔥 EWMA 预热完成: {len(precomputed_values)} 样本, 阈值={threshold:.1f}ms")
          return threshold
  
  
  # ══════════════════════════════════════════════════════════════════
  # 预热缓存
  # ══════════════════════════════════════════════════════════════════
  
  
  class WarmCache:
      """预热缓存 — 预计算滑动窗口均值，确保冷启动 < 1秒.
  
      维护一个固定大小的滑动窗口，存储最近的延迟样本，
      用于快速初始化 EWMA 统计量。
      """
  
      def __init__(self, window_size: int = 100):
          self._window_size = window_size
          self._samples: List[float] = []
          self._sum: float = 0.0
  
      def add(self, value: float) -> None:
          """添加一个样本到缓存.
  
          Args:
              value: 延迟值 (毫秒).
          """
          self._samples.append(value)
          self._sum += value
          if len(self._samples) > self._window_size:
              removed = self._samples.pop(0)
              self._sum -= removed
  
      def get_mean(self) -> float:
          """获取缓存中样本的均值.
  
          Returns:
              均值 (毫秒), 如果缓存为空返回 0.
          """
          if not self._samples:
              return 0.0
          return self._sum / len(self._samples)
  
      def get_all(self) -> List[float]:
          """获取所有缓存的样本.
  
          Returns:
              样本列表.
          """
          return list(self._samples)
  
      def size(self) -> int:
          """获取缓存中的样本数.
  
          Returns:
              样本数.
          """
          return len(self._samples)
  
      def reset(self) -> None:
          """清空缓存."""
          self._samples.clear()
          self._sum = 0.0
  
  
  # ══════════════════════════════════════════════════════════════════
  # 流量染色与路由
  # ══════════════════════════════════════════════════════════════════
  
  
  class TrafficStainer:
      """流量染色器 — 管理 x-sync-policy 标签的解析与路由.
  
      根据节点类型 (高扇出节点优先) 和流量分配比例，
      决定是否将请求染色为实验组 (ewma) 或对照组
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
          self._sse_queues: Dict[str, List[asyncio.Queue]] = {}  # discussion_id → queues
          self._discussion_locks: Dict[str, asyncio.Lock] = {}
          self._chat_fn: Optional[Callable] = None  # ChatHarness.chat reference
  
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
      
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose (完整产出)
  
  # PM分解 — project_manager
  
  任务: 将成本异常纳入SLO监控，制定成本相关的应急回滚Runbook
  步骤: pm_decompose
  Agent: build_pm
  
  ---
  
  📋 任务: fa989314-404
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
    将成本异常纳入SLO监控，制定成本相关的应急回滚Runbook
    负责角色: 值班与事件指挥官
    依赖: 任务1完成
    预期产出: 成本异常告警规则，应急回滚操作手册
    负责角色: 值班与事件指挥官
    依赖: 任务1完成
    预期产出: 成本异常告警规则，应急回滚操作手册
    
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
    ... (共 970 个 src/ 文件)
    
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
            evolution
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

# 技术调研报告：成本异常纳入SLO监控与应急回滚Runbook

## 1. 目标与范围

**任务**：将 LLM 调用成本（token 消耗）纳入系统服务水平目标 (SLO) 监控，并建立成本异常时的应急回滚操作手册。  
**负责角色**：值班与事件指挥官 (On-call & Incident Commander)。  
**依赖**：前序任务 1 (PM 分解) 已完成，提供了任务规划。  
**预期产出**：
- 成本异常告警规则（定义在 SLO 内）
- 应急回滚操作手册（包含具体步骤和自动化回滚接口）

本调研基于项目现有代码库 `src/backend/`（Python/FastAPI）和 `src/frontend/`（HTML/JS），分析需要修改和新增的文件，评估实现可行性，并给出具体修改点。

## 2. 现有关键组件分析

### 2.1 事件总线 (`agents/event_bus.py`)
- **路径**: `src/backend/agents/event_bus.py`（位于项目文件列表中，未提供内容，但已知存在）
- **作用**: 系统的中央事件分发机制。测试文件 `test_evolution_race.py` 中展示了执行器通过事件记录执行开始/结束等。
- **利用方式**: 当检测到成本异常时，发布事件（如 `cost.anomaly.detected`），供监控系统或告警模块消费。

### 2.2 运维操作 API (`agents/operation_api.py` / `operation_models.py` / `operation_store.py`)
- **路径**: `src/backend/agents/operation_api.py`、`operation_models.py`、`operation_store.py`
- **测试**: `src/backend/tests/test_operation_store.py` 存在。
- **推测功能**: 提供系统运维相关操作（如健康检查、配置管理、回滚等）的 REST 端点。
- **利用方式**: 可在此模块添加成本异常的查询接口、主动回滚触发接口。

### 2.3 Token 预算测试 (`tests/test_token_budget.py`)
- **路径**: `src/backend/tests/test_token_budget.py`（存在但无内容）
- **推测**: 已有 token 预算或限额的测试逻辑，可能对应某个尚未列出的模块（如 `agents/token_budget.py`），但鉴于项目规则仅能引用已列出文件，我们认定该功能尚未实现或仅在测试层面存在。
- **注意**: 无法引用 `agents/token_budget.py`，但可在新模块中实现成本追踪。

### 2.4 系统演化与回滚 (`channels/system_evolution`)
- **路径**: `channels/system_evolution`（在测试文件 `test_evolution_race.py` 中大量使用），不在项目文件列表内，但测试引用了它，推测位于 `src/backend/channels/` 下。
- **测试**: `test_evolution_race.py` 展示了 `EvolutionExecutor` 的并发执行、断网容错和审核流竞态逻辑，以及 `SystemEvolutionChannel` 的演化项状态转换。
- **回滚机制**: `EvolutionItem` 有 `retry_count` 和状态回退能力，且包含 `mark_build_complete` 等守卫逻辑。应急回滚可复用这些模式：对已派发但成本异常的任务，触发状态回滚或版本回退。

### 2.5 其他相关模块
- `agents/agent_loop.py`：应该是 LLM 交互的主循环，此处在每次 API 调用后记录 token 使用量是最佳切入点。文件存在但未提供内容，需在实现时查阅。
- `agents/api.py`：统一入口，可能包含 `_submit_internal_task` 等。可在此挂载成本计量钩子。
- `frontend/`: 前端尚无成本监控仪表板，但本次任务重点在后端规则和手册，前端可延后。

## 3. 方案设计

### 3.1 成本数据采集
- **采集点**: 在 `agents/agent_loop.py` 的 LLM 调用完成回调中，提取响应中的 `usage` 字段（OpenAI 格式），累计 token 数并转换为费用（参考模型单价）。
- **存储**: 使用 `operation_store` 保存按时间窗口聚合的成本数据，或新增一个 `CostTracker` 类。
- **对齐 SLO 窗口**: 以 `operation_store` 已有的时间序列存储能力为基础，记录每分钟/每小时的费用总量。

### 3.2 成本 SLO 定义与告警规则
定义如下 SLO 指标：
- **SLO-1**: 每小时 token 消耗不超过预算上限（如 100 万 token）。
- **SLO-2**: 滚动 24 小时成本增幅不超过 50% 对比前一天同时段。
- **告警触发**: 在 `event_bus` 上发布 `cost.budget_exceeded` 事件，携带当前窗口���据。
- **告警规则实现**: 新增模块 `agents/cost_monitor.py`，定期（通过 `asyncio` 任务）检查 `operation_store` 中的成本累计值，根据规则判断是否越界，并发布事件。

### 3.3 成本异常的应急回滚 Runbook 与自动化
**回滚操作手册内容**：  
1. 确认异常：查看成本仪表板（可后端 API 提供 `/ops/cost/current`）。  
2. 识别源头：通过 `event_bus` 事件标记的 `agent_loop` 上下文，定位引发大量 token 消耗的任务/讨论。  
3. 执行回滚：  
   - 手动调用 `/ops/rollback` 接口，回滚最近一次更改。  
   - 或自动触发：当成本连续两个 SLO 窗口超限时，自动停止相关 `EvolutionExecutor` 中的任务并回滚。

**自动化回滚接口**：
在 `agents/operation_api.py` 中新增：
- `POST /ops/cost-rollback`：接收参数（如 `item_id`），查找对应演化项，若其状态为 `IN_PROGRESS` 或 `DISPATCHED`，将其状态回退到 `DRAFT` 并取消关联任务，同时记录审计日志。

## 4. 需要修改的文件清单（基于项目上下文已存在的路径）

| 文件路径 | 修改类型 | 说明 |
|----------|----------|------|
| `src/backend/agents/agent_loop.py` | 修改 | 添加 token 用量采集，在每次 LLM 调用结束时发布 `token.usage` 事件 |
| `src/backend/agents/event_bus.py` | 修改 | 定义新事件类型：`token.usage`, `cost.budget_exceeded`, `cost.rollback.triggered` |
| `src/backend/agents/operation_store.py` | 修改 | 增加成本时间序列存储方法（`record_cost_entry`） |
| `src/backend/agents/operation_models.py` | 修改 | 新增成本数据模型 `CostRecord`，回滚请求/响应模型 |
| `src/backend/agents/operation_api.py` | 修改 | 新增成本查询端点 `GET /ops/cost/current`、`GET /ops/cost/history`；新增回滚端点 `POST /ops/cost-rollback` |
| `src/backend/channels/system_evolution.py` (假设存在) | 修改 | 在 `EvolutionItem` 状态机中新增 `ROLLED_BACK` 状态，支持从 `IN_PROGRESS`/`DISPATCHED` 回退 |
| `src/backend/agents/api.py` | 修改 | 在任务提交或演化派发时注入成本标签，确保回滚时可回溯 |
| `src/backend/tests/test_token_budget.py` | 修改/新增内容 | 补充成本异常检测与回滚的集成测试 |
| `src/backend/tests/test_operation_store.py` | 修改 | 添加成本记录存储的单元测试 |
| `src/backend/tests/test_event_bus.py` (可能新增) | 新增 | 验证成本事件发布与订阅 |

**新增文件**（推荐）：
- `src/backend/agents/cost_monitor.py`：实现定时成本检查逻辑、SLO 评估、告警触发。
- `src/backend/agents/cost_rollback.py`：回滚编排逻辑，与 system_evolution 交互。

## 5. 具体修改点示例（引用现有代码）

### 5.1 在 `agent_loop.py` 中记录 token 使用
*由于未提供 `agent_loop.py` 内容，以下为基于常见设计模式的伪代码说明，实际需参照真实代码行号。*

假设 `agent_loop.py` 中有 `async def run_loop(...)`，在调用 `LLM.chat()` 之后，解析返回的 `response.usage`：
```python
# 伪代码，位置约在 LLM 调用完成后
usage = response.get("usage", {})
total_tokens = usage.get("total_tokens", 0)
# 发布事件
from agents.event_bus import event_bus
event_bus.publish("token.usage", {
    "timestamp": time.time(),
    "agent_id": agent_id,
    "task_id": task_id,
    "tokens": total_tokens,
})
```
然后将成本累计写入 `operation_store`。

### 5.2 在 `event_bus.py` 中注册新事件类型
文件列表中存在 `event_bus.py`，需在其中声明事件常量。修改位置在模块顶部。
```python
COST_BUDGET_EXCEEDED = "cost.budget_exceeded"
TOKEN_USAGE = "token.usage"
COST_ROLLBACK_TRIGGERED = "cost.rollback.triggered"
```

### 5.3 在 `operation_models.py` 中定义模型
`operation_models.py` 已存在，可在文件末尾追加：
```python
class CostRecord(BaseModel):
    timestamp: float
    tokens: int
    estimated_cost: float  # 美元
    source_task_id: Optional[str] = None
    source_team_id: Optional[str] = None
```

### 5.4 在 `operation_api.py` 中添加回滚端点
文件存在，需新增路由。例如：
```python
@router.post("/cost-rollback")
async def cost_rollback(request: CostRollbackRequest):
    # 调用 cost_rollback 模块执行回滚
    result = await cost_rollback_service.rollback(request.task_id)
    return {"status": "rollback_initiated", "detail": result}
```

## 6. 可行性评估

- **技术基础**：现有项目已具备事件总线、运维存储、演化状态机，能够快速扩展成本采集和回滚逻辑。
- **耦合度**：回滚操作依赖 `system_evolution` 模块，需确认该模块支持状态回退并记录审计日志。测试 `test_evolution_race.py` 显示演化项状态管理较健全，回滚不破坏现有并发控制。
- **风险**：成本采集如果放在主 agent 循环中，应注意性能开销（仅发布事件，开销极低）。告警与回滚应异步执行，避免阻塞主流程。
- **测试保证**：扩展现有测试框架（`test_token_budget.py` 和 `test_operation_store.py`），通过模拟 token 消耗和告警条件，验证告警发布与回滚行为。

## 7. 推荐实施步骤

1. **实现成本追踪**：修改 `agent_loop.py` 和 `operation_store.py`，完成 token 使用量记录。
2. **定义 SLO 与告警**：新建 `cost_monitor.py`，利用 `operation_store` 数据进行周期性检查，通过 `event_bus` 发送告警。
3. **实现回滚接口**：在 `operation_api.py` 和 `system_evolution` 中添加成本异常回滚能力，编写 `cost_rollback.py` 编排。
4. **编写 Runbook 文档**：基于自动化接口产出操作手册，明确手动触发步骤和自动策略。
5. **测试与验证**：补全 `test_token_budget.py`，编写集成测试覆盖成本异常产生到回滚的全流程。

## 8. 结论

将成本异常纳入 SLO 监控并建立回滚机制在现有架构上是可行的，仅需在已有模块上进行少量扩展并新增一个监控模块。通过事件总线解耦，可让成本数据被独立监控系统订阅，同时保留业务逻辑清晰。应急回滚借助现有的演化状态机可实现安全回退，满足值班团队在成本告警时的快速响应需求。

**下一步**：依据本调研报告，由 developer 角色进行具体编码实现。

────────────────────────────────────────────────────────────
✅ deepseek-v4-pro 完成
