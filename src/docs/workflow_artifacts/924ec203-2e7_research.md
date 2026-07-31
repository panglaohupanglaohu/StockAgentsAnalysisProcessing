# 研究分析 — researcher

任务: 执行代码 review、单步变更和彩排回滚
步骤: research
Agent: build_researcher

---

📋 任务: 924ec203-2e7
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
  执行代码 review、单步变更和彩排回滚
  负责角色: 运维操作员
  依赖: 任务2
  预期产出: 审核记录、执行日志、回滚验证结果
  负责角色: 运维操作员
  依赖: 任务2
  预期产出: 审核记录、执行日志、回滚验证结果
  
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
  src/frontend/js/global-nav.js.bak
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
  ... (共 1569 个 src/ 文件)
  
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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;700&family=Noto+Serif:wght@200;300;400;600;900&family=Noto+Serif+SC:wght@200;300;400;600;900&family=Noto+Sans+SC:wght@300;400;500;700&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/theme.css">
    <link rel="stylesheet" href="/css/components.css">
    <link rel="stylesheet" href="/css/ws-theme-bridge.css">
    <link rel="stylesheet" href="/css/agent-team-config.css">
    <link rel="stylesheet" href="/css/topbar-ws.css">
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
          <a href="/system-evolution.html">系统演进</a>
          <a href="/cost-dashboard.html">成本监控</a>
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
      <div id="view-models" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🧠 模型与连接</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('llm')">🔌 LLM / TTS</button><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-model')">＋ 添加模型</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>名称</th><th>提供商</th><th>Max Tokens</th><th>温度</th><th>默认</th><th>操作</th></tr></thead><tbody id="models-tb"></tbody></table></div></div>
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
          <div style="display:flex;gap:10px"><input class="fi" id="ss-query" placeholder="搜索所有持久化会话的内容..." style="flex:1" onkeydown="if(event.key==='Enter
  ```
  
  ### 文件: `src/frontend/sandbox-twin.html`
  ```html
  <!DOCTYPE html>
  <html lang="zh-CN">
  <head>
  <meta charset="UTF-8">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://ga.jspm.io https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; connect-src 'self' http://127.0.0.1:* ws://127.0.0.1:*; img-src 'self' data:;">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SECS 协同沙箱 — 在孪生环境里演练 Agent 协作</title>
  <script type="importmap">
  {
    "imports": {
      "three": "https://cdn.jsdelivr.net/npm/three@0.174.0/build/three.module.js",
      "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.174.0/examples/jsm/"
    }
  }
  </script>
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/theme.css">
    <link rel="stylesheet" href="/css/components.css">
    <link rel="stylesheet" href="/css/topbar-ws.css">
    <link rel="stylesheet" href="/css/sandbox-twin.css">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600&family=Noto+Sans+SC:wght@300;400;500;600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  </head>
  <body>
  
  <!-- ══════════════════════════════════════════════════════════════
       ① 演练导航 Nav (顶栏 + 跨域分组)
       ══════════════════════════════════════════════════════════════ -->
  <header class="topbar-ws">
    <div class="topbar-ws__left">
      <h1>🏖️ SECS 演练总台</h1>
      <span class="subject-badge">在孪生环境里演练 Agent 协作</span>
    </div>
    <nav class="topbar-ws__nav nav-grouped" aria-label="主导航">
      <div class="nav-group">
        <span class="nav-group__label">演练</span>
        <span class="cur">沙箱</span>
        <a href="/Agent-digital-twin.html">孪生</a>
      </div>
      <div class="nav-group">
        <span class="nav-group__label">资产</span>
        <a href="/agent-team-config.html">智能体</a>
        <a href="/skill-extract.html">技能</a>
        <a href="/plaza.html">广场</a>
      </div>
      <div class="nav-group">
        <span class="nav-group__label">观测</span>
        <a href="/system-evolution.html">演进</a>
        <a href="/cost-dashboard.html">成本</a>
      </div>
    </nav>
    <div class="topbar-ws__right">
      <span class="refresh-indicator" id="refresh-indicator" title="每 30s 自动刷新">⏱ 自动刷新</span>
      <button class="btn btn-sm" onclick="loadStats()">↻</button>
      <div class="topbar-ws__user">
        <span class="topbar-ws__user-avatar" id="topbar-avatar">U</span>
        <span class="topbar-ws__user-name" id="topbar-user">guest</span>
        <button class="topbar-ws__logout-btn" onclick="window._agLogout && window._agLogout()">登出</button>
      </div>
    </div>
  </header>
  
  <!-- ══════════════════════════════════════════════════════════════
       ② KPI 状态条 (4 个 mini-stat: 沙箱 / 总步 / SOP / 最优)
       ══════════════════════════════════════════════════════════════ -->
  <section class="kpi-bar">
    <div class="kpi-bar__cell">
      <span class="kpi-bar__label">沙箱会话</span>
      <span class="kpi-bar__value" id="kpi-sessions">0</span>
    </div>
    <div class="kpi-bar__cell">
      <span class="kpi-bar__label">总仿真步</span>
      <span class="kpi-bar__value" id="kpi-steps">0</span>
    </div>
    <div class="kpi-bar__cell">
      <span class="kpi-bar__label">提取 SOP</span>
      <span class="kpi-bar__value" id="kpi-sops">0</span>
    </div>
    <div class="kpi-bar__cell">
      <span class="kpi-bar__label">最优评分</span>
      <span class="kpi-bar__value" id="kpi-score">—</span>
    </div>
    <div class="kpi-bar__cell kpi-bar__cell--wide">
      <span class="kpi-bar__label">运行时</span>
      <span class="kpi-bar__sub">
        <span class="runtime-dot" id="kpi-runtime-dot">○</span>
        <span id="kpi-runtime-text">加载中</span>
        <button class="btn btn-sm" onclick="loadRuntimeStatus()">刷新</button>
        <button class="btn btn-sm btn-primary" onclick="runRuntimeSelfCheck()">自检</button>
      </span>
    </div>
  </section>
  
  <!-- ══════════════════════════════════════════════════════════════
       🧭 用户引导横幅（首次访问 · 可关闭）
       ══════════════════════════════════════════════════════════════ -->
  <section class="guide-banner" id="guide-banner">
    <div class="guide-banner__content">
      <div class="guide-banner__icon">🧪</div>
      <div class="guide-banner__text">
        <strong>SECS 协同沙箱演练总台</strong>
        <span>选团队 → 选场景 → 开始演练：Lite 模式下无需 Docker / LLM 即可运行仿真，内置规则引擎驱动 5 角色 Agent 协作。</span>
      </div>
      <div class="guide-banner__actions">
        <button class="btn btn-secondary btn-sm" onclick="openTeamSelector()" id="btn-team-select">👥 团队选择</button>
        <button class="btn btn-secondary btn-sm" onclick="openSceneSelector()" id="btn-scene-select">🏟️ 场景选择</button>
        <button class="btn btn-primary btn-sm" onclick="startExercise()" id="btn-start-exercise">▶ 开始演练</button>
        <button class="guide-banner__dismiss" onclick="dismissGuideBanner()" title="不再显示">✕</button>
      </div>
    </div>
    <!-- 已选标签 -->
    <div class="guide-banner__tags" id="guide-tags" style="display:none">
      <span class="guide-banner__tag" id="tag-team">未选团队</span>
      <span class="guide-banner__tag" id="tag-scene">未选场景</span>
    </div>
  </section>
  
  <!-- ══════════════════════════════════════════════════════════════
       👥 团队选择 Modal
       ══════════════════════════════════════════════════════════════ -->
  <div class="overlay" id="team-overlay" style="display:none">
    <div class="modal-select" id="team-modal">
      <div class="modal-select__header">
        <h3>👥 选择演练团队</h3>
        <button class="modal-select__close" onclick="closeTeamSelector()">✕</button>
      </div>
      <div class="modal-select__body">
        <div class="modal-select__loading" id="team-loading">加载团队列表…</div>
        <div class="modal-select__list" id="team-list"></div>
      </div>
      <div class="modal-select__members" id="team-members" style="display:none">
        <div class="modal-select__members-title">选择参演成员</div>
        <div class="modal-select__members-grid" id="team-members-grid"></div>
      </div>
      <div class="modal-select__footer">
        <span class="modal-select__hint" id="team-hint">请先选择一个团队</span>
        <button class="btn btn-primary btn-sm" onclick="confirmTeamSelection()">✓ 确认选择</button>
      </div>
    </div>
  </div>
  
  <!-- ══════════════════════════════════════════════════════════════
       🏟️ 场景选择 Modal
       ══════════════════════════════════════════════════════════════ -->
  <div class="overlay" id="scene-overlay" style="display:none">
    <div class="modal-select" id="scene-modal">
      <div class="modal-select__header">
        <h3>🏟️ 选择演练场景</h3>
        <button class="modal-select__close" onclick="closeSceneSelector()">✕</button>
      </div>
      <div class="modal-select__body">
        <div class="modal-select__loading" id="scene-loading">加载孪生场景…</div>
        <div class="modal-select__list" id="scene-list"></div>
      </div>
      <div class="modal-select__footer">
        <span class="modal-select__hint" id="scene-hint">从数字孪生的 3D 环境空间中选择演练场地</span>
        <button class="btn btn-primary btn-sm" onclick="confirmSceneSelection()">✓ 确认选择</button>
      </div>
    </div>
  </div>
  
  <!-- ══════════════════════════════════════════════════════════════
       ③ 四层流水线 Pipeline (L1→L2→L3→L4 + 回流箭头 L4→L2)
       ══════════════════════════════════════════════════════════════ -->
  <section class="pipeline-bar" id="pipeline-bar">
    <div class="pipeline-node" data-layer="L1" id="pipe-L1">
      <div class="pipeline-node__num">L1</div>
      <div class="pipeline-node__name">🌐 MADTwin</div>
      <div class="pipeline-node__sub">环境语义</div>
      <div class="pipeline-node__status" id="pipe-status-L1">●</div>
    </div>
    <div class="pipeline-arrow"></div>
    <div class="pipeline-node" data-layer="L2" id="pipe-L2">
      <div class="pipeline-node__num">L2</div>
      <div class="pipeline-node__name">📋 AAS</div>
      <div class="pipeline-node__sub">协作 SOP</div>
      <div class="pipeline-node__status" id="pipe-status-L2">●</div>
    </div>
    <div class="pipeline-arrow"></div>
    <div class="pipeline-node pipeline-node--active" data-layer="L3" id="pipe-L3">
      <div class="pipeline-node__num">L3</div>
      <div class="pipeline-node__name">🎮 TwinLoop</div>
      <div class="pipeline-node__sub">仿真演练</div>
      <div class="pipeline-node__status" id="pipe-status-L3">●</div>
    </div>
    <div class="pipeline-arrow"></div>
    <div class="pipeline-node" data-layer="L4" id="pipe-L4">
      <div class="pipeline-node__num">L4</div>
      <div class="pipeline-node__name">🎯 MADCG</div>
      <div class="pipeline-node__sub">全局评价</div>
      <div class="pipeline-node__status" id="pipe-status-L4">●</div>
    </div>
    <div class="pipeline-arrow pipeline-arrow--return" title="L4 评价回流到 L2 SOP 库">
      <span class="pipeline-arrow__label">回流进化</span>
    </div>
    <div class="pipeline-node pipeline-node--return" data-layer="EVOLVE" id="pipe-EVOLVE">
      <div class="pipeline-node__name">🌀 SECS Loop</div>
      <div class="pipeline-node__sub">沉淀→再演练</div>
    </div>
  </section>
  
  <!-- ══════════════════════════════════════════════════════════════
       ④ 沙箱 ID (主区) — I/O 镜像
       ══════════════════════════════════════════════════════════════ -->
  <section class="session-bar" id="session-bar">
    <div class="session-bar__id">
      <span class="session-bar__label">沙箱 ID</span>
      <code class="session-bar__code" id="session-id-display">— 尚未启动 —</code>
      <button class="btn btn-sm session-bar__copy" id="session-bar__copy" onclick="copySessionId()" title="复制完整 session id">📋</button>
    </div>
    <div class="session-bar__meta" id="session-bar__meta">
      <span>mode · <strong id="session-mode">—</strong></span>
      <span>步数 · <strong id="session-step">0</strong></span>
      <span>评分 · <strong id="session-score">—</strong></span>
      <span>状态 · <strong id="session-status">空闲</strong></span>
    </div>
    <div class="session-bar__actions">
      <button class="btn btn-sm" onclick="loadSessionDetail()" id="btn-refresh-session">↻ 概要详情</button>
    </div>
  </section>
  
  <!-- Session 详情弹出层 -->
  <div class="session-detail-modal" id="session-detail-modal" style="display:none" onclick="if(event.target===this) closeSessionDetail()">
    <div class="session-detail-modal__inner" id="session-detail-modal__inner">
      <div class="session-detail-modal__header">
        <span>📋 Session 概要详情</span>
        <button class="btn btn-sm" onclick="closeSessionDetail()">✕</button>
      </div>
      <div class="session-detail-modal__body" id="session-detail-modal__body">
        <div class="io-empty">点击「↻ 概要详情」加载</div>
      </div>
    </div>
  </div>
  
  <main class="io-grid">
    <!-- ④.1 Input · 沙箱进料 -->
    <div class="io-panel io-panel--input">
      <div class="io-panel__header">
        <span class="io-panel__title">📥 Input · 沙箱进料</span>
        <span class="io-panel__hint">你喂进去什么</span>
      </div>
      <div class="io-tabs" id="input-tabs">
        <button class="io-tab io-tab--active" data-tab="task">任务</button>
        <button class="io-tab" data-tab="env">环境</button>
        <button class="io-tab" data-tab="seed">种子技能</button>
        <button class="io-tab" data-tab="params">运行参数</button>
      </div>
      <div class="io-tab-content" id="input-content-task">
        <div class="io-empty">启动仿真后此处显示具体任务描述</div>
      </div>
      <div class="io-tab-content" id="input-content-env" style="display:none">
        <div class="io-empty">数字孪生环境的初始 Agent 集合与状态</div>
      </div>
      <div class="io-tab-content" id="input-content-seed" style="display:none">
        <div style="margin-bottom:8px;display:flex;gap:6px;flex-wrap:wrap;align-items:center">
          <input type="text" id="skill-inject-team" placeholder="team_id (默认 public)" style="background:var(--bg);color:var(--text);border:1px solid var(--border);padding:5px 8px;border-radius:5px;font-size:11px;width:140px">
          <button class="btn btn-sm" onclick="loadSkillCatalog()">↻ 加载技能库</button>
          <select id="skill-inject-select" style="background:var(--bg);color:var(--text);border:1px solid var(--border);padding:5px 8px;border-radius:5px;font-size:11px;flex:1;min-width:160px">
            <option value="">-- 先加载 --</option>
          </select>
        </div>
        <div id="skill-inject-panel" class="skill-grid">
          <div class="io-empty">点击「加载技能库」后此处显示可注入的技能卡片</div>
        </div>
        <div id="skill-inject-result" style="margin-top:8px;font-size:11px;color:var(--muted);font-family:var(--font-mono)"></div>
      </div>
      <div class="io-tab-content" id="input-content-params" style="display:none">
        <div class="param-row"><label>仿真模式</label>
          <select id="sim-mode">
            <option value="what_if">What-if 单场景</option>
            <option value="parallel">并行多策略</option>
            <option value="evolutionary" selected>演化搜索</option>
          </select></div>
        <div class="param-row"><label>最大步数</label><input type="number" id="sim-steps" value="50" min="10" max="500"></div>
        <div class="param-row"><label>加速倍率</label><input type="number" id="sim-speed" value="10" min="1" max="100"></div>
        <div class="param-row"><label>并行分支</label><input type="number" id="sim-branches" value="3" min="1" max="10"></div>
      </div>
      <div class="io-panel__action">
        <button class="btn btn-primary" onclick="createAndRun()" id="btn-launch" style="flex:1">▶ 启动仿真</button>
        <button class="btn btn-stop" id="btn-stop" onclick="stopSimulation()" style="display:none;flex:1">⏹ 停止</button>
        <button class="btn btn-danger" id="btn-inject" onclick="injectStrategy()" disabled style="flex:1">💉 注入</button>
      </div>
      <div id="sim-status" class="io-status"></div>
    </div>
  
    <!-- ④.1.5 3D 演练场景 · 具像化 Agent 协作 -->
    <div class="io-panel io-panel--scene" id="scene-3d-panel">
      <div class="io-panel__header">
        <span class="io-panel__title">🎮 3D 演练场景</span>
        <span class="io-panel__hint" id="scene-3d-label">演练场</span>
      </div>
      <div class="scene-3d-container" id="scene-3d-container">
        <canvas id="scene-3d-canvas"></canvas>
        <div class="scene-3d-info" id="scene-3d-info">初始化中…</div>
        <div class="scene-3d-controls">
          <button class="btn btn-sm" onclick="sw3dTopView()" title="俯视图">⬆</button>
          <button class="btn btn-sm" onclick="sw3dFrontView()" title="前视图">⬛</button>
          <button class="btn btn-sm" onclick="sw3dResetView()" title="重置视角">🔄</button>
        </div>
      </div>
    </div>
  
    <!-- ④.2 Output · 沙箱出料 -->
    <div class="io-panel io-panel--output">
      <div class="io-panel__header">
        <span class="io-panel__title">📤 Output · 沙箱出料</span>
        <span class="io-panel__hint">它跑出什么</span>
      </div>
      <div class="io-tabs" id="output-tabs">
        <button class="io-tab io-tab--active" data-tab="reward">收益曲线</button>
        <button class="io-tab" data-tab="log">执行日志</button>
        <button class="io-tab" data-tab="sop">提取 SOP</button>
        <button class="io-tab" data-tab="critic">评分/建议</button>
      </div>
      <div class="io-tab-content" id="output-content-reward">
        <div class="reward-meta">
          <span class="reward-meta__k">步数 <strong id="step-counter">0</strong></span>
          <span class="reward-meta__k">最大收益 <strong id="reward-max">—</strong></span>
          <span class="reward-meta__k">趋势 <strong id="r
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
          assert broadcast_events[-1][1]["status_counts"][Evolution
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose (完整产出)
  
  # PM分解 — project_manager
  
  任务: 执行代码 review、单步变更和彩排回滚
  步骤: pm_decompose
  Agent: build_pm
  
  ---
  
  📋 任务: 924ec203-2e7
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
    执行代码 review、单步变更和彩排回滚
    负责角色: 运维操作员
    依赖: 任务2
    预期产出: 审核记录、执行日志、回滚验证结果
    负责角色: 运维操作员
    依赖: 任务2
    预期产出: 审核记录、执行日志、回滚验证结果
    
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
    src/frontend/js/global-nav.js.bak
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
    ... (共 1569 个 src/ 文件)
    
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
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;700&family=Noto+Serif:wght@200;300;400;600;900&family=Noto+Serif+SC:wght@200;300;400;600;900&family=Noto+Sans+SC:wght@300;400;500;700&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="/css/base.css">
      <link rel="stylesheet" href="/css/theme.css">
      <link rel="stylesheet" href="/css/components.css">
      <link rel="stylesheet" href="/css/ws-theme-bridge.css">
      <link rel="stylesheet" href="/css/agent-team-config.css">
      <link rel="stylesheet" href="/css/topbar-ws.css">
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
            <a href="/system-evolution.html">系统演进</a>
            <a href="/cost-dashboard.html">成本监控</a>
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
        <div id="view-models" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🧠 模型与连接</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('llm')">🔌 LLM / TTS</button><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-model')">＋ 添加模型</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>名称</th><th>提供商</th><th>Max Tokens</th><th>温度</th><th>默认</th><th>操作</th></tr></thead><tbody id="models-tb"></tbody></table></div></div>
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
            <div style="display:flex;gap:10px"><input class="fi" id="ss-query" placeholder="搜索所有持久化会话的内容..." style="flex:1" onkeydown="if(event.key==='Enter
    ```
    
    ### 文件: `src/frontend/sandbox-twin.html`
    ```html
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
    <meta charset="UTF-8">
      <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://ga.jspm.io https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; connect-src 'self' http://127.0.0.1:* ws://127.0.0.1:*; img-src 'self' data:;">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SECS 协同沙箱 — 在孪生环境里演练 Agent 协作</title>
    <script type="importmap">
    {
      "imports": {
        "three": "https://cdn.jsdelivr.net/npm/three@0.174.0/build/three.module.js",
        "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.174.0/examples/jsm/"
      }
    }
    </script>
      <link rel="stylesheet" href="/css/base.css">
      <link rel="stylesheet" href="/css/theme.css">
      <link rel="stylesheet" href="/css/components.css">
      <link rel="stylesheet" href="/css/topbar-ws.css">
      <link rel="stylesheet" href="/css/sandbox-twin.css">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600&family=Noto+Sans+SC:wght@300;400;500;600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    </head>
    <body>
    
    <!-- ══════════════════════════════════════════════════════════════
         ① 演练导航 Nav (顶栏 + 跨域分组)
         ══════════════════════════════════════════════════════════════ -->
    <header class="topbar-ws">
      <div class="topbar-ws__left">
        <h1>🏖️ SECS 演练总台</h1>
        <span class="subject-badge">在孪生环境里演练 Agent 协作</span>
      </div>
      <nav class="topbar-ws__nav nav-grouped" aria-label="主导航">
        <div class="nav-group">
          <span class="nav-group__label">演练</span>
          <span class="cur">沙箱</span>
          <a href="/Agent-digital-twin.html">孪生</a>
        </div>
        <div class="nav-group">
          <span class="nav-group__label">资产</span>
          <a href="/agent-team-config.html">智能体</a>
          <a href="/skill-extract.html">技能</a>
          <a href="/plaza.html">广场</a>
        </div>
        <div class="nav-group">
          <span class="nav-group__label">观测</span>
          <a href="/system-evolution.html">演进</a>
          <a href="/cost-dashboard.html">成本</a>
        </div>
      </nav>
      <div class="topbar-ws__right">
        <span class="refresh-indicator" id="refresh-indicator" title="每 30s 自动刷新">⏱ 自动刷新</span>
        <button class="btn btn-sm" onclick="loadStats()">↻</button>
        <div class="topbar-ws__user">
          <span class="topbar-ws__user-avatar" id="topbar-avatar">U</span>
          <span class="topbar-ws__user-name" id="topbar-user">guest</span>
          <button class="topbar-ws__logout-btn" onclick="window._agLogout && window._agLogout()">登出</button>
        </div>
      </div>
    </header>
    
    <!-- ══════════════════════════════════════════════════════════════
         ② KPI 状态条 (4 个 mini-stat: 沙箱 / 总步 / SOP / 最优)
         ══════════════════════════════════════════════════════════════ -->
    <section class="kpi-bar">
      <div class="kpi-bar__cell">
        <span class="kpi-bar__label">沙箱会话</span>
        <span class="kpi-bar__value" id="kpi-sessions">0</span>
      </div>
      <div class="kpi-bar__cell">
        <span class="kpi-bar__label">总仿真步</span>
        <span class="kpi-bar__value" id="kpi-steps">0</span>
      </div>
      <div class="kpi-bar__cell">
        <span class="kpi-bar__label">提取 SOP</span>
        <span class="kpi-bar__value" id="kpi-sops">0</span>
      </div>
      <div class="kpi-bar__cell">
        <span class="kpi-bar__label">最优评分</span>
        <span class="kpi-bar__value" id="kpi-score">—</span>
      </div>
      <div class="kpi-bar__cell kpi-bar__cell--wide">
        <span class="kpi-bar__label">运行时</span>
        <span class="kpi-bar__sub">
          <span class="runtime-dot" id="kpi-runtime-dot">○</span>
          <span id="kpi-runtime-text">加载中</span>
          <button class="btn btn-sm" onclick="loadRuntimeStatus()">刷新</button>
          <button class="btn btn-sm btn-primary" onclick="runRuntimeSelfCheck()">自检</button>
        </span>
      </div>
    </section>
    
    <!-- ══════════════════════════════════════════════════════════════
         🧭 用户引导横幅（首次访问 · 可关闭）
         ══════════════════════════════════════════════════════════════ -->
    <section class="guide-banner" id="guide-banner">
      <div class="guide-banner__content">
        <div class="guide-banner__icon">🧪</div>
        <div class="guide-banner__text">
          <strong>SECS 协同沙箱演练总台</strong>
          <span>选团队 → 选场景 → 开始演练：Lite 模式下无需 Docker / LLM 即可运行仿真，内置规则引擎驱动 5 角色 Agent 协作。</span>
        </div>
        <div class="guide-banner__actions">
          <button class="btn btn-secondary btn-sm" onclick="openTeamSelector()" id="btn-team-select">👥 团队选择</button>
          <button class="btn btn-secondary btn-sm" onclick="openSceneSelector()" id="btn-scene-select">🏟️ 场景选择</button>
          <button class="btn btn-primary btn-sm" onclick="startExercise()" id="btn-start-exercise">▶ 开始演练</button>
          <button class="guide-banner__dismiss" onclick="dismissGuideBanner()" title="不再显示">✕</button>
        </div>
      </div>
      <!-- 已选标签 -->
      <div class="guide-banner__tags" id="guide-tags" style="display:none">
        <span class="guide-banner__tag" id="tag-team">未选团队</span>
        <span class="guide-banner__tag" id="tag-scene">未选场景</span>
      </div>
    </section>
    
    <!-- ══════════════════════════════════════════════════════════════
         👥 团队选择 Modal
         ══════════════════════════════════════════════════════════════ -->
    <div class="overlay" id="team-overlay" style="display:none">
      <div class="modal-select" id="team-modal">
        <div class="modal-select__header">
          <h3>👥 选择演练团队</h3>
          <button class="modal-select__close" onclick="closeTeamSelector()">✕</button>
        </div>
        <div class="modal-select__body">
          <div class="modal-select__loading" id="team-loading">加载团队列表…</div>
          <div class="modal-select__list" id="team-list"></div>
        </div>
        <div class="modal-select__members" id="team-members" style="display:none">
          <div class="modal-select__members-title">选择参演成员</div>
          <div class="modal-select__members-grid" id="team-members-grid"></div>
        </div>
        <div class="modal-select__footer">
          <span class="modal-select__hint" id="team-hint">请先选择一个团队</span>
          <button class="btn btn-primary btn-sm" onclick="confirmTeamSelection()">✓ 确认选择</button>
        </div>
      </div>
    </div>
    
    <!-- ══════════════════════════════════════════════════════════════
         🏟️ 场景选择 Modal
         ══════════════════════════════════════════════════════════════ -->
    <div class="overlay" id="scene-overlay" style="display:none">
      <div class="modal-select" id="scene-modal">
        <div class="modal-select__header">
          <h3>🏟️ 选择演练场景</h3>
          <button class="modal-select__close" onclick="closeSceneSelector()">✕</button>
        </div>
        <div class="modal-select__body">
          <div class="modal-select__loading" id="scene-loading">加载孪生场景…</div>
          <div class="modal-select__list" id="scene-list"></div>
        </div>
        <div class="modal-select__footer">
          <span class="modal-select__hint" id="scene-hint">从数字孪生的 3D 环境空间中选择演练场地</span>
          <button class="btn btn-primary btn-sm" onclick="confirmSceneSelection()">✓ 确认选择</button>
        </div>
      </div>
    </div>
    
    <!-- ══════════════════════════════════════════════════════════════
         ③ 四层流水线 Pipeline (L1→L2→L3→L4 + 回流箭头 L4→L2)
         ══════════════════════════════════════════════════════════════ -->
    <section class="pipeline-bar" id="pipeline-bar">
      <div class="pipeline-node" data-layer="L1" id="pipe-L1">
        <div class="pipeline-node__num">L1</div>
        <div class="pipeline-node__name">🌐 MADTwin</div>
        <div class="pipeline-node__sub">环境语义</div>
        <div class="pipeline-node__status" id="pipe-status-L1">●</div>
      </div>
      <div class="pipeline-arrow"></div>
      <div class="pipeline-node" data-layer="L2" id="pipe-L2">
        <div class="pipeline-node__num">L2</div>
        <div class="pipeline-node__name">📋 AAS</div>
        <div class="pipeline-node__sub">协作 SOP</div>
        <div class="pipeline-node__status" id="pipe-status-L2">●</div>
      </div>
      <div class="pipeline-arrow"></div>
      <div class="pipeline-node pipeline-node--active" data-layer="L3" id="pipe-L3">
        <div class="pipeline-node__num">L3</div>
        <div class="pipeline-node__name">🎮 TwinLoop</div>
        <div class="pipeline-node__sub">仿真演练</div>
        <div class="pipeline-node__status" id="pipe-status-L3">●</div>
      </div>
      <div class="pipeline-arrow"></div>
      <div class="pipeline-node" data-layer="L4" id="pipe-L4">
        <div class="pipeline-node__num">L4</div>
        <div class="pipeline-node__name">🎯 MADCG</div>
        <div class="pipeline-node__sub">全局评价</div>
        <div class="pipeline-node__status" id="pipe-status-L4">●</div>
      </div>
      <div class="pipeline-arrow pipeline-arrow--return" title="L4 评价回流到 L2 SOP 库">
        <span class="pipeline-arrow__label">回流进化</span>
      </div>
      <div class="pipeline-node pipeline-node--return" data-layer="EVOLVE" id="pipe-EVOLVE">
        <div class="pipeline-node__name">🌀 SECS Loop</div>
        <div class="pipeline-node__sub">沉淀→再演练</div>
      </div>
    </section>
    
    <!-- ══════════════════════════════════════════════════════════════
         ④ 沙箱 ID (主区) — I/O 镜像
         ══════════════════════════════════════════════════════════════ -->
    <section class="session-bar" id="session-bar">
      <div class="session-bar__id">
        <span class="session-bar__label">沙箱 ID</span>
        <code class="session-bar__code" id="session-id-display">— 尚未启动 —</code>
        <button class="btn btn-sm session-bar__copy" id="session-bar__copy" onclick="copySessionId()" title="复制完整 session id">📋</button>
      </div>
      <div class="session-bar__meta" id="session-bar__meta">
        <span>mode · <strong id="session-mode">—</strong></span>
        <span>步数 · <strong id="session-step">0</strong></span>
        <span>评分 · <strong id="session-score">—</strong></span>
        <span>状态 · <strong id="session-status">空闲</strong></span>
      </div>
      <div class="session-bar__actions">
        <button class="btn btn-sm" onclick="loadSessionDetail()" id="btn-refresh-session">↻ 概要详情</button>
      </div>
    </section>
    
    <!-- Session 详情弹出层 -->
    <div class="session-detail-modal" id="session-detail-modal" style="display:none" onclick="if(event.target===this) closeSessionDetail()">
      <div class="session-detail-modal__inner" id="session-detail-modal__inner">
        <div class="session-detail-modal__header">
          <span>📋 Session 概要详情</span>
          <button class="btn btn-sm" onclick="closeSessionDetail()">✕</button>
        </div>
        <div class="session-detail-modal__body" id="session-detail-modal__body">
          <div class="io-empty">点击「↻ 概要详情」加载</div>
        </div>
      </div>
    </div>
    
    <main class="io-grid">
      <!-- ④.1 Input · 沙箱进料 -->
      <div class="io-panel io-panel--input">
        <div class="io-panel__header">
          <span class="io-panel__title">📥 Input · 沙箱进料</span>
          <span class="io-panel__hint">你喂进去什么</span>
        </div>
        <div class="io-tabs" id="input-tabs">
          <button class="io-tab io-tab--active" data-tab="task">任务</button>
          <button class="io-tab" data-tab="env">环境</button>
          <button class="io-tab" data-tab="seed">种子技能</button>
          <button class="io-tab" data-tab="params">运行参数</button>
        </div>
        <div class="io-tab-content" id="input-content-task">
          <div class="io-empty">启动仿真后此处显示具体任务描述</div>
        </div>
        <div class="io-tab-content" id="input-content-env" style="display:none">
          <div class="io-empty">数字孪生环境的初始 Agent 集合与状态</div>
        </div>
        <div class="io-tab-content" id="input-content-seed" style="display:none">
          <div style="margin-bottom:8px;display:flex;gap:6px;flex-wrap:wrap;align-items:center">
            <input type="text" id="skill-inject-team" placeholder="team_id (默认 public)" style="background:var(--bg);color:var(--text);border:1px solid var(--border);padding:5px 8px;border-radius:5px;font-size:11px;width:140px">
            <button class="btn btn-sm" onclick="loadSkillCatalog()">↻ 加载技能库</button>
            <select id="skill-inject-select" style="background:var(--bg);color:var(--text);border:1px solid var(--border);padding:5px 8px;border-radius:5px;font-size:11px;flex:1;min-width:160px">
              <option value="">-- 先加载 --</option>
            </select>
          </div>
          <div id="skill-inject-panel" class="skill-grid">
            <div class="io-empty">点击「加载技能库」后此处显示可注入的技能卡片</div>
          </div>
          <div id="skill-inject-result" style="margin-top:8px;font-size:11px;color:var(--muted);font-family:var(--font-mono)"></div>
        </div>
        <div class="io-tab-content" id="input-content-params" style="display:none">
          <div class="param-row"><label>仿真模式</label>
            <select id="sim-mode">
              <option value="what_if">What-if 单场景</option>
              <option value="parallel">并行多策略</option>
              <option value="evolutionary" selected>演化搜索</option>
            </select></div>
          <div class="param-row"><label>最大步数</label><input type="number" id="sim-steps" value="50" min="10" max="500"></div>
          <div class="param-row"><label>加速倍率</label><input type="number" id="sim-speed" value="10" min="1" max="100"></div>
          <div class="param-row"><label>并行分支</label><input type="number" id="sim-branches" value="3" min="1" max="10"></div>
        </div>
        <div class="io-panel__action">
          <button class="btn btn-primary" onclick="createAndRun()" id="btn-launch" style="flex:1">▶ 启动仿真</button>
          <button class="btn btn-stop" id="btn-stop" onclick="stopSimulation()" style="display:none;flex:1">⏹ 停止</button>
          <button class="btn btn-danger" id="btn-inject" onclick="injectStrategy()" disabled style="flex:1">💉 注入</button>
        </div>
        <div id="sim-status" class="io-status"></div>
      </div>
    
      <!-- ④.1.5 3D 演练场景 · 具像化 Agent 协作 -->
      <div class="io-panel io-panel--scene" id="scene-3d-panel">
        <div class="io-panel__header">
          <span class="io-panel__title">🎮 3D 演练场景</span>
          <span class="io-panel__hint" id="scene-3d-label">演练场</span>
        </div>
        <div class="scene-3d-container" id="scene-3d-container">
          <canvas id="scene-3d-canvas"></canvas>
          <div class="scene-3d-info" id="scene-3d-info">初始化中…</div>
          <div class="scene-3d-controls">
            <button class="btn btn-sm" onclick="sw3dTopView()" title="俯视图">⬆</button>
            <button class="btn btn-sm" onclick="sw3dFrontView()" title="前视图">⬛</button>
            <button class="btn btn-sm" onclick="sw3dResetView()" title="重置视角">🔄</button>
          </div>
        </div>
      </div>
    
      <!-- ④.2 Output · 沙箱出料 -->
      <div class="io-panel io-panel--output">
        <div class="io-panel__header">
          <span class="io-panel__title">📤 Output · 沙箱出料</span>
          <span class="io-panel__hint">它跑出什么</span>
        </div>
        <div class="io-tabs" id="output-tabs">
          <button class="io-tab io-tab--active" data-tab="reward">收益曲线</button>
          <button class="io-tab" data-tab="log">执行日志</button>
          <button class="io-tab" data-tab="sop">提取 SOP</button>
          <button class="io-tab" data-tab="critic">评分/建议</button>
        </div>
        <div class="io-tab-content" id="output-content-reward">
          <div class="reward-meta">
            <span class="reward-meta__k">步数 <strong id="step-counter">0</strong></span>
            <span class="reward-meta__k">最大收益 <strong id="reward-max">—</strong></span>
            <span class="reward-meta__k">趋势 <strong id="r
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
            tasks = plaza_routes._p
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

🔗 API: api.deepseek.com | 模型: deepseek-v4-flash
────────────────────────────────────────────────────────────



⚠️ LLM 执行降级：API 错误: 401 Authorization Required {"error":{"message":"Authentication Fails, Your api key: ****8cba is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}
系统已生成确定性任务草稿，供人工 review / 后续真实模型补跑。

## 降级执行草稿
- 先确认变更目标、风险、依赖和验收指标。
- 将任务拆成 plan / dry-run / review / apply / rollback / observe 六段。
- 所有生产动作必须保留审计日志、回滚条件和成本/合规检查。
- 对 OpenSearch/ElasticSearch 伸缩类任务，必须覆盖容量基线、分片重平衡、CloudWatch/OpenSearch 指标门禁、RI/Savings Plan 影响和北美数据驻留。

## 原始任务摘要
你是 AgentsGroup2026 系统的 Researcher (researcher)。
请执行以下开发任务:

你是技术研究员。请对以下任务进行技术调研:

## 任务
执行代码 review、单步变更和彩排回滚
负责角色: 运维操作员
依赖: 任务2
预期产出: 审核记录、执行日志、回滚验证结果
负责角色: 运维操作员
依赖: 任务2
预期产出: 审核记录、执行日志、回滚验证结果

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
src/frontend/js/agent-team-config
