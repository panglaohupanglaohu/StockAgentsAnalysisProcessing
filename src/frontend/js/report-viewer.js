/* StockAgents immersive report reader — renders only versioned, sanitized documents. */
(function () {
  'use strict';
  var CHANNELS = {
    ai_news_60s: { label: 'AI 60 秒 · 沉浸式情报阅读', lede: '从原始证据到主题、信号、业务影响和反证的可追溯分析链。' },
    dufu_world_intel: { label: '独夫之心 · 世界趋势阅读', lede: '把事件、时间线、驱动因素、情景与反证编排成可回看的世界趋势故事板。' }
  };
  var CARDS = [
    ['cover', '封面 / 本轮论点'], ['editor-note', '本轮核心判断'], ['executive-summary', '结论摘要'], ['signal-landscape', '主题景观'],
    ['evidence-pulse', '证据脉冲'], ['two-state-gap', '比较信号'], ['confidence-bubble', '置信度气泡'], ['evidence-donut', '来源构成'],
    ['top-three', 'Top-3 比较'], ['source-ranking', '来源排名'], ['dual-track', '双轨比较'], ['second-tier', '长尾多样性'],
    ['focal-signal', '焦点信号'], ['flow-map', '事件到业务路径'], ['pareto', '集中度 Pareto'], ['evidence-hub', '证据关系 Hub'],
    ['uncertainty', '不确定性与反证'], ['adoption-cost-proxy', '采用 / 成本代理'], ['risk-quadrant', '四象限风险'], ['closing', '结论与继续监测']
  ];
  var state = { doc: null, current: 0, documentUrl: '', focus: false, cards: CARDS, hasAnchors: false };
  var $ = function (id) { return document.getElementById(id); };
  var safeChannel = function (value) { return CHANNELS[value] ? value : 'ai_news_60s'; };
  var text = function (value, fallback) { return String(value == null || value === '' ? (fallback || '—') : value); };
  var request = function (path) { return window.api.request(path); };
  var params = new URLSearchParams(window.location.search);
  var channel = safeChannel(params.get('channel'));

  function number(value, fallback) {
    var parsed = Number(value);
    return Number.isFinite(parsed) ? String(parsed) : text(value, fallback);
  }
  function detail(value) {
    if (Array.isArray(value)) value = value[0];
    if (value && typeof value === 'object') return text(value.text || value.title || value.name || value.label, '');
    return text(value, '');
  }
  function reportAnalysis(doc) { return doc && doc.report && doc.report.analysis ? doc.report.analysis : {}; }
  function documentHtmlUrl(doc) {
    return '/api/v1/information-documents/' + encodeURIComponent(doc.document_id) +
      '/versions/' + encodeURIComponent(String(doc.version)) + '/render';
  }
  function metric(doc, key, fallback) {
    var analysis = reportAnalysis(doc);
    if (analysis[key] != null) return number(analysis[key], fallback);
    if (key === 'source_count') return number((doc.evidence_ids || []).length, fallback);
    return fallback || '—';
  }
  function cardsFor(doc) {
    return doc && doc.render_contract && doc.render_contract.stable_card_anchors
      ? CARDS
      : [['document', '完整报告']];
  }
  function frameUrl(cardId) {
    return state.documentUrl + (state.hasAnchors && cardId ? '#' + cardId : '');
  }
  function titleFor(doc) {
    var report = doc && doc.report || {};
    return detail(report.headline || report.what_happened) || doc.title || '研究报告';
  }
  function setText(id, value) { var el = $(id); if (el) el.textContent = text(value); }

  function renderShell(doc) {
    var meta = CHANNELS[doc.channel] || CHANNELS[channel];
    var analysis = reportAnalysis(doc);
    document.title = titleFor(doc) + ' · StockAgents';
    setText('run-label', (doc.channel || channel) + ' · v' + text(doc.version) + ' · ' + text(doc.run_id, 'run'));
    setText('report-channel', meta.label.toUpperCase());
    setText('report-title', titleFor(doc));
    setText('report-lede', meta.lede);
    setText('report-stamp', 'DATA CUTOFF · ' + text(doc.as_of) + ' · VERSION v' + text(doc.version));
    setText('metric-evidence', metric(doc, 'source_count', (doc.evidence_ids || []).length));
    setText('metric-domains', metric(doc, 'source_diversity', '0'));
    setText('metric-topics', Array.isArray(analysis.topic_clusters) ? analysis.topic_clusters.length : metric(doc, 'topic_count', '—'));
    setText('metric-version', 'v' + text(doc.version));
    setText('orbit-count', state.cards.length);
    setText('orbit-evidence', metric(doc, 'source_count', '0') + ' EVIDENCE');
    setText('rail-label', state.cards.length === 1 ? '报告目录' : state.cards.length + ' 卡目录');
    $('story-rail').setAttribute('aria-label', state.cards.length === 1 ? '完整报告导航' : state.cards.length + ' 张报告卡片导航');
    setText('report-footer', '运行 ' + text(doc.run_id, '—') + ' · 文档版本 v' + text(doc.version) + ' · 数据截止 ' + text(doc.as_of, '—') + ' · 本内容仅供研究与模拟，不构成投资建议。');
  }

  function renderCardRail() {
    $('story-cards').innerHTML = state.cards.map(function (item, index) {
      return '<a class="story-card' + (index === state.current ? ' active' : '') + '" href="' + frameUrl(item[0]) + '" target="report-canvas" data-card-id="' + item[0] + '" aria-label="在报告画布中打开第 ' + (index + 1) + ' 张：' + item[1] + '">' +
        '<span class="story-index">' + String(index + 1).padStart(2, '0') + '</span><b>' + item[1] + '</b><i class="story-state neutral" aria-hidden="true"></i></a>';
    }).join('');
    $('story-cards').querySelectorAll('[data-card-id]').forEach(function (node) {
      node.addEventListener('click', function () { setCurrent(state.cards.findIndex(function (item) { return item[0] === node.dataset.cardId; })); });
    });
  }
  function setCurrent(index) {
    state.current = Math.max(0, Math.min(state.cards.length - 1, index));
    var id = state.cards[state.current][0];
    $('story-cards').querySelectorAll('.story-card').forEach(function (node, at) { node.classList.toggle('active', at === state.current); });
    setText('card-counter', String(state.current + 1).padStart(2, '0') + ' / ' + state.cards.length);
    $('reading-progress').style.width = Math.round((state.current + 1) / state.cards.length * 100) + '%';
    window.history.replaceState({}, '', window.location.pathname + window.location.search.replace(/#.*$/, '') + '#' + id);
  }
  function gotoCard(id) {
    var index = state.cards.findIndex(function (item) { return item[0] === id; });
    if (index < 0) return;
    setCurrent(index);
    $('report-frame').src = frameUrl(id);
  }
  function wireFrame() {
    setText('screen-status', state.cards.length + ' CARD ' + (state.hasAnchors ? 'DECK' : 'DOCUMENT') + ' · ' + text(state.doc.version, '—') + ' 已装载');
  }
  function installInteractions() {
    $('report-frame').addEventListener('load', wireFrame);
    $('btn-prev').addEventListener('click', function () { gotoCard(state.cards[state.current - 1] ? state.cards[state.current - 1][0] : state.cards[0][0]); });
    $('btn-next').addEventListener('click', function () { gotoCard(state.cards[state.current + 1] ? state.cards[state.current + 1][0] : state.cards[state.cards.length - 1][0]); });
    $('btn-focus').addEventListener('click', function () {
      state.focus = !state.focus; $('reader').classList.toggle('focus', state.focus); $('btn-focus').setAttribute('aria-pressed', String(state.focus)); $('btn-focus').textContent = state.focus ? '退出焦点' : '焦点阅读';
    });
    $('btn-fullscreen').addEventListener('click', function () {
      var screen = $('screen');
      if (document.fullscreenElement) document.exitFullscreen(); else if (screen.requestFullscreen) screen.requestFullscreen();
    });
    $('btn-print').addEventListener('click', function () { window.print(); });
    $('btn-back').addEventListener('click', function () { window.location.href = '/data-intelligence.html'; });
    $('btn-error-back').addEventListener('click', function () { window.location.href = '/data-intelligence.html'; });
    window.addEventListener('keydown', function (event) {
      if (event.target && /input|textarea|select/i.test(event.target.tagName)) return;
      if (event.key === 'ArrowLeft') { event.preventDefault(); $('btn-prev').click(); }
      if (event.key === 'ArrowRight' || event.key === ' ') { event.preventDefault(); $('btn-next').click(); }
      if (event.key.toLowerCase() === 'f') $('btn-focus').click();
    });
  }
  async function getDocument() {
    var documentId = params.get('document_id'), version = params.get('version');
    if (documentId || version) {
      if (!/^[A-Za-z0-9_-]{1,180}$/.test(documentId || '') || !/^[1-9][0-9]*$/.test(version || '')) {
        throw new Error('报告链接无效。请从工作台的报告列表重新打开。');
      }
      return request('/api/v1/information-documents/' + encodeURIComponent(documentId) + '/versions/' + encodeURIComponent(version) + '?include_html=false');
    }
    return request('/api/v1/information-documents/latest/' + encodeURIComponent(channel) + '?include_html=false');
  }
  async function init() {
    installInteractions();
    try {
      state.doc = await getDocument();
      if (!state.doc || !state.doc.document_id) throw new Error('报告版本不可用');
      state.documentUrl = documentHtmlUrl(state.doc);
      state.cards = cardsFor(state.doc);
      state.hasAnchors = state.cards.length > 1;
      var requestedCard = window.location.hash.slice(1);
      state.current = Math.max(0, state.cards.findIndex(function (item) { return item[0] === requestedCard; }));
      renderShell(state.doc);
      renderCardRail();
      setText('stage-guide', state.hasAnchors
        ? 'LIVE REPORT CANVAS · 点击左侧分镜跳转，方向键可前后阅读'
        : 'IMMUTABLE DOCUMENT CANVAS · 这是早期版本，向内滚动阅读完整报告');
      setCurrent(state.current);
      $('report-frame').src = frameUrl(state.cards[state.current][0]);
      $('loading-state').hidden = true; $('report-shell').hidden = false;
    } catch (error) {
      $('loading-state').hidden = true; $('error-state').hidden = false;
      setText('error-copy', (error && error.message) || '请返回工作台生成一份报告，或从历史文档再次打开。');
    }
  }
  init();
}());
