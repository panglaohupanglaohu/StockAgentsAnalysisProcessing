# 研究分析 — researcher

任务: 成本优化: service ml-inference
步骤: research
Agent: build_researcher

---

📋 任务: f67bdcd7-681
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
  成本优化: service ml-inference
  来源: cost-dashboard
  治理目标: service ml-inference
  当前成本: $493.17
  筛选窗口: 24h
  
  请分析资源利用率、标签归因、预算影响和可回滚优化方案。完成后回写成本变化、验证证据和后续演进建议。
  
  ## 📂 项目上下文 (系统自动预加载)
  
  ### 项目文件结构 (src/ 目录)
  ```
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
  src/frontend/css/openbridge-theme.css
  src/frontend/css/skill-extract-timeline.css
  src/frontend/css/skill-extract.css
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
  src/backend/tests/test_token_budget.py
  src/backend/tests/test_unified_tool_loop.py
  src/backend/agents/__init__.py
  src/backend/agents/ab_testing.py
  src/backend/agents/agent_loop.py
  src/backend/agents/agent_toolbox.py
  ... (共 1153 个 src/ 文件)
  
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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;700&family=Noto+Serif:wght@200;300;400;600;900&family=Noto+Serif+SC:wght@200;300;400;600;900&family=Noto+Sans+SC:wght@300;400;500;700&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/agent-team-config.css">
    <link rel="stylesheet" href="/css/openbridge-theme.css">
    <link rel="stylesheet" href="/css/ws-theme-bridge.css">
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
      <div class="topbar"><div class="topbar-left"><h1 id="main-title">团队概览</h1><span class="badge" id="main-badge" style="background:rgba(152,245,167,0.15);color:var(--lime)"></span></div><nav class="global-nav"></nav><div class="topbar-right"><button class="btn btn-sm" onclick="openModal('modal-create-team')">＋ 创建团队</button><button class="btn btn-sm btn-ghost" onclick="deleteTeam()" style="color:var(--red)">🗑 删除团队</button></div></div>
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
          <div style="display:flex;gap:10px"><input class="fi" id="ss-query" placeholder="搜索所有持久化会话的内容..." style="flex:1" onkeydown="if(event.key==='Enter')searchPersistedSessions()"><button class="btn btn-pink btn-sm" onclick="searchPersistedSessions()">搜索</button></div>
          <div id="ss-search-results" style="margin-top:12px"></div>
        </div>
        <div class="card" style="padding:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><div class="section-title" style="margin:0">📁 已保存的会话</div><span id="ss-count" style="color:var(--dim);font-size:12px"></span></div>
          <div id="ss-list"></div>
        </div>
      </div></div>
      <!-- PortRuntime View -->
      <div id="view-runtime" class="main-inner hidden"><div class="main-scroll">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🚀 PortRuntime 路由引擎</div></div>
        <div class="card" style="margin-bottom:20px;padding:20px">
          <div class="section-title" style="margin-top:0;margin-bottom:12px">🎯 Prompt 路由</div>
          <p styl
  ```
  
  ### 文件: `src/frontend/cost-dashboard.html`
  ```html
  <!DOCTYPE html>
  <html lang="zh-CN">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>成本治理工作台 - AgentsGroup2026</title>
    <link rel="stylesheet" href="/css/variables.css">
    <link rel="stylesheet" href="/css/openbridge-theme.css">
    <style>
      .cost-dashboard { padding: 24px; max-width: 1400px; margin: 0 auto; }
      .cost-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
      .cost-header h1 { font-size: 24px; font-weight: 700; color: var(--fg); margin: 0; letter-spacing: 0; }
      .cost-header p { color: var(--muted); font-size: 13px; margin: 4px 0 0; }
      .cost-status { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
      .status-dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
      .status-dot.healthy { background: var(--lime); box-shadow: 0 0 6px var(--lime); }
      .status-dot.unhealthy { background: var(--pink); box-shadow: 0 0 6px var(--pink); }
      .status-dot.unknown { background: var(--dim); }
      .dashboard-alert { display: none; margin-bottom: 16px; padding: 12px 14px; border: 1px solid rgba(224,27,36,0.25); background: rgba(224,27,36,0.08); color: var(--shu); font-size: 13px; border-radius: 8px; }
      .dashboard-alert.show { display: block; }
  
      .filter-bar { display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; align-items: flex-end; }
      .filter-bar label { font-size: 12px; color: var(--muted); display: flex; flex-direction: column; gap: 4px; }
      .filter-bar select, .filter-bar input {
        background: var(--panel); border: 1px solid var(--line); border-radius: 6px;
        color: var(--fg); padding: 8px 12px; font-size: 13px; min-width: 120px;
      }
      .filter-bar select:focus, .filter-bar input:focus { outline: none; border-color: var(--pink); }
  
      .summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px; }
      .summary-card {
        background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 18px;
        display: flex; flex-direction: column; gap: 6px; min-height: 108px;
      }
      .summary-card .card-label { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0; }
      .summary-card .card-value { font-size: 27px; font-weight: 700; color: var(--fg); line-height: 1.1; }
      .summary-card .card-sub { font-size: 12px; color: var(--dim); line-height: 1.5; }
      .summary-card.accent .card-value { color: var(--pink); }
      .summary-card.success .card-value { color: var(--lime); }
  
      .workbench-grid { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 20px; margin-bottom: 20px; }
      .charts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
      @media (max-width: 1100px) { .workbench-grid, .charts-grid { grid-template-columns: 1fr; } }
      .panel {
        background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 20px;
      }
      .panel h3 { font-size: 15px; font-weight: 600; margin: 0 0 16px; color: var(--fg); letter-spacing: 0; }
      .chart-container { position: relative; min-height: 260px; }
      .bar-chart { display: flex; align-items: flex-end; gap: 10px; height: 210px; padding: 0 10px; }
      .bar-item { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; min-width: 34px; }
      .bar { width: 100%; max-width: 60px; background: linear-gradient(180deg, var(--pink) 0%, rgba(255,107,157,0.3) 100%); border-radius: 6px 6px 0 0; min-height: 4px; transition: height 0.3s ease; }
      .trend-bar { width: 100%; max-width: 40px; background: linear-gradient(180deg,var(--lime),rgba(152,245,167,0.2)); border-radius: 3px 3px 0 0; min-height: 2px; }
      .bar-label { font-size: 10px; color: var(--muted); text-align: center; word-break: break-word; max-width: 80px; }
      .bar-value { font-size: 11px; color: var(--dim); font-weight: 600; }
  
      .governance-stack { display: flex; flex-direction: column; gap: 12px; }
      .governance-row { display: flex; justify-content: space-between; gap: 12px; padding: 10px 0; border-bottom: 1px solid var(--hairline); font-size: 13px; }
      .governance-row:last-child { border-bottom: 0; }
      .governance-row strong { color: var(--fg); }
      .action-box { border: 1px solid var(--line); background: rgba(232,240,250,0.25); border-radius: 8px; padding: 12px; display: flex; flex-direction: column; gap: 10px; }
      .action-box label { font-size: 12px; color: var(--muted); display: flex; flex-direction: column; gap: 4px; }
      .action-box select { background: var(--panel); border: 1px solid var(--line); border-radius: 6px; color: var(--fg); padding: 8px 10px; font-size: 13px; width: 100%; }
      .action-buttons { display: flex; gap: 8px; flex-wrap: wrap; }
      .action-result { min-height: 18px; font-size: 12px; color: var(--dim); line-height: 1.5; }
  
      .data-table { width: 100%; border-collapse: collapse; font-size: 13px; }
      .data-table th { text-align: left; padding: 10px 14px; color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0; border-bottom: 1px solid var(--line); white-space: nowrap; }
      .data-table td { padding: 10px 14px; border-bottom: 1px solid var(--hairline); color: var(--fg); vertical-align: middle; }
      .data-table tr:hover td { background: rgba(232,240,250,0.3); }
      .cost-positive { color: var(--pink); font-weight: 600; }
      .pill { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 600; white-space: nowrap; }
      .pill.production, .pill.prod { background: rgba(255,107,157,0.12); color: var(--pink); }
      .pill.staging { background: rgba(249,200,14,0.12); color: #d4a900; }
      .pill.development, .pill.dev { background: rgba(152,245,167,0.12); color: var(--lime); }
      .pill.unknown { background: rgba(120,130,145,0.15); color: var(--muted); }
  
      .loading-state, .empty-state { text-align: center; padding: 48px 20px; color: var(--muted); }
      .loading-state .spinner {
        width: 36px; height: 36px; border: 3px solid var(--line); border-top-color: var(--pink);
        border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 16px;
      }
      @keyframes spin { to { transform: rotate(360deg); } }
      .empty-state .icon { font-size: 34px; margin-bottom: 12px; }
      .refresh-hint { font-size: 11px; color: var(--dim); cursor: pointer; }
      .refresh-hint:hover { color: var(--pink); }
      .table-wrap { overflow-x: auto; }
    </style>
  </head>
  <body>
    <script src="/js/global-nav.js" data-page="cost"></script>
  
    <div class="cost-dashboard">
      <div class="cost-header">
        <div>
          <h1>成本治理工作台</h1>
          <p>把 OpenCost、Cost Gate、任务派发串成可以执行的 FinOps 闭环</p>
        </div>
        <div class="cost-status">
          <span style="font-size:12px;color:var(--muted)">OpenCost</span>
          <span class="status-dot unknown" id="status-dot"></span>
          <span style="font-size:12px;color:var(--dim)" id="status-text">检测中...</span>
          <span style="font-size:11px;color:var(--dim)" id="cache-age"></span>
          <button class="btn" onclick="refreshDashboard()" id="refresh-btn">刷新</button>
        </div>
      </div>
  
      <div id="dashboard-alert" class="dashboard-alert"></div>
  
      <div class="filter-bar">
        <label>聚合维度
          <select id="filter-aggregation" onchange="refreshDashboard()">
            <option value="service">按服务</option>
            <option value="environment">按环境</option>
            <option value="team">按团队</option>
          </select>
        </label>
        <label>时间窗口
          <select id="filter-window" onchange="refreshDashboard()">
            <option value="24h">最近 24 小时</option>
            <option value="7d">最近 7 天</option>
            <option value="30d">最近 30 天</option>
          </select>
        </label>
        <label>环境
          <select id="filter-environment" onchange="refreshDashboard()">
            <option value="">全部</option>
            <option value="production">production</option>
            <option value="staging">staging</option>
            <option value="development">development</option>
          </select>
        </label>
        <label>服务
          <input type="text" id="filter-service" placeholder="输入服务名..." onchange="refreshDashboard()">
        </label>
        <label style="align-self:flex-end">
          <button class="btn btn-sm" onclick="resetFilters()">重置</button>
        </label>
      </div>
  
      <div class="summary-grid" id="summary-grid">
        <div class="loading-state"><div class="spinner"></div><div>加载中...</div></div>
      </div>
  
      <div class="workbench-grid">
        <div class="charts-grid">
          <div class="panel">
            <h3>成本构成 Top 10</h3>
            <div class="chart-container" id="breakdown-chart">
              <div class="loading-state"><div class="spinner"></div></div>
            </div>
          </div>
          <div class="panel">
            <h3>成本趋势</h3>
            <div class="chart-container" id="trends-chart">
              <div class="loading-state"><div class="spinner"></div></div>
            </div>
          </div>
        </div>
  
        <div class="panel">
          <h3>治理动作</h3>
          <div class="governance-stack" id="governance-panel">
            <div class="loading-state"><div class="spinner"></div></div>
          </div>
        </div>
      </div>
  
      <div class="panel" style="margin-bottom:24px">
        <h3>Pod 成本明细 <span style="font-size:12px;color:var(--muted);font-weight:400" id="pod-count"></span></h3>
        <div class="table-wrap">
          <table class="data-table" id="pods-table">
            <thead>
              <tr>
                <th>Pod</th>
                <th>命名空间</th>
                <th>服务</th>
                <th>环境</th>
                <th>团队</th>
                <th>CPU</th>
                <th>内存</th>
                <th>网络</th>
                <th>总计</th>
                <th>动作</th>
              </tr>
            </thead>
            <tbody id="pods-tbody">
              <tr><td colspan="10" class="loading-state"><div class="spinner" style="margin:20px auto"></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <div style="text-align:center;padding:16px;color:var(--dim);font-size:11px">
        <span id="last-refresh">-</span>
        <span class="refresh-hint" onclick="refreshDashboard()" style="margin-left:8px">点击刷新</span>
      </div>
    </div>
  
    <script src="/js/utils.js"></script>
    <script src="/js/api.js"></script>
    <script src="/js/evidence-runs.js"></script>
    <script src="/js/cost-dashboard.js"></script>
  </body>
  </html>
  
  ```
  
  ### 文件: `src/frontend/js/cost-dashboard.js`
  ```js
  /**
   * AgentsGroup2026 — Cost Governance Workbench
   * Repairs the OpenCost dashboard path and connects cost anomalies to task work.
   */
  (function () {
    'use strict';
  
    var COST_API = '/api/v1/cost';
    var GATE_API = '/api/v1/cost-gate';
    var AGENT_API = '/api/v1/agent-config';
    var state = {
      teams: [],
      summary: null,
      breakdown: [],
      trends: [],
      pods: [],
      health: null,
      gateHealth: null,
      gateStats: null,
      filters: {},
    };
  
    function $(id) {
      return document.getElementById(id);
    }
  
    function esc(value) {
      if (window.AG && typeof window.AG.escapeHtml === 'function') {
        return window.AG.escapeHtml(value);
      }
      return String(value == null ? '' : value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }
  
    function money(value) {
      return '$' + Number(value || 0).toFixed(2);
    }
  
    function compactNumber(value) {
      return Number(value || 0).toLocaleString();
    }
  
    function setText(id, value) {
      var node = $(id);
      if (node) node.textContent = value;
    }
  
    function setHtml(id, value) {
      var node = $(id);
      if (node) node.innerHTML = value;
    }
  
    function showAlert(message) {
      var alert = $('dashboard-alert');
      if (!alert) return;
      if (!message) {
        alert.classList.remove('show');
        alert.textContent = '';
        return;
      }
      var requestId = window.api && typeof window.api.getLastRequestId === 'function'
        ? window.api.getLastRequestId()
        : '';
      alert.textContent = requestId ? message + ' · 请求ID: ' + requestId : message;
      alert.classList.add('show');
    }
  
    async function requestJson(url, opts) {
      if (window.api && typeof window.api.request === 'function') {
        return await window.api.request(url, opts);
      }
      var response = await fetch(url, opts || { credentials: 'same-origin' });
      if (!response.ok) return null;
      return await response.json();
    }
  
    function getFilters() {
      return {
        aggregation: ($('filter-aggregation') && $('filter-aggregation').value) || 'service',
        window: ($('filter-window') && $('filter-window').value) || '24h',
        environment: ($('filter-environment') && $('filter-environment').value) || '',
        service: (($('filter-service') && $('filter-service').value) || '').trim(),
      };
    }
  
    function queryString(params) {
      var query = new URLSearchParams();
      Object.keys(params || {}).forEach(function (key) {
        if (params[key] !== undefined && params[key] !== null && params[key] !== '') {
          query.set(key, params[key]);
        }
      });
      return query.toString();
    }
  
    function asItems(payload, key) {
      if (Array.isArray(payload)) return payload;
      if (!payload) return [];
      if (Array.isArray(payload[key])) return payload[key];
      if (Array.isArray(payload.items)) return payload.items;
      return [];
    }
  
    function normalizeTrends(payload) {
      return asItems(payload, 'trends').map(function (series) {
        var points = Array.isArray(series.points)
          ? series.points
          : Array.isArray(series.data_points)
            ? series.data_points
            : [];
        return {
          dimension: series.dimension || '',
          value: series.value || '',
          total: Number(series.total || 0),
          points: points.map(function (point) {
            return {
              timestamp: point.timestamp || '',
              cost: Number(point.total_cost != null ? point.total_cost : point.cost || 0),
            };
          }),
        };
      });
    }
  
    function normalizePods(payload) {
      return asItems(payload, 'pods').map(function (pod) {
        var labels = pod.labels || {};
        return {
          pod: pod.pod || pod.pod_name || pod.name || '',
          namespace: pod.namespace || 'default',
          service: pod.service || labels.service || labels.app || '',
          environment: pod.environment || labels.environment || '',
          team: pod.team || labels.team || '',
          cpu_cost: Number(pod.cpu_cost || 0),
          ram_cost: Number(pod.ram_cost || 0),
          network_cost: Number(pod.network_cost || 0),
          pv_cost: Number(pod.pv_cost || 0),
          total_cost: Number(pod.total_cost || 0),
          labels: labels,
        };
      });
    }
  
    function renderSummary(payload) {
      var grid = $('summary-grid');
      if (!grid) return;
      var summary = payload && payload.summary ? payload.summary : null;
      if (!summary) {
        grid.innerHTML = '<div class="empty-state"><div class="icon">--</div><div>暂无成本摘要</div><div style="font-size:12px;color:var(--dim);margin-top:4px">请检查 OpenCost 或后端接口状态</div></div>';
        return;
      }
  
      grid.innerHTML = [
        '<div class="summary-card accent">',
        '<div class="card-label">总成本</div>',
        '<div class="card-value">' + money(summary.total_cost) + '</div>',
        '<div class="card-sub">' + esc(state.filters.window || '24h') + ' 窗口</div>',
        '</div>',
        '<div class="summary-card">',
        '<div class="card-label">活跃 Pod</div>',
        '<div class="card-value">' + compactNumber(summary.pod_count || summary.total_pods || 0) + '</div>',
        '<div class="card-sub">容器 ' + compactNumber(summary.container_count || 0) + '</div>',
        '</div>',
        '<div class="summary-card">',
        '<div class="card-label">服务 / 环境</div>',
        '<div class="card-value">' + compactNumber(summary.service_count || (summary.by_service || []).length) + '</div>',
        '<div class="card-sub">环境 ' + compactNumber(summary.environment_count || (summary.by_environment || []).length) + '</div>',
        '</div>',
        '<div class="summary-card success">',
        '<div class="card-label">团队归因</div>',
        '<div class="card-value">' + compactNumber(summary.team_count || (summary.by_team || []).length) + '</div>',
        '<div class="card-sub">最大团队成本 ' + money(maxCost(summary.by_team)) + '</div>',
        '</div>',
      ].join('');
    }
  
    function maxCost(items) {
      items = Array.isArray(items) ? items : [];
      return items.reduce(function (max, item) {
        return Math.max(max, Number(item.total_cost || 0));
      }, 0);
    }
  
    function renderBreakdown(items) {
      var container = $('breakdown-chart');
      if (!container) return;
      if (!items || !items.length) {
        container.innerHTML = '<div class="empty-state"><div class="icon">--</div><div>该维度下暂无数据</div></div>';
        return;
      }
  
      var sorted = items.slice().sort(function (a, b) {
        return Number(b.total_cost || 0) - Number(a.total_cost || 0);
      }).slice(0, 10);
      var max = Math.max.apply(null, sorted.map(function (item) { return Number(item.total_cost || 0); }).concat([0.01]));
  
      container.innerHTML = [
        '<div class="bar-chart">',
        sorted.map(function (item) {
          var height = Math.max((Number(item.total_cost || 0) / max) * 180, 4);
          return [
            '<div class="bar-item">',
            '<div class="bar-value">' + money(item.total_cost) + '</div>',
            '<div class="bar" style="height:' + height + 'px" title="' + esc(item.value || '?') + ': ' + money(item.total_cost) + '"></div>',
            '<div class="bar-label">' + esc(item.value || '?') + '</div>',
            '</div>',
          ].join('');
        }).join(''),
        '</div>',
      ].join('');
    }
  
    function renderTrends(seriesList) {
      var container = $('trends-chart');
      if (!container) return;
      var series = Array.isArray(seriesList) && seriesList.length ? seriesList[0] : null;
      if (!series || !series.points || series.points.length < 1) {
        container.innerHTML = '<div class="empty-state"><div class="icon">--</div><div>趋势数据不足</div><div style="font-size:12px;color:var(--dim)">需要 OpenCost 返回至少一个时间点</div></div>';
        return;
      }
  
      var values = series.points.map(function (point) { return Number(point.cost || 0); });
      var max = Math.max.apply(null, values.concat([0.01]));
      var min = Math.min.apply(null, values.concat([0]));
      container.innerHTML = [
        '<div style="display:flex;flex-direction:column;gap:12px">',
        '<div style="display:flex;align-items:flex-end;gap:4px;height:190px;padding:0 10px">',
        series.points.map(function (point) {
          var value = Number(point.cost || 0);
          var height = Math.max(((value - min) / (max - min || 1)) * 160, 4);
          var label = point.timestamp ? point.timestamp.slice(11, 16) || point.timestamp.slice(5, 10) : '?';
          return [
            '<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:2px" title="' + esc(label) + ': ' + money(value) + '">',
            '<div style="font-size:9px;color:var(--dim)">' + money(value) + '</div>',
            '<div class="trend-bar" style="height:' + height + 'px"></div>',
            '<div style="font-size:8px;color:var(--dim);transform:rotate(-45deg);white-space:nowrap">' + esc(label) + '</div>',
            '</div>',
          ].join('');
        }).join(''),
        '</div>',
        '<div style="text-align:center;font-size:12px;color:var(--muted)">' + esc(series.dimension || 'series') + ': ' + esc(series.value || '-') + ' · 总计 ' + money(series.total) + '</div>',
        '</div>',
      ].join('');
    }
  
    function renderPodsTable(pods) {
      var tbody = $('pods-tbody');
      if (!tbody) return;
      if (!pods || !pods.length) {
        tbody.innerHTML = '<tr><td colspan="10"><div class="empty-state"><div class="icon">--</div><div>暂无 Pod 成本明细</div><div style="font-size:12px;color:var(--dim)">等待 OpenCost 数据采集或调整筛选条件</div></div></td></tr>';
        setText('pod-count', '');
        return;
      }
  
      setText('pod-count', '(共 ' + pods.length + ' 个 Pod，显示前 50 个)');
      tbody.innerHTML = pods.slice(0, 50).map(function (pod, index) {
        var envClass = (pod.environment || 'unknown').toLowerCase();
        return [
          '<tr>',
          '<td style="font-family:monospace;font-size:12px">' + esc(pod.pod || '?') + '</td>',
          '<td>' + esc(pod.namespace || 'default') + '</td>',
          '<td><strong>' + esc(pod.service || '-') + '</strong></td>',
          '<td><span class="pill ' + esc(envClass || 'unknown') + '">' + esc(pod.environment || '-') + '</span></td>',
          '<td>' + esc(pod.team || '-') + '</td>',
          '<td>' + money(pod.cpu_cost) + '</td>',
          '<td>' + money(pod.ram_cost) + '</td>',
          '<td>' + money(pod.network_cost) + '</td>',
          '<td class="cost-positive">' + money(pod.total_cost) + '</td>',
          '<td><div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn btn-sm" onclick="createOptimizationTask(\'pod\',' + index + ')">创建任务</button><button class="btn btn-sm" onclick="generateLabelPatch(\'pod\',' + index + ')">标签补丁</button></div></td>',
          '</tr>',
        ].join('');
      }).join('');
    }
  
    function renderGovernance() {
      var panel = $('governance-panel');
      if (!panel) return;
      var health = state.health || {};
      var gate = state.gateHealth || {};
      var stats = state.gateStats || {};
      var top = state.breakdown[0] || null;
      var topLabel = top ? (top.dimension || state.filters.aggregation || 'cost') + ': ' + (top.value || '-') : '暂无异常目标';
      var topCost = top ? money(top.total_cost) : '-';
      var gateStatus = gate.status || gate.decision || '未知';
      var gateStatText = [
        '通过 ' + compactNumber(stats.passed || stats.pass || 0),
        '警告 ' + compactNumber(stats.warned || stats.warn || 0),
        '阻断 ' + compactNumber(stats.blocked || stats.block || 0),
      ].join(' · ');
  
      panel.innerHTML = [
        '<div class="governance-row"><span>OpenCost 数据</span><strong>' + esc(health.status || 'unknown') + '</strong></div>',
        '<div class="governance-row"><span>数据年龄</span><strong>' + compactNumber(health.data_age_seconds || health.data_freshness_seconds || 0) + ' 秒</strong></div>',
        '<div class="governance-row"><span>Cost Gate</span><strong>' + esc(gateStatus) + '</strong></div>',
        '<div class="governance-row"><span>Gate 统计</span><strong>' + esc(gateStatText) + '</strong></div>',
        '<div class="action-box">',
        '<div><strong>当前治理目标</strong><div style="font-size:12px;color:var(--muted);margin-top:4px">' + esc(topLabel) + ' · ' + esc(topCost) + '</div></div>',
        '<label>指派团队<select id="cost-action-team">' + teamOptionsHtml() + '</select></label>',
        '<div class="action-buttons">',
        '<button class="btn btn-pink btn-sm" onclick="createOptimizationTask(\'breakdown\',0)">创建优化任务</button>',
        '<button class="btn btn-sm" onclick="createPlazaTopic(\'breakdown\',0)">创建 Plaza 话题</button>',
        '<button class="btn btn-sm" onclick="generateLabelPatch(\'pod\',0)">生成标签补丁</button>',
        '<button class="btn btn-sm" onclick="runCostGateSelfCheck()">运行 Cost Gate 自检</button>',
        '</div>',
        '<div class="action-result" id="cost-action-result"></div>',
        '</div>',
      ].join('');
    }
  
    function teamOptionsHtml() {
      if (!state.teams.length) return '<option value="">加载团队中...</option>';
      return state.teams.map(function (team) {
        return '<option value="' + esc(team.team_id) + '"' + (team.preferred ? ' selected' : '') + '>' + esc(team.name || team.team_id) + '</option>';
      }).join('');
    }
  
    function updateStatus(summaryPayload) {
      var dot = $('status-dot');
      var text = $('status-text');
      var cache = $('cache-age');
      if (!dot || !text || !cache) return;
      dot.className = 'status-dot';
      if (summaryPayload && summaryPayload.summary) {
        dot.classList.add('healthy');
        text.textContent = '已连接';
        text.style.color = 'var(--lime)';
        var summary = summaryPayload.summary;
        cache.textContent = '服务 ' + compactNumber(summary.service_count || 0) + ' · Pod ' + compactNumber(summary.pod_count || 0);
      } else if (state.health && state.health.status) {
        dot.classList.add(state.health.status === 'ok' ? 'healthy' : 'unhealthy');
        text.textContent = state.health.status;
        text.style.color = state.health.status === 'ok' ? 'var(--lime)' : 'var(--pink)';
        cache.textContent = state.health.last_error ? state.health.last_error : '';
      } else {
        dot.classList.add('unknown');
        text.textContent = '无数据';
        text.style.color = 'var(--dim)';
        cache.textContent = '';
      }
    }
  
    function setLoading() {
      setHtml('summary-grid', '<div class="loading-state"><div class="spinner"></div><div>加载中...</div></div>');
      setHtml('breakdown-chart', '<div class="loading-state"><div class="spinner"></div></div>');
      setHtml('trends-chart', '<div class="loading-state"><div class="spinner"></div></div>');
      setHtml('governance-panel', '<div class="loading-state"><div class="spinner"></div></div>');
      var tbody = $('pods-tbody');
      if (tbody) tbody.innerHTML = '<tr><td colspan="10" class="loading-state"><div class="spinner" style="margin:20px auto"></div></td></tr>';
    }
  
    async function loadTeams() {
      var payload = await requestJson(AGENT_API + '/teams?limit=200&offset=0');
      var teams = asItems(payload, 'items');
      var preferredIndex = teams.findIndex(function (team) {
        var text = ((team.name || '') + 
  ```
  
  ### 文件: `src/frontend/js/i18n.js`
  ```js
  /**
   * AgentsGroup2026 — i18n Internationalization Module v2
   * DOM text-walker approach: walks all text nodes and replaces Chinese↔English.
   * Usage: <script src="/js/i18n.js"></script>
   * Pages can extend via: PX_I18N.addTexts({ '中文': 'English', ... })
   */
  (function () {
    'use strict';
  
    const LANGS = ['zh', 'en'];
    const STORAGE_KEY = 'px-lang';
  
    /* ── Shared text map: zh → en ── */
    const TEXT_MAP = new Map([
      // ─── Index / Home page ───
      ['深海远洋双体船舶智能综合信息系统', 'Deep-Sea Ocean-Going Catamaran Intelligent Information System'],
      ['船长中控台', 'Captain Cockpit'],
      ['智能导航', 'Smart Navigation'],
      ['数据中心孪生', 'DC Digital Twin'],
      ['态势感知', 'Situation Awareness'],
      ['船岸通信', 'Ship-Shore Link'],
      ['气象海况', 'Weather & Sea'],
      ['海上作业', 'Offshore Operations'],
      ['进入系统', 'Enter System'],
  
      // ─── Page titles ───
      ['船长智能中控台', 'Captain Cockpit'],
      ['船长驾驶舱', 'Captain Cockpit'],
      ['导航与操纵', 'Navigation & Maneuvering'],
      ['动力定位', 'DP Control'],
      ['推进控制', 'Thruster Control'],
      ['全船监控', 'Full Ship Monitor'],
      ['设备健康', 'CMS Health'],
      ['控制台', 'HMI Console'],
      ['海工特种作业', 'Offshore Operations'],
      ['海工特種作业', 'Offshore Operations'],
      ['气象海洋', 'Weather & Ocean'],
      ['船员管理', 'Crew Management'],
      ['仿真训练', 'Simulation & Training'],
      ['能效合规', 'Energy Compliance'],
      ['船载数据中心', 'Marine Datacenter'],
      ['安全应急', 'Safety & Emergency'],
      ['船岸协同', 'Ship-Shore Sync'],
      ['数字孪生', 'Digital Twin'],
      ['智能体', 'AI Agents'],
      ['系统自我演进', 'System Self-Evolution'],
      ['系统演进', 'System Evolution'],
      ['知识库', 'Knowledge Base'],
      ['系统配置', 'System Configuration'],
      ['全球船舶监控平台', 'Global Ship Monitoring'],
      ['船舶避免碰撞增强现实系统', 'Ship Collision Avoidance AR System'],
  
      // ─── Nav sidebar ───
      ['船长总览', 'Captain'],
      ['导航', 'Navigation'],
      ['全船监控', 'Monitor'],
      ['海工作业', 'Offshore Ops'],
      ['船员管理', 'Crew Mgmt'],
  
      // ─── Common status / UI ───
      ['正常', 'Normal'],
      ['报警', 'Alarm'],
      ['警告', 'Warning'],
      ['离线', 'Offline'],
      ['在线', 'Online'],
      ['已连接', 'Connected'],
      ['待命', 'Standby'],
      ['就绪', 'Ready'],
      ['待确认', 'Pending'],
      ['已执行', 'Executed'],
      ['已确认', 'Confirmed'],
      ['已接收', 'Received'],
      ['已批准', 'Approved'],
      ['已提交', 'Submitted'],
      ['有效', 'Valid'],
      ['即将到期', 'Expiring Soon'],
      ['检修中', 'Under Maintenance'],
      ['加载中', 'Loading'],
      ['初始化中', 'Initializing'],
      ['搜索', 'Search'],
      ['保存', 'Save'],
      ['取消', 'Cancel'],
      ['确认', 'Confirm'],
      ['关闭', 'Close'],
      ['刷新', 'Refresh'],
      ['导出', 'Export'],
      ['状态', 'Status'],
      ['设置', 'Settings'],
      ['提交', 'Submit'],
      ['返回', 'Back'],
      ['折叠', 'Collapse'],
      ['全屏', 'Fullscreen'],
      ['隐藏', 'Hide'],
      ['开始', 'Start'],
      ['暂停', 'Pause'],
      ['重置', 'Reset'],
      ['清空', 'Clear'],
      ['添加', 'Add'],
      ['保存配置', 'Save Config'],
      ['刷新全部', 'Refresh All'],
  
      // ─── Captain cockpit ───
      ['快捷指令', 'Quick Commands'],
      ['拋錨', 'Drop Anchor'],
      ['抛锚', 'Drop Anchor'],
      ['响笛', 'Sound Horn'],
      ['紧急停车', 'Emergency Stop'],
      ['信号灯', 'Signal Light'],
      ['信号燈', 'Signal Light'],
      ['航行日志', 'Navigation Log'],
      ['航行日誌', 'Navigation Log'],
      ['系统设置', 'System Settings'],
      ['性能报告', 'Performance Report'],
      ['气象更新', 'Weather Update'],
      ['操作日志', 'Operation Log'],
      ['操作日誌', 'Operation Log'],
      ['操作人', 'Operator'],
      ['事件', 'Event'],
      ['结果', 'Result'],
      ['完成', 'Complete'],
      ['大副', 'Chief Officer'],
      ['轮机长', 'Chief Engineer'],
      ['船长', 'Captain'],
      ['调整航向', 'Adjust Heading'],
      ['主机转速', 'M/E RPM'],
      ['确认航线', 'Confirm Route'],
      ['您好', 'Hello'],
      ['当前航行状态如何', 'Current navigation status?'],
      ['当前航速', 'Current Speed'],
      ['航向', 'Heading'],
      ['主机功率', 'M/E Power'],
      ['子系统全部在线', 'All subsystems online'],
      ['抵达下一航路点', 'ETA next waypoint'],
      ['首页', 'Home'],
      ['中控台', 'Control Center'],
      ['广播', 'Broadcast'],
  
      // ─── Safety & Emergency ───
      ['消防区域矩阵', 'Fire Zone Matrix'],
      ['救生设备清单', 'Life Saving Equipment'],
      ['应急预案', 'Emergency Plans'],
      ['集合站点', 'Muster Stations'],
      ['正常区域', 'Normal Zones'],
      ['注意区域', 'Caution Zones'],
      ['报警区域', 'Alarm Zones'],
      ['救生设备', 'Life Saving Equip.'],
      ['预案就绪', 'Plans Ready'],
      ['设备', 'Equipment'],
      ['数量', 'Qty'],
      ['容量', 'Capacity'],
      ['检验日期', 'Inspection Date'],
      ['救生艇', 'Lifeboat'],
      ['救生筏', 'Life Raft'],
      ['救生圈', 'Life Buoy'],
      ['救生衣', 'Life Jacket'],
      ['发光', 'Illuminated'],
      ['烟雾', 'Smoke Signal'],
      ['火灾', 'Fire'],
      ['弃船', 'Abandon Ship'],
      ['人落水', 'Man Overboard'],
      ['碰撞', 'Collision'],
      ['搁浅', 'Grounding'],
      ['进水', 'Flooding'],
      ['污染', 'Pollution'],
      ['医疗', 'Medical'],
      ['机舱', 'Engine Room'],
      ['货舱', 'Cargo Hold'],
      ['住舱', 'Accommodation'],
      ['驾驶', 'Bridge'],
      ['甲板', 'Deck'],
      ['左舷甲板', 'Port Deck'],
      ['右舷甲板', 'Starboard Deck'],
      ['驾驶台', 'Bridge'],
      ['机舱控制室', 'Engine Control Room'],
      ['人已到', 'Arrived'],
  
      // ─── Ship-Shore ───
      ['通信链路', 'Communication Links'],
      ['数据同步', 'Data Sync'],
      ['岸基指令历史', 'Shore Command History'],
      ['远程数据流', 'Remote Data Flow'],
      ['上行', 'Uplink'],
      ['下行', 'Downlink'],
      ['延迟', 'Latency'],
      ['航行数据', 'Navigation Data'],
      ['实时', 'Real-time'],
      ['岸基', 'Shore'],
      ['云存储', 'Cloud Storage'],
      ['云存儲', 'Cloud Storage'],
      ['视频监控', 'Video Monitor'],
      ['視频监控', 'Video Monitor'],
      ['岸基指令', 'Shore Command'],
      ['船端', 'Ship-side'],
      ['时间', 'Time'],
      ['来源', 'Source'],
      ['指令', 'Command'],
      ['航速调整', 'Speed Adjustment'],
      ['进港航道确认', 'Port Channel Confirm'],
      ['台风预警转发', 'Typhoon Alert Forward'],
      ['优化建议下发', 'Optimization Advice'],
      ['沿海', 'Coastal'],
      ['双频', 'Dual Freq'],
  
      // ─── Simulation & Training ───
      ['综合评分', 'Overall Score'],
      ['綜合評分', 'Overall Score'],
      ['训练次数', 'Training Count'],
      ['本月', 'This Month'],
      ['累计时长', 'Total Duration'],
      ['船员排名', 'Crew Ranking'],
      ['场景配置', 'Scenario Config'],
      ['训练场景', 'Training Scenario'],
      ['故障注入', 'Fault Injection'],
      ['训练日志', 'Training Log'],
      ['训练日誌', 'Training Log'],
      ['能力评估雷达图', 'Competency Radar'],
      ['能力評估雷达图', 'Competency Radar'],
      ['成绩详情', 'Score Details'],
      ['成績详情', 'Score Details'],
      ['评分趋势', 'Score Trend'],
      ['評分趨勢', 'Score Trend'],
      ['避碰判断', 'Collision Avoidance'],
      ['导航精度', 'Navigation Accuracy'],
      ['通信规范', 'Communication Standards'],
      ['应急反应', 'Emergency Response'],
      ['操纵技能', 'Maneuvering Skills'],
      ['团队协作', 'Teamwork'],
      ['平均反应时间', 'Avg. Response Time'],
      ['天气', 'Weather'],
      ['海况', 'Sea State'],
      ['交通密度', 'Traffic Density'],
      ['能见度', 'Visibility'],
      ['模拟时间', 'Simulation Time'],
      ['主机故障', 'M/E Failure'],
      ['舵机故障', 'Rudder Lock'],
      ['雷达故障', 'Radar Fail'],
      ['通信中断', 'Comms Down'],
      ['电力丧失', 'Blackout'],
      ['优秀', 'Excellent'],
      ['合格', 'Pass'],
      ['失败', 'Fail'],
      ['晴朗', 'Clear'],
      ['多云', 'Cloudy'],
      ['暴雨', 'Storm'],
      ['台风', 'Typhoon'],
      ['轻浪', 'Slight'],
      ['大浪', 'Rough'],
      ['狂浪', 'Very Rough'],
      ['狂涛', 'High'],
      ['蒲氏风级', 'Beaufort Scale'],
      ['评价', 'Grade'],
      ['右舷让路避让', 'Starboard Give-way'],
      ['雷达标绘', 'Radar Plotting'],
      ['联络确认', 'Communication Confirm'],
      ['狭水道右舷通行', 'Narrow Channel Starboard'],
      ['应急舵切换', 'Emergency Steering Switch'],
      ['追越船避让', 'Overtaking Avoidance'],
      ['避碰', 'COLREG Avoidance'],
      ['分道通航', 'TSS'],
      ['港口进出', 'Port Entry/Exit'],
      ['应急操纵', 'Emergency Maneuvering'],
      ['锚泊作业', 'Anchoring Ops'],
  
      // ─── System Evolution ───
      ['达尔文棘轮', 'Darwin Ratchet'],
      ['自然选择', 'Natural Selection'],
      ['棘轮机制', 'Ratchet Mechanism'],
      ['演进时间线', 'Evolution Timeline'],
      ['初始化棘轮引擎中', 'Initializing Ratchet Engine'],
      ['演进流水线', 'Evolution Pipeline'],
      ['演进操作', 'Evolution Ops'],
      ['演进趋势', 'Evolution Trend'],
      ['域覆盖雷达', 'Domain Radar'],
      ['审查热力图', 'Audit Heatmap'],
      ['合规评级', 'Compliance Rating'],
      ['合规区域', 'Compliance Zones'],
      ['升级仪表板', 'Upgrade Dashboard'],
      ['双重检查单', 'Double Checklist'],
      ['公司级', 'Company Level'],
      ['船舶级', 'Vessel Level'],
      ['审计轨迹', 'Audit Trail'],
      ['审查规则库', 'Audit Rules'],
      ['演进条目', 'Evolution Entries'],
      ['审查历史', 'Audit History'],
      ['运行审查', 'Runtime Audit'],
      ['派发', 'Dispatch'],
      ['验证', 'Verify'],
      ['完整周期', 'Full Cycle'],
      ['已锁定的演化特性只增不减', 'Locked traits only grow, never regress'],
      ['永不回退', 'Never Rollback'],
      ['系统自我演进引擎就绪', 'Self-Evolution Engine Ready'],
      ['正在加载演进数据', 'Loading evolution data'],
      ['活跃', 'Active'],
  
      // ─── Thruster Control ───
      ['机舱综合状态', 'Engine Room Overview'],
      ['机舱綜合狀态', 'Engine Room Overview'],
      ['功率趋势', 'Power Trend'],
      ['功率趨勢', 'Power Trend'],
      ['振动频谱', 'Vibration Spectrum'],
      ['振动频譜', 'Vibration Spectrum'],
      ['缸温分布', 'Cylinder Temp Distribution'],
      ['缸溫分布', 'Cylinder Temp Distribution'],
      ['燃油流量', 'Fuel Flow'],
      ['能效指标', 'Efficiency Indicators'],
      ['额定', 'Rated'],
      ['负荷', 'Load'],
      ['燃油压力', 'Fuel Pressure'],
      ['排气温度', 'Exhaust Temp'],
      ['振动水平', 'Vibration Level'],
      ['舱底水位', 'Bilge Water Level'],
      ['推进效率', 'Propulsion Efficiency'],
      ['总运行时', 'Total Runtime'],
      ['下次保养', 'Next Maintenance'],
      ['高级控制', 'Advanced Control'],
      ['限值', 'Limit'],
      ['滑油温度', 'Lube Oil Temp'],
      ['冷却水温', 'Cooling Water Temp'],
      ['车钟', 'Telegraph'],
      ['车鐘', 'Telegraph'],
  
      // ─── Weather & Ocean ───
      ['风场', 'Wind Field'],
      ['風场', 'Wind Field'],
      ['海浪谱', 'Wave Spectrum'],
      ['海浪譜', 'Wave Spectrum'],
      ['海况综合', 'Sea Conditions'],
      ['海況綜合', 'Sea Conditions'],
      ['道格拉斯海况', 'Douglas Sea State'],
      ['蒲福风级', 'Beaufort Scale'],
      ['气温', 'Air Temp'],
      ['水温', 'Water Temp'],
      ['气压', 'Pressure'],
      ['湿度', 'Humidity'],
      ['洋流', 'Current'],
      ['涌浪', 'Swell'],
      ['表面流速', 'Surface Current Speed'],
      ['流向', 'Current Direction'],
      ['涌浪评估', 'Swell Assessment'],
      ['适航', 'Seaworthy'],
      ['潮汐', 'Tide'],
      ['当前潮高', 'Current Tide Height'],
      ['气象预警', 'Weather Warning'],
      ['大风蓝色预警', 'Blue Gale Warning'],
      ['天气窗口', 'Weather Window'],
      ['可作业', 'Operable'],
      ['航线天气评估', 'Route Weather Assessment'],
      ['良好', 'Good'],
      ['预报', 'Forecast'],
      ['方向', 'Direction'],
      ['风速', 'Wind Speed'],
      ['风向', 'Wind Dir'],
      ['浪高', 'Wave Height'],
  
      // ─── Offshore Operations ───
      ['作业状态', 'Operation Status'],
      ['作业狀态', 'Operation Status'],
      ['作业类型', 'Operation Type'],
      ['起重吊装', 'Crane Lifting'],
      ['许可状态', 'Permit Status'],
      ['許可狀态', 'Permit Status'],
      ['作业区域', 'Work Zone'],
      ['客户', 'Client'],
      ['起重机状态', 'Crane Status'],
      ['起重机狀态', 'Crane Status'],
      ['臂仰角', 'Boom Angle'],
      ['回转角', 'Slew Angle'],
      ['吃钩高度', 'Hook Height'],
      ['吃鉤高度', 'Hook Height'],
      ['环境条件', 'Environment Conditions'],
      ['环境條件', 'Environment Conditions'],
      ['作业限制', 'Op. Limits'],
      ['未超限', 'Within Limits'],
      ['安全检查单', 'Safety Checklist'],
      ['安全检查單', 'Safety Checklist'],
      ['系统状态确认', 'System Status Confirmed'],
      ['系统狀态确认', 'System Status Confirmed'],
      ['通信链路测试', 'Comms Link Test'],
      ['通信链路测試', 'Comms Link Test'],
      ['人员就位确认', 'Personnel Positioned'],
      ['气象窗口核实', 'Weather Window Verified'],
      ['应急预案就绪', 'Emergency Plan Ready'],
      ['应急预案就緒', 'Emergency Plan Ready'],
      ['吊具检验合格', 'Rigging Inspection Pass'],
      ['吊具检驗合格', 'Rigging Inspection Pass'],
      ['安全区域清场', 'Safety Zone Cleared'],
      ['平台东南侧', 'Platform SE Side'],
      ['平台東南側', 'Platform SE Side'],
  
      // ─── Crew Management ───
      ['总船员', 'Total Crew'],
      ['当值', 'On Watch'],
      ['休息', 'Off Watch'],
      ['疲劳预警', 'Fatigue Alert'],
      ['疲勞预警', 'Fatigue Alert'],
      ['证书到期', 'Certificate Expiring'],
      ['证書到期', 'Certificate Expiring'],
      ['船员花名册', 'Crew Roster'],
      ['船员花名冊', 'Crew Roster'],
      ['休息时间合规', 'Work/Rest Compliance'],
      ['休息时間合规', 'Work/Rest Compliance'],
      ['疲劳风险', 'Fatigue Risk'],
      ['疲勞風险', 'Fatigue Risk'],
      ['船舶评分', 'Vessel Score'],
      ['高风险人员', 'High Risk Personnel'],
      ['达标', 'Compliant'],
      ['证书监控', 'Certificate Monitor'],
      ['证書监控', 'Certificate Monitor'],
      ['应急演练记录', 'Emergency Drill Records'],
      ['值班安排', 'Watch Schedule'],
      ['当前班次', 'Current Watch'],
      ['甲班', 'Watch A'],
      ['下次换班', 'Next Changeover'],
      ['大管轮', 'Second Engineer'],
      ['水手长', 'Bosun'],
      ['机工', 'Motorman'],
  
      // ─── Energy Compliance ───
      ['当前', 'Current'],
      ['年度评级', 'Annual Rating'],
      ['年度轨迹', 'Annual Trajectory'],
      ['实时追踪', 'Real-time Tracking'],
      ['月度燃油消耗', 'Monthly Fuel Consumption'],
      ['排放监测', 'Emissions Monitoring'],
      ['二氧化碳', 'CO₂'],
      ['年度申报', 'Annual Declaration'],
      ['硫氧化物', 'SOx'],
      ['氮氧化物', 'NOx'],
      ['颗粒物', 'Particulate Matter'],
      ['合规文档', 'Compliance Documents'],
      ['文档名称', 'Document Name'],
      ['编号', 'Number'],
      ['有效期', 'Validity'],
      ['更新日期', 'Update Date'],
      ['审核机构', 'Audit Authority'],
      ['技术档案', 'Technical File'],
      ['改善方案', 'Improvement Plan'],
      ['国际能效证书', 'International Energy Cert.'],
      ['排放合规声明', 'E
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose (完整产出)
  
  # PM分解 — project_manager
  
  任务: 成本优化: service ml-inference
  步骤: pm_decompose
  Agent: build_pm
  
  ---
  
  📋 任务: f67bdcd7-681
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
    成本优化: service ml-inference
    来源: cost-dashboard
    治理目标: service ml-inference
    当前成本: $493.17
    筛选窗口: 24h
    
    请分析资源利用率、标签归因、预算影响和可回滚优化方案。完成后回写成本变化、验证证据和后续演进建议。
    
    ## 📂 项目上下文 (系统自动预加载)
    
    ### 项目文件结构 (src/ 目录)
    ```
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
    src/frontend/css/openbridge-theme.css
    src/frontend/css/skill-extract-timeline.css
    src/frontend/css/skill-extract.css
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
    src/backend/tests/test_token_budget.py
    src/backend/tests/test_unified_tool_loop.py
    src/backend/agents/__init__.py
    src/backend/agents/ab_testing.py
    src/backend/agents/agent_loop.py
    src/backend/agents/agent_toolbox.py
    ... (共 1153 个 src/ 文件)
    
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
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@300;400;500;700&family=Noto+Serif:wght@200;300;400;600;900&family=Noto+Serif+SC:wght@200;300;400;600;900&family=Noto+Sans+SC:wght@300;400;500;700&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="/css/agent-team-config.css">
      <link rel="stylesheet" href="/css/openbridge-theme.css">
      <link rel="stylesheet" href="/css/ws-theme-bridge.css">
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
        <div class="topbar"><div class="topbar-left"><h1 id="main-title">团队概览</h1><span class="badge" id="main-badge" style="background:rgba(152,245,167,0.15);color:var(--lime)"></span></div><nav class="global-nav"></nav><div class="topbar-right"><button class="btn btn-sm" onclick="openModal('modal-create-team')">＋ 创建团队</button><button class="btn btn-sm btn-ghost" onclick="deleteTeam()" style="color:var(--red)">🗑 删除团队</button></div></div>
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
            <div style="display:flex;gap:10px"><input class="fi" id="ss-query" placeholder="搜索所有持久化会话的内容..." style="flex:1" onkeydown="if(event.key==='Enter')searchPersistedSessions()"><button class="btn btn-pink btn-sm" onclick="searchPersistedSessions()">搜索</button></div>
            <div id="ss-search-results" style="margin-top:12px"></div>
          </div>
          <div class="card" style="padding:20px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><div class="section-title" style="margin:0">📁 已保存的会话</div><span id="ss-count" style="color:var(--dim);font-size:12px"></span></div>
            <div id="ss-list"></div>
          </div>
        </div></div>
        <!-- PortRuntime View -->
        <div id="view-runtime" class="main-inner hidden"><div class="main-scroll">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🚀 PortRuntime 路由引擎</div></div>
          <div class="card" style="margin-bottom:20px;padding:20px">
            <div class="section-title" style="margin-top:0;margin-bottom:12px">🎯 Prompt 路由</div>
            <p styl
    ```
    
    ### 文件: `src/frontend/cost-dashboard.html`
    ```html
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>成本治理工作台 - AgentsGroup2026</title>
      <link rel="stylesheet" href="/css/variables.css">
      <link rel="stylesheet" href="/css/openbridge-theme.css">
      <style>
        .cost-dashboard { padding: 24px; max-width: 1400px; margin: 0 auto; }
        .cost-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
        .cost-header h1 { font-size: 24px; font-weight: 700; color: var(--fg); margin: 0; letter-spacing: 0; }
        .cost-header p { color: var(--muted); font-size: 13px; margin: 4px 0 0; }
        .cost-status { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
        .status-dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
        .status-dot.healthy { background: var(--lime); box-shadow: 0 0 6px var(--lime); }
        .status-dot.unhealthy { background: var(--pink); box-shadow: 0 0 6px var(--pink); }
        .status-dot.unknown { background: var(--dim); }
        .dashboard-alert { display: none; margin-bottom: 16px; padding: 12px 14px; border: 1px solid rgba(224,27,36,0.25); background: rgba(224,27,36,0.08); color: var(--shu); font-size: 13px; border-radius: 8px; }
        .dashboard-alert.show { display: block; }
    
        .filter-bar { display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; align-items: flex-end; }
        .filter-bar label { font-size: 12px; color: var(--muted); display: flex; flex-direction: column; gap: 4px; }
        .filter-bar select, .filter-bar input {
          background: var(--panel); border: 1px solid var(--line); border-radius: 6px;
          color: var(--fg); padding: 8px 12px; font-size: 13px; min-width: 120px;
        }
        .filter-bar select:focus, .filter-bar input:focus { outline: none; border-color: var(--pink); }
    
        .summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px; }
        .summary-card {
          background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 18px;
          display: flex; flex-direction: column; gap: 6px; min-height: 108px;
        }
        .summary-card .card-label { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0; }
        .summary-card .card-value { font-size: 27px; font-weight: 700; color: var(--fg); line-height: 1.1; }
        .summary-card .card-sub { font-size: 12px; color: var(--dim); line-height: 1.5; }
        .summary-card.accent .card-value { color: var(--pink); }
        .summary-card.success .card-value { color: var(--lime); }
    
        .workbench-grid { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 20px; margin-bottom: 20px; }
        .charts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        @media (max-width: 1100px) { .workbench-grid, .charts-grid { grid-template-columns: 1fr; } }
        .panel {
          background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 20px;
        }
        .panel h3 { font-size: 15px; font-weight: 600; margin: 0 0 16px; color: var(--fg); letter-spacing: 0; }
        .chart-container { position: relative; min-height: 260px; }
        .bar-chart { display: flex; align-items: flex-end; gap: 10px; height: 210px; padding: 0 10px; }
        .bar-item { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px; min-width: 34px; }
        .bar { width: 100%; max-width: 60px; background: linear-gradient(180deg, var(--pink) 0%, rgba(255,107,157,0.3) 100%); border-radius: 6px 6px 0 0; min-height: 4px; transition: height 0.3s ease; }
        .trend-bar { width: 100%; max-width: 40px; background: linear-gradient(180deg,var(--lime),rgba(152,245,167,0.2)); border-radius: 3px 3px 0 0; min-height: 2px; }
        .bar-label { font-size: 10px; color: var(--muted); text-align: center; word-break: break-word; max-width: 80px; }
        .bar-value { font-size: 11px; color: var(--dim); font-weight: 600; }
    
        .governance-stack { display: flex; flex-direction: column; gap: 12px; }
        .governance-row { display: flex; justify-content: space-between; gap: 12px; padding: 10px 0; border-bottom: 1px solid var(--hairline); font-size: 13px; }
        .governance-row:last-child { border-bottom: 0; }
        .governance-row strong { color: var(--fg); }
        .action-box { border: 1px solid var(--line); background: rgba(232,240,250,0.25); border-radius: 8px; padding: 12px; display: flex; flex-direction: column; gap: 10px; }
        .action-box label { font-size: 12px; color: var(--muted); display: flex; flex-direction: column; gap: 4px; }
        .action-box select { background: var(--panel); border: 1px solid var(--line); border-radius: 6px; color: var(--fg); padding: 8px 10px; font-size: 13px; width: 100%; }
        .action-buttons { display: flex; gap: 8px; flex-wrap: wrap; }
        .action-result { min-height: 18px; font-size: 12px; color: var(--dim); line-height: 1.5; }
    
        .data-table { width: 100%; border-collapse: collapse; font-size: 13px; }
        .data-table th { text-align: left; padding: 10px 14px; color: var(--muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0; border-bottom: 1px solid var(--line); white-space: nowrap; }
        .data-table td { padding: 10px 14px; border-bottom: 1px solid var(--hairline); color: var(--fg); vertical-align: middle; }
        .data-table tr:hover td { background: rgba(232,240,250,0.3); }
        .cost-positive { color: var(--pink); font-weight: 600; }
        .pill { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 10px; font-weight: 600; white-space: nowrap; }
        .pill.production, .pill.prod { background: rgba(255,107,157,0.12); color: var(--pink); }
        .pill.staging { background: rgba(249,200,14,0.12); color: #d4a900; }
        .pill.development, .pill.dev { background: rgba(152,245,167,0.12); color: var(--lime); }
        .pill.unknown { background: rgba(120,130,145,0.15); color: var(--muted); }
    
        .loading-state, .empty-state { text-align: center; padding: 48px 20px; color: var(--muted); }
        .loading-state .spinner {
          width: 36px; height: 36px; border: 3px solid var(--line); border-top-color: var(--pink);
          border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 16px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        .empty-state .icon { font-size: 34px; margin-bottom: 12px; }
        .refresh-hint { font-size: 11px; color: var(--dim); cursor: pointer; }
        .refresh-hint:hover { color: var(--pink); }
        .table-wrap { overflow-x: auto; }
      </style>
    </head>
    <body>
      <script src="/js/global-nav.js" data-page="cost"></script>
    
      <div class="cost-dashboard">
        <div class="cost-header">
          <div>
            <h1>成本治理工作台</h1>
            <p>把 OpenCost、Cost Gate、任务派发串成可以执行的 FinOps 闭环</p>
          </div>
          <div class="cost-status">
            <span style="font-size:12px;color:var(--muted)">OpenCost</span>
            <span class="status-dot unknown" id="status-dot"></span>
            <span style="font-size:12px;color:var(--dim)" id="status-text">检测中...</span>
            <span style="font-size:11px;color:var(--dim)" id="cache-age"></span>
            <button class="btn" onclick="refreshDashboard()" id="refresh-btn">刷新</button>
          </div>
        </div>
    
        <div id="dashboard-alert" class="dashboard-alert"></div>
    
        <div class="filter-bar">
          <label>聚合维度
            <select id="filter-aggregation" onchange="refreshDashboard()">
              <option value="service">按服务</option>
              <option value="environment">按环境</option>
              <option value="team">按团队</option>
            </select>
          </label>
          <label>时间窗口
            <select id="filter-window" onchange="refreshDashboard()">
              <option value="24h">最近 24 小时</option>
              <option value="7d">最近 7 天</option>
              <option value="30d">最近 30 天</option>
            </select>
          </label>
          <label>环境
            <select id="filter-environment" onchange="refreshDashboard()">
              <option value="">全部</option>
              <option value="production">production</option>
              <option value="staging">staging</option>
              <option value="development">development</option>
            </select>
          </label>
          <label>服务
            <input type="text" id="filter-service" placeholder="输入服务名..." onchange="refreshDashboard()">
          </label>
          <label style="align-self:flex-end">
            <button class="btn btn-sm" onclick="resetFilters()">重置</button>
          </label>
        </div>
    
        <div class="summary-grid" id="summary-grid">
          <div class="loading-state"><div class="spinner"></div><div>加载中...</div></div>
        </div>
    
        <div class="workbench-grid">
          <div class="charts-grid">
            <div class="panel">
              <h3>成本构成 Top 10</h3>
              <div class="chart-container" id="breakdown-chart">
                <div class="loading-state"><div class="spinner"></div></div>
              </div>
            </div>
            <div class="panel">
              <h3>成本趋势</h3>
              <div class="chart-container" id="trends-chart">
                <div class="loading-state"><div class="spinner"></div></div>
              </div>
            </div>
          </div>
    
          <div class="panel">
            <h3>治理动作</h3>
            <div class="governance-stack" id="governance-panel">
              <div class="loading-state"><div class="spinner"></div></div>
            </div>
          </div>
        </div>
    
        <div class="panel" style="margin-bottom:24px">
          <h3>Pod 成本明细 <span style="font-size:12px;color:var(--muted);font-weight:400" id="pod-count"></span></h3>
          <div class="table-wrap">
            <table class="data-table" id="pods-table">
              <thead>
                <tr>
                  <th>Pod</th>
                  <th>命名空间</th>
                  <th>服务</th>
                  <th>环境</th>
                  <th>团队</th>
                  <th>CPU</th>
                  <th>内存</th>
                  <th>网络</th>
                  <th>总计</th>
                  <th>动作</th>
                </tr>
              </thead>
              <tbody id="pods-tbody">
                <tr><td colspan="10" class="loading-state"><div class="spinner" style="margin:20px auto"></div></td></tr>
              </tbody>
            </table>
          </div>
        </div>
    
        <div style="text-align:center;padding:16px;color:var(--dim);font-size:11px">
          <span id="last-refresh">-</span>
          <span class="refresh-hint" onclick="refreshDashboard()" style="margin-left:8px">点击刷新</span>
        </div>
      </div>
    
      <script src="/js/utils.js"></script>
      <script src="/js/api.js"></script>
      <script src="/js/evidence-runs.js"></script>
      <script src="/js/cost-dashboard.js"></script>
    </body>
    </html>
    
    ```
    
    ### 文件: `src/frontend/js/cost-dashboard.js`
    ```js
    /**
     * AgentsGroup2026 — Cost Governance Workbench
     * Repairs the OpenCost dashboard path and connects cost anomalies to task work.
     */
    (function () {
      'use strict';
    
      var COST_API = '/api/v1/cost';
      var GATE_API = '/api/v1/cost-gate';
      var AGENT_API = '/api/v1/agent-config';
      var state = {
        teams: [],
        summary: null,
        breakdown: [],
        trends: [],
        pods: [],
        health: null,
        gateHealth: null,
        gateStats: null,
        filters: {},
      };
    
      function $(id) {
        return document.getElementById(id);
      }
    
      function esc(value) {
        if (window.AG && typeof window.AG.escapeHtml === 'function') {
          return window.AG.escapeHtml(value);
        }
        return String(value == null ? '' : value)
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;')
          .replace(/'/g, '&#39;');
      }
    
      function money(value) {
        return '$' + Number(value || 0).toFixed(2);
      }
    
      function compactNumber(value) {
        return Number(value || 0).toLocaleString();
      }
    
      function setText(id, value) {
        var node = $(id);
        if (node) node.textContent = value;
      }
    
      function setHtml(id, value) {
        var node = $(id);
        if (node) node.innerHTML = value;
      }
    
      function showAlert(message) {
        var alert = $('dashboard-alert');
        if (!alert) return;
        if (!message) {
          alert.classList.remove('show');
          alert.textContent = '';
          return;
        }
        var requestId = window.api && typeof window.api.getLastRequestId === 'function'
          ? window.api.getLastRequestId()
          : '';
        alert.textContent = requestId ? message + ' · 请求ID: ' + requestId : message;
        alert.classList.add('show');
      }
    
      async function requestJson(url, opts) {
        if (window.api && typeof window.api.request === 'function') {
          return await window.api.request(url, opts);
        }
        var response = await fetch(url, opts || { credentials: 'same-origin' });
        if (!response.ok) return null;
        return await response.json();
      }
    
      function getFilters() {
        return {
          aggregation: ($('filter-aggregation') && $('filter-aggregation').value) || 'service',
          window: ($('filter-window') && $('filter-window').value) || '24h',
          environment: ($('filter-environment') && $('filter-environment').value) || '',
          service: (($('filter-service') && $('filter-service').value) || '').trim(),
        };
      }
    
      function queryString(params) {
        var query = new URLSearchParams();
        Object.keys(params || {}).forEach(function (key) {
          if (params[key] !== undefined && params[key] !== null && params[key] !== '') {
            query.set(key, params[key]);
          }
        });
        return query.toString();
      }
    
      function asItems(payload, key) {
        if (Array.isArray(payload)) return payload;
        if (!payload) return [];
        if (Array.isArray(payload[key])) return payload[key];
        if (Array.isArray(payload.items)) return payload.items;
        return [];
      }
    
      function normalizeTrends(payload) {
        return asItems(payload, 'trends').map(function (series) {
          var points = Array.isArray(series.points)
            ? series.points
            : Array.isArray(series.data_points)
              ? series.data_points
              : [];
          return {
            dimension: series.dimension || '',
            value: series.value || '',
            total: Number(series.total || 0),
            points: points.map(function (point) {
              return {
                timestamp: point.timestamp || '',
                cost: Number(point.total_cost != null ? point.total_cost : point.cost || 0),
              };
            }),
          };
        });
      }
    
      function normalizePods(payload) {
        return asItems(payload, 'pods').map(function (pod) {
          var labels = pod.labels || {};
          return {
            pod: pod.pod || pod.pod_name || pod.name || '',
            namespace: pod.namespace || 'default',
            service: pod.service || labels.service || labels.app || '',
            environment: pod.environment || labels.environment || '',
            team: pod.team || labels.team || '',
            cpu_cost: Number(pod.cpu_cost || 0),
            ram_cost: Number(pod.ram_cost || 0),
            network_cost: Number(pod.network_cost || 0),
            pv_cost: Number(pod.pv_cost || 0),
            total_cost: Number(pod.total_cost || 0),
            labels: labels,
          };
        });
      }
    
      function renderSummary(payload) {
        var grid = $('summary-grid');
        if (!grid) return;
        var summary = payload && payload.summary ? payload.summary : null;
        if (!summary) {
          grid.innerHTML = '<div class="empty-state"><div class="icon">--</div><div>暂无成本摘要</div><div style="font-size:12px;color:var(--dim);margin-top:4px">请检查 OpenCost 或后端接口状态</div></div>';
          return;
        }
    
        grid.innerHTML = [
          '<div class="summary-card accent">',
          '<div class="card-label">总成本</div>',
          '<div class="card-value">' + money(summary.total_cost) + '</div>',
          '<div class="card-sub">' + esc(state.filters.window || '24h') + ' 窗口</div>',
          '</div>',
          '<div class="summary-card">',
          '<div class="card-label">活跃 Pod</div>',
          '<div class="card-value">' + compactNumber(summary.pod_count || summary.total_pods || 0) + '</div>',
          '<div class="card-sub">容器 ' + compactNumber(summary.container_count || 0) + '</div>',
          '</div>',
          '<div class="summary-card">',
          '<div class="card-label">服务 / 环境</div>',
          '<div class="card-value">' + compactNumber(summary.service_count || (summary.by_service || []).length) + '</div>',
          '<div class="card-sub">环境 ' + compactNumber(summary.environment_count || (summary.by_environment || []).length) + '</div>',
          '</div>',
          '<div class="summary-card success">',
          '<div class="card-label">团队归因</div>',
          '<div class="card-value">' + compactNumber(summary.team_count || (summary.by_team || []).length) + '</div>',
          '<div class="card-sub">最大团队成本 ' + money(maxCost(summary.by_team)) + '</div>',
          '</div>',
        ].join('');
      }
    
      function maxCost(items) {
        items = Array.isArray(items) ? items : [];
        return items.reduce(function (max, item) {
          return Math.max(max, Number(item.total_cost || 0));
        }, 0);
      }
    
      function renderBreakdown(items) {
        var container = $('breakdown-chart');
        if (!container) return;
        if (!items || !items.length) {
          container.innerHTML = '<div class="em
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
