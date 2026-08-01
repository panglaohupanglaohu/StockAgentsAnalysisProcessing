import { readFileSync } from 'node:fs';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

/**
 * Contract smoke for hugohe3 research deck (P14).
 * Source is Python-rendered; we assert the generator embeds result-first structure.
 */
const hugo = readFileSync(
  path.join(process.cwd(), 'src/backend/domain/information_sources/hugohe3.py'),
  'utf8',
);

describe('Report output content (P14)', () => {
  it('binds twenty stable card ids', () => {
    const ids = [
      'cover',
      'editor-note',
      'executive-summary',
      'signal-landscape',
      'evidence-pulse',
      'two-state-gap',
      'confidence-bubble',
      'evidence-donut',
      'top-three',
      'source-ranking',
      'dual-track',
      'second-tier',
      'focal-signal',
      'flow-map',
      'pareto',
      'evidence-hub',
      'uncertainty',
      'adoption-cost-proxy',
      'risk-quadrant',
      'closing',
    ];
    ids.forEach((id) => {
      expect(hugo).toContain(`"${id}"`);
    });
  });

  it('puts executive finding before method docs', () => {
    expect(hugo).toContain('EXECUTIVE FINDING');
    expect(hugo).toContain('编辑结论');
    expect(hugo).toContain('deck-method');
    expect(hugo).toContain('as_of');
    expect(hugo).toMatch(/非投资建议/);
  });

  it('summary card contains conclusions rather than a duplicate menu', () => {
    expect(hugo).toContain('executive-summary');
    expect(hugo).toContain('结论摘要 · 先看发生了什么');
    expect(hugo).not.toContain('目录 · 真实摘要与状态');
  });

  it('numeric cards read analysis fields not hard-coded demo markets', () => {
    expect(hugo).toContain('source_breakdown');
    expect(hugo).toContain('topic_clusters');
    expect(hugo).toContain('top_signals');
    expect(hugo).toContain('coverage_gaps');
    expect(hugo).not.toContain('硬编码营收');
  });
});
