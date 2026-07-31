# 架构设计 — architect

任务: 完成北美 AI 项目区域合规与部署限制检查
步骤: architecture
Agent: build_architect

---

📋 任务: 2920f571-f5a
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
  完成北美 AI 项目区域合规与部署限制检查
  负责角色: 北美 AI 项目运维员
  依赖: 任务2
  预期产出: 合规检查表、区域部署准入结论
  负责角色: 北美 AI 项目运维员
  依赖: 任务2
  预期产出: 合规检查表、区域部署准入结论
  
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
  ... (共 1572 个 src/ 文件)
  
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
  
  ### 文件: `src/backend/agent_team_api.py`
  ```py
  # -*- coding: utf-8 -*-
  """
  Agent Team API Routes - 双团队管理 REST API
  
  提供构建团队 & 执行团队的状态查询、KPI 考核、
  任务分配、报告查询等端点。挂载至 FastAPI 的 router。
  """
  
  from __future__ import annotations
  
  from fastapi import APIRouter, HTTPException, Query
  from pydantic import BaseModel, Field
  from typing import Any, Dict, List, Optional
  
  router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
  
  try:
      from config import DEFAULT_PAGE_SIZE as _DEFAULT_PAGE_SIZE
      from config import MAX_PAGE_SIZE as _MAX_PAGE_SIZE
  except Exception:
      _DEFAULT_PAGE_SIZE = 50
      _MAX_PAGE_SIZE = 200
  
  
  # ---------------------------------------------------------------------------
  # 全局引用（在 main.py startup 时注入）
  # ---------------------------------------------------------------------------
  _build_team = None
  _execution_team = None
  _scheduler = None
  _evolution_engine = None
  
  
  def _paginate_optional(items: List[Dict[str, Any]], *, limit: int, offset: int) -> Any:
      """Preserve old array responses by default while enabling optional pagination."""
      limit = getattr(limit, "default", limit)
      offset = getattr(offset, "default", offset)
      limit = int(limit or 0)
      offset = max(int(offset or 0), 0)
      if limit <= 0 and offset <= 0:
          return items
      if limit <= 0:
          limit = _DEFAULT_PAGE_SIZE
      limit = min(limit, _MAX_PAGE_SIZE)
      total = len(items)
      return {
          "items": items[offset:offset + limit],
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  def set_teams(build_team, execution_team, scheduler, evolution_engine=None):
      """在应用启动时由 main.py 调用，注入团队实例."""
      global _build_team, _execution_team, _scheduler, _evolution_engine
      _build_team = build_team
      _execution_team = execution_team
      _scheduler = scheduler
      _evolution_engine = evolution_engine
  
  
  # ---------------------------------------------------------------------------
  # Request / Response Models
  # ---------------------------------------------------------------------------
  
  class TaskAssignment(BaseModel):
      agent_id: str
      task: str
  
  
  class EvolutionCloseRequest(BaseModel):
      reason: str = Field(default="", description="关闭理由")
      verify_conclusion: str = Field(default="", description="验证结论")
  
  
  class EvolutionCompleteRequest(BaseModel):
      code_changes: List[str] = Field(default_factory=list, description="构建阶段产生的代码或配置变更")
      artifact_dir: str = Field(default="", description="构建阶段产物目录")
  
  
  class FeedbackSubmission(BaseModel):
      category: str = "optimization"
      severity: str = "medium"
      title: str
      detail: str
  
  # ── 演化优化请求模型 ──────────────────────────────────────────
  
  class OptimizeRequest(BaseModel):
      target_type: str = "skill"
      target_id: str = ""
      team_id: str = "build_system"
      iterations: int = Field(default=5, ge=1, le=10)
      content: str = ""
  
  class AutoTriageRequest(BaseModel):
      team_id: str = "build_system"
      top_n: int = Field(default=5, ge=1, le=10)
  
  class DatasetGenerateRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      count: int = Field(default=15, ge=1, le=30)
  
  class ExampleItem(BaseModel):
      task_input: str
      rubric: str
  
  class DatasetManualRequest(BaseModel):
      dataset_id: str = ""
      skill_id: str = ""
      examples: List[ExampleItem] = Field(default_factory=list)
      skill_name: str = ""
  
  class DatasetImportKBRequest(BaseModel):
      skill_id: str = ""
      skill_name: str = ""
      dataset_id: str = ""
      max_examples: int = Field(default=20, ge=1, le=50)
  
  class UpdateExamplesRequest(BaseModel):
      action: str = "replace_all"
      examples: List[ExampleItem] = Field(default_factory=list)
      indices: List[int] = Field(default_factory=list)
      index: int = -1
      example: Optional[ExampleItem] = None
  
  class StepBaselineRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      dataset_id: str = ""
  
  class FailureItem(BaseModel):
      task_input: str = ""
      rubric: str = ""
      composite: float = 0.0
      reasoning: str = ""
  
  class StepReflectRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      failures: List[FailureItem] = Field(default_factory=list)
      user_hints: str = ""
  
  class StepMutateRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      reflection: Dict[str, Any] = Field(default_factory=dict)
  
  class StepEvaluateCandidateRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      dataset_id: str = ""
      instructions: str = ""
  
  class StepApplyRequest(BaseModel):
      skill_id: str = ""
      team_id: str = "build_system"
      instructions: str = ""
      baseline_score: float = 0.0
      new_score: float = 0.0
  
  
  # ---------------------------------------------------------------------------
  # Minimal AgentScheduler — provides basic scheduling status & tick
  # ---------------------------------------------------------------------------
  
  import time as _time
  
  
  class AgentScheduler:
      """轻量级调度器，提供运行状态、tick 计数、报告生成等基本能力。
  
      在 main.py startup 时自动创建并注入，确保前端团队概览的
      「调度器」卡片显示「运行中」而非「已停止」。
      """
  
      def __init__(self) -> None:
          self._started_at = _time.time()
          self._tick_count: int = 0
          self._last_tick_at: float = 0.0
  
      def get_status(self) -> Dict[str, Any]:
          return {
              "running": True,
              "tick_count": self._tick_count,
              "uptime_seconds": _time.time() - self._started_at,
              "last_tick_at": self._last_tick_at if self._last_tick_at else None,
          }
  
      def tick_once(self) -> Dict[str, Any]:
          """手动触发一次 tick（供调试/手动推进）."""
          self._tick_count += 1
          self._last_tick_at = _time.time()
          # 每次 tick 尝试驱动 evolution engine 的审查周期（如果存在）
          try:
              global _evolution_engine
              if _evolution_engine is not None:
                  _evolution_engine.audit()
          except Exception:
              pass
          return {"tick": self._tick_count, "ok": True}
  
      def generate_report_now(self) -> Dict[str, Any]:
          return {
              "status": self.get_status(),
              "summary": (f"调度器已运行 {self.get_status()['uptime_seconds']:.0f} 秒，"
                          f"累计 {self._tick_count} 次 tick"),
          }
  
  
  # ---------------------------------------------------------------------------
  # Scheduler API
  # ---------------------------------------------------------------------------
  
  @router.get("/scheduler/status")
  async def scheduler_status():
      if not _scheduler:
          raise HTTPException(503, "Scheduler not initialized")
      return _scheduler.get_status()
  
  
  @router.post("/scheduler/report")
  async def scheduler_generate_report():
      if not _scheduler:
          raise HTTPException(503, "Scheduler not initialized")
      return _scheduler.generate_report_now()
  
  
  @router.post("/scheduler/tick")
  async def scheduler_tick_once():
      """手动触发一次调度 tick (调试用)."""
      if not _scheduler:
          raise HTTPException(503, "Scheduler not initialized")
      return _scheduler.tick_once()
  
  
  # ---------------------------------------------------------------------------
  # Build Team
  # ---------------------------------------------------------------------------
  
  @router.get("/build/status")
  async def build_team_status():
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      return _build_team.get_status()
  
  
  @router.get("/build/kpis")
  async def build_team_kpis():
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      return _build_team.get_agent_kpis()
  
  
  @router.get("/build/agents/{agent_id}")
  async def build_agent_detail(agent_id: str):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      agent = _build_team.agents.get(agent_id)
      if not agent:
          raise HTTPException(404, f"Agent '{agent_id}' not found")
      return agent.to_dict()
  
  
  @router.post("/build/assign")
  async def build_assign_task(body: TaskAssignment):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      ok = _build_team.assign_task(body.agent_id, body.task)
      if not ok:
          raise HTTPException(404, f"Agent '{body.agent_id}' not found")
      return {"status": "assigned", "agent_id": body.agent_id, "task": body.task}
  
  
  @router.get("/build/reports")
  async def build_reports(
      limit: int = Query(default=10, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      items = [r.to_dict() for r in _build_team.hourly_reports]
      if limit > 0 and offset == 0:
          items = items[-limit:]
          return items
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
  @router.get("/build/issues")
  async def build_issues(
      limit: int = Query(default=0, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      items = list(_build_team.issue_backlog)
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
  # ---------------------------------------------------------------------------
  # Execution Team
  # ---------------------------------------------------------------------------
  
  @router.get("/execution/status")
  async def execution_team_status():
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      return _execution_team.get_status()
  
  
  @router.get("/execution/agents/{agent_id}")
  async def execution_agent_detail(agent_id: str):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      agent = _execution_team.agents.get(agent_id)
      if not agent:
          raise HTTPException(404, f"Agent '{agent_id}' not found")
      return agent.to_dict()
  
  
  @router.get("/execution/reports")
  async def execution_reports(
      limit: int = Query(default=10, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      items = [r.to_dict() for r in _execution_team.execution_reports]
      if limit > 0 and offset == 0:
          items = items[-limit:]
          return items
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
  @router.get("/execution/feedback")
  async def execution_feedback(
      limit: int = Query(default=0, ge=0, le=_MAX_PAGE_SIZE),
      offset: int = Query(default=0, ge=0),
  ):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      items = [item.to_dict() for item in _execution_team.feedback_queue]
      return _paginate_optional(items, limit=limit, offset=offset)
  
  
  @router.post("/execution/feedback")
  async def submit_feedback(body: FeedbackSubmission):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      item = _execution_team.submit_feedback(
          category=body.category,
          severity=body.severity,
          title=body.title,
          detail=body.detail,
      )
      return item.to_dict()
  
  
  # ---------------------------------------------------------------------------
  # Combined
  # ---------------------------------------------------------------------------
  
  @router.get("/overview")
  async def teams_overview(team_id: Optional[str] = None):
      """一站式获取双团队全局概览."""
      result: Dict[str, Any] = {}
      if _build_team:
          bs = _build_team.get_status()
          result["build_team"] = {
              "health": bs["health"],
              "agent_count": bs["agent_count"],
              "metrics": bs["metrics"],
          }
      if _execution_team:
          es = _execution_team.get_status()
          result["execution_team"] = {
              "health": es["health"],
              "agent_count": es["agent_count"],
              "metrics": es["metrics"],
          }
      if _scheduler:
          result["scheduler"] = _scheduler.get_status()
      if _evolution_engine:
          result["evolution"] = {
              **_evolution_engine.get_status(),
              "compliance_rating": _serialize_compliance_rating(),
          }
      if team_id:
          result["current_team"] = _serialize_current_team(team_id)
      return result
  
  
  def _serialize_current_team(team_id: str) -> Optional[Dict[str, Any]]:
      try:
          from .agents.api import _summarize_team_tasks, _team_manager
      except ImportError:
          from agents.api import _summarize_team_tasks, _team_manager
  
      if _team_manager is None:
          return None
  
      team = _team_manager.get_team(team_id)
      if team is None:
          return None
  
      return {
          **team.to_dict(),
          "tasks": _summarize_team_tasks(team_id),
      }
  
  
  # ---------------------------------------------------------------------------
  # System Evolution (自我演进引擎)
  # ---------------------------------------------------------------------------
  
  @router.get("/evolution/status")
  async def evolution_status():
      """获取自我演进引擎状态。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      status = _evolution_engine.get_status()
      return {
          "status": "initialized" if status.get("initialized") else "not_initialized",
          **status,
      }
  
  
  @router.get("/evolution/summary")
  async def evolution_summary():
      """获取演进项汇总。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_evolution_summary()
  
  
  @router.get("/evolution/items")
  async def evolution_items(status: Optional[str] = None, limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
      """获取演进项列表，可按状态过滤、分页。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      items = _evolution_engine.get_evolution_items(status=status)
      total = len(items)
      sliced = items[offset:offset + limit]
      return {
          "items": sliced,
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  @router.get("/evolution/rules")
  async def evolution_rules(limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
      """获取审查规则列表（分页）。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      items = [r.to_dict() for r in _evolution_engine.audit_rules]
      total = len(items)
      sliced = items[offset:offset + limit]
      return {
          "items": sliced,
          "total": total,
          "limit": limit,
          "offset": offset,
          "has_more": offset + limit < total,
      }
  
  
  @router.post("/evolution/audit")
  async def evolution_run_audit():
      """手动触发一次审查。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.run_full_audit()
  
  
  @router.post("/evolution/cycle")
  async def evolution_run_cycle():
      """运行完整演进周期（审查→派发→验证→关闭）。"""
      if not _evolution_engine:
          raise HTTPExceptio
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
  
          assert payload["co
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose
  任务: 完成北美 AI 项目区域合规与部署限制检查
  步骤: pm_decompose
  📋 任务: 2920f571-f5a
  🤖 Agent: PM (project_manager)
  📂 工作目录: /Users/panglaohu/Downloads/AgentsGroup2026
  🔧 执行方式: DeepSeek API (直连)
  ────────────────────────────────────────────────────────────
  你是 AgentsGroup2026 系统的 PM (project_manager)。
  你是项目经理 (PM)。请对以下任务进行分解和规划:
  完成北美 AI 项目区域合规与部署限制检查
  负责角色: 北美 AI 项目运维员
  预期产出: 合规检查表、区域部署准入结论
  负责角色: 北美 AI 项目运维员
  预期产出: 合规检查表、区域部署准入结论
  ## 📂 项目上下文 (系统自动预加载)
  **子任务拆解:**
    - 先确认变更目标、风险、依赖和验收指标。
    - 将任务拆成 plan / dry-run / review / apply / rollback / observe 六段。
    - 所有生产动作必须保留审计日志、回滚条件和成本/合规检查。
    - 对 OpenSearch/ElasticSearch 伸缩类任务，必须覆盖容量基线、分片重平衡、CloudWatch/OpenSearch 指标门禁、RI/Savings Plan 影响和北美数据驻留。
  
  ### 步骤 02: research (完整产出)
  
  # 研究分析 — researcher
  
  任务: 完成北美 AI 项目区域合规与部署限制检查
  步骤: research
  Agent: build_researcher
  
  ---
  
  📋 任务: 2920f571-f5a
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
    完成北美 AI 项目区域合规与部署限制检查
    负责角色: 北美 AI 项目运维员
    依赖: 任务2
    预期产出: 合规检查表、区域部署准入结论
    负责角色: 北美 AI 项目运维员
    依赖: 任务2
    预期产出: 合规检查表、区域部署准入结论
    
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
    ... (共 1572 个 src/ 文件)
    
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
    
    ### 文件: `src/backend/agent_team_api.py`
    ```py
    # -*- coding: utf-8 -*-
    """
    Agent Team API Routes - 双团队管理 REST API
    
    提供构建团队 & 执行团队的状态查询、KPI 考核、
    任务分配、报告查询等端点。挂载至 FastAPI 的 router。
    """
    
    from __future__ import annotations
    
    from fastapi import APIRouter, HTTPException, Query
    from pydantic import BaseModel, Field
    from typing import Any, Dict, List, Optional
    
    router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
    
    try:
        from config import DEFAULT_PAGE_SIZE as _DEFAULT_PAGE_SIZE
        from config import MAX_PAGE_SIZE as _MAX_PAGE_SIZE
    except Exception:
        _DEFAULT_PAGE_SIZE = 50
        _MAX_PAGE_SIZE = 200
    
    
    # ---------------------------------------------------------------------------
    # 全局引用（在 main.py startup 时注入）
    # ---------------------------------------------------------------------------
    _build_team = None
    _execution_team = None
    _scheduler = None
    _evolution_engine = None
    
    
    def _paginate_optional(items: List[Dict[str, Any]], *, limit: int, offset: int) -> Any:
        """Preserve old array responses by default while enabling optional pagination."""
        limit = getattr(limit, "default", limit)
        offset = getattr(offset, "default", offset)
        limit = int(limit or 0)
        offset = max(int(offset or 0), 0)
        if limit <= 0 and offset <= 0:
            return items
        if limit <= 0:
            limit = _DEFAULT_PAGE_SIZE
        limit = min(limit, _MAX_PAGE_SIZE)
        total = len(items)
        return {
            "items": items[offset:offset + limit],
            "total": total,
            "limit": limit,
            "offset": offset,
            "has_more": offset + limit < total,
        }
    
    
    def set_teams(build_team, execution_team, scheduler, evolution_engine=None):
        """在应用启动时由 main.py 调用，注入团队实例."""
        global _build_team, _execution_team, _scheduler, _evolution_engine
        _build_team = build_team
        _execution_team = execution_team
        _scheduler = scheduler
        _evolution_engine = evolution_engine
    
    
    # ---------------------------------------------------------------------------
    # Request / Response Models
    # ---------------------------------------------------------------------------
    
    class TaskAssignment(BaseModel):
        agent_id: str
        task: str
    
    
    class EvolutionCloseRequest(BaseModel):
        reason: str = Field(default="", description="关闭理由")
        verify_conclusion: str = Field(default="", description="验证结论")
    
    
    class EvolutionCompleteRequest(BaseModel):
        code_changes: List[str] = Field(default_factory=list, description="构建阶段产生的代码或配置变更")
        artifact_dir: str = Field(default="", description="构建阶段产物目录")
    
    
    class FeedbackSubmission(BaseModel):
        category: str = "optimization"
        severity: str = "medium"
        title: str
        detail: str
    
    # ── 演化优化请求模型 ──────────────────────────────────────────
    
    class OptimizeRequest(BaseModel):
        target_type: str = "skill"
        target_id: str = ""
        team_id: str = "build_system"
        iterations: int = Field(default=5, ge=1, le=10)
        content: str = ""
    
    class AutoTriageRequest(BaseModel):
        team_id: str = "build_system"
        top_n: int = Field(default=5, ge=1, le=10)
    
    class DatasetGenerateRequest(BaseModel):
        skill_id: str = ""
        team_id: str = "build_system"
        count: int = Field(default=15, ge=1, le=30)
    
    class ExampleItem(BaseModel):
        task_input: str
        rubric: str
    
    class DatasetManualRequest(BaseModel):
        dataset_id: str = ""
        skill_id: str = ""
        examples: List[ExampleItem] = Field(default_factory=list)
        skill_name: str = ""
    
    class DatasetImportKBRequest(BaseModel):
        skill_id: str = ""
        skill_name: str = ""
        dataset_id: str = ""
        max_examples: int = Field(default=20, ge=1, le=50)
    
    class UpdateExamplesRequest(BaseModel):
        action: str = "replace_all"
        examples: List[ExampleItem] = Field(default_factory=list)
        indices: List[int] = Field(default_factory=list)
        index: int = -1
        example: Optional[ExampleItem] = None
    
    class StepBaselineRequest(BaseModel):
        skill_id: str = ""
        team_id: str = "build_system"
        dataset_id: str = ""
    
    class FailureItem(BaseModel):
        task_input: str = ""
        rubric: str = ""
        composite: float = 0.0
        reasoning: str = ""
    
    class StepReflectRequest(BaseModel):
        skill_id: str = ""
        team_id: str = "build_system"
        failures: List[FailureItem] = Field(default_factory=list)
        user_hints: str = ""
    
    class StepMutateRequest(BaseModel):
        skill_id: str = ""
        team_id: str = "build_system"
        reflection: Dict[str, Any] = Field(default_factory=dict)
    
    class StepEvaluateCandidateRequest(BaseModel):
        skill_id: str = ""
        team_id: str = "build_system"
        dataset_id: str = ""
        instructions: str = ""
    
    class StepApplyRequest(BaseModel):
        skill_id: str = ""
        team_id: str = "build_system"
        instructions: str = ""
        baseline_score: float = 0.0
        new_score: float = 0.0
    
    
    # ---------------------------------------------------------------------------
    # Minimal AgentScheduler — provides basic scheduling status & tick
    # ---------------------------------------------------------------------------
    
    import time as _time
    
    
    class AgentScheduler:
        """轻量级调度器，提供运行状态、tick 计数、报告生成等基本能力。
    
        在 main.py startup 时自动创建并注入，确保前端团队概览的
        「调度器」卡片显示「运行中」而非「已停止」。
        """
    
        def __init__(self) -> None:
            self._started_at = _time.time()
            self._tick_count: int = 0
            self._last_tick_at: float = 0.0
    
        def get_status(self) -> Dict[str, Any]:
            return {
                "running": True,
                "tick_count": self._tick_count,
                "uptime_seconds": _time.time() - self._started_at,
                "last_tick_at": self._last_tick_at if self._last_tick_at else None,
            }
    
        def tick_once(self) -> Dict[str, Any]:
            """手动触发一次 tick（供调试/手动推进）."""
            self._tick_count += 1
            self._last_tick_at = _time.time()
            # 每次 tick 尝试驱动 evolution engine 的审查周期（如果存在）
            try:
                global _evolution_engine
                if _evolution_engine is not None:
                    _evolution_engine.audit()
            except Exception:
                pass
            return {"tick": self._tick_count, "ok": True}
    
        def generate_report_now(self) -> Dict[str, Any]:
            return {
                "status": self.get_status(),
                "summary": (f"调度器已运行 {self.get_status()['uptime_seconds']:.0f} 秒，"
                            f"累计 {self._tick_count} 次 tick"),
            }
    
    
    # ---------------------------------------------------------------------------
    # Scheduler API
    # ---------------------------------------------------------------------------
    
    @router.get("/scheduler/status")
    async def scheduler_status():
        if not _scheduler:
            raise HTTPException(503, "Scheduler not initialized")
        return _scheduler.get_status()
    
    
    @router.post("/scheduler/report")
    async def scheduler_generate_report():
        if not _scheduler:
            raise HTTPException(503, "Scheduler not initialized")
        return _scheduler.generate_report_now()
    
    
    @router.post("/scheduler/tick")
    async def scheduler_tick_once():
        """手动触发一次调度 tick (调试用)."""
        if not _scheduler:
            raise HTTPException(503, "Scheduler not initialized")
        return _scheduler.tick_once()
    
    
    # ---------------------------------------------------------------------------
    # Build Team
    # ---------------------------------------------------------------------------
    
    @router.get("/build/status")
    async def build_team_status():
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        return _build_team.get_status()
    
    
    @router.get("/build/kpis")
    async def build_team_kpis():
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        return _build_team.get_agent_kpis()
    
    
    @router.get("/build/agents/{agent_id}")
    async def build_agent_detail(agent_id: str):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        agent = _build_team.agents.get(agent_id)
        if not agent:
            raise HTTPException(404, f"Agent '{agent_id}' not found")
        return agent.to_dict()
    
    
    @router.post("/build/assign")
    async def build_assign_task(body: TaskAssignment):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        ok = _build_team.assign_task(body.agent_id, body.task)
        if not ok:
            raise HTTPException(404, f"Agent '{body.agent_id}' not found")
        return {"status": "assigned", "agent_id": body.agent_id, "task": body.task}
    
    
    @router.get("/build/reports")
    async def build_reports(
        limit: int = Query(default=10, ge=0, le=_MAX_PAGE_SIZE),
        offset: int = Query(default=0, ge=0),
    ):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        items = [r.to_dict() for r in _build_team.hourly_reports]
        if limit > 0 and offset == 0:
            items = items[-limit:]
            return items
        return _paginate_optional(items, limit=limit, offset=offset)
    
    
    @router.get("/build/issues")
    async def build_issues(
        limit: int = Query(default=0, ge=0, le=_MAX_PAGE_SIZE),
        offset: int = Query(default=0, ge=0),
    ):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        items = list(_build_team.issue_backlog)
        return _paginate_optional(items, limit=limit, offset=offset)
    
    
    # ---------------------------------------------------------------------------
    # Execution Team
    # ---------------------------------------------------------------------------
    
    @router.get("/execution/status")
    async def execution_team_status():
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        return _execution_team.get_status()
    
    
    @router.get("/execution/agents/{agent_id}")
    async def execution_agent_detail(agent_id: str):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        agent = _execution_team.agents.get(agent_id)
        if not agent:
            raise HTTPException(404, f"Agent '{agent_id}' not found")
        return agent.to_dict()
    
    
    @router.get("/execution/reports")
    async def execution_reports(
        limit: int = Query(default=10, ge=0, le=_MAX_PAGE_SIZE),
        offset: int = Query(default=0, ge=0),
    ):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        items = [r.to_dict() for r in _execution_team.execution_reports]
        if limit > 0 and offset == 0:
            items = items[-limit:]
            return items
        return _paginate_optional(items, limit=limit, offset=offset)
    
    
    @router.get("/execution/feedback")
    async def execution_feedback(
        limit: int = Query(default=0, ge=0, le=_MAX_PAGE_SIZE),
        offset: int = Query(default=0, ge=0),
    ):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        items = [item.to_dict() for item in _execution_team.feedback_queue]
        return _paginate_optional(items, limit=limit, offset=offset)
    
    
    @router.post("/execution/feedback")
    async def submit_feedback(body: FeedbackSubmission):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        item = _execution_team.submit_feedback(
            category=body.category,
            severity=body.severity,
            title=body.title,
            detail=body.detail,
        )
        return item.to_dict()
    
    
    # ---------------------------------------------------------------------------
    # Combined
    # ---------------------------------------------------------------------------
    
    @router.get("/overview")
    async def teams_overview(team_id: Optional[str] = None):
        """一站式获取双团队全局概览."""
        result: Dict[str, Any] = {}
        if _build_team:
            bs = _build_team.get_status()
            result["build_team"] = {
                "health": bs["health"],
                "agent_count": bs["agent_count"],
                "metrics": bs["metrics"],
            }
        if _execution_team:
            es = _execution_team.get_status()
            result["execution_team"] = {
                "health": es["health"],
                "agent_count": es["agent_count"],
                "metrics": es["metrics"],
            }
        if _scheduler:
            result["scheduler"] = _scheduler.get_status()
        if _evolution_engine:
            result["evolution"] = {
                **_evolution_engine.get_status(),
                "compliance_rating": _serialize_compliance_rating(),
            }
        if team_id:
            result["current_team"] = _serialize_current_team(team_id)
        return result
    
    
    def _serialize_current_team(team_id: str) -> Optional[Dict[str, Any]]:
        try:
            from .agents.api import _summarize_team_tasks, _team_manager
        except ImportError:
            from agents.api import _summarize_team_tasks, _team_manager
    
        if _team_manager is None:
            return None
    
        team = _team_manager.get_team(team_id)
        if team is None:
            return None
    
        return {
            **team.to_dict(),
            "tasks": _summarize_team_tasks(team_id),
        }
    
    
    # ---------------------------------------------------------------------------
    # System Evolution (自我演进引擎)
    # ---------------------------------------------------------------------------
    
    @router.get("/evolution/status")
    async def evolution_status():
        """获取自我演进引擎状态。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        status = _evolution_engine.get_status()
        return {
            "status": "initialized" if status.get("initialized") else "not_initialized",
            **status,
        }
    
    
    @router.get("/evolution/summary")
    async def evolution_summary():
        """获取演进项汇总。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_evolution_summary()
    
    
    @router.get("/evolution/items")
    async def evolution_items(status: Optional[str] = None, limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
        """获取演进项列表，可按状态过滤、分页。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        items = _evolution_engine.get_evolution_items(status=status)
        total = len(items)
        sliced = items[offset:offset + limit]
        return {
            "items": sliced,
            "total": total,
            "limit": limit,
            "offset": offset,
            "has_more": offset + limit < total,
        }
    
    
    @router.get("/evolution/rules")
    async def evolution_rules(limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
        """获取审查规则列表（分页）。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        items = [r.to_dict() for r in _evolution_engine.audit_rules]
        total = len(items)
        sliced = items[offset:offset + limit]
        return {
            "items": sliced,
            "total": total,
            "limit": limit,
            "offset": offset,
            "has_more": offset + limit < total,
        }
    
    
    @router.post("/evolution/audit")
    async def evolution_run_audit():
        """手动触发一次审查。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.run_full_audit()
    
    
    @router.post("/evolution/cycle")
    async def evolution_run_cycle():
        """运行完整演进周期（审查→派发→验证→关闭）。"""
        if not _evolution_engine:
            raise HTTPExceptio
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
        from agents.team_store import TeamSto
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
你是 AgentsGroup2026 系统的 Architect (architect)。
请执行以下开发任务:

你是系统架构师。请为以下任务设计技术方案:

## 任务
完成北美 AI 项目区域合规与部署限制检查
负责角色: 北美 AI 项目运维员
依赖: 任务2
预期产出: 合规检查表、区域部署准入结论
负责角色: 北美 AI 项目运维员
依赖: 任务2
预期产出: 合规检查表、区域部署准入结论

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
src/frontend/js/agent-team-
