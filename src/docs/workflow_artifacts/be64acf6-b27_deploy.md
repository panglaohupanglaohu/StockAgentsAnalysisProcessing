# 部署上线 — devops

任务: 完成北美 AI 项目区域合规与部署限制检查
步骤: deploy
Agent: build_deployer

---

📋 任务: be64acf6-b27
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
  完成北美 AI 项目区域合规与部署限制检查
  负责角色: 北美 AI 项目运维员
  依赖: 任务2
  预期产出: 合规检查表、区域部署准入结论
  负责角色: 北美 AI 项目运维员
  执行智能体: build_deploy
  依赖: 任务2
  预期产出: 合规检查表、区域部署准入结论
  
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
              }
            : {
                id: a.id, name: a.name || a.id, role: a.role || '', team: a.team || '',
                collar: COLLARS[i % COLLARS.length], activity: 'working',
                deskIndex: nextFree++, layer: state.mirror ? 'mirror' : 'prod',
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
      default:
        break;
    }
    return state;
  }
  
  /** 协作热度排行 —— 考察「哪些 Agent 之间的协作是可取的」的数据基础 */
  export function collabStats(state, limit) {
    return Object.entries(state.collab)
      .map(([pair, count]) => ({ pair, count }))
      .sort((a, b) => b.count - a.count)
      .slice(0, limit || 5);
  }
  
  /** 简易 store */
  export function createStore() {
    let state = initialState();
    const listeners = new Set();
    return {
      getState: () => state,
      dispatch(event) {
        state = reduce(state, event);
        listeners.forEach((fn
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
   
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 04: develop
  任务: 完成北美 AI 项目区域合规与部署限制检查
  Agent: build_developer
  📋 任务: be64acf6-b27
  🤖 Agent: Developer (developer)
  📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
  🔧 执行方式: Claude Code CLI
  ────────────────────────────────────────────────────────────
  你是 AgentsGroup2026 系统的 Developer (developer)。
  你是开发工程师 (DeepSeek V4 + 工具循环模式)。
  你**已经被赋予真正的工具能力**: read_file / grep / list_files / write_file / patch_file / run_python。
  禁止凭空想象 — 所有写代码前必须先用工具读真实代码。
  完成北美 AI 项目区域合规与部署限制检查
  负责角色: 北美 AI 项目运维员
  预期产出: 合规检查表、区域部署准入结论
  负责角色: 北美 AI 项目运维员
  
  ### 步骤 05: test (完整产出)
  
  # 测试验证 — qa_engineer
  
  任务: 完成北美 AI 项目区域合规与部署限制检查
  步骤: test
  Agent: build_tester
  
  ---
  
  📋 任务: be64acf6-b27
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
    完成北美 AI 项目区域合规与部署限制检查
    负责角色: 北美 AI 项目运维员
    依赖: 任务2
    预期产出: 合规检查表、区域部署准入结论
    负责角色: 北美 AI 项目运维员
    执行智能体: build_deploy
    依赖: 任务2
    预期产出: 合规检查表、区域部署准入结论
    
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
                }
              : {
                  id: a.id, name: a.name || a.id, role: a.role || '', team: a.team || '',
                  collar: COLLARS[i % COLLARS.length], activity: 'working',
                  deskIndex: nextFree++, layer: state.mirror ? 'mirror' : 'prod',
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
        default:
          break;
      }
      return state;
    }
    
    /** 协作热度排行 —— 考察「哪些 Agent 之间的协作是可取的」的数据基础 */
    export function collabStats(state, limit) {
      return Object.entries(state.collab)
        .map(([pair, count]) => ({ pair, count }))
        .sort((a, b) => b.count - a.count)
        .slice(0, limit || 5);
    }
    
    /** 简易 store */
    export function createStore() {
      let state = initialState();
      const listeners = new Set();
      return {
        getState: () => state,
        dispatch(event) {
          state = reduce(state, event);
          listeners.forEach((fn
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
        def test_build_from_text_p
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
⏳ 等待 DeepSeek 响应... (180s)
API Error: Unable to connect to API (ConnectionRefused)


⚠️ Claude Code 退出码: 1
