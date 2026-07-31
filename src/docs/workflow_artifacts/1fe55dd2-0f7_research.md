# 研究分析 — researcher

任务: [广场计划] 现场引入openclaw的agent，这代表了以后的agent都由终端来构建
步骤: research
Agent: build_researcher

---

📋 任务: 1fe55dd2-0f7
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
  [广场计划] 现场引入openclaw的agent，这代表了以后的agent都由终端来构建
  ## 技术概要
  主目标：构建可审计的终端Agent构建环境，使每个终端的推理、编译与执行链具备不可篡改的因果锚定。核心方案：终端输出锚定结构，强制包含因果向量时钟、状态默克尔根、可复现执行计划哈希，并要求编译器将自身转换过程视为一级推理，输出转换因果哈希，实现故障根双向穿透编译边界。关键约束：锚定必须暴露推理因果图以支撑审计，隐私保护暂为次级目标。最大风险：编译器诚实性仍依赖其自身因果链自证，若编译器伪造转换哈希，上层验证将被系统性欺骗。首要动作：定义并冻结 `context.lock` 及编译器因果接口规范，产出签名方案与默克尔根构建协议。
  
  ## 加权结论 (P0→P1→P2)
  - [P0] 终端必须输出包含因果向量时钟 + 构建图哈希 + 状态默克尔根的不可篡改锚定结构；同时编译器必须输出转换因果哈希，否则构建链在编译边界断裂。 | Architect, Developer | 这是所有后续构建、调试与审计的基础，没有此锚定，分布式终端将退化为不可维护的碎片。
  - [P1] 回归测试框架需支持利用锚定结构进行故障二分定位，要求编译器因果图可被测试工具消费，否则质量门禁无法区分模型谬误与电路编码错误。 | Tester, Architect | 直接决定构建产物的质量可追溯性，是P0方案的必然配套。
  - [P2] 零知识证明可作为可选层附加于锚定之上，以在特定场景隐藏推理路径，但不侵蚀主锚定的因果可审计性，仅在后续版本中评估其性能影响。
  
  ## 执行计划
  | 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |
  |---|---|---|---|---|---|
  | 1 | 设计并发布`context.lock`锚定结构及编译器因果接口规范，包含向量时钟、默克尔根与执行计划哈希的字段定义与签名机制。 | Architect | P0 | 无 | 冻结的锚定结构规范文档，附带示例与签名算法说明。 |
  | 2 | 在终端Agent侧实现`context.lock`生成逻辑，确保每次构建推断均可输出完整锚定记录并本地存储。 | Developer | P0 | 规范冻结 | 终端锚定输出模块，可通过命令行/API调用验证完整性。 |
  | 3 | 实现编译器转换因果哈希输出，修改编译管线使其将输入状态与转换图哈希注入锚定流。 | 全栈开发 | P0 | 规范冻结 | 编译器插件或钩子，输出包含因果哈希的编译日志并接入锚定。 |
  | 4 | 开发测试二分工具，基于锚定链执行等价性检测与故障隔离，支持对比两次构建的向量时钟分歧点。 | Tester | P1 | 终端与编译器锚定实现 | 测试CLI工具，输入两次锚定快照可定位至编译或推理层差异节点。 |
  | 5 | 探索性评估zk-SNARK证明附加方案，在不改动主锚定的前提下，为推理步骤生成可选验证证明。 | 技术研究员 | P2 | 终端锚定模块 | 原型验证报告，给出性能损耗与隐私增益对比，决策是否纳入后续版本。 |
  
  ## 补充观察
  zk-SNARK附加层的计算开销可能显著增加终端能耗与延迟，需在P2评估中严格限定启用场景，避免影响主构建流程的性能基线。
  
  ## 📂 项目上下文 (系统自动预加载)
  
  ### 项目文件结构 (src/ 目录)
  ```
  src/frontend/agent-team-config.html
  src/frontend/datacenter-ratchet-evolution.html
  src/frontend/demo-fieldio-particles.html
  src/frontend/demo-lupi-data-humanism.html
  src/frontend/demo-takram-biosynthetic.html
  src/frontend/digital-twin-cli.html
  src/frontend/extraction-pipeline.html
  src/frontend/index.html
  src/frontend/login.html
  src/frontend/plaza-dark.html
  src/frontend/plaza-old.html
  src/frontend/plaza-wabisabi-v2.html
  src/frontend/plaza-wabisabi.html
  src/frontend/plaza.html
  src/frontend/sandbox-twin.html
  src/frontend/skill-extract.html
  src/frontend/system-evolution.html
  src/frontend/tasks.html
  src/frontend/css/agent-team-config.css
  src/frontend/css/openbridge-theme.css
  src/frontend/css/skill-extract-timeline.css
  src/frontend/css/ws-theme-bridge.css
  src/frontend/js/agent-team-config.js
  src/frontend/js/i18n.js
  src/frontend/js/nav-sidebar.js
  src/frontend/js/skill-extract-timeline.js
  src/backend/__init__.py
  src/backend/agent_team_api.py
  src/backend/main.py
  src/backend/main.py.bak
  src/backend/server.log
  src/backend/startup_check.py
  src/backend/startup_validator.py
  src/backend/tests/__init__.py
  src/backend/tests/conftest.py
  src/backend/tests/conftest.py.bak
  src/backend/tests/test_ab_testing.py
  src/backend/tests/test_agent_toolbox.py
  src/backend/tests/test_evolution_race.py
  src/backend/tests/test_evolution_race.py.bak
  src/backend/tests/test_fingerprint.py
  src/backend/tests/test_fingerprint.py.bak
  src/backend/tests/test_gate_evaluator.py
  src/backend/tests/test_gate_evaluator.py.bak
  src/backend/tests/test_merge_plugin.py
  src/backend/tests/test_merge_plugin.py.bak
  src/backend/tests/test_models.py
  src/backend/tests/test_models.py.bak
  src/backend/tests/test_operation_store.py
  src/backend/tests/test_qa_gate_pipeline.py
  src/backend/tests/test_qa_gate_pipeline.py.bak
  src/backend/tests/test_review_integration.py
  src/backend/tests/test_review_integration.py.bak
  src/backend/tests/test_task_engine.py
  src/backend/tests/test_task_engine.py.bak
  src/backend/tests/test_team_manager.py
  src/backend/tests/test_team_manager.py.bak
  src/backend/tests/test_template_variants.py
  src/backend/tests/test_template_variants.py.bak
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
  src/backend/agents/evolution/__init__.py
  src/backend/agents/evolution/auto_triage.py
  src/backend/agents/evolution/comparator.py
  src/backend/agents/evolution/constraints.py
  src/backend/agents/evolution/dataset_builder.py
  src/backend/agents/evolution/fitness.py
  src/backend/agents/evolution/mutator.py
  src/backend/agents/evolution/optimizer.py
  src/backend/agents/teams/__init__.py
  src/backend/agents/teams/ai_coding_team.py
  src/backend/agents/teams/build_team.py
  src/backend/agents/teams/energy_team.py
  src/backend/agents/teams/xops_team.py
  src/backend/agents/skills/__init__.py
  src/backend/agents/skills/greeting.py
  src/backend/agents/skills/hello.py
  src/backend/sandbox/__init__.py
  src/backend/sandbox/api.py
  src/backend/sandbox/channel.py
  src/backend/sandbox/drift_detector.py
  src/backend/sandbox/global_critic.py
  src/backend/sandbox/llm_decision.py
  src/backend/sandbox/memory_system.py
  src/backend/sandbox/models.py
  src/backend/sandbox/orchestrator.py
  src/backend/sandbox/strategy_aligner.py
  src/backend/sandbox/twin_loop.py
  src/backend/sandbox/world_state.py
  src/backend/sandbox/zero_exp_engine.py
  ... (共 914 个 src/ 文件)
  
  ```
  
  ### 文件: `src/frontend/agent-team-config.html`
  ```html
  <!DOCTYPE html>
  <html lang="zh-CN">
  <head>
    <meta charset="UTF-8">
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
  <div class="app">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="sb-header"><h2><span class="seal">智</span> AgentsGroup</h2><select class="fi" id="team-select" style="font-size:12px;padding:6px 8px"></select></div>
      <div class="sb-nav">
        <a class="active" data-view="overview" onclick="switchView('overview')"><span class="seal">览</span> 仪表盘</a>
        <a data-view="models" onclick="switchView('models')"><span class="seal">腦</span> 模型与连接</a>
        <a data-view="tools" onclick="switchView('tools')"><span class="seal seal-koke">具</span> 工具</a>
        <a data-view="skills" onclick="switchView('skills')"><span class="seal seal-kitsune">能</span> 技能</a>
        <a data-view="tasks" onclick="switchView('tasks')"><span class="seal">务</span> 任务</a>
        <a data-view="sessions" onclick="switchView('sessions')"><span class="seal">存</span> 会话存档</a>
        <a data-view="registry" onclick="switchView('registry')"><span class="seal">厂</span> Token 工厂</a>
      </div>
      <div class="sb-section">团队成员</div>
      <div class="sb-agents" id="sb-agents"></div>
      <div class="sb-footer"><button class="btn btn-pink btn-sm" onclick="openWizard()" style="width:100%;justify-content:center">＋ 新建智能体</button></div>
    </div>
    <!-- Main -->
    <div class="main">
      <div class="topbar"><div class="topbar-left"><h1 id="main-title">团队概览</h1><span class="badge" id="main-badge" style="background:rgba(152,245,167,0.15);color:var(--lime)"></span></div><nav class="global-nav"><span class="cur">智能体团队</span><a href="/plaza.html">议事广场</a><a href="/skill-extract.html">技能萃取/赋予</a><a href="/digital-twin-cli.html">数字孪生</a><a href="/sandbox-twin.html">SECS沙箱</a><a href="/system-evolution.html">系统演进</a></nav><div class="topbar-right"><button class="btn btn-sm" onclick="openModal('modal-create-team')">＋ 创建团队</button></div></div>
      <!-- Views -->
      <div id="view-overview" class="main-inner"><div class="main-scroll"><div class="card-grid" id="ov-stats"></div><div class="section" id="ov-team-section"><div class="section-title" id="ov-team-title"></div><table class="tbl"><thead><tr><th>Agent</th><th>角色</th><th>状态</th><th>技能</th><th>操作</th></tr></thead><tbody id="ov-team-agents"></tbody></table></div>
  <!-- 演进状态摘要 -->
  <div class="section" id="evo-section"><div class="section-title" style="display:flex;justify-content:space-between;align-items:center"><span>演进状态</span><a href="/system-evolution.html" class="btn btn-sm">→ 系统演进</a></div><div id="evo-compliance" class="card-grid"></div></div>
  </div></div>
      <div id="view-models" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🧠 模型与连接</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('llm')">🔌 LLM / TTS</button><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-model')">＋ 添加模型</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>名称</th><th>提供商</th><th>Max Tokens</th><th>温度</th><th>默认</th><th>操作</th></tr></thead><tbody id="models-tb"></tbody></table></div></div>
      <div id="view-tools" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🔧 可用工具</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('registry')">🏭 Token 工厂</button><button class="btn btn-sm" onclick="showToolSearch()">🔍 搜索</button></div></div><div id="tools-search-bar" class="hidden" style="margin-bottom:12px"><div style="display:flex;gap:10px"><input class="fi" id="tools-search-input" placeholder="搜索工具..." oninput="filterToolCards(this.value)" style="flex:1"><button class="btn btn-sm" onclick="el('tools-search-bar').classList.add('hidden')">✕</button></div></div><div id="tools-cards"></div></div></div>
      <div id="view-skills" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">⚡ 可用技能</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="exportSkillsMD()">📤 导出</button></div></div><div id="skills-cards"></div></div></div>
      <div id="view-tasks" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">📋 并发任务</div><div style="display:flex;gap:8px"><span id="task-stats" style="font-size:12px;color:var(--muted);display:flex;align-items:center"></span><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-task')">＋ 提交任务</button><button class="btn btn-sm" onclick="openModal('modal-batch-task')">📦 批量提交</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>标题</th><th>Agent</th><th>优先级</th><th>依赖</th><th>状态</th><th>操作</th></tr></thead><tbody id="tasks-tb"></tbody></table></div></div>
      <div id="view-llm" class="main-inner hidden"><div class="main-scroll">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div style="display:flex;align-items:center;gap:12px"><button class="btn btn-sm" onclick="switchView('models')">← 返回</button><div class="section-title" style="margin:0">🔌 LLM / TTS 配置</div></div><button class="btn btn-pink btn-sm" onclick="testLLM()">🧪 测试连接</button></div>
        <div id="llm-status-card" class="card" style="margin-bottom:20px;padding:20px"><p style="color:var(--dim)">加载中...</p></div>
        <div class="card" style="padding:20px;margin-bottom:20px">
          <div class="section-title" style="margin-top:0;margin-bottom:12px">⚙️ 配置 LLM 提供商</div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
            <div class="form-group"><label class="form-label">提供商</label><select class="fi" id="llm-provider"><option value="deepseek">DeepSeek</option><option value="openai">OpenAI</option><option value="anthropic">Anthropic</option><option value="local">本地 (Ollama/vLLM)</option><option value="openrouter">OpenRouter</option><option value="github">GitHub Models</option><option value="qwen">通义千问</option></select></div>
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
          <p style="color:var(--muted);font-size:12px;margin-bottom:14px">输入自然语言指令，系统将自动匹配最佳工具和命令 (claw-code-parity PortRuntime)</p>
          <div style="display:grid;gap:12px">
            <div class="form-group" style="margin:0"><label class="form-label">Prompt</label><textarea class="fi" id="rt-prompt" rows="3" placeholder="例: 检查主机状态并分析油温趋势"></textarea></div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
              <div class="form-group" style="margin:0"><label class="form-label">最大匹配数</label><input class="fi" id="rt-limit" type="number" value="5" min="1" max="20"></div>
              <div class="form-group" style="margin:0"><label class="form-label">禁用工具 (逗号分隔)</label><input class="fi" id="rt-deny" placeholder="web_search, run_python"></div>
              <div class="form-group" style="margin:0"><label class="form-label">禁用前缀</label><input class="fi" id="rt-deny-pfx" placeholder="mcp_, debug_"></div>
            </div>
            <div style="display:flex;gap:10px"><button class="btn btn-pink" onclick="doRoutePrompt()">🎯 路由匹配</button><button class="btn" onclick="doBootstrapSession()">⚡ 引导会话</button><button class="btn" onclick="doRouteAndChat()">💬 路由+对话</button></div>
          </div>
        </div>
        <div id="rt-results" class="card hidden" style="padding:20px"><div class="section-title" style="margin-top:0;margin-bottom:12px">📊 路由结果</div><div id="rt-results-content"></div></div>
        <div class="card" style="margin-top:20px;padding:20px">
          <div class="section-title" style="margin-top:0;margin-bottom:12px">🏊 Tool Pool 装配</div>
          <p style="color:var(--muted);font-size:12px;margin-bottom:14px">按权限上下文装配工具池 — 模拟 Clawith / claw-code-parity ToolPool</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
            <label style="display:flex;align-items:center;gap:8px;font-size:13px"><input type="checkbox" id="tp-simple"> 简单模式 (仅核心工具)</label>
            <label style="display:flex;align-items:center;gap:8px;font-size:13px"><input type="checkbox" id="tp-mcp" checked> 包含 MCP 工具</label>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
            <div class="form-group" style="margin:0"><label class="form-label">禁用工具</label><input class="fi" id="tp-deny" placeholder="逗号分隔"></div>
            <div class="form-group" style="margin:0"><label class="form-label">禁用前缀</label><input class="fi" id="tp-deny-pfx" placeholder="逗号分隔"></div>
          </div>
          <button class="btn btn-pink btn-sm" onclick="doAssemblePool()">🏊 装配 Tool Pool</button>
          <div id="tp-results" style="margin-top:12px"></div>
        </div>
      </div></div>
      <!-- Token Factory View -->
      <div id="view-registr
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
  
  from fastapi import APIRouter, HTTPException
  from pydantic import BaseModel
  from typing import Any, Dict, List, Optional
  
  router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
  
  
  # ---------------------------------------------------------------------------
  # 全局引用（在 main.py startup 时注入）
  # ---------------------------------------------------------------------------
  _build_team = None
  _execution_team = None
  _scheduler = None
  _evolution_engine = None
  
  
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
  
  class FeedbackSubmission(BaseModel):
      category: str = "optimization"
      severity: str = "medium"
      title: str
      detail: str
  
  
  # ---------------------------------------------------------------------------
  # Scheduler
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
  async def build_reports(limit: int = 10):
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      reports = _build_team.hourly_reports[-limit:]
      return [r.to_dict() for r in reports]
  
  
  @router.get("/build/issues")
  async def build_issues():
      if not _build_team:
          raise HTTPException(503, "Build team not initialized")
      return _build_team.issue_backlog
  
  
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
  async def execution_reports(limit: int = 10):
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      reports = _execution_team.execution_reports[-limit:]
      return [r.to_dict() for r in reports]
  
  
  @router.get("/execution/feedback")
  async def execution_feedback():
      if not _execution_team:
          raise HTTPException(503, "Execution team not initialized")
      return [item.to_dict() for item in _execution_team.feedback_queue]
  
  
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
  async def evolution_items(status: Optional[str] = None):
      """获取演进项列表，可按状态过滤。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_evolution_items(status=status)
  
  
  @router.get("/evolution/rules")
  async def evolution_rules():
      """获取审查规则列表。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return [r.to_dict() for r in _evolution_engine.audit_rules]
  
  
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
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.run_evolution_cycle()
  
  
  @router.post("/evolution/dispatch")
  async def evolution_dispatch():
      """派发所有待处理演进项给 Build 团队。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.dispatch_all_pending()
  
  
  @router.post("/evolution/verify")
  async def evolution_verify():
      """验证所有待验证项。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.verify_all_pending()
  
  
  @router.get("/evolution/items/{item_id}")
  async def evolution_item_detail(item_id: str):
      """获取单个演进项详情。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      item = _evolution_engine.evolution_items.get(item_id)
      if not item:
          raise HTTPException(404, f"Item '{item_id}' not found")
      return item.to_dict()
  
  
  @router.post("/evolution/items/{item_id}/progress")
  async def evolution_mark_progress(item_id: str):
      """标记演进项为进行中。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      ok = _evolution_engine.mark_in_progress(item_id)
      if not ok:
          raise HTTPException(404, f"Item '{item_id}' not found")
      return {"status": "ok", "item_id": item_id, "new_status": "in_progress"}
  
  
  @router.post("/evolution/items/{item_id}/complete")
  async def evolution_mark_complete(item_id: str):
      """标记演进项构建完成，进入待验证。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      ok = _evolution_engine.mark_build_complete(item_id)
      if not ok:
          raise HTTPException(404, f"Item '{item_id}' not found")
      return {"status": "ok", "item_id": item_id, "new_status": "verify_pending"}
  
  
  @router.post("/evolution/close-verified")
  async def evolution_close_verified():
      """关闭所有已验证通过的演进项。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      closed = _evolution_engine.close_verified()
      return {"closed": closed, "count": len(closed)}
  
  
  @router.post("/evolution/close")
  async def evolution_close():
      """关闭所有已验证通过的演进项 (close-verified 别名)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      closed = _evolution_engine.close_verified()
      return {"closed": closed, "count": len(closed)}
  
  
  @router.get("/evolution/history")
  async def evolution_audit_history():
      """获取审查历史记录。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      raw = _evolution_engine.get_audit_history()
      # Normalize field names for frontend (expects timestamp, total)
      result = []
      for h in raw:
          entry = dict(h)
          entry.setdefault("timestamp", entry.pop("time", None))
          entry.setdefault("total", (entry.get("passed") or 0) + (entry.get("failed") or 0) + (entry.get("skipped") or 0))
          result.append(entry)
      return result
  
  
  @router.get("/evolution/analytics")
  async def evolution_analytics():
      """获取演进分析数据 (域覆盖、严重度分布、趋势)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      summary = _evolution_engine.get_evolution_summary()
      history = _evolution_engine.get_audit_history()
      status = _evolution_engine.get_status()
  
      return {
          "summary": summary,
          "history": history,
          "stats": status.get("stats", {}),
          "items_by_status": status.get("items_by_status", {}),
          "rules_count": status.get("audit_rules_count", 0),
      }
  
  
  # ---------------------------------------------------------------------------
  # Phase 3: 业界标准化改进 API
  # ---------------------------------------------------------------------------
  
  @router.get("/evolution/compliance-rating")
  async def evolution_compliance_rating():
      """获取 DNV CII 风格 A~E 合规评级。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _serialize_compliance_rating()
  
  
  def _serialize_compliance_rating() -> Dict[str, Any]:
      data = _evolution_engine.get_compliance_rating()
      data["grade"] = data.get("rating", "?")
      data["description"] = data.get("rating_label", "")
      escalation = _evolution_engine.get_escalation_status()
      data["escalation_tier"] = "corrective" if escalation.get("escalated_count", 0) > 0 else "normal"
      return data
  
  
  @router.post("/evolution/compliance-rating/calculate")
  async def evolution_calculate_rating():
      """重新计算合规评级 (运行快速审查)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.calculate_compliance_rating()
  
  
  @router.get("/evolution/checklist")
  async def evolution_checklist(level: Optional[str] = None):
      """获取 ClassNK 双层自查清单 (company/ship)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_checklist(level=level)
  
  
  @router.get("/evolution/zones")
  async def evolution_zones():
      """获取所有合规区域。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_all_zones()
  
  
  @router.get("/evolution/zones/active")
  async def evolution_active_zones():
      """获取当前激活的合规区域。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_active_zones()
  
  
  @router.post("/evolution/zones/update-position")
  async def evolution_update_position(lat: float = 0.0, lon: float = 0.0):
      """更新船舶位置，自动检测合规区域进入/离开。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.update_vessel_position(lat, lon)
  
  
  @router.get("/evolution/escalation")
  async def evolution_escalation():
      """获取失败升级状态 (DNV SEEMP Part III 风格)。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      return _evolution_engine.get_escalation_status()
  
  
  @router.get("/evolution/trend")
  async def evolution_trend():
      """获取合规评级趋势分析。"""
      if not _evolution_engine:
          raise HTTPException(404, "Evolution engine not registered")
      data = _evo
  ```
  
  ### 文件: `src/backend/agents/fingerprint.py`
  ```py
  # -*- coding: utf-8 -*-
  """
  Fingerprint 计算模块 — 模板提取、动态变量剔除、精确哈希、自检与稳定性监控埋点。
  
  核心功能:
  1. 模板提取: 从 Agent 配置/行为快照中提取结构性骨架
  2. 动态变量剔除: 剥离 timestamps, UUIDs, session IDs, counters 等运行时变量
  3. 精确哈希: SHA-256 确定性哈希，用于指纹比对
  4. 自检: 确定性验证、模板一致性检查、哈希碰撞检测
  5. 稳定性监控埋点: 追踪指纹变异率、哈希漂移、模板稳定性
  
  与 ab_testing.ABTestMetrics.behavior_fingerprint_mutation_rate 集成。
  与 monitoring.collector 集成埋点上报。
  """
  
  from __future__ import annotations
  
  import hashlib
  import json
  import logging
  import re
  import time
  from dataclasses import dataclass, field
  from datetime import datetime, timezone
  from typing import Any, Callable, Dict, List, Optional, Set, Tuple
  
  logger = logging.getLogger(__name__)
  
  
  # ══════════════════════════════════════════════════════════════════
  # 配置与数据模型
  # ══════════════════════════════════════════════════════════════════
  
  
  @dataclass
  class FingerprintConfig:
      """指纹计算配置.
  
      Attributes:
          hash_algorithm: 哈希算法, 默认 sha256
          canonical_sort_keys: 序列化时是否按 key 排序 (保证确定性)
          indent: JSON 缩进 (None = 紧凑模式)
          dynamic_field_patterns: 需要剔除的动态字段名/正则模式
          strip_uuids: 是否剥离 UUID
          strip_timestamps: 是否剥离时间戳浮点数
          strip_counters: 是否剥离计数器字段
          stability_window_size: 稳定性追踪滑动窗口大小
          mutation_alert_threshold: 变异率告警阈值 (0.0-1.0)
          self_check_on_init: 初始化时是否执行自检
      """
      hash_algorithm: str = "sha256"
      canonical_sort_keys: bool = True
      indent: Optional[int] = None
      dynamic_field_patterns: List[str] = field(default_factory=lambda: [
          "timestamp", "created_at", "updated_at", "last_seen",
          "session_id", "request_id", "trace_id", "span_id",
          "counter", "clock", "lamport_clock", "_counter",
          "random_seed", "nonce", "token",
      ])
      strip_uuids: bool = True
      strip_timestamps: bool = True
      strip_counters: bool = True
      stability_window_size: int = 100
      mutation_alert_threshold: float = 0.05
      self_check_on_init: bool = True
  
      def to_dict(self) -> Dict[str, Any]:
          return {
              "hash_algorithm": self.hash_algorithm,
              "canonical_sort_keys": self.canonical_sort_keys,
              "dynamic_field_patterns": list(self.dynamic_field_patterns),
              "strip_uuids": self.strip_uuids,
              "strip_timestamps": self.strip_timestamps,
              "strip_counters": self.strip_counters,
              "stability_window_size": self.stability_window_size,
              "mutation_alert_threshold": self.mutation_alert_threshold,
          }
  
      @classmethod
      def from_dict(cls, data: Dict[str, Any]) -> FingerprintConfig:
          return cls(
              hash_algorithm=data.get("hash_algorithm", "sha256"),
              canonical_sort_keys=data.get("canonical_sort_keys", True),
              indent=data.get("indent"),
              dynamic_field_patterns=data.get("dynamic_field_patterns", []),
              strip_uuids=data.get("strip_uuids", True),
              strip_timestamps=data.get("strip_timestamps", True),
              strip_counters=data.get("strip_counters", True),
              stability_window_size=data.get("stability_window_size", 100),
              mutation_alert_threshold=data.get("mutation_alert_threshold", 0.05),
          )
  
  
  @dataclass
  class FingerprintResult:
      """指纹计算结果.
  
      Attributes:
          fingerprint_hash: SHA-256 哈希值 (hex)
          template: 剥离动态变量后的规范模板 (dict)
          dynamic_fields_removed: 被剔除的动态字段列表
          computed_at: 计算时间戳
          input_type: 输入对象的类型名
          stability_score: 稳定性评分 (0.0-1.0, 1.0=完全稳定)
          metadata: 额外元数据
      """
      fingerprint_hash: str
      template: Dict[str, Any] = field(default_factory=dict)
      dynamic_fields_removed: List[str] = field(default_factory=list)
      computed_at: float = field(default_factory=time.time)
      input_type: str = ""
      stability_score: float = 1.0
      metadata: Dict[str, Any] = field(default_factory=dict)
  
      def to_dict(self) -> Dict[str, Any]:
          return {
              "fingerprint_hash": self.fingerprint_hash,
              "template_summary": _summarize_template(self.template),
              "dynamic_fields_removed": self.dynamic_fields_removed,
              "computed_at": self.computed_at,
              "input_type": self.input_type,
              "stability_score": self.stability_score,
              "metadata": self.metadata,
          }
  
      @property
      def hash_prefix(self) -> str:
          """返回哈希值的前 12 个字符, 便于日志和对比."""
          return self.fingerprint_hash[:12]
  
  
  @dataclass
  class SelfCheckResult:
      """自检结果.
  
      Attributes:
          passed: 是否通过自检
          checks: 各检查项结果列表
          issues: 发现的问题列表
          duration_ms: 自检耗时 (毫秒)
      """
      passed: bool = True
      checks: List[Dict[str, Any]] = field(default_factory=list)
      issues: List[str] = field(default_factory=list)
      duration_ms: float = 0.0
  
      def add_check(self, name: str, ok: bool, detail: str = ""):
          self.checks.append({"name": name, "ok": ok, "detail": detail})
          if not ok:
              self.passed = False
              self.issues.append(f"[{name}] {detail}")
  
  
  @dataclass
  class StabilityRecord:
      """稳定性追踪记录 — 单次指纹计算快照."""
      fingerprint_hash: str
      computed_at: float
      input_type: str
      dynamic_count: int = 0
  
  
  # ══════════════════════════════════════════════════════════════════
  # 动态字段检测工具
  # ══════════════════════════════════════════════════════════════════
  
  # 预编译的 UUID 正则
  _UUID_RE = re.compile(
      r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
  )
  
  # ISO 8601 时间戳正则
  _ISO_TIMESTAMP_RE = re.compile(
      r'^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}'
  )
  
  
  def _is_uuid(value: str) -> bool:
      """判断字符串是否为 UUID 格式."""
      return bool(_UUID_RE.match(value))
  
  
  def _is_iso_timestamp(value: str) -> bool:
      """判断字符串是否为 ISO 8601 时间戳格式."""
      return bool(_ISO_TIMESTAMP_RE.match(value))
  
  
  def _is_counter_field(field_name: str) -> bool:
      """判断字段名是否为计数器类型."""
      counter_patterns = ("counter", "_count", "count_", "tick", "sequence", "seq_")
      lower = field_name.lower()
      return any(p in lower for p in counter_patterns)
  
  
  def _is_timestamp_field(field_name: str) -> bool:
      """判断字段名是否为时间戳类型."""
      ts_patterns = (
          "timestamp", "created_at", "updated_at", "last_seen",
          "computed_at", "last_modified", "modified_at", "created",
          "last_active", "last_login", "expires_at", "expiry",
      )
      lower = field_name.lower()
      return any(p in lower for p in ts_patterns)
  
  
  def _is_session_id_like(value: str) -> bool:
      """判断字符串是否像 session ID."""
      if len(value) > 16 and '-' in value:
          parts = value.split('-')
          if all(len(p) >= 4 for p in parts[:3]):
              return True
      # hex string 32+ chars
      if len(value) >= 32 and all(c in '0123456789abcdef' for c in value.lower()):
          return True
      return False
  
  
  # ══════════════════════════════════════════════════════════════════
  # 模板提取引擎
  # ══════════════════════════════════════════════════════════════════
  
  
  def _summarize_template(template: Dict[str, Any], max_keys: int = 10) -> Dict[str, Any]:
      """生成模板摘要, 避免完整模板过大."""
      keys = list(template.keys())[:max_keys]
      return {k: type(template[k]).__name__ for k in keys}
  
  
  class FingerprintEngine:
      """指纹计算引擎 — 核心算法.
  
      流程:
      1. extract_template: 从对象中提取结构性骨架
      2. strip_dynamic: 剔除动态字段
      3. canonical_serialize: 规范序列化 (排序 key, 紧凑 JSON)
      4. compute_hash: SHA-256 哈希
  
      Usage:
          >>> engine = FingerprintEngine()
          >>> result = engine.fingerprint(agent_profile)
          >>> print(result.fingerprint_hash)
      """
  
      def __init__(self, config: Optional[FingerprintConfig] = None):
          self.config = config or FingerprintConfig()
          self._stability_window: List[StabilityRecord] = []
          self._last_hash: Optional[str] = None
          self._mutation_count: int = 0
          self._total_fingerprints: int = 0
          self._self_check_result: Optional[SelfCheckResult] = None
  
          if self.config.self_check_on_init:
              self._self_check_result = self.self_check()
              # 自检不应污染稳定性窗口
              self.reset_stability()
  
      # ── 公共 API ─────────────────────────────────────────────────
  
      def fingerprint(self, obj: Any, obj_type: Optional[str] = None) -> FingerprintResult:
          """计算对象的指纹.
  
          Args:
              obj: 任意可序列化对象 (dict, dataclass, Pydantic model 等)
              obj_type: 对象类型标签 (可选, 默认使用 type(obj).__name__)
  
          Returns:
              FingerprintResult 包含哈希值、模板、元数据
          """
          t0 = time.time()
          input_type = obj_type or type(obj).__name__
  
          # 1. 将对象转为 dict
          raw_dict = self._to_dict(obj)
  
          # 2. 提取模板: 剔除动态字段
          template, removed = self._strip_dynamic(raw_dict)
  
          # 3. 规范序列化
          canonical_json = self._canonical_serialize(template)
  
          # 4. 计算哈希
          fp_hash = self._compute_hash(canonical_json)
  
          # 5. 稳定性评分
          stability_score = self._compute_stability(fp_hash)
  
          # 6. 更新内部追踪
          self._update_tracking(fp_hash, input_type, len(removed))
  
          result = FingerprintResult(
              fingerprint_hash=fp_hash,
              template=template,
              dynamic_fields_removed=removed,
              computed_at=time.time(),
              input_type=input_type,
              stability_score=stability_score,
              metadata={
                  "template_depth": _dict_depth(template),
                  "canonical_size_bytes": len(canonical_json),
                  "elapsed_ms": round((time.time() - t0) * 1000, 2),
              },
          )
  
          logger.debug(
              "Fingerprint computed: hash=%s type=%s removed=%d fields elapsed=%.2fms",
              result.hash_prefix, input_type, len(removed),
              result.metadata["elapsed_ms"],
          )
          return result
  
      def diff(self, fp1: FingerprintResult, fp2: FingerprintResult) -> Dict[str, Any]:
          """比较两个指纹, 返回差异信息.
  
          Returns:
              dict with keys: identical, hash_match, template_diff_keys, ...
          """
          hash_match = fp1.fingerprint_hash == fp2.fingerprint_hash
          keys1 = set(fp1.template.keys())
          keys2 = set(fp2.template.keys())
  
          return {
              "identical": hash_match,
              "hash_match": hash_match,
              "hash1_prefix": fp1.hash_prefix,
              "hash2_prefix": fp2.hash_prefix,
              "only_in_first": sorted(keys1 - keys2),
              "only_in_second": sorted(keys2 - keys1),
              "common_keys": sorted(keys1 & keys2),
              "type1": fp1.input_type,
              "type2": fp2.input_type,
          }
  
      # ── 自检 ─────────────────────────────────────────────────────
  
      def self_check(self) -> SelfCheckResult:
          """执行完整自检: 确定性验证、模板一致性、哈希碰撞检测.
  
          Returns:
              SelfCheckResult 包含各检查项结果
          """
          t0 = time.time()
          result = SelfCheckResult()
  
          # 检查 1: 确定性 — 相同输入产生相同哈希
          self._check_determinism(result)
  
          # 检查 2: 动态字段剔除有效性
          self._check_dynamic_stripping(result)
  
          # 检查 3: 不同输入产生不同哈希 (碰撞抵抗)
          self._check_collision_resistance(result)
  
          # 检查 4: 空输入处理
          self._check_empty_input(result)
  
          # 检查 5: 嵌套结构处理
          self._check_nested_structure(result)
  
          result.duration_ms = round((time.time() - t0) * 1000, 2)
  
          if result.passed:
              logger.info("✅ Fingerprint self-check PASSED (%d checks, %.2fms)",
                          len(result.checks), result.duration_ms)
          else:
              logger.warning("❌ Fingerprint self-check FAILED: %s", result.issues)
  
          self._self_check_result = result
          return result
  
      def _check_determinism(self, result: SelfCheckResult):
          """验证确定性: 相同输入 → 相同哈希."""
          test_obj = {
              "team_id": "test-team",
              "name": "测试团队",
              "agents": ["agent-1", "agent-2"],
              "config": {"max_tokens": 8192, "temperature": 0.7},
          }
          fp1 = self.fingerprint(test_obj, obj_type="determinism_test")
          fp2 = self.fingerprint(test_obj, obj_type="determinism_test")
          ok = fp1.fingerprint_hash == fp2.fingerprint_hash
          result.add_check(
              "determinism",
              ok,
              f"Hash match: {fp1.hash_prefix} == {fp2.hash_prefix}" if ok else
              f"MISMATCH: {fp1.hash_prefix} != {fp2.hash_prefix}"
          )
  
      def _check_dynamic_stripping(self, result: SelfCheckResult):
          """验证动态字段剔除: 仅 timestamp 不同的两个输入应产生相同哈希."""
          base = {
              "team_id": "test-team",
              "name": "测试团队",
              "config": {"max_tokens": 8192},
              "timestamp": 1000.0,
              "request_id": "abc-def-1234-5678",
          }
          modified = {
              **base,
              "timestamp": 9999.0,
              "request_id": "xyz-ghi-9999-0000",
          }
          fp1 = self.fingerprint(base, obj_type="strip_test")
          fp2 = self.fingerprint(modified, obj_type="strip_test")
          ok = fp1.fingerprint_hash == fp2.fingerprint_hash
          result.add_check(
              "dynamic_stripping",
              ok,
              f"Stripped hash match: {fp1.hash_prefix} == {fp2.hash_prefix}" if ok else
              f"STRIP FAILED: {fp1.hash_prefix} != {fp2.hash_prefix}"
          )
  
      def _check_collision_resistance(self, result: SelfCheckResult):
          """验证碰撞抵抗: 不同输入应产生不同哈希."""
          obj_a = {"id": "team-a", "name": "Alpha", "config": {"temperature": 0.5}}
          obj_b = {"id": "team-b", "name": "Beta", "config": {"temperature": 0.9}}
          fp_a = self.fingerprint(obj_a, obj_type="collision_test")
          fp_b = self.fingerprint(obj_b, obj_type="collision_test")
          ok = fp_a.fingerprint_hash != fp_b.fingerprint_hash
          result.add_check(
              "collision_resistance",
              ok,
              f"Different hashes: {fp_a.hash_prefix} != {fp_b.hash_prefix}" if ok else
              f"COLLISION: {fp_a.hash_prefix} == {fp_b.hash_prefix}"
          )
  
      def _check_empty_input(self, result: SelfCheckResult):
          """验证空输入处理不崩溃."""
          try:
              fp = self.fingerprint({}, obj_type="empty_test")
              ok = len(fp.fingerprint_hash) == 64  # SHA-256 hex length
              result.add_check(
                  "empty_input",
                  ok,
                  f"Empty dict hash: {fp.hash_prefix}"
              )
          except Exception as e:
              result.add_check("empty_input", False, f"Exception: {e}")
  
      def _check_nested_structure(self, result: SelfCheckResult):
          """验证嵌套结构处理."""
          nested = {
              "team": {
                  "name": "Test",
                  "agents": [
                      {"id": "agent-1", "role": "developer", "timestamp": 12345.0},
                      {"id": "agent-2", "role": "researcher", "timestamp": 67890.0},
                  ],
                  "metadata": {"version": 1, "updated_at": "2024-01-01T00:00:00Z"},
              }
          }
          try:
              fp = self.fingerprint(nested, obj_type="nested_test")
              # 验证 template 中 nested 结构被保留但动态字段被剔除
              ok = (
                  len(fp.fingerprint_hash) == 64
                  and "team" in fp.template
                  
  ```
  
  ### 文件: `src/backend/agents/operation_api.py`
  ```py
  # -*- coding: utf-8 -*-
  """操作事件 & 情境切片 API — 查询/追溯/统计 REST 端点.
  
  提供:
    - GET  /api/v1/operations           — 查询操作事件列表
    - GET  /api/v1/operations/{id}      — 获取单个操作事件
    - GET  /api/v1/operations/{id}/trace — 获取操作追溯 (操作+关联切片)
    - GET  /api/v1/operations/{id}/chain — 获取操作因果链
    - GET  /api/v1/context-slices        — 查询情境切片列表
    - GET  /api/v1/context-slices/{id}   — 获取单个情境切片
    - GET  /api/v1/operations/stats      — 存储统计
    - GET  /api/v1/operations/verify     — 完整性验证
    - POST /api/v1/operations/record     — 记录操作事件 (内部调用)
  
  设计原则:
    - 只读端点 (GET) 公开给前端审计面板
    - 写入端点 (POST /record) 供后端 Agent 内部调用
    - 所有响应包含完整性状态
  """
  
  from __future__ import annotations
  
  import logging
  from typing import Any, Dict, List, Optional
  
  from fastapi import APIRouter, HTTPException, Query
  from pydantic import BaseModel, Field
  
  from .operation_models import (
      OperationEvent,
      OperationType,
      OperationQuery,
      OperationTrace,
      ContextQuery,
      ContextSlice,
      ContextType,
  )
  from .operation_store import get_operation_store
  
  logger = logging.getLogger(__name__)
  
  router = APIRouter(prefix="/api/v1/operations", tags=["Operations"])
  
  # 额外的情境切片子路由
  slices_router = APIRouter(prefix="/api/v1/context-slices", tags=["Context Slices"])
  
  
  # ═══════════════════════════════════════════════════════════════
  # Pydantic Schemas
  # ═══════════════════════════════════════════════════════════════
  
  
  class RecordOperationRequest(BaseModel):
      """记录操作事件的请求体."""
      operation_type: str = Field(..., description="操作类型: tool_call / task_started / ...")
      agent_id: str = Field(default="system")
      team_id: str = Field(default="default")
      summary: str = Field(default="")
      detail: Optional[Dict[str, Any]] = Field(default_factory=dict)
      parent_operation_id: Optional[str] = None
      session_id: Optional[str] = None
      task_id: Optional[str] = None
      idempotency_key: Optional[str] = None
      # 可选的情境切片
      context_slices: Optional[List[Dict[str, Any]]] = None
  
  
  class OperationResponse(BaseModel):
      """操作事件响应."""
      ok: bool = True
      operation: Dict[str, Any]
  
  
  class OperationListResponse(BaseModel):
      """操作事件列表响应."""
      ok: bool = True
      operations: List[Dict[str, Any]]
      total: int
      limit: int
      offset: int
  
  
  class TraceResponse(BaseModel):
      """操作追溯响应."""
      ok: bool = True
      trace: Dict[str, Any]
  
  
  class ChainResponse(BaseModel):
      """因果链响应."""
      ok: bool = True
      chain: List[Dict[str, Any]]
      depth: int
  
  
  class SliceResponse(BaseModel):
      """情境切片响应."""
      ok: bool = True
      slice: Dict[str, Any]
  
  
  class SliceListResponse(BaseModel):
      """情境切片列表响应."""
      ok: bool = True
      slices: List[Dict[str, Any]]
      total: int
      limit: int
      offset: int
  
  
  class StatsResponse(BaseModel):
      """统计响应."""
      ok: bool = True
      stats: Dict[str, Any]
  
  
  class VerifyResponse(BaseModel):
      """完整性验证响应."""
      ok: bool = True
      verification: Dict[str, Any]
      healthy: bool
  
  
  # ═══════════════════════════════════════════════════════════════
  # Operation Endpoints
  # ═══════════════════════════════════════════════════════════════
  
  
  @router.post("/record", response_model=OperationResponse)
  async def record_operation(req: RecordOperationRequest):
      """记录一条操作事件 (内部调用).
  
      支持可选的情境切片列表，原子写入。
      幂等键去重: 相同 idempotency_key 不重复写入。
      """
      store = get_operation_store()
  
      # 解析 operation_type
      try:
          op_type = OperationType(req.operation_type)
      except ValueError:
          raise HTTPException(status_code=400, detail=f"未知操作类型: {req.operation_type}")
  
      event = OperationEvent.create(
          operation_type=op_type,
          agent_id=req.agent_id,
          team_id=req.team_id,
          summary=req.summary,
          detail=req.detail or {},
          parent_operation_id=req.parent_operation_id,
          session_id=req.session_id,
          task_id=req.task_id,
          idempotency_key=req.idempotency_key,
      )
  
      # 构建情境切片
      slices: List[ContextSlice] = []
      if req.context_slices:
          for cs_data in req.context_slices:
              ctx_type_str = cs_data.get("context_type", "custom")
              try:
                  ctx_type = ContextType(ctx_type_str)
              except ValueError:
                  ctx_type = ContextType.CUSTOM
              cs = ContextSlice.create(
                  operation_id=event.operation_id,
                  context_type=ctx_type,
                  payload=cs_data.get("payload", {}),
                  summary=cs_data.get("summary", ""),
                  entity_id=cs_data.get("entity_id"),
                  entity_type=cs_data.get("entity_type"),
              )
              slices.append(cs)
  
      if slices:
          ok = await store.record_operation_with_context(event, slices)
      else:
          ok = await store.append_operation(event)
  
      if not ok:
          return OperationResponse(
              ok=True,
              operation={
                  "operation_id": event.operation_id,
                  "status": "duplicate (idempotent)",
              }
          )
  
      return OperationResponse(ok=True, operation=event.to_dict())
  
  
  @router.get("", response_model=OperationListResponse)
  async def list_operations(
      operation_type: Optional[str] = Query(None, description="按操作类型过滤"),
      agent_id: Optional[str] = Query(None, description="按 Agent ID 过滤"),
      team_id: Optional[str] = Query(None, description="按团队 ID 过滤"),
      session_id: Optional[str] = Query(None, description="按会话 ID 过滤"),
      task_id: Optional[str] = Query(None, description="按任务 ID 过滤"),
      parent_operation_id: Optional[str] = Query(None, description="按父操作 ID 过滤"),
      start_time: Optional[str] = Query(None, description="起始时间 (ISO 8601)"),
      end_time: Optional[str] = Query(None, description="结束时间 (ISO 8601)"),
      limit: int = Query(100, ge=1, le=1000, description="返回条数"),
      offset: int = Query(0, ge=0, description="偏移量"),
  ):
      """查询操作事件列表."""
      store = get_operation_store()
  
      op_type_enum = None
      if operation_type:
          try:
              op_type_enum = OperationType(operation_type)
          except ValueError:
              raise HTTPException(status_code=400, detail=f"未知操作类型: {operation_type}")
  
      q = OperationQuery(
          operation_type=op_type_enum,
          agent_id=agent_id,
          team_id=team_id,
          session_id=session_id,
          task_id=task_id,
          parent_operation_id=parent_operation_id,
          start_time=start_time,
          end_time=end_time,
          limit=limit,
          offset=offset,
      )
  
      results = await store.query_operations(q)
      return OperationListResponse(
          operations=[op.to_dict() for op in results],
          total=len(results),
          limit=limit,
          offset=offset,
      )
  
  
  @router.get("/stats", response_model=StatsResponse)
  async def get_stats():
      """获取操作存储统计."""
      store = get_operation_store()
      stats = await store.get_stats()
      return StatsResponse(ok=True, stats=stats)
  
  
  @router.get("/verify", response_model=VerifyResponse)
  async def verify_integrity():
      """验证存储数据完整性."""
      store = get_operation_store()
      v = await store.verify_all()
      healthy = v["corrupt_ops"] == 0 and v["corrupt_slices"] == 0
      return VerifyResponse(ok=True, verification=v, healthy=healthy)
  
  
  @router.get("/{operation_id}", response_model=OperationResponse)
  async def get_operation(operation_id: str):
      """获取单个操作事件."""
      store = get_operation_store()
      op = await store.get_operation(operation_id)
      if not op:
          raise HTTPException(status_code=404, detail=f"操作 {operation_id} 不存在")
      return OperationResponse(ok=True, operation=op.to_dict())
  
  
  @router.get("/{operation_id}/trace", response_model=TraceResponse)
  async def get_operation_trace(operation_id: str):
      """获取操作追溯 — 操作事件 + 关联情境切片."""
      store = get_operation_store()
      trace = await store.get_trace(operation_id)
      if not trace:
          raise HTTPException(status_code=404, detail=f"操作 {operation_id} 不存在")
      return TraceResponse(ok=True, trace=trace.to_dict())
  
  
  @router.get("/{operation_id}/chain", response_model=ChainResponse)
  async def get_causal_chain(
      operation_id: str,
      max_depth: int = Query(20, ge=1, le=100, description="最大追溯深度"),
  ):
      """获取操作因果链 — 沿 parent_operation_id 回溯."""
      store = get_operation_store()
      chain = await store.get_causal_chain(operation_id, max_depth=max_depth)
      return ChainResponse(
          ok=True,
          chain=[op.to_dict() for op in chain],
          depth=len(chain),
      )
  
  
  # ═══════════════════════════════════════════════════════════════
  # Context Slice Endpoints (via slices_router)
  # ═══════════════════════════════════════════════════════════════
  
  
  @slices_router.get("", response_model=SliceListResponse)
  async def list_slices(
      operation_id: Optional[str] = Query(None, description="按操作 ID 过滤"),
      context_type: Optional[str] = Query(None, description="按情境类型过滤"),
      entity_id: Optional[str] = Query(None, description="按实体 ID 过滤"),
      entity_type: Optional[str] = Query(None, description="按实体类型过滤"),
      start_time: Optional[str] = Query(None, description="起始时间"),
      end_time: Optional[str] = Query(None, description="结束时间"),
      limit: int = Query(100, ge=1, le=1000),
      offset: int = Query(0, ge=0),
  ):
     
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose (完整产出)
  
  # PM分解 — project_manager
  
  任务: [广场计划] 现场引入openclaw的agent，这代表了以后的agent都由终端来构建
  步骤: pm_decompose
  Agent: build_pm
  
  ---
  
  📋 任务: 1fe55dd2-0f7
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
    [广场计划] 现场引入openclaw的agent，这代表了以后的agent都由终端来构建
    ## 技术概要
    主目标：构建可审计的终端Agent构建环境，使每个终端的推理、编译与执行链具备不可篡改的因果锚定。核心方案：终端输出锚定结构，强制包含因果向量时钟、状态默克尔根、可复现执行计划哈希，并要求编译器将自身转换过程视为一级推理，输出转换因果哈希，实现故障根双向穿透编译边界。关键约束：锚定必须暴露推理因果图以支撑审计，隐私保护暂为次级目标。最大风险：编译器诚实性仍依赖其自身因果链自证，若编译器伪造转换哈希，上层验证将被系统性欺骗。首要动作：定义并冻结 `context.lock` 及编译器因果接口规范，产出签名方案与默克尔根构建协议。
    
    ## 加权结论 (P0→P1→P2)
    - [P0] 终端必须输出包含因果向量时钟 + 构建图哈希 + 状态默克尔根的不可篡改锚定结构；同时编译器必须输出转换因果哈希，否则构建链在编译边界断裂。 | Architect, Developer | 这是所有后续构建、调试与审计的基础，没有此锚定，分布式终端将退化为不可维护的碎片。
    - [P1] 回归测试框架需支持利用锚定结构进行故障二分定位，要求编译器因果图可被测试工具消费，否则质量门禁无法区分模型谬误与电路编码错误。 | Tester, Architect | 直接决定构建产物的质量可追溯性，是P0方案的必然配套。
    - [P2] 零知识证明可作为可选层附加于锚定之上，以在特定场景隐藏推理路径，但不侵蚀主锚定的因果可审计性，仅在后续版本中评估其性能影响。
    
    ## 执行计划
    | 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |
    |---|---|---|---|---|---|
    | 1 | 设计并发布`context.lock`锚定结构及编译器因果接口规范，包含向量时钟、默克尔根与执行计划哈希的字段定义与签名机制。 | Architect | P0 | 无 | 冻结的锚定结构规范文档，附带示例与签名算法说明。 |
    | 2 | 在终端Agent侧实现`context.lock`生成逻辑，确保每次构建推断均可输出完整锚定记录并本地存储。 | Developer | P0 | 规范冻结 | 终端锚定输出模块，可通过命令行/API调用验证完整性。 |
    | 3 | 实现编译器转换因果哈希输出，修改编译管线使其将输入状态与转换图哈希注入锚定流。 | 全栈开发 | P0 | 规范冻结 | 编译器插件或钩子，输出包含因果哈希的编译日志并接入锚定。 |
    | 4 | 开发测试二分工具，基于锚定链执行等价性检测与故障隔离，支持对比两次构建的向量时钟分歧点。 | Tester | P1 | 终端与编译器锚定实现 | 测试CLI工具，输入两次锚定快照可定位至编译或推理层差异节点。 |
    | 5 | 探索性评估zk-SNARK证明附加方案，在不改动主锚定的前提下，为推理步骤生成可选验证证明。 | 技术研究员 | P2 | 终端锚定模块 | 原型验证报告，给出性能损耗与隐私增益对比，决策是否纳入后续版本。 |
    
    ## 补充观察
    zk-SNARK附加层的计算开销可能显著增加终端能耗与延迟，需在P2评估中严格限定启用场景，避免影响主构建流程的性能基线。
    
    ## 📂 项目上下文 (系统自动预加载)
    
    ### 项目文件结构 (src/ 目录)
    ```
    src/frontend/agent-team-config.html
    src/frontend/datacenter-ratchet-evolution.html
    src/frontend/demo-fieldio-particles.html
    src/frontend/demo-lupi-data-humanism.html
    src/frontend/demo-takram-biosynthetic.html
    src/frontend/digital-twin-cli.html
    src/frontend/extraction-pipeline.html
    src/frontend/index.html
    src/frontend/login.html
    src/frontend/plaza-dark.html
    src/frontend/plaza-old.html
    src/frontend/plaza-wabisabi-v2.html
    src/frontend/plaza-wabisabi.html
    src/frontend/plaza.html
    src/frontend/sandbox-twin.html
    src/frontend/skill-extract.html
    src/frontend/system-evolution.html
    src/frontend/tasks.html
    src/frontend/css/agent-team-config.css
    src/frontend/css/openbridge-theme.css
    src/frontend/css/skill-extract-timeline.css
    src/frontend/css/ws-theme-bridge.css
    src/frontend/js/agent-team-config.js
    src/frontend/js/i18n.js
    src/frontend/js/nav-sidebar.js
    src/frontend/js/skill-extract-timeline.js
    src/backend/__init__.py
    src/backend/agent_team_api.py
    src/backend/main.py
    src/backend/main.py.bak
    src/backend/server.log
    src/backend/startup_check.py
    src/backend/startup_validator.py
    src/backend/tests/__init__.py
    src/backend/tests/conftest.py
    src/backend/tests/conftest.py.bak
    src/backend/tests/test_ab_testing.py
    src/backend/tests/test_agent_toolbox.py
    src/backend/tests/test_evolution_race.py
    src/backend/tests/test_evolution_race.py.bak
    src/backend/tests/test_fingerprint.py
    src/backend/tests/test_fingerprint.py.bak
    src/backend/tests/test_gate_evaluator.py
    src/backend/tests/test_gate_evaluator.py.bak
    src/backend/tests/test_merge_plugin.py
    src/backend/tests/test_merge_plugin.py.bak
    src/backend/tests/test_models.py
    src/backend/tests/test_models.py.bak
    src/backend/tests/test_operation_store.py
    src/backend/tests/test_qa_gate_pipeline.py
    src/backend/tests/test_qa_gate_pipeline.py.bak
    src/backend/tests/test_review_integration.py
    src/backend/tests/test_review_integration.py.bak
    src/backend/tests/test_task_engine.py
    src/backend/tests/test_task_engine.py.bak
    src/backend/tests/test_team_manager.py
    src/backend/tests/test_team_manager.py.bak
    src/backend/tests/test_template_variants.py
    src/backend/tests/test_template_variants.py.bak
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
    src/backend/agents/evolution/__init__.py
    src/backend/agents/evolution/auto_triage.py
    src/backend/agents/evolution/comparator.py
    src/backend/agents/evolution/constraints.py
    src/backend/agents/evolution/dataset_builder.py
    src/backend/agents/evolution/fitness.py
    src/backend/agents/evolution/mutator.py
    src/backend/agents/evolution/optimizer.py
    src/backend/agents/teams/__init__.py
    src/backend/agents/teams/ai_coding_team.py
    src/backend/agents/teams/build_team.py
    src/backend/agents/teams/energy_team.py
    src/backend/agents/teams/xops_team.py
    src/backend/agents/skills/__init__.py
    src/backend/agents/skills/greeting.py
    src/backend/agents/skills/hello.py
    src/backend/sandbox/__init__.py
    src/backend/sandbox/api.py
    src/backend/sandbox/channel.py
    src/backend/sandbox/drift_detector.py
    src/backend/sandbox/global_critic.py
    src/backend/sandbox/llm_decision.py
    src/backend/sandbox/memory_system.py
    src/backend/sandbox/models.py
    src/backend/sandbox/orchestrator.py
    src/backend/sandbox/strategy_aligner.py
    src/backend/sandbox/twin_loop.py
    src/backend/sandbox/world_state.py
    src/backend/sandbox/zero_exp_engine.py
    ... (共 914 个 src/ 文件)
    
    ```
    
    ### 文件: `src/frontend/agent-team-config.html`
    ```html
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
      <meta charset="UTF-8">
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
    <div class="app">
      <!-- Sidebar -->
      <div class="sidebar">
        <div class="sb-header"><h2><span class="seal">智</span> AgentsGroup</h2><select class="fi" id="team-select" style="font-size:12px;padding:6px 8px"></select></div>
        <div class="sb-nav">
          <a class="active" data-view="overview" onclick="switchView('overview')"><span class="seal">览</span> 仪表盘</a>
          <a data-view="models" onclick="switchView('models')"><span class="seal">腦</span> 模型与连接</a>
          <a data-view="tools" onclick="switchView('tools')"><span class="seal seal-koke">具</span> 工具</a>
          <a data-view="skills" onclick="switchView('skills')"><span class="seal seal-kitsune">能</span> 技能</a>
          <a data-view="tasks" onclick="switchView('tasks')"><span class="seal">务</span> 任务</a>
          <a data-view="sessions" onclick="switchView('sessions')"><span class="seal">存</span> 会话存档</a>
          <a data-view="registry" onclick="switchView('registry')"><span class="seal">厂</span> Token 工厂</a>
        </div>
        <div class="sb-section">团队成员</div>
        <div class="sb-agents" id="sb-agents"></div>
        <div class="sb-footer"><button class="btn btn-pink btn-sm" onclick="openWizard()" style="width:100%;justify-content:center">＋ 新建智能体</button></div>
      </div>
      <!-- Main -->
      <div class="main">
        <div class="topbar"><div class="topbar-left"><h1 id="main-title">团队概览</h1><span class="badge" id="main-badge" style="background:rgba(152,245,167,0.15);color:var(--lime)"></span></div><nav class="global-nav"><span class="cur">智能体团队</span><a href="/plaza.html">议事广场</a><a href="/skill-extract.html">技能萃取/赋予</a><a href="/digital-twin-cli.html">数字孪生</a><a href="/sandbox-twin.html">SECS沙箱</a><a href="/system-evolution.html">系统演进</a></nav><div class="topbar-right"><button class="btn btn-sm" onclick="openModal('modal-create-team')">＋ 创建团队</button></div></div>
        <!-- Views -->
        <div id="view-overview" class="main-inner"><div class="main-scroll"><div class="card-grid" id="ov-stats"></div><div class="section" id="ov-team-section"><div class="section-title" id="ov-team-title"></div><table class="tbl"><thead><tr><th>Agent</th><th>角色</th><th>状态</th><th>技能</th><th>操作</th></tr></thead><tbody id="ov-team-agents"></tbody></table></div>
    <!-- 演进状态摘要 -->
    <div class="section" id="evo-section"><div class="section-title" style="display:flex;justify-content:space-between;align-items:center"><span>演进状态</span><a href="/system-evolution.html" class="btn btn-sm">→ 系统演进</a></div><div id="evo-compliance" class="card-grid"></div></div>
    </div></div>
        <div id="view-models" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🧠 模型与连接</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('llm')">🔌 LLM / TTS</button><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-model')">＋ 添加模型</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>名称</th><th>提供商</th><th>Max Tokens</th><th>温度</th><th>默认</th><th>操作</th></tr></thead><tbody id="models-tb"></tbody></table></div></div>
        <div id="view-tools" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">🔧 可用工具</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="switchView('registry')">🏭 Token 工厂</button><button class="btn btn-sm" onclick="showToolSearch()">🔍 搜索</button></div></div><div id="tools-search-bar" class="hidden" style="margin-bottom:12px"><div style="display:flex;gap:10px"><input class="fi" id="tools-search-input" placeholder="搜索工具..." oninput="filterToolCards(this.value)" style="flex:1"><button class="btn btn-sm" onclick="el('tools-search-bar').classList.add('hidden')">✕</button></div></div><div id="tools-cards"></div></div></div>
        <div id="view-skills" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">⚡ 可用技能</div><div style="display:flex;gap:8px"><button class="btn btn-sm" onclick="exportSkillsMD()">📤 导出</button></div></div><div id="skills-cards"></div></div></div>
        <div id="view-tasks" class="main-inner hidden"><div class="main-scroll"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div class="section-title" style="margin:0">📋 并发任务</div><div style="display:flex;gap:8px"><span id="task-stats" style="font-size:12px;color:var(--muted);display:flex;align-items:center"></span><button class="btn btn-pink btn-sm" onclick="openModal('modal-add-task')">＋ 提交任务</button><button class="btn btn-sm" onclick="openModal('modal-batch-task')">📦 批量提交</button></div></div><table class="tbl"><thead><tr><th>ID</th><th>标题</th><th>Agent</th><th>优先级</th><th>依赖</th><th>状态</th><th>操作</th></tr></thead><tbody id="tasks-tb"></tbody></table></div></div>
        <div id="view-llm" class="main-inner hidden"><div class="main-scroll">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><div style="display:flex;align-items:center;gap:12px"><button class="btn btn-sm" onclick="switchView('models')">← 返回</button><div class="section-title" style="margin:0">🔌 LLM / TTS 配置</div></div><button class="btn btn-pink btn-sm" onclick="testLLM()">🧪 测试连接</button></div>
          <div id="llm-status-card" class="card" style="margin-bottom:20px;padding:20px"><p style="color:var(--dim)">加载中...</p></div>
          <div class="card" style="padding:20px;margin-bottom:20px">
            <div class="section-title" style="margin-top:0;margin-bottom:12px">⚙️ 配置 LLM 提供商</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
              <div class="form-group"><label class="form-label">提供商</label><select class="fi" id="llm-provider"><option value="deepseek">DeepSeek</option><option value="openai">OpenAI</option><option value="anthropic">Anthropic</option><option value="local">本地 (Ollama/vLLM)</option><option value="openrouter">OpenRouter</option><option value="github">GitHub Models</option><option value="qwen">通义千问</option></select></div>
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
            <p style="color:var(--muted);font-size:12px;margin-bottom:14px">输入自然语言指令，系统将自动匹配最佳工具和命令 (claw-code-parity PortRuntime)</p>
            <div style="display:grid;gap:12px">
              <div class="form-group" style="margin:0"><label class="form-label">Prompt</label><textarea class="fi" id="rt-prompt" rows="3" placeholder="例: 检查主机状态并分析油温趋势"></textarea></div>
              <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
                <div class="form-group" style="margin:0"><label class="form-label">最大匹配数</label><input class="fi" id="rt-limit" type="number" value="5" min="1" max="20"></div>
                <div class="form-group" style="margin:0"><label class="form-label">禁用工具 (逗号分隔)</label><input class="fi" id="rt-deny" placeholder="web_search, run_python"></div>
                <div class="form-group" style="margin:0"><label class="form-label">禁用前缀</label><input class="fi" id="rt-deny-pfx" placeholder="mcp_, debug_"></div>
              </div>
              <div style="display:flex;gap:10px"><button class="btn btn-pink" onclick="doRoutePrompt()">🎯 路由匹配</button><button class="btn" onclick="doBootstrapSession()">⚡ 引导会话</button><button class="btn" onclick="doRouteAndChat()">💬 路由+对话</button></div>
            </div>
          </div>
          <div id="rt-results" class="card hidden" style="padding:20px"><div class="section-title" style="margin-top:0;margin-bottom:12px">📊 路由结果</div><div id="rt-results-content"></div></div>
          <div class="card" style="margin-top:20px;padding:20px">
            <div class="section-title" style="margin-top:0;margin-bottom:12px">🏊 Tool Pool 装配</div>
            <p style="color:var(--muted);font-size:12px;margin-bottom:14px">按权限上下文装配工具池 — 模拟 Clawith / claw-code-parity ToolPool</p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
              <label style="display:flex;align-items:center;gap:8px;font-size:13px"><input type="checkbox" id="tp-simple"> 简单模式 (仅核心工具)</label>
              <label style="display:flex;align-items:center;gap:8px;font-size:13px"><input type="checkbox" id="tp-mcp" checked> 包含 MCP 工具</label>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px">
              <div class="form-group" style="margin:0"><label class="form-label">禁用工具</label><input class="fi" id="tp-deny" placeholder="逗号分隔"></div>
              <div class="form-group" style="margin:0"><label class="form-label">禁用前缀</label><input class="fi" id="tp-deny-pfx" placeholder="逗号分隔"></div>
            </div>
            <button class="btn btn-pink btn-sm" onclick="doAssemblePool()">🏊 装配 Tool Pool</button>
            <div id="tp-results" style="margin-top:12px"></div>
          </div>
        </div></div>
        <!-- Token Factory View -->
        <div id="view-registr
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
    
    from fastapi import APIRouter, HTTPException
    from pydantic import BaseModel
    from typing import Any, Dict, List, Optional
    
    router = APIRouter(prefix="/api/v1/agent-teams", tags=["Agent Teams"])
    
    
    # ---------------------------------------------------------------------------
    # 全局引用（在 main.py startup 时注入）
    # ---------------------------------------------------------------------------
    _build_team = None
    _execution_team = None
    _scheduler = None
    _evolution_engine = None
    
    
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
    
    class FeedbackSubmission(BaseModel):
        category: str = "optimization"
        severity: str = "medium"
        title: str
        detail: str
    
    
    # ---------------------------------------------------------------------------
    # Scheduler
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
    async def build_reports(limit: int = 10):
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        reports = _build_team.hourly_reports[-limit:]
        return [r.to_dict() for r in reports]
    
    
    @router.get("/build/issues")
    async def build_issues():
        if not _build_team:
            raise HTTPException(503, "Build team not initialized")
        return _build_team.issue_backlog
    
    
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
    async def execution_reports(limit: int = 10):
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        reports = _execution_team.execution_reports[-limit:]
        return [r.to_dict() for r in reports]
    
    
    @router.get("/execution/feedback")
    async def execution_feedback():
        if not _execution_team:
            raise HTTPException(503, "Execution team not initialized")
        return [item.to_dict() for item in _execution_team.feedback_queue]
    
    
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
    async def evolution_items(status: Optional[str] = None):
        """获取演进项列表，可按状态过滤。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_evolution_items(status=status)
    
    
    @router.get("/evolution/rules")
    async def evolution_rules():
        """获取审查规则列表。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return [r.to_dict() for r in _evolution_engine.audit_rules]
    
    
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
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.run_evolution_cycle()
    
    
    @router.post("/evolution/dispatch")
    async def evolution_dispatch():
        """派发所有待处理演进项给 Build 团队。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.dispatch_all_pending()
    
    
    @router.post("/evolution/verify")
    async def evolution_verify():
        """验证所有待验证项。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.verify_all_pending()
    
    
    @router.get("/evolution/items/{item_id}")
    async def evolution_item_detail(item_id: str):
        """获取单个演进项详情。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        item = _evolution_engine.evolution_items.get(item_id)
        if not item:
            raise HTTPException(404, f"Item '{item_id}' not found")
        return item.to_dict()
    
    
    @router.post("/evolution/items/{item_id}/progress")
    async def evolution_mark_progress(item_id: str):
        """标记演进项为进行中。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        ok = _evolution_engine.mark_in_progress(item_id)
        if not ok:
            raise HTTPException(404, f"Item '{item_id}' not found")
        return {"status": "ok", "item_id": item_id, "new_status": "in_progress"}
    
    
    @router.post("/evolution/items/{item_id}/complete")
    async def evolution_mark_complete(item_id: str):
        """标记演进项构建完成，进入待验证。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        ok = _evolution_engine.mark_build_complete(item_id)
        if not ok:
            raise HTTPException(404, f"Item '{item_id}' not found")
        return {"status": "ok", "item_id": item_id, "new_status": "verify_pending"}
    
    
    @router.post("/evolution/close-verified")
    async def evolution_close_verified():
        """关闭所有已验证通过的演进项。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        closed = _evolution_engine.close_verified()
        return {"closed": closed, "count": len(closed)}
    
    
    @router.post("/evolution/close")
    async def evolution_close():
        """关闭所有已验证通过的演进项 (close-verified 别名)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        closed = _evolution_engine.close_verified()
        return {"closed": closed, "count": len(closed)}
    
    
    @router.get("/evolution/history")
    async def evolution_audit_history():
        """获取审查历史记录。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        raw = _evolution_engine.get_audit_history()
        # Normalize field names for frontend (expects timestamp, total)
        result = []
        for h in raw:
            entry = dict(h)
            entry.setdefault("timestamp", entry.pop("time", None))
            entry.setdefault("total", (entry.get("passed") or 0) + (entry.get("failed") or 0) + (entry.get("skipped") or 0))
            result.append(entry)
        return result
    
    
    @router.get("/evolution/analytics")
    async def evolution_analytics():
        """获取演进分析数据 (域覆盖、严重度分布、趋势)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        summary = _evolution_engine.get_evolution_summary()
        history = _evolution_engine.get_audit_history()
        status = _evolution_engine.get_status()
    
        return {
            "summary": summary,
            "history": history,
            "stats": status.get("stats", {}),
            "items_by_status": status.get("items_by_status", {}),
            "rules_count": status.get("audit_rules_count", 0),
        }
    
    
    # ---------------------------------------------------------------------------
    # Phase 3: 业界标准化改进 API
    # ---------------------------------------------------------------------------
    
    @router.get("/evolution/compliance-rating")
    async def evolution_compliance_rating():
        """获取 DNV CII 风格 A~E 合规评级。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _serialize_compliance_rating()
    
    
    def _serialize_compliance_rating() -> Dict[str, Any]:
        data = _evolution_engine.get_compliance_rating()
        data["grade"] = data.get("rating", "?")
        data["description"] = data.get("rating_label", "")
        escalation = _evolution_engine.get_escalation_status()
        data["escalation_tier"] = "corrective" if escalation.get("escalated_count", 0) > 0 else "normal"
        return data
    
    
    @router.post("/evolution/compliance-rating/calculate")
    async def evolution_calculate_rating():
        """重新计算合规评级 (运行快速审查)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.calculate_compliance_rating()
    
    
    @router.get("/evolution/checklist")
    async def evolution_checklist(level: Optional[str] = None):
        """获取 ClassNK 双层自查清单 (company/ship)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_checklist(level=level)
    
    
    @router.get("/evolution/zones")
    async def evolution_zones():
        """获取所有合规区域。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_all_zones()
    
    
    @router.get("/evolution/zones/active")
    async def evolution_active_zones():
        """获取当前激活的合规区域。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_active_zones()
    
    
    @router.post("/evolution/zones/update-position")
    async def evolution_update_position(lat: float = 0.0, lon: float = 0.0):
        """更新船舶位置，自动检测合规区域进入/离开。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.update_vessel_position(lat, lon)
    
    
    @router.get("/evolution/escalation")
    async def evolution_escalation():
        """获取失败升级状态 (DNV SEEMP Part III 风格)。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        return _evolution_engine.get_escalation_status()
    
    
    @router.get("/evolution/trend")
    async def evolution_trend():
        """获取合规评级趋势分析。"""
        if not _evolution_engine:
            raise HTTPException(404, "Evolution engine not registered")
        data = _evo
    ```
    
    ### 文件: `src/backend/agents/fingerprint.py`
    ```py
    # -*- coding: utf-8 -*-
    """
    Fingerprint 计算模块 — 模板提取、动态变量剔除、精确哈希、自检与稳定性监控埋点。
    
    核心功能:
    1. 模板提取: 从 Agent 配置/行为快照中提取结构性骨架
    2. 动态变量剔除: 剥离 timestamps, UUIDs, session IDs, counters 等运行时变量
    3. 精确哈希: SHA-256 确定性哈希，用于指纹比对
    4. 自检: 确定性验证、模板一致性检查、哈希碰撞检测
    5. 稳定性监控埋点: 追踪指纹变异率、哈希漂移、模板稳定性
    
    与 ab_testing.ABTestMetrics.behavior_fingerprint_mutation_rate 集成。
    与 monitoring.collector 集成埋点上报。
    """
    
    from __future__ import annotations
    
    import hashlib
    import json
    import logging
    import re
    import time
    from dataclasses import dataclass, field
    from datetime import datetime, timezone
    from typing import Any, Callable, Dict, List, Optional, Set, Tuple
    
    logger = logging.getLogger(__name__)
    
    
    # ══════════════════════════════════════════════════════════════════
    # 配置与数据模型
    # ══════════════════════════════════════════════════════════════════
    
    
    @dataclass
    class FingerprintConfig:
        """指纹计算配置.
    
       
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
{"error":{"message":"Authentication Fails, Your api key: ****8cba is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}

🔄 连接重试 (1/2)...

⚠️ API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****8cba is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}

🔄 连接重试 (2/2)...

⚠️ API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****8cba is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}

❌ 所有重试已耗尽: API 错误: 401 Authorization Required
{"error":{"message":"Authentication Fails, Your api key: ****8cba is invalid","type":"authentication_error","param":null,"code":"invalid_request_error"}}
