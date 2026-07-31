# 架构设计 — architect

任务: 建立 ES 当前容量、索引、分片和 SLO 基线
步骤: architecture
Agent: build_architect

---

📋 任务: 50619651-39c
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
  建立 ES 当前容量、索引、分片和 SLO 基线
  负责角色: Architect
  依赖: 无
  预期产出: 容量评估表、扩容选型建议、风险清单
  负责角色: Architect
  执行智能体: build_archit
  依赖: 无
  预期产出: 容量评估表、扩容选型建议、风险清单
  
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
  ... (共 1567 个 src/ 文件)
  
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
        launch.textContent = '▶ 沙箱推演';
        launch.title = '启动沙箱推演';
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
      el.style.cssText = 'background:var(--panel2);border:1px solid '+(type==='error'||type==='warn'?'var(--red)':'var(--cyan)')+';color:var(--text);padding:10px 20px;border-radius:8px;font-size:13px;box-shadow:0 4px 20px rgba(0,0,0,0.4);animation:toastIn 0.3s ease-out;margin-top:8px;pointer-events:auto';
      el.innerHTML = '<span>'+(icons[type]||'')+'</span> <span>'+esc(msg)+'</span>';
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
        textEl.style.color = 'var(--text2)';
        textEl.style.cursor = 'default';
        if (spinner) spinner.style.display = 'none';
        _runtimeState.retryCount = 0;
        break;
      case 'offline':
        textEl.innerHTML = '离线 — 点击重连';
        textEl.className = 'runtime-text clickable';
        textEl.onclick = function(){ _retryConnect(); };
        if (spinner) spinner.style.display = 'none';
        _startAutoRetry();
        break;
      case 'error':
        textEl.innerHTML = '错误: ' + (errorMsg||'未知');
        textEl.style.color = 'var(--red)';
        textEl.style.cursor = 'default';
        if (spinner) spinner.style.display = 'none';
        break;
      }
    }
  
    function _retryConnect() {
      _runtimeState.retryCount = 0;
      if (_runtimeState.retryTimer) { clearTimeout(_runtimeState.retryTimer); _runtimeState.retryTimer = null; }
      _setRuntimeStatus('connecting');
      loadRuntimeStatus();
    }
  
    function _startAutoRetry() {
      if (_runtimeState.retryTimer) clearTimeout(_runtimeState.retryTimer);
      if (_runtimeState.retryCount >= 5) return; // 最多重试5次
      _runtimeState.retryTimer = setTimeout(function(){
        _runtimeState.retryCount++;
        _setRuntimeStatus('connecting');
        loadRuntimeStatus();
      }, 5000); // 5秒后自动重连
    }
  
    function _startAutoPoll() {
      if (_runtimeState.pollTimer) clearInterval(_runtimeState.pollTimer);
      _runtimeState.pollTimer = setInterval(function(){
        if (_runtimeState.status === 'online') loadRuntimeStatus();
      }, 30000); // 在线时每30秒自检
    }
  
    window.loadRuntimeStatus = async function() {
      try {
        var r = await _fetchWithTimeout(SECS+'/runtime-status', 4000);
        if (r.status === 401) {
          _setRuntimeStatus('offline');
          return;
        }
        if (!r.ok) throw new Error('HTTP ' + r.status);
        var d = await r.json();
        var healthy = !!d.ready;
        var mode = d.mode || d.runtime_mode || d.runtime || 'SECS';
        if (healthy) {
          _setRuntimeStatus('online', mode);
          _startAutoPoll();
        } else {
          _setRuntimeStatus('offline');
        }
      } catch(e) {
        if (_runtimeState.status === 'connecting' || _runtimeState.status === 'online') {
          _setRuntimeStatus('offline');
        }
      }
    };
  
    function _bootstrapRuntimePanel() {
      if (_runtimeBootstrapDone) return;
      _runtimeBootstrapDone = true;
      _setRuntimeStatus('connecting');
      loadRuntimeStatus();
      setTimeout(loadSecsStats, 200);
      setTimeout(loadExerciseHistory, 500);
    }
  
    // 强制同步世界状态（刷新按钮）
    window.forceSyncWorld = async function() {
      var refreshBtn = document.getElementById('btn-refresh-world');
      if (!refreshBtn) { showToast('刷新按钮未找到', 'warn'); return; }
      var origText = refreshBtn.textContent;
      refreshBtn.textContent = '同步中...';
      refreshBtn.disabled = true;
      try {
        // 使用 /sync-from-dt 从数字孪生拉取实际对象状态同步到世界状态
        var r = await fetch(SECS+'/sync-from-dt', {
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body: JSON.stringify({})
        });
        if (r.ok) {
          var d = await r.json();
          var agentCount = d.synced_agents || 0;
          showToast('世界状态已同步 (agents:'+agentCount+')', 'success');
          _logConsole('世界状态同步完成 agents='+agentCount, 'info');
        } else {
          var ej = await r.json().catch(function(){return{};});
          showToast('同步失败: ' + (ej.detail || 'HTTP '+r.status), 'warn');
        }
      } catch(e) {
        showToast('同步请求失败: '+e.message, 'error');
      }
      refreshBtn.textContent = origText;
      refreshBtn.disabled = false;
      // 同步后刷新所有依赖数据
      loadSecsStats();
      loadExerciseHistory();
      loadRuntimeStatus();
      if (typeof renderAgentList === 'function') renderAgentList();
    };
  
    // 自检：逐行诊断流
    window.runRuntimeSelfCheck = async function() {
      var btn = document.getElementById('secs-selfcheck-btn');
      if (btn) { btn.disabled = true; btn.textContent = '诊断中...'; }
      _setRuntimeStatus('connecting');
      _logConsole('══ 系统自检开始 ══', 'header');
  
      // Step 1: 数据源
      _logConsole('检测数据源 (API)...', 'info');
      try {
        var r1 = await fetch(SECS+'/runtime-status');
        var d1 = await r1.json();
        _logConsole('  ✓ 数据源正常 mode=' + (d1.mode||d1.runtime_mode||'?') + ' ready=' + !!d1.ready, 'step');
      } catch(e) {
        _logConsole('  ✗ 数据源不可达: ' + e.message, 'err');
        _logConsole('  → 建议执行: fix --api-check', 'warn');
      }
  
      // Step 2: 仿真引擎
      _logConsole('检测仿真引擎 (TwinLoop)...', 'info');
      try {
        var r2 = await fetch(SECS+'/stats');
        var d2 = await r2.json();
        var sessions = d2.twin_loop?.total_sessions ?? '?';
        _logConsole('  ✓ 仿真引擎正常 sessions=' + sessions, 'step');
      } catch(e) {
        _logConsole('  ✗ 仿真引擎不可达: ' + e.message, 'err');
        _logConsole('  → 建议执行: fix --engine-restart', 'warn');
      }
  
      // Step 3: 渲染器
      _logConsole('检测3D渲染器 (Three.js)...', 'info');
      var canvas = document.getElementById('env-3d-canvas');
      if (canvas && canvas.getContext) {
        _logConsole('  ✓ 3D渲染器 Canvas 就绪', 'step');
      } else {
        _logConsole('  ✗ 3D渲染器未就绪', 'err');
        _logConsole('  → 建议执行: fix --renderer-reinit', 'warn');
      }
  
      // Step 4: 本地存储
      _logConsole('检测本地存储...', 'info');
      try {
        var testKey = '__secs_diag__' + Date.now();
        localStorage.setItem(testKey, '1');
        localStorage.removeItem(testKey);
        _logConsole('  ✓ localStorage 读写正常', 'step');
      } catch(e) {
        _logConsole('  ✗ localStorage 不可用: ' + e.message, 'err');
      }
  
      // Step 5: 汇总
      _logConsole('══ 自检完成 ══', 'header');
      if (btn) { btn.disabled = false; btn.textContent = '自检'; }
      loadRuntimeStatus();
    };
  
    // ── Pipeline 详情面板 ──
    window.toggleLayerDetail = function(id) {
      var el = document.getElementById('layer-detail-'+id);
      if (!el) return;
      var all = document.querySelectorAll('[id^="layer-detail-L"]');
      all.forEach(function(a){ if (a!==el) a.style.display='none'; });
      el.style.display = el.style.display==='none' ? '' : 'none';
    };
  
    // ── IO Tab 切换 ──
    window.switchIOTab = function(tab, btn) {
      document.getElementById('io-panel-in').style.display = tab==='in' ? '' : 'none';
      document.getElementById('io-panel-out').style.display = tab==='out' ? '' : 'none';
      document.querySelectorAll('#io-tab-in, #io-tab-out').forEach(function(b){ b.classList.remove('active'); });
      if (btn) btn.classList.add('active');
    };
    window.switchIOSub = function(sub, btn) {
      var parent = btn.closest('#io-panel-in, #io-panel-out');
      if (!parent) return;
      parent.querySelectorAll('.io-sub').forEach(function(el){ el.style.display='none'; });
      var target = parent.querySelector('#sub-'+sub);
      if (target) target.style.display = '';
      parent.querySelectorAll('.btn[data-sub]').forEach(function(b){ b.classList.remove('active'); });
      if (btn) btn.classList.add('active');
    };
  
    // ═══════════════════════════════════════════════════════════════
    // 🎯 选择演练团队 (直接点击选中，无需二级确认)
    // ═══════════════════════════════════════════════════════════════
    window.sexyPickTeam = async function() {
      var overlay = document.getElementById('o-team');
      var listEl = document.getElementById('sexy-team-list');
      overlay.style.display = 'block';
      window._teamModalOpen = true;
      listEl.innerHTML = '<div class="modal-select__loading">加载中...</div>';
  
      try {
        var r = await
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
  import time
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
  _MAX_RETRIES = 3  # LLM 调用最大重试次数
  _RETRY_BACKOFF_BASE = 1.5  # 退避基数（秒）
  _LLM_CALL_TIMEOUT = 12.0  # 单次 LLM 调用超时，避免议事厅永久 in_progress
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
          self._escalation_queue: List[Dict[str, Any]] = []  # failed tasks for human review
          self._llm_degraded_until: float = 0.0
  
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
  
      def _is_unusable_llm_text(self, text: str) -> bool:
          """Detect provider fallback/error text that must not become a plan."""
          lowered = (text or "").lower()
          markers = (
              "当前 llm 未连接",
              "authentication fails",
              "api key",
              "invalid_request_error",
              "当前系统功能正常，但需要 llm",
              "llm 当前不可用",
              "暂时离线",
              "no choices returned",
          )
          return any(marker in lowered for marker in markers)
  
      def _mark_llm_degraded(self, seconds: float = 300.0) -> None:
          self._llm_degraded_until = max(self._llm_degraded_until, time.monotonic() + seconds)
  
      def _has_actionable_plan(self, text: str) -> bool:
          if not text or self._is_unusable_llm_text(text):
              return False
          return "## 执行计划" in text and "| 序号 | 任务 |" in text
  
      def _role_label_for(self, participants: List[Participant], keywords: List[str], fallback: str) -> str:
          for participant in participants:
              hay = f"{participant.agent_name} {participant.role}".lower()
              if any(keyword.lower() in hay for keyword in keywords):
                  return participant.agent_name or participant.role or fallback
          return fallback
  
      def _build_deterministic_plan_content(
          self,
          disc: Discussion,
          participants: List[Participant],
          reason: str,
      ) -> str:
          """Build a product-demo-safe plan when the provider is unavailable."""
          leader = self._role_label_for(participants, ["leader", "协调", "派发", "风险"], "运维 Leader")
          architect = self._role_label_for(participants, ["架构", "architect", "规划", "容量"], "上云架构师")
          operator = self._role_label_for(participants, ["操作", "operator", "terraform", "资源创建"], "运维操作员")
          monitor = self._role_label_for(participants, ["巡检", "监控", "故障", "responder"], "巡检监控员")
          cost = self._role_label_for(participants, ["成本", "cost", "ri", "账单"], "成本优化成员")
          region = self._role_label_for(participants, ["北美", "north", "合规", "ai 项目"], "北美 AI 项目运维员")
          return (
              "## 技术概要\n"
              f"围绕「{disc.topic}」，先冻结当前生产基线，再比较纵向升配与横向扩节点两条路径。"
              "首要方案是由 Build System 生成可审阅、可 dry-run、可回滚的 Terraform/运维脚本，"
              "AWS 运维团队负责容量评估、变更执行、监控验收、成本治理与区域合规。"
              "最大风险是扩容后索引迁移、热点分片和跨可用区流量导致的性能抖动；"
              "因此所有动作必须有指标门禁、回滚窗口和北美 AI 项目数据驻留检查。"
              f"本计划由系统在 {reason} 场景下生成，可直接派发任务并进入数字孪生演练。\n\n"
              "## 加权结论 (P0→P1→P2)\n"
              f"- [P0] 先完成容量与风险基线，再让 Build System 编写伸缩脚本 | {architect} / Build System | 没有基线和脚本就无法安全变更\n"
              f"- [P0] 变更执行必须绑定 dry-run、代码 review、单步 apply 和回滚脚本 | {operator} / {leader} | 降低生产误操作和不可逆变更风险\n"
              f"- [P1] 监控验收、故障注入和成本门禁必须在演练场先跑通 | {monitor} / {cost} | 保证扩容后的稳定性和预算可控\n"
              f"- [P1] 北美 AI 项目单独执行区域合规检查 | {region} | 满足数据驻留、审计和法律约束\n"
              "- [P2] 后续可把脚本模板沉淀为公共技能，并把区域合规做成特质技能\n\n"
              "## 执行计划\n"
              "| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
              "|---|---|---|---|---|---|\n"
              f"| 1 | 建立 ES 当前容量、索引、分片和 SLO 基线 | {architect} | P0 | 无 | 容量评估表、扩容选型建议、风险清单 |\n"
              "| 2 | 生成 ElasticSearch 伸缩 Terraform/运维脚本 | Build System | P0 | 任务1 | plan/dry-run/apply/rollback 脚本与 README |\n"
              f"| 3 | 执行代码 review、单步变更和彩排回滚 | {operator} | P0 | 任务2 | 审核记录、执行日志、回滚验证结果 |\n"
              f"| 4 | 配置 CloudWatch/OpenSearch 指标门禁与故障处理演练 | {monitor} | P1 | 任务2 | 告警规则、验收指标、故障演练报告 |\n"
              f"| 5 | 评估扩容账单、RI/Savings Plan 与治理阈值 | {cost} | P1 | 任务1 | 成本预测、购买建议、治理目标 |\n"
              f"| 6 | 完成北美 AI 项目区域合规与部署限制检查 | {region} | P1 | 任务2 | 合规检查表、区域部署准入结论 |\n\n"
              "## 补充观察\n"
              f"{leader} 负责把 P0 任务按变更窗口派发，并在数字孪生演练通过后再进入真实执行。"
          )
  
      def _build_fallback_agent_content(self, participant: Participant, prompt: str) -> str:
          role_text = f"{participant.agent_name or participant.agent_id}（{participant.role}）"
          lowered = prompt.lower()
          if "执行计划" in prompt or "修订后的执行计划" in prompt:
              return (
                  "## 修订说明\n"
                  "LLM 当前不可用，先按变更安全路径生成可派发计划。\n\n"
                  "## 执行计划\n"
                  "| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |\n"
                  "|---|---|---|---|---|---|\n"
                  f"| 1 | 补齐容量基线与回滚门禁 | {role_text} | P0 | 无 | 可执行变更清单 |\n"
                  "| 2 | 生成脚本并完成 review | Build System | P0 | 任务1 | 脚本、README、review 记录 |\n"
                  f"| 3 | 在演练场执行单步扩容和故障注入 | {role_text} | P1 | 任务2 | 演练报告 |\n"
              )
          if "成本" in prompt or "cost" in lowered:
              return f"{role_text} 建议先做扩容前后账单预测，把 RI/Savings Plan 建议和预算阈值写入变更门禁。"
          if "监控" in prompt or "故障" in prompt:
              return f"{role_text} 建议把 CPU、JVMMemoryPressure、写入延迟、分片迁移和 5xx 告警作为验收门禁，并保留回滚窗口。"
          if "合规" in prompt or "北美" in prompt:
              return f"{role_text} 建议单独检查北美 AI 项目的数据驻留、日志审计和区域部署限制，再进入生产变更。"
          return f"{role_text} 建议先确认容量基线、脚本 dry-run、代码 review、监控验收和回滚路径，再推进 ElasticSearch 伸缩。"
  
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
          niche_index = len(used_niches)
          # 自动扩展壁龛数
          if niche_index >= plaza.niche_count:
              plaza.niche_count = niche_index + 1
          p = Participant(
              agent_id=agent_id, agent_name=agent_name, role=role,
              team_id=team_id, seat_tier=seat_tier, niche_role=niche_role,
              niche_index=niche_index,
          )
          plaza.participants[agent_id] = p
          self._store.save_plaza(plaza)
          logger.info(f"🪑 参与者加入广场 {plaza_id}: {agent_name} (壁龛 #{niche_index})")
          return p
  
      def remove_participant(self, plaza_id: str, agent_id: str) -> bool:
          plaza = self._plazas.get(plaza_id)
          if plaza and agent_id in plaza.participants:
              del plaza.participants[agent_id]
              self._store.save_plaza(plaza)
              return True
          return False
  
      # ── 讨论管理 ──────────────────────────────────────────
  
      def create_discussion(
          self, plaza_id: str, topic: str, description: str = "",
          moderator_agent_id: str = "", max_rounds: int = 5,
      ) -> Optional[Discussion]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return None
          disc = Discussion(
              plaza_id=plaza_id, topic=topic, description=description,
              moderator_agent_id=moderator_agent_id, max_rounds=max_rounds,
          )
          plaza.discussions[disc.id] = disc
          self._store.save_plaza(plaza)
          logger.info(f"💬 讨论创建: {topic[:40]} ({disc.id})")
          return disc
  
      def get_discussion(self, plaza_id: str, discussion_id: str) -> Optional[Discussion]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return None
          return plaza.discussions.get(discussion_id)
  
      def list_discussions(self, plaza_id: str) -> List[Discussion]:
          plaza = self._plazas.get(plaza_id)
          if not plaza:
              return []
          return list(plaza.discussions.values())
  
      def delete_discussion(self, plaza_id: str, discussion_id: str) -> bool:
          plaza = self._plazas.get(plaza_id)
          if not plaza or discussion_id not in plaza.discussions:
              return False
          del plaza.discussions[discussion_id]
          self._sse_queues.pop(discussion_id, None)
          self._store.save_plaza(plaza)
          return True
  
      def reset_discussion(self, plaza_id: str, discussion_id: str) -> Optional[Discussion]:
          """重置已结束讨论，保留话题本身以便重新讨论。"""
          disc = self.get_discussion(plaza_id, discussion_id)
          if not disc:
              return None
          disc.status = DiscussionStatus.OPEN
          disc.current_round = 0
          disc.messages.clear()
          disc.summary = ""
          disc.key_conclusions.clear()
          disc.pl
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
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
建立 ES 当前容量、索引、分片和 SLO 基线
负责角色: Architect
依赖: 无
预期产出: 容量评估表、扩容选型建议、风险清单
负责角色: Architect
执行智能体: build_archit
依赖: 无
预期产出: 容量评估表、扩容选型建议、风险清单

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
src/fr
