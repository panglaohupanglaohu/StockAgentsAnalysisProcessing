# PM分解 — project_manager

任务: 配置 CloudWatch/OpenSearch 指标门禁与故障处理演练
步骤: pm_decompose
Agent: build_pm

---

📋 任务: 0f0c655c-6a2
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
  配置 CloudWatch/OpenSearch 指标门禁与故障处理演练
  负责角色: 巡检监控员
  依赖: 任务2
  预期产出: 告警规则、验收指标、故障演练报告
  负责角色: 巡检监控员
  依赖: 任务2
  预期产出: 告警规则、验收指标、故障演练报告
  
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
  src/backend/tests/test_eco_drill_v2.py
  ... (共 1951 个 src/ 文件)
  
  ```
  
  ### 文件: `src/frontend/agent-team-config.html`
  ```html
  <!DOCTYPE html>
  <html lang="zh-CN">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://ga.jspm.io https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; connect-src 'self' http://127.0.0.1:* ws://127.0.0.1:*; img-src 'self' data:;">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgentsGroup2026 — 智能体团队管理</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/theme.css">
    <link rel="stylesheet" href="/css/components.css">
    <link rel="stylesheet" href="/css/ws-theme-bridge.css">
    <link rel="stylesheet" href="/css/agent-team-config.css">
    <link rel="stylesheet" href="/css/topbar-ws.css">
  <style>:root{--ag-font-sans:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","Noto Sans SC","Segoe UI",sans-serif;--ag-font-mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}body{font-family:var(--ag-font-sans)}code,pre,kbd{font-family:var(--ag-font-mono)}</style>
  </head>
  <body>
  <a href="#main-content" class="skip-link">跳转到主内容</a>
  <div class="app">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="sb-header"><h2><span class="seal">智</span> AgentsGroup</h2><select class="fi" id="team-select" style="font-size:12px;padding:6px 8px"></select></div>
      <div class="sb-nav" role="list">
        <a class="active" aria-current="page" data-view="overview" onclick="switchView('overview')"><span class="seal">览</span> <span data-i18n="nav.dashboard">仪表盘</span></a>
        <a data-view="models" onclick="switchView('models')"><span class="seal">腦</span> <span data-i18n="nav.models">模型与连接</span></a>
        <a data-view="tools" onclick="switchView('tools')"><span class="seal seal-koke">具</span> <span data-i18n="nav.tools">工具</span></a>
        <a data-view="skills" onclick="switchView('skills')"><span class="seal seal-kitsune">能</span> <span data-i18n="nav.skills">技能</span></a>
        <a data-view="tasks" onclick="switchView('tasks')"><span class="seal">务</span> <span data-i18n="nav.tasks">任务</span></a>
        <a data-view="sessions" onclick="switchView('sessions')"><span class="seal">存</span> <span data-i18n="nav.sessions">会话存档</span></a>
        <a data-view="runtime" onclick="switchView('runtime')"><span class="seal">波</span> <span data-i18n="nav.runtime">运行时</span></a>
        <a data-view="registry" onclick="switchView('registry')"><span class="seal">厂</span> <span data-i18n="nav.token-factory">Token 工厂</span></a>
      </div>
      <div class="sb-section">团队成员</div>
      <div class="sb-agents" id="sb-agents"></div>
      <div class="sb-footer"><button class="btn btn-pink btn-sm" onclick="openWizard()" style="width:100%;justify-content:center">＋ 新建智能体</button></div>
    </div>
    <!-- Main -->
    <div class="main" id="main-content">
      <div class="topbar-ws">
        <div class="topbar-ws__left">
          <h1 id="main-title">团队概览</h1>
          <span class="badge" id="main-badge" style="background:rgba(152,245,167,0.15);color:var(--lime)"></span>
        </div>
        <nav class="topbar-ws__nav" aria-label="主导航">
          <span class="cur">智能体团队</span>
          <a href="/plaza.html">议事广场</a>
          <a href="/skill-extract.html">技能萃取/赋予</a>
          <a href="/Agent-digital-twin.html">数字孪生</a>
          <a href="/cost-dashboard.html">演进式成本优化</a><a href="/pet-config.html">🐾 仿生生态</a>
        </nav>
        <div class="topbar-ws__right">
          <button class="btn btn-sm" onclick="openModal('modal-create-team')">＋ 创建团队</button>
          <button class="btn btn-sm btn-ghost" onclick="deleteTeam()" style="color:var(--red)">🗑 删除团队</button>
          <div class="topbar-ws__user">
            <span class="topbar-ws__user-avatar" id="topbar-avatar">U</span>
            <span class="topbar-ws__user-name" id="topbar-user">guest</span>
            <button class="topbar-ws__logout-btn" onclick="window._agLogout && window._agLogout()">登出</button>
          </div>
        </div>
      </div>
      <!-- Views -->
      <div id="view-overview" class="main-inner"><div class="main-scroll"><div class="card-grid" id="ov-stats"></div><div class="section" id="ov-team-section"><div class="section-title" id="ov-team-title"></div><table class="tbl"><thead><tr><th>Agent</th><th>角色</th><th>状态</th><th>技能</th><th>操作</th></tr></thead><tbody id="ov-team-agents"></tbody></table></div>
  <!-- 演进状态摘要 -->
  <div class="section" id="evo-section"><div class="section-title" style="display:flex;justify-content:space-between;align-items:center"><span>演进状态</span><a href="/system-evolution.html" class="btn btn-sm">→ 系统演进</a></div><div id="evo-compliance" class="card-grid"></div></div>
  <div class="section" id="budget-section"><div class="section-title" style="display:flex;justify-content:space-between;align-items:center"><span>预算与告警</span><div style="display:flex;gap:8px;align-items:center"><select class="fi" id="budget-trend-days" onchange="refreshBudgetPanel()" style="width:auto;padding:5px 8px;font-size:12px"><option value="7">最近 7 天</option><option value="30">最近 30 天</option></select><button class="btn btn-sm" onclick="refreshBudgetPanel()">刷新</button></div></div><div id="budget-summary" class="card-grid"></div><div id="budget-trend"></div><div id="budget-alerts"></div></div>
  <div class="section" id="trace-section"><div class="section-title" style="display:flex;justify-content:space-between;align-items:center"><span>最近运行痕迹</span><div style="display:flex;gap:8px;align-items:center"><select class="fi" id="trace-source-filter" onchange="refreshTracePanel()" style="width:auto;padding:5px 8px;font-size:12px"><option value="">全部来源</option><option value="plaza">Plaza</option><option value="evolution">Evolution</option></select><select class="fi" id="trace-event-filter" onchange="refreshTracePanel()" style="width:auto;padding:5px 8px;font-size:12px"><option value="">全部事件</option><option value="plan_start">plan_start</option><option value="tool_result">tool_result</option><option value="pipeline_started">pipeline_started</option><option value="pipeline_completed">pipeline_completed</option><option value="pipeline_failed">pipeline_failed</option><option value="verification_state_broadcasted">verification_state_broadcasted</option></select><a id="trace-export-link" href="#" target="_blank" rel="noopener" class="btn btn-sm">导出 NDJSON</a><button class="btn btn-sm" onclick="refreshTracePanel()">刷新</button></div></div><div id="trace-summaries"></div><div id="trace-events"></div><div id="trace-detail"></div></div>
  </div></div>
      <div id="view-models" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🧠 模型与连接</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('llm')">🔌 LLM / TTS</button><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-model')">＋ 添加模型</button></div></div><div id="global-model-banner" style="margin-bottom:14px;padding:10px 14px;background:rgba(38,162,105,0.06);border:1px solid var(--line);border-radius:8px;font-size:13px"></div><table class="tbl"><thead><tr><th>ID</th><th>名称</th><th>提供商</th><th>Max Tokens</th><th>温度</th><th>默认</th><th>操作</th></tr></thead><tbody id="models-tb"></tbody></table></div></div>
      <div id="view-tools" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🔧 可用工具</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('registry')">🏭 Token 工厂</button><button class="btn btn-sm" onclick="showToolSearch()">🔍 搜索</button></div></div><div id="tools-search-bar" class="hidden" style="margin-bottom:12px"><div style="display:flex;gap:10px"><input class="fi" id="tools-search-input" placeholder="搜索工具..." oninput="filterToolCards(this.value)" style="flex:1"><button class="btn btn-sm" onclick="el('tools-search-bar').classList.add('hidden')">✕</button></div></div><div id="tools-cards"></div></div></div>
      <div id="view-skills" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">⚡ 可用技能</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="exportSkillsMD()">📤 导出</button></div></div><div id="skills-cards"></div></div></div>
      <div id="view-tasks" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">📋 并发任务</div><div style="display:flex;gap:8px"><span id="task-stats" style="font-size:12px;color:var(--muted);display:flex;align-items:center"></span><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-task')">＋ 提交任务</button><button class="btn btn-sm" onclick="openModal('modal-batch-task')">📦 批量提交</button><button class="btn btn-sm btn-ghost" onclick="cancelAllTasks()" title="取消全部运行中的任务">🧹 清理</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>标题</th><th>Agent</th><th>优先级</th><th>依赖</th><th>状态</th><th>操作</th></tr></thead><tbody id="tasks-tb"></tbody></table></div></div>
      <div id="view-llm" class="main-inner hidden"><div class="main-scroll">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div style="display:flex;align-items:center;gap:12px"><button class="btn btn-sm" onclick="switchView('models')">← 返回</button><div class="section-title" style="margin:0">🔌 LLM / TTS 配置</div></div><button class="btn btn-pink btn-sm" onclick="testLLM()">🧪 测试连接</button></div>
        <div id="llm-status-card" class="card" style="margin-bottom:20px;padding:20px"><p style="color:var(--dim)">加载中...</p></div>
        <div class="card" style="padding:20px;margin-bottom:20px">
          <div class="section-title" style="margin-top:0;margin-bottom:12px">⚙️ 配置 LLM 提供商</div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
            <div class="form-group"><label class="form-label">提供商</label><select class="fi" id="llm-provider"><option value="codebuddy">CodeBuddy</option><option value="deepseek">DeepSeek</option><option value="openai">OpenAI</option><option value="anthropic">Anthropic</option><option value="local">本地 (Ollama/vLLM)</option><option value="openrouter">OpenRouter</option><option value="github">GitHub Models</option><option value="qwen">通义千问</option></select></div>
            <div class="form-group"><label class="form-label">模型</label><input class="fi" id="llm-model" placeholder="deepseek-v4-pro"></div>
            <div class="form-group"><label class="form-label">API Key</label><input class="fi" id="llm-key" type="password" placeholder="sk-..."></div>
            <div class="form-group"><label class="form-label">API Base URL (可选)</label><input class="fi" id="llm-url" placeholder="https://api.deepseek.com"></div>
            <div class="form-group"><label class="form-label">Max Tokens</label><input class="fi" id="llm-tokens" type="number" value="4096" min="100" max="128000"></div>
            <div class="form-group"><label class="form-label">温度</label><input class="fi" id="llm-temp" type="number" value="0.7" min="0" max="2" step="0.1"></div>
          </div>
          <div style="margin-top:16px;display:flex;gap:10px"><button class="btn btn-pink" onclick="saveLLMConfig()">💾 保存配置</button><button class="btn" onclick="loadLLMStatus()">🔄 刷新状态</button></div>
        </div>
        <div id="llm-test-result" class="card hidden" style="padding:20px"><div class="section-title" style="margin-top:0;margin-bottom:8px">🧪 测试结果</div><div id="llm-test-content"></div></div>
        <!-- TTS Config Section -->
        <div class="card" style="padding:20px;margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><div class="section-title" style="margin-top:0;margin-bottom:0">🔊 TTS 语音合成配置</div><div style="display:flex;gap:8px"><span id="tts-status-badge" class="badge" style="font-size:11px">检测中...</span><button class="btn btn-sm" onclick="testTTSConnection()">🧪 测试</button><button class="btn btn-pink btn-sm" onclick="startTTSService()">▶ 启动服务</button></div></div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
            <div class="form-group"><label class="form-label">TTS 引擎</label><select class="fi" id="tts-engine"><option value="gpt-sovits">GPT-SoVITS</option><option value="edge-tts">Edge TTS (在线)</option><option value="web-speech">浏览器内置</option></select></div>
            <div class="form-group"><label class="form-label">API 地址</label><input class="fi" id="tts-api-url" placeholder="http://127.0.0.1:9880"></div>
            <div class="form-group"><label class="form-label">参考音频路径</label><input class="fi" id="tts-ref-audio" placeholder="ref_audio/male_sample.wav"></div>
            <div class="form-group"><label class="form-label">参考音频文本</label><input class="fi" id="tts-prompt-text" placeholder="参考音频对应的文字内容"></div>
            <div class="form-group"><label class="form-label">语言</label><select class="fi" id="tts-lang"><option value="zh">中文</option><option value="en">English</option><option value="ja">日本語</option><option value="auto">自动</option></select></div>
            <div class="form-group"><label class="form-label">语速</label><input class="fi" id="tts-speed" type="number" value="1.0" min="0.5" max="2.0" step="0.1"></div>
          </div>
          <div style="margin-top:16px;display:flex;gap:10px"><button class="btn btn-pink" onclick="saveTTSConfig()">💾 保存 TTS 配置</button><button class="btn" onclick="loadTTSConfig()">🔄 刷新</button></div>
          <div id="tts-test-result" style="margin-top:12px;font-size:12px;color:var(--dim)"></div>
        </div>
        <div class="card" style="padding:20px"><div class="section-title" style="margin-top:0;margin-bottom:8px">📊 会话列表</div><div id="llm-sessions"></div></div>
      </div></div>
      <div id="view-agent" class="main-inner hidden">
      <!-- Session Persistence View -->
      <div id="view-sessions" class="main-inner hidden"><div class="main-scroll">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">💾 会话存档管理</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="loadPersistedSessions()">🔄 刷新</button></div></div>
        <div class="card" style="margin-bottom:20px;padding:20px">
          <div class="section-title" style="margin-top:0;margin-bottom:12px">🔍 跨会话搜索</div>
          <div style="display:flex;gap:10px"><input class="fi" id="ss-query" placeholder="搜索所有持久化会话的内容..."
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
          ev
  ```
  
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
⚠️ DeepSeek 凭据未找到，回退到 Claude CLI...

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
⏳ 等待 DeepSeek 响应... (180s)
API Error: Unable to connect to API (ConnectionRefused)


⚠️ Claude Code 退出码: 1
