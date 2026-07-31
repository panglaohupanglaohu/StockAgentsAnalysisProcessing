# 架构设计 — architect

任务: 在CI/CD流水线中集成Redis版本校验和并发写入自动化测试，配置Prometheus监控指标（EXEC NIL频率、版本冲突率）
步骤: architecture
Agent: build_architect

---

📋 任务: 1ebf4f3a-24b
🤖 Agent: Architect (architect)
📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
🔧 执行方式: DeepSeek API (直连)
⏱️ 超时: 1200s
────────────────────────────────────────────────────────────
📝 提示词:
  你是 AgentsGroup2026 系统的 Architect (architect)。
  请执行以下开发任务:
  
  你是系统架构师。请为以下任务设计技术方案:
  
  ## 任务
  在CI/CD流水线中集成Redis版本校验和并发写入自动化测试，配置Prometheus监控指标（EXEC NIL频率、版本冲突率）
  负责角色: Deployer, Test Engineer
  依赖: 任务1, 2
  预期产出: 自动化测试用例及监控Dashboard
  负责角色: Deployer, Test Engineer
  依赖: 任务1, 2
  预期产出: 自动化测试用例及监控Dashboard
  
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
  ... (共 1196 个 src/ 文件)
  
  ```
  
  ### 文件: `src/frontend/__tests__/cost-dashboard.test.js`
  ```js
  import { readFileSync } from 'node:fs';
  import path from 'node:path';
  import vm from 'node:vm';
  import { describe, expect, it, vi } from 'vitest';
  
  function read(relPath) {
    return readFileSync(path.join(process.cwd(), relPath), 'utf8');
  }
  
  function makeElement(initial = {}) {
    return {
      innerHTML: '',
      textContent: '',
      value: '',
      disabled: false,
      style: {},
      className: '',
      classList: {
        values: new Set(),
        add(name) { this.values.add(name); },
        remove(name) { this.values.delete(name); },
        contains(name) { return this.values.has(name); },
      },
      addEventListener() {},
      setAttribute() {},
      removeAttribute() {},
      ...initial,
    };
  }
  
  function buildContext(requestImpl) {
    const elements = Object.create(null);
    const defaults = {
      'filter-aggregation': { value: 'service' },
      'filter-window': { value: '24h' },
      'filter-environment': { value: '' },
      'filter-service': { value: '' },
      'cost-action-team': { value: 'cloud_ops' },
    };
    const document = {
      hidden: false,
      readyState: 'complete',
      getElementById(id) {
        if (!elements[id]) elements[id] = makeElement(defaults[id] || {});
        return elements[id];
      },
      createElement() {
        return makeElement();
      },
      addEventListener() {},
    };
  
    const window = {
      __AG_COST_DASHBOARD_NO_INIT__: true,
      AG: {
        escapeHtml(value) {
          return String(value ?? '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
        },
      },
      api: {
        request: requestImpl,
        getLastRequestId: () => 'req-cost-1',
      },
    };
  
    const context = vm.createContext({
      window,
      document,
      URLSearchParams,
      encodeURIComponent,
      setInterval: vi.fn(),
      fetch: vi.fn(),
      console,
    });
    vm.runInContext(read('src/frontend/js/cost-dashboard.js'), context);
    return { context, elements };
  }
  
  function sampleSummary() {
    return {
      summary: {
        total_cost: 42.5,
        pod_count: 2,
        container_count: 2,
        service_count: 1,
        environment_count: 1,
        team_count: 1,
        by_team: [{ value: 'cloud', total_cost: 42.5 }],
      },
    };
  }
  
  describe('cost governance dashboard', () => {
    it('normalizes backend trend lists and renders total_cost points', () => {
      const { context, elements } = buildContext(vi.fn());
      const trends = context.window.CostDashboard.normalizeTrends([{
        dimension: 'service',
        value: 'checkout',
        total: 22.5,
        points: [
          { timestamp: '2026-06-05T08:00:00Z', total_cost: 10 },
          { timestamp: '2026-06-05T09:00:00Z', total_cost: 12.5 },
        ],
      }]);
  
      context.window.CostDashboard.renderTrends(trends);
  
      expect(elements['trends-chart'].innerHTML).toContain('$10.00');
      expect(elements['trends-chart'].innerHTML).toContain('$12.50');
      expect(elements['trends-chart'].innerHTML).toContain('checkout');
    });
  
    it('normalizes pod labels from /cost/pods and renders the pod table', () => {
      const { context, elements } = buildContext(vi.fn());
      const pods = context.window.CostDashboard.normalizePods([{
        pod: 'checkout-7d9',
        namespace: 'prod',
        cpu_cost: 3,
        ram_cost: 2,
        network_cost: 1,
        total_cost: 6,
        labels: { service: 'checkout', environment: 'production', team: 'cloud-ops' },
      }]);
  
      context.window.CostDashboard.renderPodsTable(pods);
  
      expect(elements['pods-tbody'].innerHTML).toContain('checkout-7d9');
      expect(elements['pods-tbody'].innerHTML).toContain('checkout');
      expect(elements['pods-tbody'].innerHTML).toContain('cloud-ops');
      expect(elements['pods-tbody'].innerHTML).toContain('创建任务');
      expect(elements['pods-tbody'].innerHTML).toContain('标签补丁');
    });
  
    it('refreshes summary, trends, pods, teams, and governance state through the shared API client', async () => {
      const request = vi.fn(async (url) => {
        if (url === '/api/v1/cost/health') return { status: 'ok', data_age_seconds: 12 };
        if (url === '/api/v1/cost-gate/health') return { status: 'healthy' };
        if (url === '/api/v1/cost-gate/stats') return { passed: 1, warned: 2, blocked: 3 };
        if (url.startsWith('/api/v1/cost/summary?')) return sampleSummary();
        if (url.startsWith('/api/v1/cost/by-service?')) return [{ dimension: 'service', value: 'checkout', total_cost: 42.5 }];
        if (url.startsWith('/api/v1/cost/trends?')) {
          return [{
            dimension: 'service',
            value: 'checkout',
            total: 42.5,
            points: [{ timestamp: '2026-06-05T08:00:00Z', total_cost: 42.5 }],
          }];
        }
        if (url.startsWith('/api/v1/cost/pods?')) {
          return [{
            pod: 'checkout-7d9',
            namespace: 'prod',
            total_cost: 42.5,
            labels: { service: 'checkout', environment: 'production', team: 'cloud-ops' },
          }];
        }
        if (url === '/api/v1/agent-config/teams?limit=200&offset=0') {
          return { items: [{ team_id: 'cloud_ops', name: '公有云运维团队' }] };
        }
        return null;
      });
      const { context, elements } = buildContext(request);
  
      await context.window.CostDashboard.refreshDashboard();
  
      expect(request.mock.calls.some(([url]) => url.startsWith('/api/v1/cost/pods?'))).toBe(true);
      expect(elements['summary-grid'].innerHTML).toContain('$42.50');
      expect(elements['trends-chart'].innerHTML).toContain('$42.50');
      expect(elements['pods-tbody'].innerHTML).toContain('checkout-7d9');
      expect(elements['governance-panel'].innerHTML).toContain('创建优化任务');
      expect(elements['governance-panel'].innerHTML).toContain('创建 Plaza 话题');
    });
  
    it('creates a real agent task from a cost anomaly target', async () => {
      const request = vi.fn(async (url, opts) => {
        if (url === '/api/v1/agent-config/teams/cloud_ops/tasks') {
          expect(opts.method).toBe('POST');
          const body = JSON.parse(opts.body);
          expect(body.title).toContain('成本优化');
          expect(body.metadata.source).toBe('cost-dashboard');
          expect(body.metadata.cost_target.value).toBe('checkout');
          return { task_id: 'task-cost-1' };
        }
        return null;
      });
      const { context, elements } = buildContext(request);
      context.window.CostDashboard.state.breakdown = [{ dimension: 'service', value: 'checkout', total_cost: 42.5 }];
  
      const created = await context.window.CostDashboard.createOptimizationTask('breakdown', 0);
  
      expect(created.task_id).toBe('task-cost-1');
      expect(elements['cost-action-result'].textContent).toContain('task-cost-1');
    });
  
    it('generates a label injection patch for a selected pod', async () => {
      const request = vi.fn(async (url, opts) => {
        if (url.startsWith('/api/v1/cost/labels/generate?')) {
          expect(opts.method).toBe('POST');
          expect(url).toContain('pod_name=checkout-7d9');
          expect(url).toContain('service=checkout');
          return { patch: [{ op: 'add', path: '/metadata/labels/service', value: 'checkout' }] };
        }
        return null;
      });
      const { context, elements } = buildContext(request);
      context.window.CostDashboard.state.pods = [{
        pod: 'checkout-7d9',
        namespace: 'prod',
        service: 'checkout',
        environment: 'production',
        team: 'cloud-ops',
        total_cost: 42.5,
        labels: {},
      }];
  
      const patch = await context.window.CostDashboard.generateLabelPatch('pod', 0);
  
      expect(patch.patch[0].value).toBe('checkout');
      expect(elements['cost-action-result'].innerHTML).toContain('service');
    });
  
    it('creates a Plaza discussion from the selected cost target', async () => {
      const request = vi.fn(async (url, opts) => {
        if (url === '/api/v1/agent-config/plaza?limit=50&offset=0') {
          return { items: [{ id: 'plaza-cost', name: '成本治理议事厅' }] };
        }
        if (url === '/api/v1/agent-config/plaza/plaza-cost/discussions') {
          expect(opts.method).toBe('POST');
          const body = JSON.parse(opts.body);
          expect(body.topic).toContain('成本治理');
          expect(body.description).toContain('cost-dashboard');
          expect(body.goal).toContain('成本优化任务');
          return { id: 'disc-cost-1', topic: body.topic };
        }
        return null;
      });
      const { context, elements } = buildContext(request);
      context.window.CostDashboard.state.breakdown = [{ dimension: 'service', value: 'checkout', total_cost: 42.5 }];
  
      const created = await context.window.CostDashboard.createPlazaTopic('breakdown', 0);
  
      expect(created.discussion.id).toBe('disc-cost-1');
      expect(elements['cost-action-result'].innerHTML).toContain('打开议事厅');
    });
  
    it('shows an actionable request_id error state when cost data is unavailable', async () => {
      const request = vi.fn(async () => null);
      const { context, elements } = buildContext(request);
  
      await context.window.CostDashboard.refreshDashboard();
  
      expect(elements['dashboard-alert'].textContent).toContain('成本接口暂时没有返回可用数据');
      expect(elements['dashboard-alert'].textContent).toContain('请求ID: req-cost-1');
      expect(elements['dashboard-alert'].classList.contains('show')).toBe(true);
      expect(elements['summary-grid'].innerHTML).toContain('暂无成本摘要');
      expect(elements['pods-tbody'].innerHTML).toContain('暂无 Pod 成本明细');
    });
  
    it('runs a Cost Gate self-check and refreshes gate stats', async () => {
      const request = vi.fn(async (url, opts) => {
        if (url === '/api/v1/cost-gate/evaluate') {
          expect(opts.method).toBe('POST');
          const body = JSON.parse(opts.body);
          expect(body.project_id).toBe('cost-dashboard-self-check');
          expect(body.metadata.source).toBe('cost-dashboard');
          return { decision: 'blocked', violations: [{ id: 'gpu-budget' }] };
        }
        if (url === '/api/v1/cost-gate/stats') {
          return { passed: 1, warned: 0, blocked: 1 };
        }
        return null;
      });
      const { context, elements } = buildContext(request);
  
      const report = await context.window.CostDashboard.runCostGateSelfCheck();
  
      expect(report.decision).toBe('blocked');
      expect(elements['cost-action-result'].innerHTML).toContain('Gate 决策');
      expect(elements['cost-action-result'].innerHTML).toContain('blocked');
      expect(elements['governance-panel'].innerHTML).toContain('Gate 统计');
      expect(elements['governance-panel'].innerHTML).toContain('阻断 1');
    });
  });
  
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
  
  ### 文件: `src/backend/tests/test_execution_evidence.py`
  ```py
  """Agent execution EvidenceRun regressions."""
  
  from __future__ import annotations
  
  import pytest
  
  from agents import evidence_store as evidence_store_module
  from agents.evidence_store import EvidenceQuery, EvidenceStore
  from agents.task_engine import AgentTask, TaskEngine
  from agents.tool_executor import ToolExecutor
  
  
  class FakeTaskStore:
      def __init__(self) -> None:
          self.tasks = {}
  
      def load_all(self):
          return {}
  
      def save_task(self, task: AgentTask) -> None:
          self.tasks[task.task_id] = task
  
      def delete_task(self, task_id: str) -> None:
          self.tasks.pop(task_id, None)
  
  
  @pytest.mark.asyncio
  async def test_tool_executor_records_tool_call_evidence(monkeypatch, tmp_path):
      evidence_store = EvidenceStore(str(tmp_path / "evidence_runs"))
      monkeypatch.setattr(evidence_store_module, "_evidence_store", evidence_store)
  
      result = await ToolExecutor().execute(
          "list_directory",
          {"path": str(tmp_path), "request_id": "req-tool"},
          agent_id="agent-001",
      )
  
      assert result.success is True
      runs = await evidence_store.query_evidence(EvidenceQuery(evidence_type="tool_call"))
      assert len(runs) == 1
      assert runs[0].status == "passed"
      assert runs[0].agent_id == "agent-001"
      assert runs[0].request_id == "req-tool"
      assert runs[0].runtime["tool_name"] == "list_directory"
      assert runs[0].command == "list_directory"
  
  
  @pytest.mark.asyncio
  async def test_task_engine_records_completion_evidence(monkeypatch, tmp_path):
      evidence_store = EvidenceStore(str(tmp_path / "evidence_runs"))
      monkeypatch.setattr(evidence_store_module, "_evidence_store", evidence_store)
      engine = TaskEngine(store=FakeTaskStore())
      task = AgentTask(
          task_id="task-001",
          agent_id="agent-001",
          team_id="cloud_ops",
          title="Optimize cloud cost",
          metadata={"request_id": "req-task"},
      )
  
      await engine.submit_task(task)
      await engine.complete_task("task-001", result={"ok": True})
  
      runs = await evidence_store.query_evidence(EvidenceQuery(evidence_type="agent_task"))
      assert len(runs) == 1
      assert runs[0].status == "passed"
      assert runs[0].team_id == "cloud_ops"
      assert runs[0].agent_id == "agent-001"
      assert runs[0].task_id == "task-001"
      assert runs[0].request_id == "req-task"
      assert runs[0].runtime["component"] == "task_engine"
  
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
                  },
              )
              created_tasks.append(task)
              await isolated_task_engine.submit_task(task)
              return task
  
          monkeypatch.setattr(api_module, "_submit_internal_task", fake_submit
  ```
  
  ### 文件: `src/backend/tests/test_plaza_task_artifact_bridge.py`
  ```py
  # -*- coding: utf-8 -*-
  """Plaza task artifact and evolution bridge tests."""
  
  from __future__ import annotations
  
  import json
  from pathlib import Path
  from tempfile import TemporaryDirectory
  
  import pytest
  
  import agent_team_api as agent_team_api_module
  from agents import api as api_module
  from agents import plaza_engine as plaza_engine_module
  from agents import task_engine as task_engine_module
  from agents.task_engine import AgentTask, TaskEngine, TaskStatus
  from agents.task_store import TaskStore
  from channels.system_evolution import EvolutionItem, EvolutionStatus, SystemEvolutionChannel
  
  
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
  
  
  def _build_failed_workflow(artifact_dir: str) -> list:
      return [
          {
              "key": "develop",
              "status": "completed",
              "artifact": f"{artifact_dir}/04_develop/summary.md",
              "_summary": {"files_changed": ["src/backend/main.py"]},
          },
          {
              "key": "test",
              "status": "failed",
              "artifact": f"{artifact_dir}/05_test.md",
              "_summary": {
                  "verdict": "FAIL",
                  "checklist": [{"severity": "FAIL", "detail": "核心回归未通过"}],
              },
          },
      ]
  
  
  @pytest.fixture
  def isolated_task_engine(monkeypatch):
      with TemporaryDirectory() as tmpdir:
          engine = TaskEngine(store=TaskStore(base_dir=Path(tmpdir) / "tasks"))
          monkeypatch.setattr(task_engine_module, "_engine", engine)
          yield engine, tmpdir
  
  
  class TestTaskArtifacts:
      def test_attach_task_execution_artifacts_collects_workflow_outputs(self):
          with TemporaryDirectory() as tmpdir:
              task = AgentTask(
                  task_id="task-artifacts",
                  team_id="team-build",
                  title="汇总执行产物",
                  metadata={
                      "source": "plaza",
                      "pipeline_dir": tmpdir,
                      "workflow": _build_success_workflow(tmpdir),
                  },
              )
  
              artifacts = api_module._attach_task_execution_artifacts(task)
  
              assert artifacts["artifact_dir"] == tmpdir
              assert artifacts["changed_files"] == ["src/backend/main.py"]
              assert artifacts["test_result"]["verdict"] == "PASS"
              assert artifacts["workflow_summary"]["completed_steps"] == ["develop", "test", "deploy"]
              assert task.metadata["execution_artifacts"]["build_outcome"] == "completed"
              assert artifacts["trace_context"]["task_id"] == "task-artifacts"
  
      def test_attach_task_execution_artifacts_includes_patch_preview(self):
          with TemporaryDirectory() as tmpdir:
              repo_root = Path(api_module.__file__).resolve().parents[3]
              rel_path = "storage/test_artifact_diff_preview.txt"
              current_file = repo_root / rel_path
              current_file.parent.mkdir(parents=True, exist_ok=True)
              backup_file = Path(tmpdir) / "before.txt"
              backup_file.write_text("old line\n", encoding="utf-8")
              current_file.write_text("new line\n", encoding="utf-8")
              try:
                  task = AgentTask(
                      task_id="task-diff-preview",
                      team_id="team-build",
                      title="生成 diff 证据",
                      metadata={
                          "source": "plaza",
                          "pipeline_dir": tmpdir,
                          "workflow": [
                              {
                                  "key": "deploy",
                                  "status": "completed",
                                  "deliverable_paths": [rel_path],
                                  "deploy_result": {
                                      "developer": {
                                          "applied": [{"path": rel_path}],
                                          "backup": [{"path": rel_path, "backup": str(backup_file)}],
                                          "skipped": [],
                                          "failed": [],
                                      },
                                      "deployer": {"applied": [], "backup": [], "skipped": [], "failed": []},
                                  },
                              }
                          ],
                      },
                  )
  
                  artifacts = api_module._attach_task_execution_artifacts(task)
  
                  assert rel_path in artifacts["diff_by_file"]
                  assert "-old line" in "\n".join(artifacts["diff_by_file"][rel_path])
                  assert "+new line" in artifacts["patch_preview"]
                  assert task.metadata["patch_preview"] == artifacts["patch_preview"]
              finally:
                  if current_file.exists():
                      current_file.unlink()
  
      def test_attach_task_execution_artifacts_preserves_trace_context(self):
          with TemporaryDirectory() as tmpdir:
              task = AgentTask(
                  task_id="task-trace-context",
                  team_id="team-build",
                  title="追踪上下文",
                  metadata={
                      "source": "plaza",
                      "plaza_id": "plaza-1",
                      "discussion_id": "disc-1",
                      "discussion_topic": "trace me",
                      "plan_revision": 4,
                      "plan_item_index": 1,
                      "evolution_item_ids": ["evo-1", "evo-2"],
                      "trace_context": {"custom": "value"},
                      "pipeline_dir": tmpdir,
                      "workflow": _build_success_workflow(tmpdir),
                  },
              )
  
              artifacts = api_module._attach_task_execution_artifacts(task)
  
              assert artifacts["trace_context"]["task_id"] == "task-trace-context"
              assert artifacts["trace_context"]["discussion_id"] == "disc-1"
              assert artifacts["trace_context"]["evolution_item_ids"] == ["evo-1", "evo-2"]
              assert artifacts["trace_context"]["custom"] == "value"
              trace_file = Path(tmpdir) / "trace_summary.json"
              assert trace_file.exists()
              persisted = json.loads(trace_file.read_text(encoding="utf-8"))
              assert persisted["trace_context"]["task_id"] == "task-trace-context"
              assert persisted["trace_context"]["evolution_item_ids"] == ["evo-1", "evo-2"]
  
  
  class TestPlazaEvolutionSync:
      @pytest.mark.asyncio
      async def test_finalize_completed_plaza_task_auto_closes_evolution_item(
          self,
          isolated_task_engine,
          monkeypatch,
      ):
          engine, tmpdir = isolated_task_engine
          evolution_engine = SystemEvolutionChannel()
          evolution_engine.initialize()
          evolution_engine.evolution_items["evo-1"] = EvolutionItem(
              id="evo-1",
              title="让 Plaza 任务完成后进入验证",
              status=EvolutionStatus.DISPATCHED.value,
              source_task_ids=["task-success"],
              source_discussion_id="disc-1",
          )
          monkeypatch.setattr(agent_team_api_module, "_evolution_engine", evolution_engine)
  
          task = AgentTask(
              task_id="task-success",
              team_id="team-build",
              title="成功任务",
              metadata={
                  "source": "plaza",
                  "discussion_id": "disc-1",
                  "pipeline_dir": tmpdir,
                  "workflow": _build_success_workflow(tmpdir),
              },
          )
          await engine.submit_task(task)
  
          finalized = await api_module._finalize_task_terminal_state(task)
  
          assert finalized is not None
          assert finalized.status == TaskStatus.COMPLETED
          assert finalized.metadata["changed_files"] == ["src/backend/main.py"]
          assert finalized.result["test_result"]["verdict"] == "PASS"
  
          item = evolution_engine.evolution_items["evo-1"]
          assert item.status == EvolutionStatus.CLOSED.value
          assert item.code_changes == ["src/backend/main.py"]
          assert item.artifact_dir == tmpdir
          assert item.build_artifacts["build_outcome"] == "completed"
          assert item.verify_result == "passed"
          assert item.closed_at is not None
  
      @pytest.mark.asyncio
      async def test_finalize_completed_task_keeps_explicit_verify_pending(
          self,
          isolated_task_engine,
          monkeypatch,
      ):
          engine, tmpdir = isolated_task_engine
          evolution_engine = SystemEvolutionChannel()
          evolution_engine.initialize()
          broadcast_events = []
  
          class FakePlazaEngine:
              def get_discussion(self, plaza_id, discussion_id):
                  if plaza_id == "plaza-verify" and discussion_id == "disc-verify":
                      return object()
                  return None
  
              async def _broadcast(self, discussion_id, event):
                  broadcast_events.append((discussion_id, event))
  
          monkeypatch.setattr(plaza_engine_module, "get_plaza_engine", lambda: FakePlazaEngine())
          evolution_engine.evolution_items["evo-verify"] = EvolutionItem(
              id="evo-verify",
              title="需要显式验证",
              status=EvolutionStatus.DISPATCHED.value,
              verify_test_name="manual-check",
              source_plaza_id="plaza-verify",
              source_task_ids=["task-verify"],
              source_discussion_id="disc-verify",
          )
          monkeypatch.setattr(agent_team_api_module, "_evolution_engine", evolution_engine)
  
          task = AgentTask(
              task_id="task-verify",
              team_id="team-build",
              title="成功但待验证",
              metadata={
                  "source": "plaza",
                  "plaza_id": "plaza-verify",
                  "discussion_id": "disc-verify",
                  "pipeline_dir": tmpdir,
                  "workflow": _build_success_workflow(tmpdir),
              },
          )
          await engine.submit_task(task)
  
          finalized = await api_module._finalize_task_terminal_state(task)
  
          assert finalized is not None
          item = evolution_engine.evolution_items["evo-verify"]
          assert item.status == EvolutionStatus.VERIFY_PENDING.value
          assert item.verify_result == "pending"
          assert item.verify_d
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose
  任务: 在CI/CD流水线中集成Redis版本校验和并发写入自动化测试，配置Prometheus监控指标（EXEC NIL频率、版本冲突率）
  步骤: pm_decompose
  📋 任务: 1ebf4f3a-24b
  🤖 Agent: PM (project_manager)
  📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
  🔧 执行方式: DeepSeek API (直连)
  ────────────────────────────────────────────────────────────
  你是 AgentsGroup2026 系统的 PM (project_manager)。
  你是项目经理 (PM)。请对以下任务进行分解和规划:
  在CI/CD流水线中集成Redis版本校验和并发写入自动化测试，配置Prometheus监控指标（EXEC NIL频率、版本冲突率）
  负责角色: Deployer, Test Engineer
  预期产出: 自动化测试用例及监控Dashboard
  负责角色: Deployer, Test Engineer
  预期产出: 自动化测试用例及监控Dashboard
  ## 📂 项目上下文 (系统自动预加载)
  
  ### 步骤 02: research (完整产出)
  
  # 研究分析 — researcher
  
  任务: 在CI/CD流水线中集成Redis版本校验和并发写入自动化测试，配置Prometheus监控指标（EXEC NIL频率、版本冲突率）
  步骤: research
  Agent: build_researcher
  
  ---
  
  📋 任务: 1ebf4f3a-24b
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
    在CI/CD流水线中集成Redis版本校验和并发写入自动化测试，配置Prometheus监控指标（EXEC NIL频率、版本冲突率）
    负责角色: Deployer, Test Engineer
    依赖: 任务1, 2
    预期产出: 自动化测试用例及监控Dashboard
    负责角色: Deployer, Test Engineer
    依赖: 任务1, 2
    预期产出: 自动化测试用例及监控Dashboard
    
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
    ... (共 1196 个 src/ 文件)
    
    ```
    
    ### 文件: `src/frontend/__tests__/cost-dashboard.test.js`
    ```js
    import { readFileSync } from 'node:fs';
    import path from 'node:path';
    import vm from 'node:vm';
    import { describe, expect, it, vi } from 'vitest';
    
    function read(relPath) {
      return readFileSync(path.join(process.cwd(), relPath), 'utf8');
    }
    
    function makeElement(initial = {}) {
      return {
        innerHTML: '',
        textContent: '',
        value: '',
        disabled: false,
        style: {},
        className: '',
        classList: {
          values: new Set(),
          add(name) { this.values.add(name); },
          remove(name) { this.values.delete(name); },
          contains(name) { return this.values.has(name); },
        },
        addEventListener() {},
        setAttribute() {},
        removeAttribute() {},
        ...initial,
      };
    }
    
    function buildContext(requestImpl) {
      const elements = Object.create(null);
      const defaults = {
        'filter-aggregation': { value: 'service' },
        'filter-window': { value: '24h' },
        'filter-environment': { value: '' },
        'filter-service': { value: '' },
        'cost-action-team': { value: 'cloud_ops' },
      };
      const document = {
        hidden: false,
        readyState: 'complete',
        getElementById(id) {
          if (!elements[id]) elements[id] = makeElement(defaults[id] || {});
          return elements[id];
        },
        createElement() {
          return makeElement();
        },
        addEventListener() {},
      };
    
      const window = {
        __AG_COST_DASHBOARD_NO_INIT__: true,
        AG: {
          escapeHtml(value) {
            return String(value ?? '')
              .replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&#39;');
          },
        },
        api: {
          request: requestImpl,
          getLastRequestId: () => 'req-cost-1',
        },
      };
    
      const context = vm.createContext({
        window,
        document,
        URLSearchParams,
        encodeURIComponent,
        setInterval: vi.fn(),
        fetch: vi.fn(),
        console,
      });
      vm.runInContext(read('src/frontend/js/cost-dashboard.js'), context);
      return { context, elements };
    }
    
    function sampleSummary() {
      return {
        summary: {
          total_cost: 42.5,
          pod_count: 2,
          container_count: 2,
          service_count: 1,
          environment_count: 1,
          team_count: 1,
          by_team: [{ value: 'cloud', total_cost: 42.5 }],
        },
      };
    }
    
    describe('cost governance dashboard', () => {
      it('normalizes backend trend lists and renders total_cost points', () => {
        const { context, elements } = buildContext(vi.fn());
        const trends = context.window.CostDashboard.normalizeTrends([{
          dimension: 'service',
          value: 'checkout',
          total: 22.5,
          points: [
            { timestamp: '2026-06-05T08:00:00Z', total_cost: 10 },
            { timestamp: '2026-06-05T09:00:00Z', total_cost: 12.5 },
          ],
        }]);
    
        context.window.CostDashboard.renderTrends(trends);
    
        expect(elements['trends-chart'].innerHTML).toContain('$10.00');
        expect(elements['trends-chart'].innerHTML).toContain('$12.50');
        expect(elements['trends-chart'].innerHTML).toContain('checkout');
      });
    
      it('normalizes pod labels from /cost/pods and renders the pod table', () => {
        const { context, elements } = buildContext(vi.fn());
        const pods = context.window.CostDashboard.normalizePods([{
          pod: 'checkout-7d9',
          namespace: 'prod',
          cpu_cost: 3,
          ram_cost: 2,
          network_cost: 1,
          total_cost: 6,
          labels: { service: 'checkout', environment: 'production', team: 'cloud-ops' },
        }]);
    
        context.window.CostDashboard.renderPodsTable(pods);
    
        expect(elements['pods-tbody'].innerHTML).toContain('checkout-7d9');
        expect(elements['pods-tbody'].innerHTML).toContain('checkout');
        expect(elements['pods-tbody'].innerHTML).toContain('cloud-ops');
        expect(elements['pods-tbody'].innerHTML).toContain('创建任务');
        expect(elements['pods-tbody'].innerHTML).toContain('标签补丁');
      });
    
      it('refreshes summary, trends, pods, teams, and governance state through the shared API client', async () => {
        const request = vi.fn(async (url) => {
          if (url === '/api/v1/cost/health') return { status: 'ok', data_age_seconds: 12 };
          if (url === '/api/v1/cost-gate/health') return { status: 'healthy' };
          if (url === '/api/v1/cost-gate/stats') return { passed: 1, warned: 2, blocked: 3 };
          if (url.startsWith('/api/v1/cost/summary?')) return sampleSummary();
          if (url.startsWith('/api/v1/cost/by-service?')) return [{ dimension: 'service', value: 'checkout', total_cost: 42.5 }];
          if (url.startsWith('/api/v1/cost/trends?')) {
            return [{
              dimension: 'service',
              value: 'checkout',
              total: 42.5,
              points: [{ timestamp: '2026-06-05T08:00:00Z', total_cost: 42.5 }],
            }];
          }
          if (url.startsWith('/api/v1/cost/pods?')) {
            return [{
              pod: 'checkout-7d9',
              namespace: 'prod',
              total_cost: 42.5,
              labels: { service: 'checkout', environment: 'production', team: 'cloud-ops' },
            }];
          }
          if (url === '/api/v1/agent-config/teams?limit=200&offset=0') {
            return { items: [{ team_id: 'cloud_ops', name: '公有云运维团队' }] };
          }
          return null;
        });
        const { context, elements } = buildContext(request);
    
        await context.window.CostDashboard.refreshDashboard();
    
        expect(request.mock.calls.some(([url]) => url.startsWith('/api/v1/cost/pods?'))).toBe(true);
        expect(elements['summary-grid'].innerHTML).toContain('$42.50');
        expect(elements['trends-chart'].innerHTML).toContain('$42.50');
        expect(elements['pods-tbody'].innerHTML).toContain('checkout-7d9');
        expect(elements['governance-panel'].innerHTML).toContain('创建优化任务');
        expect(elements['governance-panel'].innerHTML).toContain('创建 Plaza 话题');
      });
    
      it('creates a real agent task from a cost anomaly target', async () => {
        const request = vi.fn(async (url, opts) => {
          if (url === '/api/v1/agent-config/teams/cloud_ops/tasks') {
            expect(opts.method).toBe('POST');
            const body = JSON.parse(opts.body);
            expect(body.title).toContain('成本优化');
            expect(body.metadata.source).toBe('cost-dashboard');
            expect(body.metadata.cost_target.value).toBe('checkout');
            return { task_id: 'task-cost-1' };
          }
          return null;
        });
        const { context, elements } = buildContext(request);
        context.window.CostDashboard.state.breakdown = [{ dimension: 'service', value: 'checkout', total_cost: 42.5 }];
    
        const created = await context.window.CostDashboard.createOptimizationTask('breakdown', 0);
    
        expect(created.task_id).toBe('task-cost-1');
        expect(elements['cost-action-result'].textContent).toContain('task-cost-1');
      });
    
      it('generates a label injection patch for a selected pod', async () => {
        const request = vi.fn(async (url, opts) => {
          if (url.startsWith('/api/v1/cost/labels/generate?')) {
            expect(opts.method).toBe('POST');
            expect(url).toContain('pod_name=checkout-7d9');
            expect(url).toContain('service=checkout');
            return { patch: [{ op: 'add', path: '/metadata/labels/service', value: 'checkout' }] };
          }
          return null;
        });
        const { context, elements } = buildContext(request);
        context.window.CostDashboard.state.pods = [{
          pod: 'checkout-7d9',
          namespace: 'prod',
          service: 'checkout',
          environment: 'production',
          team: 'cloud-ops',
          total_cost: 42.5,
          labels: {},
        }];
    
        const patch = await context.window.CostDashboard.generateLabelPatch('pod', 0);
    
        expect(patch.patch[0].value).toBe('checkout');
        expect(elements['cost-action-result'].innerHTML).toContain('service');
      });
    
      it('creates a Plaza discussion from the selected cost target', async () => {
        const request = vi.fn(async (url, opts) => {
          if (url === '/api/v1/agent-config/plaza?limit=50&offset=0') {
            return { items: [{ id: 'plaza-cost', name: '成本治理议事厅' }] };
          }
          if (url === '/api/v1/agent-config/plaza/plaza-cost/discussions') {
            expect(opts.method).toBe('POST');
            const body = JSON.parse(opts.body);
            expect(body.topic).toContain('成本治理');
            expect(body.description).toContain('cost-dashboard');
            expect(body.goal).toContain('成本优化任务');
            return { id: 'disc-cost-1', topic: body.topic };
          }
          return null;
        });
        const { context, elements } = buildContext(request);
        context.window.CostDashboard.state.breakdown = [{ dimension: 'service', value: 'checkout', total_cost: 42.5 }];
    
        const created = await context.window.CostDashboard.createPlazaTopic('breakdown', 0);
    
        expect(created.discussion.id).toBe('disc-cost-1');
        expect(elements['cost-action-result'].innerHTML).toContain('打开议事厅');
      });
    
      it('shows an actionable request_id error state when cost data is unavailable', async () => {
        const request = vi.fn(async () => null);
        const { context, elements } = buildContext(request);
    
        await context.window.CostDashboard.refreshDashboard();
    
        expect(elements['dashboard-alert'].textContent).toContain('成本接口暂时没有返回可用数据');
        expect(elements['dashboard-alert'].textContent).toContain('请求ID: req-cost-1');
        expect(elements['dashboard-alert'].classList.contains('show')).toBe(true);
        expect(elements['summary-grid'].innerHTML).toContain('暂无成本摘要');
        expect(elements['pods-tbody'].innerHTML).toContain('暂无 Pod 成本明细');
      });
    
      it('runs a Cost Gate self-check and refreshes gate stats', async () => {
        const request = vi.fn(async (url, opts) => {
          if (url === '/api/v1/cost-gate/evaluate') {
            expect(opts.method).toBe('POST');
            const body = JSON.parse(opts.body);
            expect(body.project_id).toBe('cost-dashboard-self-check');
            expect(body.metadata.source).toBe('cost-dashboard');
            return { decision: 'blocked', violations: [{ id: 'gpu-budget' }] };
          }
          if (url === '/api/v1/cost-gate/stats') {
            return { passed: 1, warned: 0, blocked: 1 };
          }
          return null;
        });
        const { context, elements } = buildContext(request);
    
        const report = await context.window.CostDashboard.runCostGateSelfCheck();
    
        expect(report.decision).toBe('blocked');
        expect(elements['cost-action-result'].innerHTML).toContain('Gate 决策');
        expect(elements['cost-action-result'].innerHTML).toContain('blocked');
        expect(elements['governance-panel'].innerHTML).toContain('Gate 统计');
        expect(elements['governance-panel'].innerHTML).toContain('阻断 1');
      });
    });
    
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
    
    ### 文件: `src/backend/tests/test_execution_evidence.py`
    ```py
    """Agent execution EvidenceRun regressions."""
    
    from __future__ import annotations
    
    import pytest
    
    from agents import evidence_store as evidence_store_module
    from agents.evidence_store import EvidenceQuery, EvidenceStore
    from agents.task_engine import AgentTask, TaskEngine
    from agents.tool_executor import ToolExecutor
    
    
    class FakeTaskStore:
        def __init__(self) -> None:
            self.tasks = {}
    
        def load_all(self):
            return {}
    
        def save_task(self, task: AgentTask) -> None:
            self.tasks[task.task_id] = task
    
        def delete_task(self, task_id: str) -> None:
            self.tasks.pop(task_id, None)
    
    
    @pytest.mark.asyncio
    async def test_tool_executor_records_tool_call_evidence(monkeypatch, tmp_path):
        evidence_store = EvidenceStore(str(tmp_path / "evidence_runs"))
        monkeypatch.setattr(evidence_store_module, "_evidence_store", evidence_store)
    
        result = await ToolExecutor().execute(
            "list_directory",
            {"path": str(tmp_path), "request_id": "req-tool"},
            agent_id="agent-001",
        )
    
        assert result.success is True
        runs = await evidence_store.query_evidence(EvidenceQuery(evidence_type="tool_call"))
        assert len(runs) == 1
        assert runs[0].status == "passed"
        assert runs[0].agent_id == "agent-001"
        assert runs[0].request_id == "req-tool"
        assert runs[0].runtime["tool_name"] == "list_directory"
        assert runs[0].command == "list_directory"
    
    
    @pytest.mark.asyncio
    async def test_task_engine_records_completion_evidence(monkeypatch, tmp_path):
        evidence_store = EvidenceStore(str(tmp_path / "evidence_runs"))
        monkeypatch.setattr(evidence_store_module, "_evidence_store", evidence_store)
        engine = TaskEngine(store=FakeTaskStore())
        task = AgentTask(
            task_id="task-001",
            agent_id="agent-001",
            team_id="cloud_ops",
            title="Optimize cloud cost",
            metadata={"request_id": "req-task"},
        )
    
        await engine.submit_task(task)
        await engine.complete_task("task-001", result={"ok": True})
    
        runs = await evidence_store.query_evidence(EvidenceQuery(evidence_type="agent_task"))
        assert len(runs) == 1
        assert runs[0].status == "passed"
        assert runs[0].team_id == "cloud_ops"
        assert runs[0].agent_id == "agent-001"
        assert runs[0].task_id == "task-001"
        assert runs[0].request_id == "req-task"
        assert runs[0].runtime["component"] == "task_engine"
    
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
                de
  ...(截断)
  
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
