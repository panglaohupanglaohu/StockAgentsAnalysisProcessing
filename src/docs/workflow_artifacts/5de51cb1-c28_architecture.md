# 架构设计 — architect

任务: 巡检监控员
步骤: architecture
Agent: build_architect

---

📋 任务: 5de51cb1-c28
🏷 团队: build_system
🤖 Agent: Architect (architect)
📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
🔧 执行方式: 配置模型 (openai / glm-5.1)
⏱️ 超时: 1200s
────────────────────────────────────────────────────────────
📝 提示词:
  你是 AgentsGroup2026 系统的 Architect (architect)。
  请执行以下开发任务:
  
  你是系统架构师。请为以下任务设计技术方案:
  
  ## 任务
  巡检监控员
  负责角色: 指数：3
  依赖: 任务2
  预期产出: 方案文档/执行记录
  负责角色: 指数：3
  依赖: 任务2
  预期产出: 方案文档/执行记录
  
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
  src/frontend/css/taste-light.css
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
  src/frontend/js/token-workbench.js
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
  src/frontend/js/digital-twin/eco-feedback.js
  src/frontend/js/digital-twin/eco-genetics.js
  src/frontend/js/digital-twin/eco-matchup.js
  src/frontend/js/digital-twin/eco-task-hud.js
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
  ... (共 2194 个 src/ 文件)
  
  ```
  
  ### 文件: `src/frontend/agent-team-config.html`
  ```html
  <!DOCTYPE html>
  <html lang="zh-CN" class="taste-light">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://ga.jspm.io https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; connect-src 'self' http://127.0.0.1:* ws://127.0.0.1:*; img-src 'self' data:;">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>智能体团队 — AgentsGroup2026</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
    <link rel="stylesheet" href="/css/base.css">
    <link rel="stylesheet" href="/css/theme.css">
  <link rel="stylesheet" href="/css/components.css">
    <link rel="stylesheet" href="/css/ws-theme-bridge.css">
    <link rel="stylesheet" href="/css/agent-team-config.css">
    <link rel="stylesheet" href="/css/topbar-ws.css">
  <style>:root{--ag-font-sans:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei","Noto Sans SC","Segoe UI",sans-serif;--ag-font-mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}body{font-family:var(--ag-font-sans)}code,pre,kbd{font-family:var(--ag-font-mono)}</style>
    <link rel="stylesheet" href="/css/taste-light.css">
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
        <nav class="topbar-ws__nav" aria-label="主导航" data-nav-auto>
      <a href="/agent-team-config.html">智能体团队</a>
      <a href="/plaza.html">议事广场</a>
      <a href="/skill-extract.html">技能萃取</a>
      <a href="/Agent-digital-twin.html?office3d=1">数字孪生</a>
      <a href="/cost-dashboard.html">Token节省</a>
      <a href="/pet-config.html">生态配置</a>
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
          <div style="
  ```
  
  ### 文件: `src/frontend/js/agent-detail.js`
  ```js
  /**
   * AgentsGroup2026 — Agent Detail Views
   * Renders agent status, personality/soul, tools, skills,
   * relationships, workspace, chat, logs, and settings tabs.
   * Extracted from agent-team-config.js for modularity.
   * Depends on: utils.js, api.js, agent-team-config.js (parent scope)
   */
  (function(){
  'use strict';
  const csrfFetch = window._agFetch || fetch;
  const EMPLOYEE_API = '/api/v1/agent-employee';
  async function listApi(path, limit = 200, offset = 0){
    if(window.api&&typeof window.api.list==='function'){
      const payload=await window.api.list(path,limit,offset);
      return Array.isArray(payload?.items)?payload.items:[];
    }
    const payload=await api(path);
    return Array.isArray(payload)?payload:Array.isArray(payload?.items)?payload.items:[];
  }
  function _isLikelyOpaqueId(v){
    return /^[a-f0-9]{8,}$/i.test(String(v||''));
  }
  
  async function _resolveSkillLabels(teamId, skills){
    const list = Array.isArray(skills) ? skills : [];
    if (!list.length) return [];
    const payload = await api(`${A}/teams/${teamId}/skills`).catch(function(){ return null; });
    const items = Array.isArray(payload) ? payload : (Array.isArray(payload?.items) ? payload.items : []);
    const map = {};
    items.forEach(function(s){
      const name = s && s.name ? String(s.name) : '';
      if (!name) return;
      if (s.skill_id) map[String(s.skill_id)] = name;
      if (s.slug) map[String(s.slug)] = name;
      map[name] = name;
    });
    return list.map(function(raw){
      const key = String(raw||'');
      return { raw: key, label: map[key] || key };
    });
  }
  async function loadAgent(id){
    if(id){aid=id;_chatSid=''}const d=await api(`${A}/teams/${tid}/agents/${aid}`);
    if(!d){el('agent-content').innerHTML='<p style="color:var(--dim);padding:40px">加载失败</p>';return}
    el('main-title').textContent=d.name||d.agent_id;el('main-badge').textContent=d.role||d.template_type||'';
    document.querySelectorAll('.sb-agent').forEach(e=>e.classList.toggle('active',e.onclick&&e.onclick.toString().includes(aid)));
    renderATab(d);
  }
  document.querySelectorAll('#agent-tabs .tab').forEach(t=>t.addEventListener('click',()=>{document.querySelectorAll('#agent-tabs .tab').forEach(x=>x.classList.remove('active'));t.classList.add('active');atab=t.dataset.at;loadAgent()}));
  
  function renderATab(d){
    const c=el('agent-content'),p=d.personality||{},m=d.metadata||{},cr=d.created_at?d.created_at.split('T')[0]:'?';
    if(atab==='ag-status'){
      // Fetch real metrics + tasks for evidence
      Promise.all([
        api(`${A}/teams/${tid}/agents/${aid}/metrics`),
        api(`${A}/teams/${tid}/agents/${aid}/activity`),
        api(`${A}/teams/${tid}/tasks?limit=5&offset=0`),
        api(`${A}/teams/${tid}/agents/${aid}/logs?limit=5`),
      ]).then(([mt,act,tasks,lg])=>{
        mt=mt||{};act=act||{};
        const taskItems = tasks?.items || tasks || [];
        const logs = (lg?.logs || []).slice(-3).reverse();
        const recentTasksHtml = taskItems.length
          ? taskItems.slice(0,5).map(t => `<div class="focus-item" style="padding:8px 12px"><div class="title" style="font-size:12px"><span class="chip" style="font-size:9px;background:${t.status==='completed'?'rgba(38,162,105,0.1)':t.status==='failed'?'rgba(224,27,36,0.1)':'rgba(128,128,128,0.1)'};color:${t.status==='completed'?'var(--lime)':t.status==='failed'?'var(--red)':'var(--muted)'}">${escapeHtml(t.status||'pending')}</span> ${escapeHtml((t.title||t.task_id||'').slice(0,60))}</div><div class="meta">${t.created_at?t.created_at.slice(0,16):''}</div></div>`).join('')
          : '<p style="color:var(--dim);font-size:12px">暂无任务</p>';
        const evidenceHtml = logs.length
          ? logs.map(l => `<div class="focus-item" style="padding:6px 12px"><span class="chip" style="font-size:9px">${escapeHtml(l.action||'log')}</span> <span style="font-size:11px;color:var(--muted)">${escapeHtml((l.detail||'').slice(0,80))}</span></div>`).join('')
          : '<p style="color:var(--dim);font-size:12px">暂无执行记录 — 运行 Agent Loop 后显示</p>';
  
        // XF-2.4 物竞协作基因（metadata.eco_collab）只读
        const eco=m.eco_collab&&typeof m.eco_collab==='object'?m.eco_collab:null;
        const dimBar=(lab,v)=>{
          const n=Math.max(0,Math.min(1,Number(v!=null?v:0.5)));
          const pct=Math.round(n*100);
          return `<div class="detail-row" style="align-items:center"><span class="lbl">${lab}</span>`
            +`<span class="val" style="display:flex;align-items:center;gap:8px;flex:1;min-width:0">`
            +`<span style="flex:1;height:6px;background:var(--panel2);border-radius:3px;overflow:hidden;max-width:120px">`
            +`<span style="display:block;height:100%;width:${pct}%;background:var(--cyan)"></span></span>`
            +`<span style="font-size:12px;min-width:36px">${pct}%</span></span></div>`;
        };
        const ecoCard=eco
          ?`<div class="card" style="margin-top:16px;border-color:rgba(34,211,238,.35)"><div class="section-title">🧬 物竞协作基因 <span class="chip" style="font-size:10px;background:rgba(34,211,238,.12);color:var(--cyan)">eco_collab · 只读</span></div>`
            +`<p style="color:var(--dim);font-size:12px;margin:0 0 10px">仿真表型参数（非团队页关系/通道拓扑）。来源 ${escapeHtml(eco.source||'—')} · 策略 ${escapeHtml(eco.strategy||'—')}${eco.eco_fp?` · fp <code style="font-size:10px">${escapeHtml(String(eco.eco_fp).slice(0,12))}</code>`:''}</p>`
            +dimBar('share',eco.share_tendency)+dimBar('signal',eco.signal_tendency)
            +dimBar('follow',eco.follow_tendency)+dimBar('mate',eco.mate_choosiness)
            +(eco.survival_ticks!=null?`<div class="detail-row"><span class="lbl">存活 T</span><span class="val">${eco.survival_ticks}</span></div>`:'')
            +`<p style="color:var(--dim);font-size:11px;margin:10px 0 0">改拓扑请回 <a href="/Agent-digital-twin.html?office3d=1&team_id=${encodeURIComponent(tid||'')}" style="color:var(--cyan)">物竞 ③ 反馈台</a> 写回关系/通道</p></div>`
          :`<div class="card" style="margin-top:16px"><div class="section-title">🧬 物竞协作基因</div><p style="color:var(--dim);font-size:13px;margin:0">尚未写回 metadata.eco_collab — 在物竞试验田 ③ 勾选「写回协作基因」后此处可见四维倾向</p></div>`;
  
        c.innerHTML=`<div style="display:flex;gap:8px;margin-bottom:12px"><button class="btn btn-pink btn-sm" onclick="switchView('runtime')">▶ 运行 Agent Loop</button><button class="btn btn-sm" onclick="switchView('tasks')">📋 任务队列</button><button class="btn btn-sm" onclick="atab='ag-chat';loadAgent()">💬 对话</button></div>
  <div class="card-grid"><div class="stat-card"><div class="label">📋 状态</div><div class="value" style="font-size:16px"><span class="st st-${d.state||'idle'}">● ${stL(d.state)}</span></div><div class="sub"><button class="btn btn-sm" style="margin-top:6px;padding:3px 10px;font-size:11px" onclick="startStop('${escapeHtml(d.state)}')">${d.state==='working'?'⏹ 停止':'▶ 启动'}</button></div></div><div class="stat-card"><div class="label">📊 今日 Token</div><div class="value">${(mt.today_tokens||0).toLocaleString()}</div></div><div class="stat-card"><div class="label">📈 本月 Token</div><div class="value">${((mt.month_tokens||0)/1000).toFixed(1)}K</div></div><div class="stat-card"><div class="label">🤖 今日 LLM 调用</div><div class="value">${mt.today_llm_calls||0}</div><div class="sub">消息: ${mt.messages_sent||0}</div></div><div class="stat-card"><div class="label">✅ 任务完成</div><div class="value">${mt.tasks_completed||0}</div><div class="sub" style="color:${(mt.tasks_failed||0)>0?'var(--pink)':'var(--muted)'}">成功率: ${mt.success_rate?Math.round(mt.success_rate*100)+'%':'N/A'}</div></div><div class="stat-card"><div class="label">🎯 能力评分</div><div class="value" style="color:${(mt.capability_score||0)>=60?'var(--lime)':(mt.capability_score||0)>=30?'var(--amber)':'var(--red)'}">${mt.capability_score||'?'}</div><div class="sub">/100</div></div><div class="stat-card"><div class="label">🔧 工具调用</div><div class="value">${mt.tools_invoked||0}</div></div><div class="stat-card"><div class="label">⚡ 技能数</div><div class="value">${(d.skills||[]).length}</div></div></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px"><div class="card"><div class="section-title">📁 Agent 档案</div><div class="detail-row"><span class="lbl">👤 角色</span><span class="val">${escapeHtml(d.role||d.description||'-')}</span></div><div class="detail-row"><span class="lbl">📅 创建时间</span><span class="val">${cr}</span></div><div class="detail-row"><span class="lbl">🔴 最后活跃</span><span class="val">${mt.last_active?mt.last_active.split('T')[0]:'从未'}</span></div><div class="detail-row"><span class="lbl">💬 会话数</span><span class="val">${mt.sessions_created||0}</span></div></div><div class="card"><div class="section-title">🧠 模型配置</div><div class="detail-row"><span class="lbl">🟠 模型</span><span class="val">${escapeHtml(d.model_id||'未配置')}</span></div><div class="detail-row"><span class="lbl">📁 模板</span><span class="val">${escapeHtml(d.template_type||'-')}</span></div><div class="detail-row"><span class="lbl">🔧 工具数</span><span class="val">${(d.tools||[]).length}</span></div><div class="detail-row"><span class="lbl">📡 通道数</span><span class="val">${(d.channels||[]).length}</span></div></div></div>
  ${ecoCard}
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px"><div class="card"><div class="section-title">📋 最近任务</div>${recentTasksHtml}</div><div class="card"><div class="section-title">📡 执行证据</div>${evidenceHtml}</div></div>
  <div class="section" style="margin-top:20px"><div class="section-title">📊 近期活动</div>${act.recent_logs&&act.recent_logs.length?act.recent_logs.slice(-8).reverse().map(l=>`<div class="focus-item" style="padding:10px 14px"><div class="title" style="font-size:13px"><span class="chip" style="font-size:10px">${escapeHtml(l.action)}</span> ${escapeHtml(l.detail||'')}</div><div class="meta">${l.timestamp?l.timestamp.replace('T',' ').slice(0,19):''}</div></div>`).join(''):'<p style="color:var(--dim);font-size:13px">暂无活动记录 — 发送消息或启动 Agent 后将显示</p>'}</div>`;
      });
    } else if(atab==='ag-employee'){
      renderEmployeeView(d);
    } else if(atab==='ag-aware'){
      const tr=m.traits||[],bd=m.behavior_boundaries||[];
      c.innerHTML='<div class="section"><div class="section-title">关注点</div><p style="color:var(--dim);font-size:12px">加载中...</p></div>';
      _resolveSkillLabels(tid, d.skills||[]).then(function(resolved){
        c.innerHTML=`<div class="section"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><div class="section-title" style="margin:0">关注点</div><span style="color:var(--dim);font-size:12px">${resolved.length+tr.length} active</span></div><p style="color:var(--muted);font-size:12px;margin-bottom:14px">技能、性格特质与行为边界</p>${resolved.map(s=>`<div class="focus-item"><div class="title"><span class="dot" style="width:8px;height:8px;background:var(--pink)"></span>${escapeHtml(s.label)}${_isLikelyOpaqueId(s.raw)&&s.label===s.raw?` <span style="font-size:11px;color:var(--dim)">(${escapeHtml(s.raw.slice(0,8))})</span>`:''}</div><div class="meta">skill · active</div></div>`).join('')}${tr.map(t=>`<div class="focus-item"><div class="title"><span class="dot" style="width:8px;height:8px;background:var(--amber)"></span>${escapeHtml(t)}</div><div class="meta">trait · personality</div></div>`).join('')}${bd.map(b=>`<div class="focus-item"><div class="title"><span class="dot" style="width:8px;height:8px;background:var(--dim)"></span>${escapeHtml(b)}</div><div class="meta">boundary · constraint</div></div>`).join('')}${!resolved.length&&!tr.length&&!bd.length?'<p style="color:var(--dim)">暂无关注项</p>':''}</div>`;
      }).catch(function(){
        c.innerHTML=`<div class="section"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><div class="section-title" style="margin:0">关注点</div><span style="color:var(--dim);font-size:12px">${(d.skills||[]).length+tr.length} active</span></div><p style="color:var(--muted);font-size:12px;margin-bottom:14px">技能、性格特质与行为边界</p>${(d.skills||[]).map(s=>`<div class="focus-item"><div class="title"><span class="dot" style="width:8px;height:8px;background:var(--pink)"></span>${escapeHtml(s)}</div><div class="meta">skill · active</div></div>`).join('')}${tr.map(t=>`<div class="focus-item"><div class="title"><span class="dot" style="width:8px;height:8px;background:var(--amber)"></span>${escapeHtml(t)}</div><div class="meta">trait · personality</div></div>`).join('')}${bd.map(b=>`<div class="focus-item"><div class="title"><span class="dot" style="width:8px;height:8px;background:var(--dim)"></span>${escapeHtml(b)}</div><div class="meta">boundary · constraint</div></div>`).join('')}${!(d.skills||[]).length&&!tr.length&&!bd.length?'<p style="color:var(--dim)">暂无关注项</p>':''}</div>`;
      });
    } else if(atab==='ag-soul'){
      const soul=`# Soul — ${d.name||d.agent_id}\n\n## Identity\n- **名称**: ${d.name||d.agent_id}\n- **角色**: ${escapeHtml(d.role||d.description||'-')}\n- **创建时间**: ${cr}\n\n## Personality\n- ${p.tone||'professional'}\n- ${p.response_style||'concise'}\n- 创造力: ${p.creativity??0.5}\n- 语言: ${p.language||'zh-CN'}\n- 专长: ${(p.expertise_areas||[]).join(', ')||'无'}\n\n## Boundaries\n${(m.behavior_boundaries||[]).map(b=>'- '+b).join('\n')||'- 无限制'}`;
      // Load saved soul or generate default
      api(`${A}/teams/${tid}/agents/${aid}/soul`).then(sd=>{
        const savedSoul=(sd&&sd.content)?sd.content:soul;
        // Load memory files
        api(`${A}/teams/${tid}/agents/${aid}/memory`).then(mf=>{
          const files=mf||[];
          c.innerHTML=`<div class="section"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><div><div class="section-title" style="margin:0">🧬 Soul.md — 人格定义</div><p style="color:var(--muted);font-size:12px;margin-top:2px">核心身份、人格和行为边界</p></div><div><button class="btn btn-sm" id="soul-edit-btn" onclick="toggleSoulEdit()">编辑</button><button class="btn btn-pink btn-sm hidden" id="soul-save-btn" onclick="saveSoul()">保存</button></div></div><div class="soul-block" id="soul-view">${escapeHtml(savedSoul)}</div><textarea class="fi hidden" id="soul-editor" rows="16" style="font-family:'IBM Plex Mono',monospace;font-size:13px;line-height:1.7;min-height:300px">${savedSoul}</textarea></div><div class="section"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><div class="section-title" style="margin:0">🧠 记忆文件</div><button class="btn btn-sm" onclick="addMemoryFile()">＋ 新建</button></div><p style="color:var(--muted);font-size:12px;margin-bottom:12px">通过对话和经验积累的持久记忆</p><div id="memory-list">${files.length?files.map(f=>`<div class="memory-item" style="cursor:pointer" onclick="openMemoryFile('${escapeHtml(f.filename)}')"><span>📄 ${escapeHtml(f.filename)}</span><span style="display:flex;align-items:center;gap:8px"><span style="color:var(--dim);font-size:12px">${escapeHtml(f.size_display||f.size+' B')}</span><span style="cursor:pointer;color:var(--dim);font-size:14px" onclick="event.stopPropagation();delMemoryFile('${escapeHtml(f.filename)}')" title="删除">×</span></span></div>`).join(''):'<p style="color:var(--dim);font-size:13px">暂无记忆文件，点击「新建」开始积累</p
  ```
  
  ### 文件: `src/frontend/js/office/office-state.js`
  ```js
  /**
   * office-state.js — 统一办公室场景的单一数据源 (P7-1)
   * 纯函数 reducer，无 three.js 依赖，可单测。
   * 设计: docs/unified-office-3d-design.md §4
   */
  
  export const ACTIVITIES = ['working', 'meeting', 'treadmill', 'coffee', 'toilet', 'idle', 'zen'];
  
  // 共享设施: 容量均为 1，后到者 FIFO 排队。停留时长(ms): 咖啡 1min、跑步机 5min、马桶 5min。
  export const FACILITIES = ['coffee', 'treadmill', 'toilet'];
  export const DWELL_MS = { coffee: 60e3, treadmill: 300e3, toilet: 300e3 };
  
  /** 调试用时间加速（?breakspeed=60）: 停留时长同比例缩短，便于观察排队行为。 */
  export function setBreakTimeScale(factor) {
    const f = Math.max(1, Number(factor) || 1);
    DWELL_MS.coffee = 60e3 / f;
    DWELL_MS.treadmill = 300e3 / f;
    DWELL_MS.toilet = 300e3 / f;
  }
  
  // 房间语义 → 办公室活动映射（兼容旧 ROOM_MAP 的 6 房间）
  const ROOM_ACTIVITY = {
    'council-hall': 'meeting',
    'council': 'meeting',
    'extraction-lab': 'treadmill',
    'workshop': 'working',
    'knowledge-base': 'working',
    'training-ground': 'working',
    'rest-area': 'coffee',
  };
  
  const EDGE_TTL = 6;          // 协作光线存活秒数
  const EDGE_MAX = 40;         // 同屏最多光线数
  
  export function initialState() {
    return {
      agents: {},        // id -> {id,name,role,collar,activity,deskIndex,layer}
      edges: [],         // {from,to,kind,ttl}
      collab: {},        // "from→to" -> count（协作热度，考察协作能力的核心数据）
      meeting: { active: false, speakerId: null, boardLines: [] },
      mirror: false,     // 孪生镜像层
      catNote: '',       // 猫头顶气泡: 演练任务 / 仿真参数 / 种子技能注入
      workflow: [],      // M2-4: 工作流边 [{from,to,content,type,weight,order}]（结构化交接顺序+内容）
      workflowProgress: 0, // M2-4: 当前已推进到第几条边（顺序约束：前序交接未完成不得触发后序）
      workflowGraph: { nodes: [], edges: [], highlightedEdge: null }, // M3-1: 显式工作流图（节点=角色·技能·模型档，边=依赖·内容）
      biddingView: { active: false, candidates: [], winnerId: null, ranking: [] }, // M4-4: 竞标画中画
      stages: {},        // M2-5: 房间业务阶段 {room_id: stage}
      facilities: {      // facility -> {occupant, until, queue[]}
        coffee: { occupant: null, until: 0, queue: [] },
        treadmill: { occupant: null, until: 0, queue: [] },
        toilet: { occupant: null, until: 0, queue: [] },
      },
      ecoEnv: null,      // XB-6.1 生境 HUD：{demand, niche_title, living, ...}
      seq: 0,
    };
  }
  
  const COLLARS = [0xE04040, 0x7C4DFF, 0x2BB8A8, 0xE8A020, 0x4D9DE0, 0xD05CB0];
  
  function ensureAgent(state, id, extra) {
    if (!state.agents[id]) {
      // 取最小空闲座位号（与 team_reset 的粘性座位语义一致，避免编号碰撞）
      const usedDesks = new Set(Object.values(state.agents).map((a) => a.deskIndex));
      let deskIndex = 0;
      while (usedDesks.has(deskIndex)) deskIndex += 1;
      state.agents[id] = {
        id,
        name: id,
        role: '',
        team: '',
        collar: COLLARS[deskIndex % COLLARS.length],
        activity: 'working',   // 默认在工位落座干活
        deskIndex,
        layer: 'prod',
        lastAction: '',        // 最近一次 twin 动作（claim_task/execute_skill/delegate/...）
        skillUsed: '',         // execute_skill 的 skill_used
        task: '',              // 当前认领/执行的任务
        // ND-5.2: eco 模式生境字段
        health: 100,           // 血量（0~health_max）
        survivalTicks: 0,      // 生存时长
        ecoAlive: true,        // 是否存活
      };
    }
    if (extra) Object.assign(state.agents[id], extra);
    return state.agents[id];
  }
  
  function addEdge(state, from, to, kind) {
    if (!from || !to || from === to) return;
    state.edges.push({ from, to, kind: kind || 'help', ttl: EDGE_TTL });
    if (state.edges.length > EDGE_MAX) state.edges.splice(0, state.edges.length - EDGE_MAX);
    const key = from + '→' + to;
    state.collab[key] = (state.collab[key] || 0) + 1;
  }
  
  /** 纯 reducer: (state, event) → newState（浅拷贝顶层，内层原位修改副本） */
  export function reduce(prev, event) {
    const state = {
      ...prev,
      agents: { ...prev.agents },
      edges: prev.edges.slice(),
      collab: { ...prev.collab },
      meeting: { ...prev.meeting, boardLines: prev.meeting.boardLines.slice() },
      facilities: Object.fromEntries(
        Object.entries(prev.facilities).map(([k, f]) => [k, { ...f, queue: f.queue.slice() }])
      ),
      seq: prev.seq + 1,
    };
    // agents 深一层拷贝，保证 reducer 纯度
    for (const k of Object.keys(state.agents)) state.agents[k] = { ...state.agents[k] };
  
    switch (event.type) {
      case 'team_sync': {
        (event.agents || []).forEach((a, i) => {
          ensureAgent(state, a.id, {
            name: a.name || a.id,
            role: a.role || '',
            team: a.team || '',
            collar: a.collar != null ? a.collar : COLLARS[i % COLLARS.length],
          });
        });
        break;
      }
      case 'team_reset': {
        // 花名册整体替换（团队/成员筛选）：只保留 roster 内的 Agent。
        // 座位语义 = 保序前移压缩:
        //   - 同一批人顺序抖动 → 映射恒等，无人移动（不玩抢椅子）；
        //   - 有人离编 → 保留者按原座位相对次序整体前移补位（只向前、不互换），
        //     避免幽灵成员清除后 7 个人孤零零坐在第 20+ 号后排桌。
        const retained = (event.agents || [])
          .filter((a) => state.agents[a.id])
          .sort((x, y) => state.agents[x.id].deskIndex - state.agents[y.id].deskIndex);
        const deskMap = {};
        retained.forEach((a, i) => { deskMap[a.id] = i; });
        let nextFree = retained.length;
        const roster = {};
        (event.agents || []).forEach((a, i) => {
          const prev = state.agents[a.id];
          roster[a.id] = prev
            ? {
                ...prev, name: a.name || prev.name, role: a.role || prev.role,
                team: a.team || prev.team, deskIndex: deskMap[a.id],
                // v2.4 修复: noBreaks 此前只对新建 agent 生效，重跑 eco 演练时 roster 已存在，
                // noBreaks:true 被 ...prev 的旧值(false)覆盖 → 演练结束作息欠账放行 → 全员涌向设施排成一列跑出镜头。
                // 事件显式携带 noBreaks 时对留任 agent 也应用之。
                noBreaks: event.noBreaks != null ? !!event.noBreaks : prev.noBreaks,
              }
            : {
                id: a.id, name: a.name || a.id, role: a.role || '', team: a.team || '',
                collar: COLLARS[i % COLLARS.length], activity: 'working',
                deskIndex: nextFree++, layer: state.mirror ? 'mirror' : 'prod',
                // v2.4: 默认允许作息调度；eco 种群由 _seedSceneRoster 显式置 true 跳过设施排队
                noBreaks: !!event.noBreaks,
              };
        });
        state.agents = roster;
        state.edges = state.edges.filter((e) => roster[e.from] && roster[e.to]);
        for (const f of Object.values(state.facilities)) {   // 清理离编成员的占位与排队
          if (f.occupant && !roster[f.occupant]) f.occupant = null;
          f.queue = f.queue.filter((id) => roster[id]);
        }
        break;
      }
      case 'position': {
        const agent = ensureAgent(state, event.agentId);
        agent.activity = ROOM_ACTIVITY[event.room] || 'working';
        break;
      }
      case 'activity': {
        if (ACTIVITIES.includes(event.activity)) {
          ensureAgent(state, event.agentId).activity = event.activity;
        }
        break;
      }
      case 'step': {
        // 孪生仿真步: agent_actions → 状态/协作光线（协作能力的观测点）
        // 对齐 twin 动作词表 (llm_decision.py):
        //   claim_task | work_on_task | execute_skill | offer_help | delegate | communicate | idle
        const actions = event.agentActions || {};
        for (const [id, act] of Object.entries(actions)) {
          const agent = ensureAgent(state, id);
          const a = typeof act === 'string' ? { action: act } : (act || {});
          const action = a.action || '';
          const target = a.target || a.to || '';
          agent.lastAction = action;
  
          // M2-4: 工作流顺序约束 — delegate/communicate 须按 workflow 边顺序推进
          // 前序交接未完成（workflowProgress < edge.order）时，不渲染协作边但仍记录动作
          const _isWorkflowOrdered = () => {
            if (!state.workflow.length) return false;
            return state.workflow.some((w) => w.from === id && (w.to === target || w.to === '*'));
          };
          const _workflowAllows = () => {
            // 无工作流边 → 不约束（自由模式）
            if (!state.workflow.length) return true;
            // 有工作流边但当前 agent/target 不在任何边上 → 不约束
            const relevant = state.workflow.filter((w) => w.from === id);
            if (!relevant.length) return true;
            // 当前 agent 有工作流边 → 检查顺序
            const nextEdge = relevant.find((w) => w.order === state.workflowProgress);
            return !!nextEdge;
          };
          const _advanceWorkflow = () => {
            // 推进到下一条边
            if (state.workflowProgress < state.workflow.length) {
              state.workflowProgress += 1;
            }
          };
  
          switch (action) {
            case 'offer_help':
              addEdge(state, id, target, 'help');
              agent.activity = 'working';
              break;
            case 'delegate':                                   // 委派：有向，与沟通区分
              if (_workflowAllows()) {
                addEdge(state, id, target, 'delegate');
                _advanceWorkflow();
              }
              agent.activity = 'working';
              break;
            case 'communicate':
              if (target === 'broadcast' || a.broadcast) {       // 广播：无定向目标
                state.edges.push({ from: id, to: '*', kind: 'broadcast', ttl: EDGE_TTL });
                if (state.edges.length > EDGE_MAX) state.edges.splice(0, state.edges.length - EDGE_MAX);
              } else {
                if (_workflowAllows()) {
                  addEdge(state, id, target, 'comm');
                  _advanceWorkflow();
                }
              }
              agent.activity = 'working';
              break;
            case 'claim_task':
              agent.task = a.task || a.task_id || agent.task || '';
              agent.activity = 'working';
              break;
            case 'execute_skill':
              agent.skillUsed = a.skill_used || a.skill || '';
              agent.activity = 'working';
              break;
            case 'work_on_task':
              if (a.task || a.task_id) agent.task = a.task || a.task_id;
              agent.activity = 'working';
              break;
            case 'disabled':
            case 'rest':
              agent.activity = 'coffee';
              break;
            case 'idle':
              agent.activity = 'idle';
              break;
            default:
              if (action) agent.activity = 'working';
          }
        }
        break;
      }
      case 'discussion': {
        state.meeting.active = !!event.active;
        state.meeting.speakerId = event.speakerId || null;
        if (event.boardLine) {
          state.meeting.boardLines.push(String(event.boardLine).slice(0, 48));
          if (state.meeting.boardLines.length > 8) state.meeting.boardLines.shift();
        }
        if (!event.active) state.meeting.boardLines = [];
        const ids = event.participantIds || Object.keys(state.agents);
        for (const id of ids) {
          const agent = state.agents[id];
          if (agent) agent.activity = event.active ? 'meeting' : 'working';
        }
        break;
      }
      case 'trial_status': {
        // running/evaluating → 镜像层（孪生进行中）；其余回生产层
        state.mirror = event.status === 'running' || event.status === 'evaluating';
        for (const k of Object.keys(state.agents)) {
          state.agents[k].layer = state.mirror ? 'mirror' : 'prod';
        }
        break;
      }
      case 'break_request': {
        // Agent 申请去设施: 空闲即占用（带释放时间戳），有人则 FIFO 排队。
        const f = state.facilities[event.facility];
        const agent = state.agents[event.agentId];
        if (!f || !agent || agent.activity !== 'working') break;
        const now = event.now != null ? event.now : Date.now();
        if (!f.occupant) {
          f.occupant = event.agentId;
          f.until = now + DWELL_MS[event.facility];
        } else if (f.occupant !== event.agentId && !f.queue.includes(event.agentId)) {
          f.queue.push(event.agentId);
        }
        agent.activity = event.facility;
        break;
      }
      case 'break_tick': {
        // 设施推进: 占用者到时释放回工位，队首补位并重新计时。
        const now = event.now != null ? event.now : Date.now();
        for (const [name, f] of Object.entries(state.facilities)) {
          if (f.occupant && now >= f.until) {
            const done = state.agents[f.occupant];
            if (done && done.activity === name) done.activity = 'working';
            f.occupant = null;
            while (f.queue.length) {
              const next = f.queue.shift();
              const na = state.agents[next];
              if (na && na.activity === name) {
                f.occupant = next;
                f.until = now + DWELL_MS[name];
                break;
              }
            }
          }
        }
        break;
      }
      case 'cat_say': {
        state.catNote = String(event.text || '').slice(0, 120);
        break;
      }
      case 'tick': {
        const dt = event.dt || 1;
        state.edges = state.edges
          .map((e) => ({ ...e, ttl: e.ttl - dt }))
          .filter((e) => e.ttl > 0);
        break;
      }
      case 'workflow_sync': {
        // M2-4: 同步工作流拓扑（源→目标 + 传递内容/类型），按给定顺序编号
        state.workflow = (event.edges || []).map((e, i) => ({
          from: e.from || e.source || '',
          to: e.to || e.target || '',
          content: e.content || e.channel || '',
          type: e.type || e.message_type || 'request',
          weight: e.weight != null ? e.weight : 1,
          order: e.order != null ? e.order : i,
        })).filter((e) => e.from && e.to);
        // 重置顺序进度
        state.workflowProgress = 0;
        break;
      }
      case 'stages_sync': {
        // M2-5: 同步房间业务阶段映射 {room_id: stage}
        state.stages = { ...(event.stages || {}) };
        break;
      }
      case 'workflow_graph_sync': {
        // M3-1: 同步显式工作流图（节点=角色·技能·模型档，边=依赖·内容）
        state.workflowGraph = {
          nodes: (event.nodes || []).map((n) => ({
            id: n.id || '',
            role: n.role || '',
            skills: Array.isArray(n.skills) ? n.skills : [],
            modelTier: n.model_tier || n.modelTier || '',
          })),
          edges: (event.edges || state.workflow || []).map((e, i) => ({
            from: e.from || e.source || '',
            to: e.to || e.target || '',
            content: e.content || e.channel || '',
            type: e.type || e.message_type || 'request',
            order: e.order != null ? e.order : i,
          })),
          highlightedEdge: null,
        };
        break;
      }
      case 'highlight_workflow_edge': {
        // M3-2: 协作热度面板点击 → 高亮工作流图对应边
        state.workflowGraph = { ...state.workflowGraph, highlightedEdge: event.edgeKey || null };
        break;
      }
      case 'bidding_sync': {
        // M4-4: 竞标画中画 — 同步候选排名与胜者
        state.biddingView = {
          active: !!event.active,
          candidates: (event.candidates || []).map((c) => ({
            id: c.id || c.candidate_id || '',
            operator: c.operator || '',
            desc: c.desc || c.operator_desc || '',
            score: c.score || c.quality_score || 0,
            token: c.token || c.token_consumed || 0,
            rank: c.rank || 0,
          })),
          winnerId: event.winnerId || event.winner_id || null,
          ranking: event.ranking || [],
        };
        break;
      }
      case 'eco_health': {
        // ND-5.2: eco 演练健康数据 → 更新 agent 血量/生存时长/存活状态
        const updates = event.updates || {};
        for (const [id, data] of Object.entries(updates)) {
          const agent = ensureAgent(state, id);
          if (data.health != null) agent.health = data.health;
          if (data.survivalTicks != null) agent.survivalTicks = data.survivalTicks;
          if (data.alive != null) agent.ecoAlive = data.alive;
        }
        break;
      }
      case 'eco_env': {
        // XB-6.1: 生境客
  ```
  
  ### 文件: `src/frontend/js/digital-twin/secs-core.js`
  ```js
  /**
   * AgentsGroup2026 — Agent Digital Twin: SECS 核心 (仿真/团队/房间/CLI/SSE)
   * 从 Agent-digital-twin.html 内联脚本拆出 (frontendBigChange F2)。
   * 加载顺序: secs-core.js → director.js → v4-scenario-evolution.js
   */
  (async function() {
    'use strict';
    const SECS = '/api/v1/sandbox';
    var _sx = { sessionId:null, simRunning:false, esrc:null, history:[], steps:0, rewardPoints:[] };
    window._sx = _sx;  // 暴露到全局，供导演台 P0 别名引用
    var _selectedTeamId = null;
    var _selectedTeamName = '';
    window._teamModalOpen = false;
    var _teamTreeData = [];  // cached teams-tree result for drill-down
  
    // ── 场景 → 模式 映射 (对齐后端枚举: what_if / parallel / evolutionary) ──
    var SCENARIO_MODE = {
      __default:       'what_if',
      __parallel:      'parallel',
      __evolutionary:  'evolutionary',
      __full_topo:     'what_if',
    };
    // ── 场景脚本：定义房间初始状态 & Agent 分布 (role → room) ──
    var SCENE_SCRIPT = {
      __default:       { focus:'council',  assign:{ council:'*', extraction:'', workshop:'', library:'', arena:'', rest:'' } },
      __parallel:      { focus:'arena',    assign:{ council:'', extraction:'', workshop:'', library:'', arena:'*', rest:'' } },
      __evolutionary:  { focus:'workshop', assign:{ council:'', extraction:'', workshop:'*', library:'', arena:'', rest:'' } },
      __full_topo:     { focus:'council',  assign:{ council:['project_manager','architect'], extraction:['researcher','documentation'], workshop:['developer','qa_engineer'], library:[], arena:['devops'], rest:[] } },
    };
    var _selectedSceneMode = 'what_if';  // 当前场景对应的模式
    var _selectedSceneId = null;         // 当前选中的场景ID
  
    // ── 演练任务选择状态 ──
    var _selectedTaskId = null;          // 选中的任务ID
    var _selectedTaskTitle = '';         // 任务标题
    var _selectedTaskGoal = null;        // 任务的 task_goal（传入试炼创建）
  
    var MODE_LABEL = { what_if:'What-if', parallel:'并行', evolutionary:'演化' };
  
    // ── 管理启动按钮 disabled 状态 ──
    function _updateLaunchButton() {
      var launch = document.getElementById('secs-btn-launch');
      if (!launch) return;
      if (_sx.simRunning) {
        launch.disabled = true;
        launch.style.opacity = '0.5';
        launch.style.cursor = 'not-allowed';
        launch.textContent = '⏳ 运行中...';
        launch.title = '演练已在运行中';
      } else if (!_selectedTeamId) {
        launch.disabled = true;
        launch.style.opacity = '0.4';
        launch.style.cursor = 'not-allowed';
        launch.textContent = '▶ 请先选择团队';
        launch.title = '需要先选择演练团队和场景';
      } else if (!_selectedSceneId) {
        launch.disabled = true;
        launch.style.opacity = '0.5';
        launch.style.cursor = 'not-allowed';
        launch.textContent = '▶ 请先选择场景';
        launch.title = '需要先选择演练场景';
      } else {
        launch.disabled = false;
        launch.style.opacity = '1';
        launch.style.cursor = 'pointer';
        launch.textContent = '▶ 运行演练';
        launch.title = '可评分闭环：建试炼→运行(含3D可视化)→五维评分→SOP/反哺/进化→棘轮';
      }
    }
  
    function _renderSimParams() {
      var mode = _selectedSceneMode || 'what_if';
      // 同步 radio
      var radio = document.querySelector('input[name="secs-mode"][value="'+mode+'"]');
      if (radio) radio.checked = true;
      // 同步显示文字
      var label = MODE_LABEL[mode] || mode;
      var modeEl = document.getElementById('secs-session-mode');
      if (modeEl) modeEl.textContent = label;
      var paramEl = document.getElementById('param-mode');
      if (paramEl) paramEl.textContent = label;
      // 同步步数
      var stepsEl = document.getElementById('param-steps');
      var stepsVal = document.getElementById('secs-steps');
      if (stepsEl && stepsVal) stepsEl.textContent = stepsVal.value;
      if (stepsVal) document.getElementById('secs-steps-val').textContent = stepsVal.value;
    }
  
    // ── Utilities ──
    function setT(id, v) { var el = document.getElementById(id); if (el) el.textContent = String(v ?? '—'); }
    function esc(s) { return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
    function _syncTaskflowState(d) {
      if (!d) return;
      var activeIds = Array.isArray(d.active_task_ids) ? d.active_task_ids.slice() : [];
      if (!activeIds.length && d.active_task_id) activeIds = [d.active_task_id];
      if (activeIds.length || d.active_task_id !== undefined) {
        _sx.activeTaskIds = activeIds;
        _sx.activeTaskId = activeIds[0] || d.active_task_id || '';
      }
      if (Array.isArray(d.done_task_ids)) _sx.doneTaskIds = d.done_task_ids.slice();
    }
  
    // ── 控制台日志 ──
    var _consoleLines = [];
    function _logConsole(msg, level) {
      level = level || 'info';
      var colors = { info:'#888', step:'#22d3ee', skill:'#a78bfa', reward:'#34d399', eval:'#f59e0b', warn:'#f97316', err:'#ef4444', header:'#fff' };
      var icon = { info:'  ', step:'▶ ', skill:'🔧', reward:'💰', eval:'📊', warn:'⚠️ ', err:'❌', header:'══' };
      var time = new Date().toLocaleTimeString('zh-CN', {hour12:false});
      var line = '<span style="color:#555">' + time + '</span> <span style="color:' + (colors[level]||'#888') + '">' + (icon[level]||'') + msg + '</span>';
      _consoleLines.push(line);
      // 限制最多 200 行
      if (_consoleLines.length > 200) _consoleLines.shift();
      // 写入独立控制台（始终可见）
      var liveEl = document.getElementById('live-console');
      if (liveEl) {
        liveEl.innerHTML = _consoleLines.join('\n');
        liveEl.scrollTop = liveEl.scrollHeight;
      }
    }
  
    function showToast(msg, type) {
      type = type || 'info';
      var container = document.getElementById('toast-container');
      if (!container) return;
      var icons = { success:'✅', error:'❌', warning:'⚠️', info:'ℹ️', warn:'⚠️' };
      var el = document.createElement('div');
      el.className = 'toast';
      el.style.cssText = 'position:fixed;left:50%;bottom:24px;transform:translateX(-50%);display:flex;align-items:center;gap:6px;white-space:nowrap;width:max-content;max-width:90vw;writing-mode:horizontal-tb;background:var(--panel2);border:1px solid '+(type==='error'||type==='warn'?'var(--red)':'var(--cyan)')+';color:var(--text);padding:10px 20px;border-radius:8px;font-size:13px;line-height:1.4;box-shadow:0 4px 20px rgba(0,0,0,0.4);animation:toastIn 0.3s ease-out;pointer-events:auto';
      el.innerHTML = '<span>'+(icons[type]||'')+'</span><span>'+esc(msg)+'</span>';
      container.appendChild(el);
      setTimeout(function(){ if(el.parentNode)el.parentNode.removeChild(el); }, 3500);
    }
  
    // ── 统计 ──
    // P1: 更新浮动仪表盘数值
    window._updateEsFloat = function(sessions, steps, sops, score) {
      var setT = function(id, v) { var el = document.getElementById(id); if(el) el.textContent = v; };
      setT('esf-sessions', sessions || 0);
      setT('esf-steps', steps || 0);
      setT('esf-sops', sops || 0);
      setT('esf-score', score !== null && score !== undefined ? Number(score).toFixed(3) : '—');
    };
  
    async function loadSecsStats() {
      try {
        var r = await fetch(SECS+'/stats');
        var d = await r.json();
        setT('secs-kpi-sessions', d.twin_loop?.total_sessions||0);
        setT('secs-kpi-steps', d.twin_loop?.total_steps_executed||d.twin_loop?.total_steps||0);
        setT('secs-kpi-sops', d.extractor?.total_sops||0);
        var sc = d.critic?.max_score;
        setT('secs-kpi-score', sc ? Number(sc).toFixed(3) : '—');
      } catch(e) {}
    }
  
    // ═══════════════════════════════════════════════════════════════
    // P0-1 运行时状态机：connecting → online / offline / error
    // ═══════════════════════════════════════════════════════════════
    var _runtimeState = { status:'connecting', mode:'', retryCount:0, pollTimer:null, retryTimer:null };
    var _runtimeBootstrapDone = false;
  
    async function _fetchWithTimeout(url, timeoutMs) {
      var controller = new AbortController();
      var timer = setTimeout(function(){ controller.abort(); }, timeoutMs || 4000);
      try {
        return await fetch(url, { signal: controller.signal });
      } finally {
        clearTimeout(timer);
      }
    }
  
    function _setRuntimeStatus(status, mode, errorMsg) {
      _runtimeState.status = status;
      _runtimeState.mode = mode || '';
      var dot = document.getElementById('secs-runtime-dot');
      var textEl = document.getElementById('secs-runtime-text');
      var spinner = document.getElementById('secs-runtime-spinner');
      if (!dot || !textEl) return;
  
      // 清除所有状态class
      dot.className = 'runtime-dot ' + status;
      textEl.className = 'runtime-text';
  
      if (spinner) spinner.style.display = status === 'connecting' ? '' : 'none';
  
      switch (status) {
      case 'connecting':
        textEl.innerHTML = (spinner ? '' : '<span class="runtime-spinner"></span>') + '连接中...';
        textEl.style.cursor = 'default';
        break;
      case 'online':
        textEl.innerHTML = (mode || 'SECS') + ' · 在线';
        textEl.style.c
  ```
  
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
  
  
  ## 协作拓扑（执行时生效）
  
  ## 协作拓扑（任务执行生效）
  
  ### 协作者
  - 🤖 bad20104 (`bad20104`) — 协作者
  - 🤖 Developer (`build_developer` · developer) — 协作者, 同队编制, 通道:build_bus
  - 🤖 Doc Writer (`build_doc_writer` · documentation) — 协作者, 同队编制, 通道:build_bus
  
  ### 通道协作
  - 🤖 Deployer (`build_deployer` · devops) — 同队编制, 通道:build_bus
  - 🤖 PM (`build_pm` · project_manager) — 同队编制, 通道:build_bus
  - 🤖 Researcher (`build_researcher` · researcher) — 同队编制, 通道:build_bus
  - 🤖 Tester (`build_tester` · qa_engineer) — 同队编制, 通道:build_bus
  
  规则：可委派/交接/发消息的对象须在上述名单内（同队编制、共总线、门禁边任一即可）。 hard 门禁下名单外对象会被拒绝。
  
  本步由 `build_researcher` 交接而来，路径=channel:build_bus layers=['team_peer', 'channel:build_bus']
  
  委派/发消息请使用 list_agents 与上述名单内对象；broadcast 须绑定通道 publish 权限。
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

# 巡检监控员 — 技术方案设计

## 1. 概述

### 1.1 角色定义
巡检监控员是 AgentsGroup2026 系统中的自动化巡检与健康监控模块，负责：
- 定期对 Agent 团队、任务队列、资源消耗、系统日志进行健康检查
- 生成巡��报告（含异常告警、趋势分析）
- 提供可视化仪表盘，支持手动触发巡检与历史回溯

### 1.2 设计目标
- **低侵入**：复用现有 API 与数据模型，不破坏已有业务逻辑
- **可扩展**：巡检项可配置（如 Agent 存活、任务积压、Token 超限、错误率）
- **实时性**：支持 SSE 推送巡检进度与结果
- **可观测**：所有巡检记录持久化，支持导出与审计

### 1.3 依赖关系
- 依赖任务 2（假设为“团队配置与任务管理”），需使用 `/api/v1/teams`、`/api/v1/tasks`、`/api/v1/agent-employee` 等接口
- 依赖现有前端组件（`agent-team-config.html`、`tasks.html`、`cost-dashboard.html`）

---

## 2. 技术方案

### 2.1 整体架构

```
┌─────────────────────────────────────────────────────┐
│                   前端 (HTML+JS)                      │
│  inspection-dashboard.html                          │
│  js/inspection.js                                   │
│  css/inspection.css                                 │
└──────────────┬──────────────────────────────────────┘
               │ HTTP / SSE
               ▼
┌─────────────────────────────────────────────────────┐
│                后端 (Python FastAPI)                  │
│  inspection_api.py                                  │
│  inspection_service.py (核心逻辑)                    │
│  inspection_scheduler.py (定时任务)                  │
└──────────────┬──────────────���───────────────────────┘
               │ 读写
               ▼
┌─────────────────────────────────────────────────────┐
│              数据存储 (SQLite / PostgreSQL)           │
│  inspection_reports 表                               │
│  inspection_items 表                                 │
└─────────────────────────────────────────────────────┘
```

### 2.2 后端设计

#### 2.2.1 新增文件

| 文件 | 说明 |
|------|------|
| `src/backend/inspection_api.py` | 巡检 API 路由 |
| `src/backend/inspection_service.py` | 巡检核心逻辑（检查项执行、报告生成） |
| `src/backend/inspection_scheduler.py` | 定时巡检调度器（可选，基于 APScheduler） |

#### 2.2.2 数据模型

```python
# inspection_service.py 中定义
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class InspectionItem(BaseModel):
    item_id: str          # 唯一标识
    category: str         # agent / task / token / error / system
    name: str             # 检查项名称
    status: str           # ok / warning / critical
    message: str          # 描述
    detail: Optional[dict] = None

class InspectionReport(BaseModel):
    report_id: str
    team_id: str
    started_at: datetime
    finished_at: Optional[datetime] = None
    status: str           # running / completed / failed
    summary: dict         # {"total": 10, "ok": 8, "warning": 1, "critical": 1}
    items: List[InspectionItem]
    triggered_by: str     # manual / scheduled
```

#### 2.2.3 API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/v1/inspection/run` | 触发一次巡检（可指定 team_id） |
| GET  | `/api/v1/inspection/reports` | 获取历史报告列表（分页） |
| GET  | `/api/v1/inspection/reports/{report_id}` | 获取单个报告详情 |
| GET  | `/api/v1/inspection/status` | 获取当前是否有巡检正在运行 |
| GET  | `/api/v1/inspection/stream` | SSE 推送巡检进度（可选） |

**请求/响应示例**：

```json
POST /api/v1/inspection/run
{
  "team_id": "team-abc123",
  "categories": ["agent", "task", "token"]  // 可选，默认全部
}

Response 202:
{
  "report_id": "rpt-20260321-001",
  "status": "running",
  "started_at": "2026-03-21T10:00:00Z"
}
```

#### 2.2.4 巡检项实现（inspection_service.py）

```python
class InspectionService:
    def __init__(self, db_session):
        self.db = db_session

    async def run_inspection(self, team_id: str, categories: List[str] = None) -> InspectionReport:
        report = InspectionReport(
            report_id=f"rpt-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
            team_id=team_id,
            started_at=datetime.utcnow(),
            status="running",
            triggered_by="manual"
        )
        items = []
        # 1. Agent 健康检查
        if not categories or "agent" in categories:
            items += await self._check_agents(team_id)
        # 2. 任务队列检查
        if not categories or "task" in categories:
            items += await self._check_tasks(team_id)
        # 3. Token 消耗检查
        if not categories or "token" in categories:
            items += await self._check_token(team_id)
        # 4. 错误日志检查
        if not categories or "error" in categories:
            items += await self._check_errors(team_id)
        # 5. 系统资源检查（可选）
        if not categories or "system" in categories:
            items += await self._check_system()

        report.items = items
        report.summary = self._summarize(items)
        report.status = "completed"
        report.finished_at = datetime.utcnow()
        # 持久化到数据库
        await self._save_report(report)
        return report

    async def _check_agents(self, team_id):
        # 调用 /api/v1/teams/{team_id}/agents 获取所有 Agent
        # 检查：状态是否为 idle/working，最后活跃时间是否超过阈值，技能是否缺失
        items = []
        agents = await self._fetch_agents(team_id)
        for agent in agents:
            if agent.state not in ("idle", "working"):
                items.append(InspectionItem(
                    item_id=f"agent-{agent.id}",
                    category="agent",
                    name=f"Agent {agent.name} 状态异常",
                    status="critical",
                    message=f"当前状态: {agent.state}"
                ))
            # 检查最后活跃时间
            if agent.last_active and (datetime.utcnow() - agent.last_active).days > 7:
                items.append(InspectionItem(
                    item_id=f"agent-{agent.id}-inactive",
                    category="agent",
                    name=f"Agent {agent.name} 长期未活跃",
                    status="warning",
                    message=f"最后活跃: {agent.last_active}"
                ))
        return items

    async def _check_tasks(self, team_id):
        # 调用 /api/v1/teams/{team_id}/tasks 获取任务列表
        # 检查：是否有大量 pending 任务，是否有失败任务
        items = []
        tasks = await self._fetch_tasks(team_id)
        pending = [t for t in tasks if t.status == "pending"]
        failed = [t for t in tasks if t.status == "failed"]
        if len(pending) > 20:
            items.append(InspectionItem(
                item_id="task-pending-high",
                category="task",
                name="待处理任务过多",
                status="warning",
                message=f"当前 {len(pending)} 个 pending 任务"
            ))
        if len(failed) > 5:
            items.append(InspectionItem(
                item_id="task-failed-high",
                category="task",
                name="失败任务过多",
                status="critical",
                message=f"当前 {len(failed)} 个 failed 任务"
            ))
        return items

    async def _check_token(self, team_id):
        # 调用 /api/v1/teams/{team_id}/cost 获取 Token 消耗
        # 检查：是否接近预算上限
        items = []
        cost = await self._fetch_cost(team_id)
        if cost.usage_ratio > 0.9:
            items.append(InspectionItem(
                item_id="token-budget-critical",
                category="token",
                name="Token 预算即将耗尽",
                status="critical",
                message=f"已使用 {cost.used}/{cost.budget} ({cost.usage_ratio*100:.1f}%)"
            ))
        return items

    async def _check_errors(self, team_id):
        # 调用 /api/v1/teams/{team_id}/logs?level=error 获取错误日志
        # 检查：最近 1 小时错误数
        items = []
        logs = await self._fetch_error_logs(team_id, hours=1)
        if len(logs) > 10:
            items.append(InspectionItem(
                item_id="error-rate-high",
                category="error",
                name="错误率过高",
                status="critical",
                message=f"最近 1 小时 {len(logs)} 条错误"
            ))
        return items

    def _summarize(self, items):
        total = len(items)
        ok = sum(1 for i in items if i.status == "ok")
        warning = sum(1 for i in items if i.status == "warning")
        critical = sum(1 for i in items if i.status == "critical")
        return {"total": total, "ok": ok, "warning": warning, "critical": critical}
```

#### 2.2.5 定时调度（inspection_scheduler.py）

```python
# 使用 APScheduler 实现定时巡检（可选）
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

async def scheduled_inspection():
    # 获取所有团队 ID
    teams = await fetch_all_teams()
    for team in teams:
        await inspection_service.run_inspection(team.id, triggered_by="scheduled")

def start_scheduler():
    scheduler.add_job(scheduled_inspection, 'interval', hours=6)
    scheduler.start()
```

### 2.3 前端设计

#### 2.3.1 新增文件

| 文件 | 说明 |
|------|------|
| `src/frontend/inspection-dashboard.html` | 巡检监控页面 |
| `src/frontend/js/inspection.js` | 巡检逻辑（触发、渲染、SSE 监听） |
| `src/frontend/css/inspection.css` | 页面样式 |

#### 2.3.2 页面布局

```
┌─────────────────────────────────────────────────────┐
│  Topbar (复用现有组件)                                │
├─────────────────────────────────────────────────────┤
│  左侧导航 (复用 sidebar)                              │
│  ┌─────────────────────────────────────────────────┐│
│  │  巡检仪表盘                                      ││
│  │  ┌──────────┬──────────┬──────────┬──────────┐ ││
│  │  │ 总巡检次数 │ 健康率   │ 告警数   │ 上次巡检 │ ││
│  │  ├──────────┼──────────┼──────────┼──────────┤ ││
│  │  │  12      │  85%     │  3       │ 10分钟前 │ ││
│  │  └──────────┴──────────┴──────────┴──────────┘ ││
│  │  ┌─────────────────────────────────────────────┐││
│  │  │  巡检项分类图表 (饼图/柱状图)                 │││
│  │  └─────────────────────────────────────────────┘││
│  │  ┌─────────────────────────────────────────────┐││
│  │  │  最近巡检报告列表 (表格)                     │││
│  │  │  ID | 时间 | 状态 | 摘要 | 操作              │││
│  │  └─────────────────────────────────────────────┘││
│  │  ┌─────────────────────────────────────────────┐││
│  │  │  手动触发按钮 + 选择团队/分类                │││
│  │  └─────────────────────────────────────────────┘││
│  └─────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

#### 2.3.3 核心 JS 逻辑（inspection.js）

```javascript
// 全局对象
const Inspection = {
  currentReportId: null,
  sse: null,

  // 初始化页面
  async init() {
    this.loadStats();
    this.loadReports();
    this.bindEvents();
  },

  // 加载统计概览
  async loadStats() {
    const reports = await api('/api/v1/inspection/reports?limit=100');
    const total = reports.length;
    const okRate = reports.filter(r => r.summary.critical === 0).length / total * 100;
    const alerts = reports.reduce((sum, r) => sum + r.summary.critical, 0);
    const last = reports[0]?.finished_at || '无';
    document.getElementById('inspection-total').textContent = total;
    document.getElementById('inspection-health-rate').textContent = `${okRate.toFixed(0)}%`;
    document.getElementById('inspection-alerts').textContent = alerts;
    document.getElementById('inspection-last').textContent = last;
  },

  // 加载报告列表
  async loadReports(page = 1) {
    const data = await api(`/api/v1/inspection/reports?page=${page}&limit=20`);
    const tbody = document.getElementById('inspection-reports-tbody');
    tbody.innerHTML = data.items.map(r => `
      <tr>
        <td>${r.report_id}</td>
        <td>${r.finished_at || r.started_at}</td>
        <td><span class="badge ${r.status}">${r.status}</span></td>
        <td>✅ ${r.summary.ok} ⚠️ ${r.summary.warning} ❌ ${r.summary.critical}</td>
        <td><button onclick="Inspection.viewReport('${r.report_id}')">查看</button></td>
      </tr>
    `).join('');
  },

  // 触发巡检
  async runInspection() {
    const teamId = document.getElementById('inspection-team-select').value;
    const categories = Array.from(document.querySelectorAll('input[name="inspection-cat"]:checked'))
      .map(cb => cb.value);
    const btn = document.getElementById('inspection-run-btn');
    btn.disabled = true;
    btn.textContent = '⏳ 运行中...';
    try {
      const res = await api('/api/v1/inspection/run', {
        method: 'POST',
        body: JSON.stringify({ team_id: teamId, categories })
      });
      this.currentReportId = res.report_id;
      // 启动 SSE 监听进度
      this.startSSE(res.report_id);
    } catch (e) {
      showToast('巡检启动失败', 'error');
      btn.disabled = false;
      btn.textContent = '▶ 运行巡检';
    }
  },

  // SSE 监听
  startSSE(reportId) {
    if (this.sse) this.sse.close();
    this.sse = new EventSource(`/api/v1/inspection/stream?report_id=${reportId}`);
    this.sse.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'progress') {
        document.getElementById('inspection-progress').textContent = 
          `进度: ${data.done}/${data.total}`;
      } else if (data.type === 'completed') {
        this.sse.close();
        document.getElementById('inspection-run-btn').disabled = false;
        document.getElementById('inspection-run-btn').textContent = '▶ 运行巡检';
        showToast('巡检完成', 'success');
        this.loadReports();
        this.loadStats();
      }
    };
    this.sse.onerror = () => {
      this.sse.close();
      document.getElementById('inspection-run-btn').disabled = false;
      document.getElementById('inspection-run-btn').textContent = '▶ 运行巡检';
    };
  },

  // 查看报告详情
  async viewReport(reportId) {
    const report = await api(`/api/v1/inspection/reports/${reportId}`);
    // 渲染模态框或跳转详情页
    renderReportDetail(report);
  }
};

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', () => Inspection.init());
```

#### 2.3.4 导航集成

修改 `src/frontend/agent-team-config.html` 中的 topbar 导航，增加“巡检监控”链接：

```html
<nav class="topbar-ws__nav" aria-label="主导航" data-nav-auto>
  <a href="/agent-team-config.html">智能体团队</a>
  <a href="/plaza.html">议事广场</a>
  <a href="/skill-extract.html">技能萃取</a>
  <a href="/Agent-digital-twin.html?office3d=1">数字孪生</a>
  <a href="/cost-dashboard.html">Token节省</a>
  <a href="/inspection-dashboard.html">巡检监控</a>   <!-- 新增 -->
  <a href="/pet-config.html">生态配置</a>
</nav>
```

### 2.4 数据库表结构（SQLite）

```sql
CREATE TABLE inspection_reports (
    report_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    status TEXT NOT NULL DEFAULT 'running',
    summary TEXT,  -- JSON
    triggered_by TEXT DEFAULT 'manual',
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE inspection_items (
    item_id TEXT PRIMARY KEY,
    report_id TEXT NOT NULL,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    message TEXT,
    detail TEXT,  -- JSON
    FOREIGN KEY (report_id) REFERENCES inspection_reports(report_id)
);
```

---

## 3. 需要修改的文件清单

| 文件 | 修改类型 | 说明 |
|------|----------|------|
| `src/backend/main.py` | 修改 | 注册 `inspection_api.py` 路由 |
| `src/backend/config.py` | 修改 | 添加巡检相关配置（如定时间隔） |
| `src/frontend/agent-team-config.html` | 修改 | 导航栏增加“巡检监控”链接 |
| `src/frontend/js/global-nav.js` | 修改 | 可选，同步导航高亮逻辑 |
| `src/frontend/css/base.css` | 修改 | 可选，增加巡检相关样式变量 |

**新增文件**：
- `src/backend/inspection_api.py`
- `src/backend/inspection_service.py`
- `src/backend/inspection_scheduler.py`（可选）
- `src/frontend/inspection-dashboard.html`
- `src/frontend/js/inspection.js`
- `src/frontend/css/inspection.css`

---

## 4. 接口规范汇总

| 接口 | 方法 | 请求参数 | 响应 | 说明 |
|------|------|----------|------|------|
| `/api/v1/inspection/run` | POST | `{team_id, categories?}` | `{report_id, status, started_at}` | 触发巡检 |
| `/api/v1/inspection/reports` | GET | `page, limit, team_id?` | `{items: [...], total, page, limit}` | 分页列表 |
| `/api/v1/inspection/reports/{id}` | GET | - | `InspectionReport` | 详情 |
| `/api/v1/inspection/status` | GET | - | `{running: bool, report_id?}` | 当前状态 |
| `/api/v1/inspection/stream` | GET | `report_id` | SSE 事件流 | 进度推送 |

---

## 5. 实施步骤（开发工程师指南）

### Step 1: 后端数据模型与存储
- 在 `src/backend/` 下创建 `inspection_service.py`，实现 `InspectionReport`、`InspectionItem` 数据类
- 使用现有数据库（SQLite）创建表，或集成到现有 ORM（如 SQLAlchemy）
- 实现 `save_report`、`get_report`、`list_reports` 方法

### Step 2: 后端巡检逻辑
- 在 `inspection_service.py` 中实现 `_check_agents`、`_check_tasks`、`_check_token`、`_check_errors` 等方法
- 复用现有 API 调用（如 `fetch` 到内部 `/api/v1/teams/...`）
- 注意异常处理与超时

### Step 3: 后端 API 路由
- 创建 `inspection_api.py`，注册路由
- 在 `main.py` 中 `app.include_router(inspection_router)`
- 实现 SSE 端点（使用 `StreamingResponse`）

### Step 4: 前端页面
- 创建 `inspection-dashboard.html`，引用 `inspection.js` 和 `inspection.css`
- 实现统计卡片、报告列表、触发按钮、进度条
- 集成 SSE 监听

### Step 5: 导航集成
- 修改 `agent-team-config.html` 的 topbar 导航
- 确保新页面可正常访问

### Step 6: 测试
- 后端单元测试：`src/backend/tests/test_inspection.py`
- 前端测试：`src/frontend/__tests__/inspection.test.js`
- 手动测试：触发巡检、查看报告、SSE 推送

---

## 6. 风险与注意事项

- **性能**：巡检可能涉及大量 API 调用，建议使用异步并发（`asyncio.gather`）并设置超时
- **数据一致性**：巡检报告中的快照数据可能与实时数据有偏差，需在报告中注明时间戳
- **权限**：巡检 API 应继承现有认证机制（CSRF Token、Session）
- **定时任务**：若使用 APScheduler，需确保单实例运行，避免重复触发

---

## 7. 附录：巡检项扩展建议

| 类别 | 检查项 | 阈值 | 严重级别 |
|------|--------|------|----------|
| agent | Agent 状态异常 | 非 idle/working | critical |
| agent | Agent 长期未活跃 | >7天 | warning |
| task | 待处理任务过多 | >20 | warning |
| task | 失败任务过多 | >5 | critical |
| token | 预算使用率 >90% | >90% | critical |
| token | 预算使用率 >80% | >80% | warning |
| error | 最近1小时错误数 | >10 | critical |
| error | 最近1小时警告数 | >50 | warning |
| system | 后端响应延迟 | >5s | warning |

---

以上方案基于现有项目结构设计，所有修改均指向实际存在的文件路径。开发工程师可按照实施步骤逐步完成。

────────────────────────────────────────────────────────────
✅ glm-5.1 完成
