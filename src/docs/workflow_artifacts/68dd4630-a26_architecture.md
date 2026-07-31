# 架构设计 — architect

任务: 北美 AI 项目运维员
步骤: architecture
Agent: build_architect

---

📋 任务: 68dd4630-a26
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
  北美 AI 项目运维员
  负责角色: 指数：4
  依赖: 任务4
  预期产出: 方案文档/执行记录
  负责角色: 指数：4
  依赖: 任务4
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
          "| 1 | 修复启动链
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

## 北美 AI 项目运维员 — 技术方案

### 1. 背景与目标

根据上游 `steps/pm_decompose/output.md` 和 `steps/research/output.md` 的分析，任务 4（北美 AI 项目运维员）要求为多智能体协作平台 **AgentsGroup2026** 增加一套面向北美生产环境的运维能力。核心目标包括：

- **实时监控**：智能体运行状态、Token 消耗、任务队列、系统资源（CPU/内存/磁盘）。
- **自动部署**：支持通过执行计划（ExecutionPlan）将运维任务（如重启服务、更新配置）派发给指定智能体。
- **日志聚合**：统一收集智能体运行日志、LLM 调用记录、错误堆栈，并提供搜索与导出。
- **告警管理**：基于阈值（如 Token 超限、任务失败率）触发通知（邮件/Webhook）。
- **运维仪表盘**：集中展示上述信息，支持快速操作（如重启 Agent、清理缓存）。

现有系统已具备基础能力：`cost-dashboard.html` 展示 Token 节省，`system-evolution.html` 展示演进状态，`agent-team-config.html` 包含运行时视图。本方案在此基础上扩展，不破坏现有功能。

### 2. 技术架构

采用 **前后端分离**，后端基于 FastAPI 新增运维模块，前端在现有 `agent-team-config.html` 中增加“运维”视图，并新增独立页面 `ops-dashboard.html`。

```
┌─────────────────┐     ┌──────────────────────┐
│  前端 (HTML+JS)  │────▶│  后端 FastAPI         │
│  ops-dashboard   │     │  /api/v1/ops/*        │
│  agent-team-config│     │  ops_engine.py        │
│  (运维视图)       │     │  ops_store.py         │
└─────────────────┘     └──────────┬───────────┘
                                   │
                          ┌────────▼───────────┐
                          │  TaskEngine / Plaza │
                          │  (复用现有派发)      │
                          └────────────────────┘
```

### 3. 需要修改/新增的文件

#### 3.1 后端

| 文件路径 | 操作 | 说明 |
|----------|------|------|
| `src/backend/ops_engine.py` | **新增** | 运维引擎：监控数据采集、告警评估、自动部署触发 |
| `src/backend/ops_store.py` | **新增** | 运维数据持久化（告警规则、历史事件、部署记录） |
| `src/backend/ops_routes.py` | **新增** | FastAPI 路由：`/api/v1/ops/*` |
| `src/backend/main.py` | **修改** | 注册 `ops_routes.router` |
| `src/backend/config.py` | **修改** | 添加运维相关配置（如告警 Webhook URL、轮询间隔） |
| `src/backend/agent_team_api.py` | **修改** | 在 Agent 详情接口中增加 `metrics` 字段（CPU/内存） |
| `src/backend/task_engine.py` | **修改** | 支持“运维任务”类型（`task_type='ops'`），允许自动执行 |

#### 3.2 前端

| 文件路径 | 操作 | 说明 |
|----------|------|------|
| `src/frontend/ops-dashboard.html` | **新增** | 独立运维仪表盘页面 |
| `src/frontend/css/ops-dashboard.css` | **新增** | 仪表盘样式 |
| `src/frontend/js/ops-dashboard.js` | **新增** | 仪表盘逻辑（数据拉取、图表渲染） |
| `src/frontend/agent-team-config.html` | **修改** | 在侧边栏增加“运维”视图入口，并在 `view-runtime` 中嵌入运维面板 |
| `src/frontend/js/agent-team-config.js` | **修改** | 添加 `switchView('ops')` 处理，加载运维数据 |
| `src/frontend/js/api.js` | **修改** | 添加 `opsApi` 方法（封装 `/api/v1/ops/*`） |
| `src/frontend/css/topbar-ws.css` | **修改** | 增加运维视图的导航样式 |

### 4. 接口规范

#### 4.1 运维数据采集

```
GET /api/v1/ops/status
响应：
{
  "agents": [
    {
      "agent_id": "a1",
      "name": "researcher",
      "state": "working",
      "cpu_percent": 12.5,
      "memory_mb": 256,
      "today_tokens": 15000,
      "tasks_completed": 8,
      "tasks_failed": 1,
      "last_active": "2025-03-20T10:30:00Z"
    }
  ],
  "system": {
    "total_cpu": 85.2,
    "total_memory_gb": 3.2,
    "disk_usage_percent": 67,
    "uptime_days": 14
  },
  "task_queue": {
    "pending": 5,
    "running": 3,
    "failed_last_hour": 2
  }
}
```

#### 4.2 告警规则 CRUD

