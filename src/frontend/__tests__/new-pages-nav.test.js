import { readFileSync } from 'node:fs';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

function read(rel) {
  return readFileSync(path.join(process.cwd(), rel), 'utf8');
}

describe('new pages and nav isolation (T505)', () => {
  it('nav.js appends exactly two new page ids without removing legacy seven', () => {
    const nav = read('src/frontend/js/nav.js');
    const legacy = [
      'agent-team-config.html',
      'plaza.html',
      'skill-extract.html',
      'agent-memory.html',
      'Agent-digital-twin.html',
      'cost-dashboard.html',
      'pet-config.html',
    ];
    for (const href of legacy) {
      expect(nav).toContain(href);
    }
    expect(nav).toContain('data-intelligence.html');
    expect(nav).toContain('investment-engine.html');
    expect(nav).toContain("id: 'data-intelligence'");
    expect(nav).toContain("id: 'investment-engine'");
  });

  it('data-intelligence.html keeps focused teams primary and utility views in the right rail', () => {
    const html = read('src/frontend/data-intelligence.html');
    expect(html).toContain('data-tab="add-source"');
    expect(html).toContain('data-tab="health"');
    expect(html).toContain('data-tab="ai60"');
    expect(html).toContain('data-tab="world"');
    expect(html).toContain('data-tab="docs"');
    expect(html).toContain('class="inspector"');
    expect(html).toContain('aria-label="收集流程导航"');
    expect(html).not.toContain('data-tab="queue"');
    expect(html).not.toContain('data-tab="sources"');
    expect(html).not.toContain('href="/sources.html"');
    expect(html).not.toContain('href="/ai-brief.html"');
  });

  it('promotes AI60 and world trend to independent focused workspace tabs', () => {
    const html = read('src/frontend/data-intelligence.html');
    expect(html).toContain('class="workbench-primary-nav"');
    expect(html).toContain('aria-label="独立团队工作区"');
    expect(html).toContain('class="tab primary active"');
    expect(read('src/frontend/js/data-intelligence.js')).toContain('switchTab(\'ai60\');');
  });

  it('data-intelligence.html exposes an add-source form backed by the source API', () => {
    const html = read('src/frontend/data-intelligence.html');
    for (const id of ['panel-add-source', 'source-form', 'source-name', 'source-kind', 'source-url', 'source-profile', 'source-options', 'source-fixture-items', 'btn-submit-source', 'preview-ai60', 'preview-dufu']) {
      expect(html).toContain(`id="${id}"`);
    }
    const controller = read('src/frontend/js/data-intelligence.js');
    expect(controller).toContain('createSource');
    expect(controller).toContain('syncSourcePreview');
    expect(controller).toContain("/api/v1/information-sources");
  });

  it('source library keeps its column width and supports select all', () => {
    const html = read('src/frontend/data-intelligence.html');
    expect(html).toContain('id="sources-body"');
    expect(html).toContain('id="btn-select-all-sources"');
    expect(html).toContain('id="btn-save-source-selection"');
    expect(html).toContain('id="source-selection-status"');
    expect(html).toContain('class="head-actions"');
    const controller = read('src/frontend/js/data-intelligence.js');
    expect(controller).toContain('function toggleAllSources()');
    expect(controller).toContain('function sourceTreeHtml(sources)');
    expect(controller).toContain('function saveSourceSelection()');
    expect(controller).toContain('source-group-check');
    expect(controller).toContain('method: \'PATCH\'');
    expect(controller).toContain('updateSourceSelectionButton');
  });

  it('uses a 30-minute default cadence for newly created information schedules', () => {
    const html = read('src/frontend/data-intelligence.html');
    expect(html).toContain('id="schedule-interval" type="number" value="30"');
  });

  it('latest report action opens an immutable report snapshot in a new reading page', () => {
    const controller = read('src/frontend/js/data-intelligence.js');
    expect(controller).toContain('function openReport(channel, doc)');
    expect(controller).toContain('report-viewer.html?channel=');
    expect(controller).toContain('document_id=');
    expect(controller).toContain('encodeURIComponent(doc.document_id)');
    expect(controller).toContain('target="_blank"');
    expect(controller).toContain('rel="noopener noreferrer"');
    expect(controller).toContain('查看完整动态 HTML');
  });

  it('ships a safe immersive report reader with version addressing and reduced-motion support', () => {
    const html = read('src/frontend/report-viewer.html');
    const reader = read('src/frontend/js/report-viewer.js');
    expect(html).toContain('id="report-frame"');
    expect(html).toContain('sandbox="allow-popups allow-popups-to-escape-sandbox"');
    expect(html).not.toContain('allow-same-origin');
    expect(html).not.toContain('allow-scripts');
    expect(html).toContain('referrerpolicy="no-referrer"');
    expect(html).toContain('role="alert"');
    expect(html).toContain('prefers-reduced-motion');
    expect(reader).toContain('URLSearchParams');
    expect(reader).toContain('/versions/');
    expect(reader).toContain('/render');
    expect(reader).toContain('document_id');
    expect(reader).toContain('report-canvas');
    expect(reader).toContain('include_html=false');
    expect(reader).toContain('stable_card_anchors');
  });

  it('data intelligence includes chat-driven RSS directory import', () => {
    const html = read('src/frontend/data-intelligence.html');
    for (const id of ['directory-chat', 'directory-chat-form', 'directory-chat-input', 'directory-preview', 'btn-directory-commit']) {
      expect(html).toContain(`id="${id}"`);
    }
    const controller = read('src/frontend/js/data-intelligence.js');
    expect(controller).toContain('parseDirectoryChat');
    expect(controller).toContain('/api/v1/information-sources/import-directory/preview');
    expect(controller).toContain('/api/v1/information-sources/import-directory/commit');
  });

  it('research tabs expose both agent rows and progressive delivery boxes', () => {
    const html = read('src/frontend/data-intelligence.html');
    for (const id of ['ai60-agent-row', 'ai60-box-grid', 'dufu-agent-row', 'dufu-slide-grid', 'btn-start-ai60', 'btn-start-dufu']) {
      expect(html).toContain(`id="${id}"`);
    }
    const controller = read('src/frontend/js/data-intelligence.js');
    expect(controller).toContain('loadTeamAgents');
    expect(controller).toContain('animateTeamProgress');
    expect(controller).toContain('主题与信号');
    expect(controller).toContain('动态研判驾驶舱');
    expect(controller).toContain('running / collecting');
  });

  it('keeps delivery boxes bounded and strips raw feed markup in summaries', () => {
    const html = read('src/frontend/data-intelligence.html');
    expect(html).toContain('height:150px');
    expect(html).toContain('-webkit-line-clamp:4');
    const controller = read('src/frontend/js/data-intelligence.js');
    expect(controller).toContain('function plainSummary');
    expect(controller).toContain('replace(/<[^>]*>/g');
  });

  it('investment-engine.html supports create/start/cancel and drag-drop zone', () => {
    const html = read('src/frontend/investment-engine.html');
    expect(html).toContain('id="sector"');
    expect(html).toContain('id="ticker"');
    expect(html).toContain('id="ticker-presets"');
    expect(html).toContain('id="btn-create"');
    expect(html).toContain('id="btn-start"');
    expect(html).toContain('id="btn-cancel"');
    expect(html).toContain('id="source-drop"');
    expect(html).toContain('id="timeline"');
    expect(html).toContain('id="portfolio"');
    expect(html).toContain('不构成投资建议');
  });

  it('investment engine exposes a horizontal assembly spine and draggable team parts', () => {
    const html = read('src/frontend/investment-engine.html');
    expect(html).toContain('id="source-drop"');
    expect(html).toContain('id="module-library"');
    expect(html).toContain('id="assembly-count"');
    expect(html).toContain('data-id="team:ai_news_60s"');
    expect(html).toContain('data-id="team:dufu_world_intel"');
    const controller = read('src/frontend/js/investment-engine.js');
    expect(controller).toContain("text/kind");
    expect(controller).toContain("assembly-count");
  });

  it('investment engine exposes a dynamic HTML journey cockpit', () => {
    const html = read('src/frontend/investment-engine.html');
    for (const id of ['dynamic-dashboard', 'engine-hud', 'engine-progress-bar', 'engine-route', 'judgment-card', 'plan-card', 'revenue-card', 'risk-card', 'portfolio-card', 'context-card']) {
      expect(html).toContain(`id="${id}"`);
    }
    const controller = read('src/frontend/js/investment-engine.js');
    // P8: single-state render path (replaces legacy renderJourney name)
    expect(controller).toContain('renderFromState');
    expect(controller).toContain('phaseLabels');
    expect(controller).toContain('btn-engine-start');
  });
});
