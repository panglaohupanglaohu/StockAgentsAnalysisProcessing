# 研究分析 — researcher

任务: [广场计划] api.js:247 API 404: /api/v1/agent-config/plaza/esc
步骤: research
Agent: build_researcher

---

📋 任务: 93dd2e6d-e3c
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
  [广场计划] api.js:247 API 404: /api/v1/agent-config/plaza/esc
  ## 技术概要
  前端 `discussion-list.js:87` 将 MongoDB ObjectId (`discussion._id`) 误传为 `plaza_id`，后端期望 UUID v4 格式，导致 plaza 存在性校验失败返回 404。修复方案：前端改为取 `discussion.plaza_uuid`；后端在网关或依赖注入层对 `plaza_id` 做 UUID 格式校验，格式不符直接返回 400/422。最大风险是同类型 ID 混用问题可能存在于其他接口，需全量排查。首要动作是前端改字段并验证，同时后端加参数校验。
  
  ## 加权结论 (P0→P1→P2)
  - [P0] 前端 `discussion-list.js:87` 将 `discussion._id` 改为 `discussion.plaza_uuid`，并处理 `plaza_uuid` 为 null 的降级逻辑 | 全栈开发、Developer | 这是 404 的直接根因，修复即可恢复功能
  - [P0] 后端在网关层或 FastAPI 依赖注入层对 `plaza_id` 做 UUID 格式校验，非法格式返回 400/422，不穿透到业务层 | Architect、Developer | 防止类似参数错误再次绕过业务层返回模糊错误，降低排查成本
  - [P1] 全量排查所有涉及 `plaza_id`、`discussion_id` 跨域引用的接口，确认前端传参字段与后端期望一致 | 技术研究员、Developer | 避免其他功能（评论、点赞等）存在同样的 ID 混用隐患
  - [P1] 在 pytest 中补充 `plaza_id` 非法格式的参数化测试 case（ObjectId、空串、超长串），断言返回 400 | Tester | 补上集成测试的边界覆盖，防止回归
  - [P2] 在 OpenAPI/Swagger 定义中将 `plaza_id` 的 pattern 约束为 UUID v4 正则，便于前后端自动生成校验逻辑 | Researcher | 长期改善 API contract 的可维护性
  
  ## 执行计划
  | 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |
  |---|---|---|---|---|---|
  | 1 | 修复前端 `discussion-list.js:87`，将 `discussion._id` 改为 `discussion.plaza_uuid`，并处理 null 降级 | 全栈开发 | P0 | 无 | 提 PR，本地验证 escalations 页面正常加载 |
  | 2 | 后端 escalations 接口加 `plaza_id` UUID 格式校验（FastAPI 依赖注入或网关中间件），非法格式返回 400/422 | Developer、Architect | P0 | 无 | 非法 `plaza_id` 请求被拦截在业务层外，返回明确错误信息 |
  | 3 | 全量排查所有 `plaza_id`/`discussion_id` 跨域引用接口，输出不一致清单 | 技术研究员、Developer | P1 | 任务1完成 | 排查报告 + 需要修复的接口列表 |
  | 4 | 补充 pytest 参数化测试：`plaza_id` 非法格式 case，断言返回 400 | Tester | P1 | 任务2完成 | 测试用例通过，覆盖边界条件 |
  | 5 | OpenAPI spec 中约束 `plaza_id` 为 UUID v4 pattern | Researcher | P2 | 任务2完成 | spec 更新，前后端可基于此生成校验 |
  
  ## 补充观察
  排查过程中如发现 discussion 文档旧数据 `plaza_uuid` 为 null 的比例较高，可考虑在数据迁移脚本中补全，但不阻塞本次修复上线。
  
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
  ... (共 1651 个 src/ 文件)
  
  ```
  
  ### 文件: `src/frontend/js/plaza.js`
  ```js
  import * as THREE from 'three';
  import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
  import { buildExtractRouting } from './extract-routing.js';
  
  /* ═══════════ GLOBALS ═══════════ */
  const API = '/api/v1/agent-config';
  // E-3: TTS 日志收敛 — 默认静默
  const DEBUG_TTS = false;
  const tlog = (...a) => { if (DEBUG_TTS) console.log(...a); };
  const twarn = (...a) => { if (DEBUG_TTS) console.warn(...a); };
  let curPlaza = null, curDisc = null, curDiscData = null, evtSrc = null;
  let allTeams = [], allParticipants = [];
  let knownPlazas = [];
  let curVerificationState = null;
  let curConsensusState = null;
  let curEscalationState = null;
  const escalationFetchBlocked = new Set();
  const escalationFetchInFlight = new Set();
  let discussionSignalTimer = null;
  // SSE reconnect state
  let _sseRetryTimer = null, _sseRetryDelay = 1000, _sseClosedByUs = false;
  const SSE_MAX_DELAY = 10000;
  // Rendered-message dedup (guards against SSE history replay on reconnect)
  const _seenMsgKeys = new Set();
  function msgKey(m) { return m?.id || `${m?.round_number || 0}|${m?.agent_id || ''}|${String(m?.content ?? '').slice(0, 40)}`; }
  function markMsgSeen(m) { _seenMsgKeys.add(msgKey(m)); }
  const Q = new URLSearchParams(window.location.search);
  const deepLinkPlazaId = Q.get('plaza_id') || '';
  const deepLinkDiscussionId = Q.get('discussion_id') || '';
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const asItems = payload => Array.isArray(payload) ? payload : Array.isArray(payload?.items) ? payload.items : [];
  
  function stripQueryParams(keys) {
    if (!Array.isArray(keys) || !keys.length) return;
    try {
      const u = new URL(window.location.href);
      let changed = false;
      keys.forEach(k => {
        if (u.searchParams.has(k)) {
          u.searchParams.delete(k);
          changed = true;
        }
      });
      if (changed) window.history.replaceState({}, '', `${u.pathname}${u.search}${u.hash}`);
    } catch (e) {
      // ignore URL cleanup failures
    }
  }
  
  function normalizePlazaSelectionOnError() {
    curPlaza = null;
    curDisc = null;
    curDiscData = null;
    curVerificationState = null;
    curConsensusState = null;
    curEscalationState = null;
    localStorage.removeItem('plaza_curPlaza');
    localStorage.removeItem('plaza_curDisc');
    clearDiscussionSignals();
    clearSpeechPlayback();
    teardownSSE();
    renderArena3D([]);
    $('disc-list').innerHTML = '<div style="color:var(--dim);font-size:10px">先选择广场</div>';
    $('msg-log').innerHTML = '<div style="text-align:center;padding:40px 0;color:var(--dim);font-size:10px;letter-spacing:1px;font-family:var(--font-mono)">SELECT PLAZA · CREATE DISCUSSION<br>全员自动入座</div>';
    $('plan-panel').style.display = 'none';
    $('btn-start').disabled = true;
    $('btn-start').textContent = '开始';
    $('status-text').textContent = '';
  }
  
  function isKnownPlaza(id) {
    if (!id) return false;
    return knownPlazas.some(p => p.id === id);
  }
  
  function activePlazaIdFromDOM() {
    return document.querySelector('#plaza-list .plaza-card.active')?.dataset?.plazaId || '';
  }
  
  function activeDiscussionIdFromDOM() {
    return document.querySelector('#disc-list .disc-item.active')?.dataset?.discussionId || '';
  }
  
  function escalationCtxKey(plazaId, discussionId) {
    return `${String(plazaId || '')}::${String(discussionId || '')}`;
  }
  
  function toast(m) {
    const text = String(m ?? '');
    const shouldDecorate = /失败|错误|异常|不可用|未找到|无法|无效|请求失败/.test(text);
    const finalText = shouldDecorate && window.api?.decorateErrorMessage ? window.api.decorateErrorMessage(text) : text;
    const t = document.createElement('div'); t.className = 'toast'; t.textContent = finalText;
    $('toasts').appendChild(t); setTimeout(() => t.remove(), 3500);
  }
  const MODAL_TEXT_INPUT_EVENTS = [
    'keydown', 'keyup', 'keypress',
    'copy', 'cut', 'paste',
    'beforeinput', 'input',
    'compositionstart', 'compositionupdate', 'compositionend'
  ];
  
  function isModalTextInput(target) {
    return !!target?.closest?.('input, textarea, select, [contenteditable="true"]');
  }
  
  function installModalInputGuards(modal) {
    if (!modal || modal._plazaInputGuardsInstalled) return;
    const guard = event => {
      if (isModalTextInput(event.target)) event.stopPropagation();
    };
    MODAL_TEXT_INPUT_EVENTS.forEach(type => modal.addEventListener(type, guard));
    modal._plazaInputGuardsInstalled = true;
  }
  
  function openM(id) {
    const modal = $(id);
    if (!modal) return;
    installModalInputGuards(modal);
    modal.classList.add('open');
  }
  function closeM(id) { $(id)?.classList.remove('open') }
  window.openM = openM; window.closeM = closeM;
  
  // P0: 防止文本选择/复制时误关闭模态框 — 全局检测选择状态
  ;(function() {
    var _closeSelGuard = function(e) {
      if (window.getSelection && !window.getSelection().isCollapsed) return;
      var overlay = e.target.closest ? e.target.closest('.modal-overlay') : null;
      if (!overlay || e.target !== overlay) return;
      // 检查事件源是否来自 input/textarea 内部(拖选后鼠标落在遮罩上)
      var active = document.activeElement;
      if (active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA' || active.isContentEditable)) {
        // 输入框内操作不关弹窗
        e.preventDefault(); e.stopPropagation(); return;
      }
      if (overlay.id) { closeM(overlay.id); return; }
      var modal = overlay.closest('.modal') || overlay.parentElement;
      if (modal && modal.id) { closeM(modal.id); }
    };
    document.addEventListener('click', _closeSelGuard, true);
  })();
  
  // E-1: 通用确认弹层 — 替代 confirm() 阻塞调用
  function showConfirm(msg, onOk) {
    var m = $('m-confirm');
    if (!m) {
      m = document.createElement('div');
      m.id = 'm-confirm';
      m.className = 'modal-overlay';
      m.setAttribute('role', 'dialog');
      m.setAttribute('aria-modal', 'true');
      m.onclick = function(e) { if (e.target === m) closeM('m-confirm'); };
      m.innerHTML = '<div class="modal" style="max-width:360px">' +
        '<h3 style="margin-bottom:10px">确认操作</h3>' +
        '<div id="confirm-msg" style="font-size:12px;padding:12px 0;color:var(--text);line-height:1.6"></div>' +
        '<div class="modal-actions">' +
        '<button class="btn-cancel" onclick="closeM(\'m-confirm\')">取消</button>' +
        '<button id="confirm-ok-btn" class="btn-primary">确认</button></div></div>';
      document.body.appendChild(m);
      // E-4.2: Esc 关闭 + 焦点归还
      m.addEventListener('keydown', function(e) { if (e.key === 'Escape') { closeM('m-confirm'); } });
    }
    $('confirm-msg').textContent = msg;
    var okBtn = $('confirm-ok-btn');
    var handler = function() { closeM('m-confirm'); onOk(); };
    okBtn.onclick = handler;
    openM('m-confirm');
    setTimeout(function() { okBtn.focus(); }, 100);
  }
  window.showConfirm = showConfirm;
  async function api(url, opts) { return window.api.request ? window.api.request(url, opts) : null; }
  async function listApi(path, limit = 200, offset = 0) {
    if (window.api?.list) return asItems(await window.api.list(path, limit, offset));
    return asItems(await api(path));
  }
  
  /* ── Team colors: muted tones on concrete ── */
  const teamColors = {
    build_system: 0x6A8E6A,
    ai_coding: 0x6A7A9E,
    energy_first_principle: 0xB08840
  };
  const teamCSS = {
    build_system: '#6A8E6A',
    ai_coding: '#6A7A9E',
    energy_first_principle: '#B08840'
  };
  const teamNames = {
    build_system: 'BUILD',
    ai_coding: '编程',
    energy_first_principle: '能源'
  };
  function tColor(tid) { return teamColors[tid] || 0x7A7470; }
  
  /* ═══════════ THREE.JS — 安藤忠雄清水混凝土议事厅 ═══════════ */
  const canvas = $('three-canvas');
  // E-4.1: 屏幕阅读器可访问
  if (canvas) canvas.setAttribute('aria-label', '议事厅 3D 场景');
  const container = $('arena-container');
  const scene = new THREE.Scene();
  
  // Exposed-concrete background
  const bgColor = new THREE.Color(0x1A2026);
  scene.background = bgColor;
  scene.fog = new THREE.FogExp2(0x1A2026, 0.0076);
  
  const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 200);
  camera.position.set(0, 14, 28);
  
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setClearColor(0x1A2026);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  
  const controls = new OrbitControls(camera, canvas);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 10;
  controls.maxDistance = 55;
  controls.maxPolarAngle = Math.PI / 2.1;
  controls.target.set(0, 1, 0);
  
  /* ── Lights: restrained Ando-style contrast ── */
  scene.add(new THREE.AmbientLight(0x9099A2, 0.06));
  
  // Main: strong top-front skylight
  const mainLight = new THREE.DirectionalLight(0xC7D0D8, 0.46);
  mainLight.position.set(3, 30, 5);
  mainLight.castShadow = true;
  mainLight.shadow.mapSize.set(2048, 2048);
  mainLight.shadow.camera.near = 1; mainLight.shadow.camera.far = 60;
  mainLight.shadow.camera.left = -25; mainLight.shadow.camera.right = 25;
  mainLight.shadow.camera.top = 25; mainLight.shadow.camera.bottom = -25;
  mainLight.shadow.bias = -0.001;
  mainLight.shadow.normalBias = 0.02;
  scene.add(mainLight);
  
  scene.add(new THREE.HemisphereLight(0x98A2AB, 0x353D46, 0.04));
  
  // Raking architectural light to keep the concrete edges legible
  const rakingLight = new THREE.SpotLight(0xCCD4DC, 0.12, 70, Math.PI / 8, 0.65, 1.3);
  rakingLight.position.set(-18, 24, -6);
  rakingLight.target.position.set(0, 0.8, 0);
  rakingLight.castShadow = true;
  scene.add(rakingLight);
  scene.add(rakingLight.target);
  
  /* ── Material factories ── */
  function concreteMat(color, rough = 0.92) {
    return new THREE.MeshStandardMaterial({ color, roughness: rough, metalness: 0.0 });
  }
  function bronzeMat(color = 0x626A72, rough = 0.35) {
    return new THREE.MeshStandardMaterial({
      color, roughness: rough, metalness: 0.6,
      emissive: new THREE.Color(color).multiplyScalar(0.05), emissiveIntensity: 0.3
    });
  }
  
  /* ── Ground ── */
  const ground = new THREE.Mesh(
    new THREE.CircleGeometry(35, 64),
    concreteMat(0xA9AFB5)
  );
  ground.rotation.x = -Math.PI / 2;
  ground.receiveShadow = true;
  scene.add(ground);
  
  /* ── Tiered Arena: Ando stepped concrete ── */
  const tierDefs = [
    { innerR: 14, outerR: 19, y: 2.4, stepH: 1.0, color: 0x7F8790 },
    { innerR: 9,  outerR: 13, y: 1.5, stepH: 0.8, color: 0x939BA4 },
    { innerR: 5,  outerR: 8,  y: 0.7, stepH: 0.6, color: 0xAEB5BC },
  ];
  tierDefs.forEach(tier => {
    // Ring surface
    const top = new THREE.Mesh(
      new THREE.RingGeometry(tier.innerR, tier.outerR, 96),
      concreteMat(tier.color, 0.88)
    );
    top.rotation.x = -Math.PI / 2; top.position.y = tier.y;
    top.receiveShadow = true;
    scene.add(top);
  
    // Inner wall
    const wall = new THREE.Mesh(
      new THREE.CylinderGeometry(tier.innerR, tier.innerR, tier.stepH, 96, 1, true),
      concreteMat(new THREE.Color(tier.color).multiplyScalar(0.72), 0.92)
    );
    wall.position.y = tier.y - tier.stepH / 2;
    wall.receiveShadow = true; wall.castShadow = true;
    scene.add(wall);
  
    // Outer wall
    const outer = new THREE.Mesh(
      new THREE.CylinderGeometry(tier.outerR, tier.outerR, tier.y, 96, 1, true),
      concreteMat(new THREE.Color(tier.color).multiplyScalar(0.8), 0.92)
    );
    outer.position.y = tier.y / 2;
    scene.add(outer);
  
    // Formwork seam
    const seam = new THREE.Mesh(
      new THREE.RingGeometry(tier.innerR - 0.01, tier.outerR + 0.01, 96),
      new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.075, side: THREE.DoubleSide })
    );
    seam.rotation.x = -Math.PI / 2; seam.position.y = tier.y + 0.005;
    scene.add(seam);
  });
  
  // Center arena floor — polished concrete
  const centerFloor = new THREE.Mesh(
    new THREE.CircleGeometry(4.5, 64),
    concreteMat(0xE2E6E9, 0.72)
  );
  centerFloor.rotation.x = -Math.PI / 2; centerFloor.position.y = 0.01;
  centerFloor.receiveShadow = true;
  scene.add(centerFloor);
  
  // Formwork grid
  for (let i = -4; i <= 4; i++) {
    const lineMat = new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.08, side: THREE.DoubleSide });
    const hLine = new THREE.Mesh(new THREE.PlaneGeometry(9, 0.015), lineMat);
    hLine.rotation.x = -Math.PI / 2; hLine.position.set(0, 0.015, i);
    scene.add(hLine);
    const vLine = new THREE.Mesh(new THREE.PlaneGeometry(9, 0.015), lineMat.clone());
    vLine.rotation.x = -Math.PI / 2; vLine.rotation.z = Math.PI / 2;
    vLine.position.set(i, 0.015, 0);
    scene.add(vLine);
  }
  
  /* ═══ 议事长座椅 — Carlo Scarpa 层叠几何 ═══ */
  const throneGroup = new THREE.Group();
  
  // Layer 1: Large concrete base (rotated slightly)
  const base1 = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.12, 2.0), concreteMat(0x9BA2A9, 0.88));
  base1.position.y = 0.06; base1.rotation.y = Math.PI / 24;
  base1.castShadow = true; base1.receiveShadow = true;
  throneGroup.add(base1);
  
  // Layer 2: Graphite plate, offset
  const base2 = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.06, 1.7), bronzeMat(0x5F666D));
  base2.position.set(0.08, 0.18, -0.05); base2.rotation.y = -Math.PI / 30;
  base2.castShadow = true;
  throneGroup.add(base2);
  
  // Layer 3: Concrete step
  const base3 = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.15, 1.3), concreteMat(0xB0B6BC, 0.84));
  base3.position.set(-0.04, 0.30, -0.02); base3.rotation.y = Math.PI / 40;
  base3.castShadow = true;
  throneGroup.add(base3);
  
  // Seat: cantilevered graphite slab
  const seatMesh = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.07, 0.85), bronzeMat(0x687078, 0.32));
  seatMesh.position.set(0, 0.56, 0.08);
  seatMesh.castShadow = true;
  throneGroup.add(seatMesh);
  
  // Armrests: asymmetric (Scarpa)
  const armL = new THREE.Mesh(new THREE.BoxGeometry(0.10, 0.06, 0.75), concreteMat(0xA6ADB4, 0.86));
  armL.position.set(-0.62, 0.82, 0.05);
  throneGroup.add(armL);
  const armR = new THREE.Mesh(new THREE.BoxGeometry(0.10, 0.06, 0.70), bronzeMat(0x5E666E, 0.32));
  armR.position.set(0.62, 0.72, 0.05);
  throneGroup.add(armR);
  
  // Sky beam: visible shaft of light falling onto the chairman seat
  const throneLight = new THREE.SpotLight(0xF4F7FA, 1.95, 22, Math.PI / 18, 0.12, 1.9);
  throneLight.position.set(0.18, 12.6, -0.42);
  throneLight.target.position.set(0.04, 0.72, 0.08);
  throneLight.castShadow = true;
  throneLight.shadow.mapSize.set(1024, 1024);
  throneLight.shadow.bias = -0.0005;
  throneGroup.add(throneLight);
  throneGroup.add(throneLight.target);
  
  const crossFill = new THREE.SpotLight(0xE6ECF1, 0.16, 10, Math.PI / 24, 0.18, 1.8);
  crossFill.position.set(-0.95, 10.8, -1.2);
  crossFill.target.position.set(0.0, 0.58, 0.04);
  throneGroup.add(crossFill);
  throneGroup.add(crossFill.target);
  
  throneGroup.position.set(0, 0, 0);
  scene.add(throneGroup);
  
  /* ═══════════ AGENT FIGURE — 发光轮廓 ═══════════ */
  const agentMeshes = new Map();
  const sceneAgents = [];
  
  function makeTextCanvas(text, color) {
    const c = document.createElement('canvas');
    c.width = 384; c.height = 104;
    const ctx = c.getContext('2d');
    ctx.clearRect(0, 0, 384, 104);
    ctx.font = '800 34px "Noto Sans SC", sans-serif';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillStyle = color || '#2A2625';
    ctx.fillText(text, 192, 52);
    return c;
  }
  
  function createAgentFigure(name, hexColor, isChairman = fal
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
  
  ### 文件: `src/backend/tests/test_plaza_retry_escalation.py`
  ```py
  # -*- coding: utf-8 -*-
  """Tests for Plaza retry + failure escalation."""
  
  from __future__ import annotations
  
  import asyncio
  import sys
  from pathlib import Path
  from types import SimpleNamespace
  from unittest.mock import AsyncMock, patch
  
  import pytest
  
  _backend_root = Path(__file__).resolve().parent.parent
  if str(_backend_root) not in sys.path:
      sys.path.insert(0, str(_backend_root))
  
  from agents.plaza import Participant, SeatTier, NicheRole
  from agents.plaza_engine import PlazaEngine, _MAX_RETRIES, _RETRY_BACKOFF_BASE
  from agents import plaza_routes
  
  
  @pytest.fixture
  def engine():
      with patch("agents.plaza_engine.PlazaStore") as mock_store:
          mock_store.return_value.load_all.return_value = {}
          e = PlazaEngine()
      return e
  
  
  @pytest.fixture
  def participant():
      return Participant(
          agent_id="test-agent",
          agent_name="Test Agent",
          role="developer",
          team_id="test-team",
          seat_tier=SeatTier.INNER,
          niche_role=NicheRole.ANALYST,
          niche_index=0,
      )
  
  
  class TestRetryAndEscalation:
      """Test LLM call retry logic and failure escalation."""
  
      @pytest.mark.asyncio
      async def test_successful_call_no_retry(self, engine, participant):
          async def good_chat(*args, **kwargs):
              return SimpleNamespace(response="Hello from agent")
  
          engine._chat_fn = good_chat
  
          content = await engine._generate_agent_content(participant, "say hello")
          assert content == "Hello from agent"
          assert len(engine._escalation_queue) == 0
  
      @pytest.mark.asyncio
      async def test_retry_on_failure_then_success(self, engine, participant, monkeypatch):
          # Patch sleep to avoid real delays
          monkeypatch.setattr(asyncio, "sleep", AsyncMock())
  
          call_count = [0]
  
          async def flaky_chat(*args, **kwargs):
              call_count[0] += 1
              if call_count[0] < 3:
                  raise Exception("LLM timeout")
              return SimpleNamespace(response="Recovered!")
  
          engine._chat_fn = flaky_chat
  
          content = await engine._generate_agent_content(participant, "test")
          assert content == "Recovered!"
          assert call_count[0] == 3
          assert len(engine._escalation_queue) == 0
  
      @pytest.mark.asyncio
      async def test_all_retries_exhausted_escalates(self, engine, participant, monkeypatch):
          monkeypatch.setattr(asyncio, "sleep", AsyncMock())
  
          async def always_fail(*args, **kwargs):
              raise Exception("permanent failure")
  
          engine._chat_fn = always_fail
  
          content = await engine._generate_agent_content(
              participant,
              "test prompt",
              plaza_id="plaza-1",
              discussion_id="disc-1",
              discussion_topic="讨论主题",
              round_number=2,
          )
          assert "暂时离线" in content
          assert len(engine._escalation_queue) == 1
          entry = engine._escalation_queue[0]
          assert entry["agent_id"] == "test-agent"
          assert entry["status"] == "pending"
          assert "permanent failure" in entry["error"]
          assert entry["plaza_id"] == "plaza-1"
          assert entry["discussion_id"] == "disc-1"
          assert entry["discussion_topic"] == "讨论主题"
          assert entry["round_number"] == 2
  
      def test_resolve_escalation(self, engine):
          engine._escalation_queue.append({
              "agent_id": "a1",
              "status": "pending",
              "error": "test",
              "timestamp": "2026-06-01T00:00:00Z",
          })
          assert engine.resolve_escalation(0) is True
          assert engine._escalation_queue[0]["status"] == "resolved"
          assert "resolved_at" in engine._escalation_queue[0]
  
      def test_resolve_escalation_invalid_index(self, engine):
          assert engine.resolve_escalation(99) is False
  
      def test_get_escalation_queue_empty(self, engine):
          assert engine.get_escalation_queue() == []
  
      @pytest.mark.asyncio
      async def test_retry_respects_max_retries_constant(self, engine, participant, monkeypatch):
          monkeypatch.setattr(asyncio, "sleep", AsyncMock())
          call_count = [0]
  
          async def counting_fail(*args, **kwargs):
              call_count[0] += 1
              raise Exception("fail")
  
          engine._chat_fn = counting_fail
  
          await engine._generate_agent_content(participant, "test")
          assert call_count[0] == _MAX_RETRIES
  
      @pytest.mark.asyncio
      async def test_escalation_route_filters_by_discussion_and_includes_index(self, engine, monkeypatch):
          engine._escalation_queue.extend([
              {
                  "agent_id": "a-1",
                  "agent_name": "Agent 1",
                  "status": "pending",
                  "error": "boom",
                  "timestamp": "2026-06-02T00:00:00Z",
                  "plaza_id": "plaza-a",
                  "discussion_id": "disc-a",
                  "discussion_topic": "Topic A",
                  "round_number": 2,
              },
              {
                  "agent_id": "a-2",
                  "agent_name": "Agent 2",
                  "status": "resolved",
                  "error": "done",
                  "timestamp": "2026-06-02T00:00:01Z",
                  "plaza_id": "plaza-a",
                  "discussion_id": "disc-a",
                  "discussion_topic": "Topic A",
                  "round_number": 3,
              },
              {
                  "agent_id": "b-1",
                  "agent_name": "Agent 3",
                  "status": "pending",
                  "error": "elsewhere",
                  "timestamp": "2026-06-02T00:00:02Z",
                  "plaza_id": "plaza-b",
                  "discussion_id": "disc-b",
                  "discussion_topic": "Topic B",
                  "round_number": 1,
              },
          ])
          monkeypatch.setattr(plaza_routes, "get_plaza_engine", lambda: engine)
  
          payload = await plaza_routes.get_escalation_queue(
              plaza_id="plaza-a",
              discussion_id="disc-a",
              entry_status="pending",
          )
  
          assert payload["total"] == 1
          assert payload["pending_count"] == 1
          assert payload["items"][0]["index"] == 0
          assert payload["items"][0]["discussion_id"] == "disc-a"
  
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
      keys = list(templa
  ```
  
  (后续文件因 token 预算已省略)
  
  (后续文件因 token 预算已省略)
  
  
  ## 前序步骤的产出 (递进式摘要)
  
  ### 步骤 01: pm_decompose (完整产出)
  
  # PM分解 — project_manager
  
  任务: [广场计划] api.js:247 API 404: /api/v1/agent-config/plaza/esc
  步骤: pm_decompose
  Agent: build_pm
  
  ---
  
  📋 任务: 93dd2e6d-e3c
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
    [广场计划] api.js:247 API 404: /api/v1/agent-config/plaza/esc
    ## 技术概要
    前端 `discussion-list.js:87` 将 MongoDB ObjectId (`discussion._id`) 误传为 `plaza_id`，后端期望 UUID v4 格式，导致 plaza 存在性校验失败返回 404。修复方案：前端改为取 `discussion.plaza_uuid`；后端在网关或依赖注入层对 `plaza_id` 做 UUID 格式校验，格式不符直接返回 400/422。最大风险是同类型 ID 混用问题可能存在于其他接口，需全量排查。首要动作是前端改字段并验证，同时后端加参数校验。
    
    ## 加权结论 (P0→P1→P2)
    - [P0] 前端 `discussion-list.js:87` 将 `discussion._id` 改为 `discussion.plaza_uuid`，并处理 `plaza_uuid` 为 null 的降级逻辑 | 全栈开发、Developer | 这是 404 的直接根因，修复即可恢复功能
    - [P0] 后端在网关层或 FastAPI 依赖注入层对 `plaza_id` 做 UUID 格式校验，非法格式返回 400/422，不穿透到业务层 | Architect、Developer | 防止类似参数错误再次绕过业务层返回模糊错误，降低排查成本
    - [P1] 全量排查所有涉及 `plaza_id`、`discussion_id` 跨域引用的接口，确认前端传参字段与后端期望一致 | 技术研究员、Developer | 避免其他功能（评论、点赞等）存在同样的 ID 混用隐患
    - [P1] 在 pytest 中补充 `plaza_id` 非法格式的参数化测试 case（ObjectId、空串、超长串），断言返回 400 | Tester | 补上集成测试的边界覆盖，防止回归
    - [P2] 在 OpenAPI/Swagger 定义中将 `plaza_id` 的 pattern 约束为 UUID v4 正则，便于前后端自动生成校验逻辑 | Researcher | 长期改善 API contract 的可维护性
    
    ## 执行计划
    | 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |
    |---|---|---|---|---|---|
    | 1 | 修复前端 `discussion-list.js:87`，将 `discussion._id` 改为 `discussion.plaza_uuid`，并处理 null 降级 | 全栈开发 | P0 | 无 | 提 PR，本地验证 escalations 页面正常加载 |
    | 2 | 后端 escalations 接口加 `plaza_id` UUID 格式校验（FastAPI 依赖注入或网关中间件），非法格式返回 400/422 | Developer、Architect | P0 | 无 | 非法 `plaza_id` 请求被拦截在业务层外，返回明确错误信息 |
    | 3 | 全量排查所有 `plaza_id`/`discussion_id` 跨域引用接口，输出不一致清单 | 技术研究员、Developer | P1 | 任务1完成 | 排查报告 + 需要修复的接口列表 |
    | 4 | 补充 pytest 参数化测试：`plaza_id` 非法格式 case，断言返回 400 | Tester | P1 | 任务2完成 | 测试用例通过，覆盖边界条件 |
    | 5 | OpenAPI spec 中约束 `plaza_id` 为 UUID v4 pattern | Researcher | P2 | 任务2完成 | spec 更新，前后端可基于此生成校验 |
    
    ## 补充观察
    排查过程中如发现 discussion 文档旧数据 `plaza_uuid` 为 null 的比例较高，可考虑在数据迁移脚本中补全，但不阻塞本次修复上线。
    
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
    ... (共 1651 个 src/ 文件)
    
    ```
    
    ### 文件: `src/frontend/js/plaza.js`
    ```js
    import * as THREE from 'three';
    import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
    import { buildExtractRouting } from './extract-routing.js';
    
    /* ═══════════ GLOBALS ═══════════ */
    const API = '/api/v1/agent-config';
    // E-3: TTS 日志收敛 — 默认静默
    const DEBUG_TTS = false;
    const tlog = (...a) => { if (DEBUG_TTS) console.log(...a); };
    const twarn = (...a) => { if (DEBUG_TTS) console.warn(...a); };
    let curPlaza = null, curDisc = null, curDiscData = null, evtSrc = null;
    let allTeams = [], allParticipants = [];
    let knownPlazas = [];
    let curVerificationState = null;
    let curConsensusState = null;
    let curEscalationState = null;
    const escalationFetchBlocked = new Set();
    const escalationFetchInFlight = new Set();
    let discussionSignalTimer = null;
    // SSE reconnect state
    let _sseRetryTimer = null, _sseRetryDelay = 1000, _sseClosedByUs = false;
    const SSE_MAX_DELAY = 10000;
    // Rendered-message dedup (guards against SSE history replay on reconnect)
    const _seenMsgKeys = new Set();
    function msgKey(m) { return m?.id || `${m?.round_number || 0}|${m?.agent_id || ''}|${String(m?.content ?? '').slice(0, 40)}`; }
    function markMsgSeen(m) { _seenMsgKeys.add(msgKey(m)); }
    const Q = new URLSearchParams(window.location.search);
    const deepLinkPlazaId = Q.get('plaza_id') || '';
    const deepLinkDiscussionId = Q.get('discussion_id') || '';
    const $ = id => document.getElementById(id);
    const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const asItems = payload => Array.isArray(payload) ? payload : Array.isArray(payload?.items) ? payload.items : [];
    
    function stripQueryParams(keys) {
      if (!Array.isArray(keys) || !keys.length) return;
      try {
        const u = new URL(window.location.href);
        let changed = false;
        keys.forEach(k => {
          if (u.searchParams.has(k)) {
            u.searchParams.delete(k);
            changed = true;
          }
        });
        if (changed) window.history.replaceState({}, '', `${u.pathname}${u.search}${u.hash}`);
      } catch (e) {
        // ignore URL cleanup failures
      }
    }
    
    function normalizePlazaSelectionOnError() {
      curPlaza = null;
      curDisc = null;
      curDiscData = null;
      curVerificationState = null;
      curConsensusState = null;
      curEscalationState = null;
      localStorage.removeItem('plaza_curPlaza');
      localStorage.removeItem('plaza_curDisc');
      clearDiscussionSignals();
      clearSpeechPlayback();
      teardownSSE();
      renderArena3D([]);
      $('disc-list').innerHTML = '<div style="color:var(--dim);font-size:10px">先选择广场</div>';
      $('msg-log').innerHTML = '<div style="text-align:center;padding:40px 0;color:var(--dim);font-size:10px;letter-spacing:1px;font-family:var(--font-mono)">SELECT PLAZA · CREATE DISCUSSION<br>全员自动入座</div>';
      $('plan-panel').style.display = 'none';
      $('btn-start').disabled = true;
      $('btn-start').textContent = '开始';
      $('status-text').textContent = '';
    }
    
    function isKnownPlaza(id) {
      if (!id) return false;
      return knownPlazas.some(p => p.id === id);
    }
    
    function activePlazaIdFromDOM() {
      return document.querySelector('#plaza-list .plaza-card.active')?.dataset?.plazaId || '';
    }
    
    function activeDiscussionIdFromDOM() {
      return document.querySelector('#disc-list .disc-item.active')?.dataset?.discussionId || '';
    }
    
    function escalationCtxKey(plazaId, discussionId) {
      return `${String(plazaId || '')}::${String(discussionId || '')}`;
    }
    
    function toast(m) {
      const text = String(m ?? '');
      const shouldDecorate = /失败|错误|异常|不可用|未找到|无法|无效|请求失败/.test(text);
      const finalText = shouldDecorate && window.api?.decorateErrorMessage ? window.api.decorateErrorMessage(text) : text;
      const t = document.createElement('div'); t.className = 'toast'; t.textContent = finalText;
      $('toasts').appendChild(t); setTimeout(() => t.remove(), 3500);
    }
    const MODAL_TEXT_INPUT_EVENTS = [
      'keydown', 'keyup', 'keypress',
      'copy', 'cut', 'paste',
      'beforeinput', 'input',
      'compositionstart', 'compositionupdate', 'compositionend'
    ];
    
    function isModalTextInput(target) {
      return !!target?.closest?.('input, textarea, select, [contenteditable="true"]');
    }
    
    function installModalInputGuards(modal) {
      if (!modal || modal._plazaInputGuardsInstalled) return;
      const guard = event => {
        if (isModalTextInput(event.target)) event.stopPropagation();
      };
      MODAL_TEXT_INPUT_EVENTS.forEach(type => modal.addEventListener(type, guard));
      modal._plazaInputGuardsInstalled = true;
    }
    
    function openM(id) {
      const modal = $(id);
      if (!modal) return;
      installModalInputGuards(modal);
      modal.classList.add('open');
    }
    function closeM(id) { $(id)?.classList.remove('open') }
    window.openM = openM; window.closeM = closeM;
    
    // P0: 防止文本选择/复制时误关闭模态框 — 全局检测选择状态
    ;(function() {
      var _closeSelGuard = function(e) {
        if (window.getSelection && !window.getSelection().isCollapsed) return;
        var overlay = e.target.closest ? e.target.closest('.modal-overlay') : null;
        if (!overlay || e.target !== overlay) return;
        // 检查事件源是否来自 input/textarea 内部(拖选后鼠标落在遮罩上)
        var active = document.activeElement;
        if (active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA' || active.isContentEditable)) {
          // 输入框内操作不关弹窗
          e.preventDefault(); e.stopPropagation(); return;
        }
        if (overlay.id) { closeM(overlay.id); return; }
        var modal = overlay.closest('.modal') || overlay.parentElement;
        if (modal && modal.id) { closeM(modal.id); }
      };
      document.addEventListener('click', _closeSelGuard, true);
    })();
    
    // E-1: 通用确认弹层 — 替代 confirm() 阻塞调用
    function showConfirm(msg, onOk) {
      var m = $('m-confirm');
      if (!m) {
        m = document.createElement('div');
        m.id = 'm-confirm';
        m.className = 'modal-overlay';
        m.setAttribute('role', 'dialog');
        m.setAttribute('aria-modal', 'true');
        m.onclick = function(e) { if (e.target === m) closeM('m-confirm'); };
        m.innerHTML = '<div class="modal" style="max-width:360px">' +
          '<h3 style="margin-bottom:10px">确认操作</h3>' +
          '<div id="confirm-msg" style="font-size:12px;padding:12px 0;color:var(--text);line-height:1.6"></div>' +
          '<div class="modal-actions">' +
          '<button class="btn-cancel" onclick="closeM(\'m-confirm\')">取消</button>' +
          '<button id="confirm-ok-btn" class="btn-primary">确认</button></div></div>';
        document.body.appendChild(m);
        // E-4.2: Esc 关闭 + 焦点归还
        m.addEventListener('keydown', function(e) { if (e.key === 'Escape') { closeM('m-confirm'); } });
      }
      $('confirm-msg').textContent = msg;
      var okBtn = $('confirm-ok-btn');
      var handler = function() { closeM('m-confirm'); onOk(); };
      okBtn.onclick = handler;
      openM('m-confirm');
      setTimeout(function() { okBtn.focus(); }, 100);
    }
    window.showConfirm = showConfirm;
    async function api(url, opts) { return window.api.request ? window.api.request(url, opts) : null; }
    async function listApi(path, limit = 200, offset = 0) {
      if (window.api?.list) return asItems(await window.api.list(path, limit, offset));
      return asItems(await api(path));
    }
    
    /* ── Team colors: muted tones on concrete ── */
    const teamColors = {
      build_system: 0x6A8E6A,
      ai_coding: 0x6A7A9E,
      energy_first_principle: 0xB08840
    };
    const teamCSS = {
      build_system: '#6A8E6A',
      ai_coding: '#6A7A9E',
      energy_first_principle: '#B08840'
    };
    const teamNames = {
      build_system: 'BUILD',
      ai_coding: '编程',
      energy_first_principle: '能源'
    };
    function tColor(tid) { return teamColors[tid] || 0x7A7470; }
    
    /* ═══════════ THREE.JS — 安藤忠雄清水混凝土议事厅 ═══════════ */
    const canvas = $('three-canvas');
    // E-4.1: 屏幕阅读器可访问
    if (canvas) canvas.setAttribute('aria-label', '议事厅 3D 场景');
    const container = $('arena-container');
    const scene = new THREE.Scene();
    
    // Exposed-concrete background
    const bgColor = new THREE.Color(0x1A2026);
    scene.background = bgColor;
    scene.fog = new THREE.FogExp2(0x1A2026, 0.0076);
    
    const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 200);
    camera.position.set(0, 14, 28);
    
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
    renderer.setClearColor(0x1A2026);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFShadowMap;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.0;
    
    const controls = new OrbitControls(camera, canvas);
    controls.enableDamping = true;
    controls.dampingFactor = 0.06;
    controls.minDistance = 10;
    controls.maxDistance = 55;
    controls.maxPolarAngle = Math.PI / 2.1;
    controls.target.set(0, 1, 0);
    
    /* ── Lights: restrained Ando-style contrast ── */
    scene.add(new THREE.AmbientLight(0x9099A2, 0.06));
    
    // Main: strong top-front skylight
    const mainLight = new THREE.DirectionalLight(0xC7D0D8, 0.46);
    mainLight.position.set(3, 30, 5);
    mainLight.castShadow = true;
    mainLight.shadow.mapSize.set(2048, 2048);
    mainLight.shadow.camera.near = 1; mainLight.shadow.camera.far = 60;
    mainLight.shadow.camera.left = -25; mainLight.shadow.camera.right = 25;
    mainLight.shadow.camera.top = 25; mainLight.shadow.camera.bottom = -25;
    mainLight.shadow.bias = -0.001;
    mainLight.shadow.normalBias = 0.02;
    scene.add(mainLight);
    
    scene.add(new THREE.HemisphereLight(0x98A2AB, 0x353D46, 0.04));
    
    // Raking architectural light to keep the concrete edges legible
    const rakingLight = new THREE.SpotLight(0xCCD4DC, 0.12, 70, Math.PI / 8, 0.65, 1.3);
    rakingLight.position.set(-18, 24, -6);
    rakingLight.target.position.set(0, 0.8, 0);
    rakingLight.castShadow = true;
    scene.add(rakingLight);
    scene.add(rakingLight.target);
    
    /* ── Material factories ── */
    function concreteMat(color, rough = 0.92) {
      return new THREE.MeshStandardMaterial({ color, roughness: rough, metalness: 0.0 });
    }
    function bronzeMat(color = 0x626A72, rough = 0.35) {
      return new THREE.MeshStandardMaterial({
        color, roughness: rough, metalness: 0.6,
        emissive: new THREE.Color(color).multiplyScalar(0.05), emissiveIntensity: 0.3
      });
    }
    
    /* ── Ground ── */
    const ground = new THREE.Mesh(
      new THREE.CircleGeometry(35, 64),
      concreteMat(0xA9AFB5)
    );
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    scene.add(ground);
    
    /* ── Tiered Arena: Ando stepped concrete ── */
    const tierDefs = [
      { innerR: 14, outerR: 19, y: 2.4, stepH: 1.0, color: 0x7F8790 },
      { innerR: 9,  outerR: 13, y: 1.5, stepH: 0.8, color: 0x939BA4 },
      { innerR: 5,  outerR: 8,  y: 0.7, stepH: 0.6, color: 0xAEB5BC },
    ];
    tierDefs.forEach(tier => {
      // Ring surface
      const top = new THREE.Mesh(
        new THREE.RingGeometry(tier.innerR, tier.outerR, 96),
        concreteMat(tier.color, 0.88)
      );
      top.rotation.x = -Math.PI / 2; top.position.y = tier.y;
      top.receiveShadow = true;
      scene.add(top);
    
      // Inner wall
      const wall = new THREE.Mesh(
        new THREE.CylinderGeometry(tier.innerR, tier.innerR, tier.stepH, 96, 1, true),
        concreteMat(new THREE.Color(tier.color).multiplyScalar(0.72), 0.92)
      );
      wall.position.y = tier.y - tier.stepH / 2;
      wall.receiveShadow = true; wall.castShadow = true;
      scene.add(wall);
    
      // Outer wall
      const outer = new THREE.Mesh(
        new THREE.CylinderGeometry(tier.outerR, tier.outerR, tier.y, 96, 1, true),
        concreteMat(new THREE.Color(tier.color).multiplyScalar(0.8), 0.92)
      );
      outer.position.y = tier.y / 2;
      scene.add(outer);
    
      // Formwork seam
      const seam = new THREE.Mesh(
        new THREE.RingGeometry(tier.innerR - 0.01, tier.outerR + 0.01, 96),
        new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.075, side: THREE.DoubleSide })
      );
      seam.rotation.x = -Math.PI / 2; seam.position.y = tier.y + 0.005;
      scene.add(seam);
    });
    
    // Center arena floor — polished concrete
    const centerFloor = new THREE.Mesh(
      new THREE.CircleGeometry(4.5, 64),
      concreteMat(0xE2E6E9, 0.72)
    );
    centerFloor.rotation.x = -Math.PI / 2; centerFloor.position.y = 0.01;
    centerFloor.receiveShadow = true;
    scene.add(centerFloor);
    
    // Formwork grid
    for (let i = -4; i <= 4; i++) {
      const lineMat = new THREE.MeshBasicMaterial({ color: 0x000000, transparent: true, opacity: 0.08, side: THREE.DoubleSide });
      const hLine = new THREE.Mesh(new THREE.PlaneGeometry(9, 0.015), lineMat);
      hLine.rotation.x = -Math.PI / 2; hLine.position.set(0, 0.015, i);
      scene.add(hLine);
      const vLine = new THREE.Mesh(new THREE.PlaneGeometry(9, 0.015), lineMat.clone());
      vLine.rotation.x = -Math.PI / 2; vLine.rotation.z = Math.PI / 2;
      vLine.position.set(i, 0.015, 0);
      scene.add(vLine);
    }
    
    /* ═══ 议事长座椅 — Carlo Scarpa 层叠几何 ═══ */
    const throneGroup = new THREE.Group();
    
    // Layer 1: Large concrete base (rotated slightly)
    const base1 = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.12, 2.0), concreteMat(0x9BA2A9, 0.88));
    base1.position.y = 0.06; base1.rotation.y = Math.PI / 24;
    base1.castShadow = true; base1.receiveShadow = true;
    throneGroup.add(base1);
    
    // Layer 2: Graphite plate, offset
    const base2 = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.06, 1.7), bronzeMat(0x5F666D));
    base2.position.set(0.08, 0.18, -0.05); base2.rotation.y = -Math.PI / 30;
    base2.castShadow = true;
    throneGroup.add(base2);
    
    // Layer 3: Concrete step
    const base3 = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.15, 1.3), concreteMat(0xB0B6BC, 0.84));
    base3.position.set(-0.04, 0.30, -0.02); base3.rotation.y = Math.PI / 40;
    base3.castShadow = true;
    throneGroup.add(base3);
    
    // Seat: cantilevered graphite slab
    const seatMesh = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.07, 0.85), bronzeMat(0x687078, 0.32));
    seatMesh.position.set(0, 0.56, 0.08);
    seatMesh.castShadow = true;
    throneGroup.add(seatMesh);
    
    // Armrests: asymmetric (Scarpa)
    const armL = new THREE.Mesh(new THREE.BoxGeometry(0.10, 0.06, 0.75), concreteMat(0xA6ADB4, 0.86));
    armL.position.set(-0.62, 0.82, 0.05);
    throneGroup.add(armL);
    const armR = new THREE.Mesh(new THREE.BoxGeometry(0.10, 0.06, 0.70), bronzeMat(0x5E666E, 0.32));
    armR.position.set(0.62, 0.72, 0.05);
    throneGroup.add(armR);
    
    // Sky beam: visible shaft of light falling onto the chairman seat
    const throneLight = new THREE.SpotLight(0xF4F7FA, 1.95, 22, Math.PI / 18, 0.12, 1.9);
    throneLight.position.set(0.18, 12.6, -0.42);
    throneLight.target.position.set(0.04, 0.72, 0.08);
    throneLight.castShadow = true;
    throneLight.shadow.mapSize.set(1024, 1024);
    throneLight.shadow.bias = -0.0005;
    throneGroup.add(throneLight);
    throneGroup.add(throneLight.target);
    
    const crossFill = new THREE.SpotLight(0xE6ECF1, 0.16, 10, Math.PI / 24, 0.18, 1.8);
    crossFill.position.set(-0.95, 10.8, -1.2);
    crossFill.target.position.set(0.0, 0.58, 0.04);
    throneGroup.add(crossFill);
    throneGroup.add(crossFill.target);
    
    throneGroup.position.set(0, 0, 0);
    scene.add(throneGroup);
    
    /* ═══════════ AGENT FIGURE — 发光轮廓 ═══════════ */
    const agentMeshes = new Map();
    const sceneAgents = [];
    
    function makeTextCanvas(text, color) {
      const c = document.createElement('canvas');
      c.width = 384; c.height = 104;
      const ctx = c.getContext('2d');
      ctx.clearRect(0, 0, 384, 104);
      ctx.font = '800 34px "Noto Sans SC", sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillStyle = color || '#2A2625';
      ctx.fillText(text, 192, 52);
      return c;
    }
    
    function createAgentFigure(name, hexColor, isChairman = fal
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
            assert channel.evolution_items[item.id].status == E
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
[广场计划] api.js:247 API 404: /api/v1/agent-config/plaza/esc
## 技术概要
前端 `discussion-list.js:87` 将 MongoDB ObjectId (`discussion._id`) 误传为 `plaza_id`，后端期望 UUID v4 格式，导致 plaza 存在性校验失败返回 404。修复方案：前端改为取 `discussion.plaza_uuid`；后端在网关或依赖注入层对 `plaza_id` 做 UUID 格式校验，格式不符直接返回 400/422。最大风险是同类型 ID 混用问题可能存在于其他接口，需全量排查。首要动作是前端改字段并验证，同时后端加参数校验。

## 加权结论 (P0→P1→P2)
- [P0] 前端 `discussion-list.js:87` 将 `discussion._id` 改为 `discussion.plaza_uuid`，并处理 `plaza_uuid` 为 null 的降级逻辑 | 全栈开发、Developer | 这是 404 的直接根因，修复即可恢复功能
- [P0] 后端在网关层或 FastAPI 依赖注入层对 `plaza_id` 做 UUID 格式校验，非法格式返回 400/422，不穿透到业务层 | Architect、Developer | 防止类似参数错误再次绕过业务层返回模糊错误，降低排查成本
- [P1] 全量排查所有涉及 `plaza_id`、`discussion_id` 跨域引用的接口，确认前端传参字段与后端期望一致 | 技术研究员、Developer | 避免其他功能（评论、点赞等）存在同样的 ID 混用隐患
- [P1] 在 pytest 中补充 `plaza_id` 非法格式的参数化测试 case（ObjectId、空串、超长串），断言返回 400 | Tester | 补上集成测试的边界覆盖，防止回归
- [P2] 在 OpenAPI/Swagger 定义中将 `plaza_id` 的 pattern 约束为 UUID v4 正则，便于前后端自动生成校验逻辑 | Researcher | 长期改善 API contract 的可维护性

## 执行计划
| 序号 | 任务 | 负责角色 | 优先级 | 依赖 | 预期产出 |
|---|---|---|---|---|---|
| 1 | 修复前端 `discussion-list.js:87`，将 `discussion._id` 改为 `discussion.plaza