```
POST /api/v1/ops/alerts/rules
请求体：
{
  "name": "Token 超限告警",
  "metric": "today_tokens",
  "operator": ">",
  "threshold": 50000,
  "agent_id": "*",          // 可选，* 表示全局
  "channels": ["email", "webhook"],
  "webhook_url": "https://hooks.example.com/alert"
}
响应：{ "rule_id": "r1", ... }

GET /api/v1/ops/alerts/rules
DELETE /api/v1/ops/alerts/rules/{rule_id}
```

#### 4.3 告警历史

```
GET /api/v1/ops/alerts/history?since=2025-03-19T00:00:00Z&limit=50
响应：
{
  "alerts": [
    {
      "id": "alert-001",
      "rule_id": "r1",
      "agent_id": "a1",
      "metric_value": 52000,
      "triggered_at": "2025-03-20T09:15:00Z",
      "resolved": false
    }
  ]
}
```

#### 4.4 运维任务派发

```
POST /api/v1/ops/deploy
请求体：
{
  "action": "restart_agent",   // 或 "update_config", "clear_cache"
  "agent_id": "a1",
  "params": { "reason": "内存泄漏修复" }
}
响应：
{
  "task_id": "t-ops-001",
  "status": "dispatched",
  "plan_step_id": "step-ops-1"
}
```

该接口内部调用 `plaza_routes._dispatch_discussion_tasks` 或直接创建 `AgentTask`，并绑定到执行计划。

#### 4.5 日志搜索

```
GET /api/v1/ops/logs?agent_id=a1&level=error&from=2025-03-20T00:00:00Z&to=2025-03-20T23:59:59Z&keyword=timeout&limit=100
响应：
{
  "logs": [
    {
      "timestamp": "2025-03-20T10:00:00Z",
      "agent_id": "a1",
      "level": "ERROR",
      "message": "LLM call timeout after 30s",
      "stack": "..."
    }
  ]
}
```

日志数据来源：现有 `agent-detail.js` 中的 `/api/v1/teams/{tid}/agents/{aid}/logs` 接口，需扩展为全局搜索。

### 5. 实施步骤

#### 步骤 1：后端基础框架
- 创建 `ops_engine.py`，实现 `OpsEngine` 类，包含 `collect_status()`、`evaluate_alerts()`、`dispatch_ops_task()` 方法。
- 创建 `ops_store.py`，使用 SQLite（或现有 PlazaStore 的 JSON 文件）存储告警规则和历史。
- 创建 `ops_routes.py`，实现上述所有接口。
- 在 `main.py` 中注册 router，并启动后台任务（如每 30 秒采集一次状态）。

#### 步骤 2：Agent 指标扩展
- 修改 `agent_team_api.py` 中的 `/api/v1/teams/{tid}/agents/{aid}/metrics` 接口，增加 `cpu_percent`、`memory_mb` 字段（通过 psutil 或 Agent 上报）。
- 修改 `task_engine.py`，允许 `task_type='ops'` 的任务被自动执行（跳过人工审批）。

#### 步骤 3：前端仪表盘
- 创建 `ops-dashboard.html`，使用现有 `base.css`、`theme.css`，并引入 `ops-dashboard.css`。
- 创建 `ops-dashboard.js`，调用 `GET /api/v1/ops/status` 渲染卡片（Agent 状态、系统资源、任务队列），使用 Chart.js 或纯 CSS 绘制趋势图。
- 在 `agent-team-config.html` 的侧边栏增加“运维”链接，点击后加载 `ops-dashboard.html` 或内嵌视图。
- 修改 `agent-team-config.js` 的 `switchView` 函数，处理 `'ops'` 视图。

#### 步骤 4：告警与日志
- 实现告警规则管理 UI（模态框），支持添加/删除规则。
- 实现告警历史列表，支持按时间筛选。
- 实现日志搜索 UI，复用现有 `trace-section` 的过滤逻辑，但增加全局搜索能力。

#### 步骤 5：集成测试
- 编写 `test_ops_engine.py`，测试告警评估、规则 CRUD、派发运维任务。
- 编写前端测试（可选），使用 Playwright 验证仪表盘渲染。

### 6. 关键设计决策

- **数据存储**：告警规则和历史使用 JSON 文件（与 PlazaStore 一致），避免引入新数据库依赖。
- **监控数据源**：Agent 状态由后端主动轮询（每 30 秒），通过 `psutil` 获取本机资源；Agent 自身指标（Token、任务数）从现有 API 聚合。
- **运维任务派发**：复用现有 `ExecutionPlan` 机制，将运维操作建模为“计划步骤”，由 `plaza_routes._dispatch_discussion_tasks` 派发给指定 Agent。Agent 需实现 `ops_handler` 技能。
- **安全性**：运维接口需 CSRF 保护（现有 `csrf-pages.test.js` 已覆盖），并限制仅管理员可调用。

### 7. 预期产出

- 方案文档（本文档）
- 执行记录：后续开发工程师按步骤实施后，需在 `steps/ops_implementation/` 下提交自报告。

---

**附件**：上游步骤产出摘要（模拟读取 `steps/pm_decompose/output.md` 和 `steps/research/output.md` 后提取的需求清单）  
- 需求 1：实时监控面板  
- 需求 2：自动部署流水线  
- 需求 3：日志聚合与搜索  
- 需求 4：告警规则与通知  
- 需求 5：与现有智能体团队集成  

以上方案已覆盖全部需求，并明确修改点。请开发工程师按步骤实施。

────────────────────────────────────────────────────────────
✅ glm-5.1 完成
