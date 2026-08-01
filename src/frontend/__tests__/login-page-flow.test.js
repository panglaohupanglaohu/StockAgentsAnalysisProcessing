import { readFileSync } from 'node:fs';
import path from 'node:path';
import { describe, expect, it } from 'vitest';

function read(relPath) {
  return readFileSync(path.join(process.cwd(), relPath), 'utf8');
}

function buildGetNextUrl(search) {
  const source = read('src/frontend/login.html');
  const match = source.match(/function getNextUrl\(\) \{[\s\S]*?return next;\n\s*\}/);
  if (!match) throw new Error('getNextUrl not found in login.html');
  // Hoist DEFAULT_AFTER_LOGIN + isSafeLocalPath when present (T002).
  const helpers = [];
  const defaultMatch = source.match(/var DEFAULT_AFTER_LOGIN = ['"][^'"]+['"];/);
  if (defaultMatch) helpers.push(defaultMatch[0]);
  const safeMatch = source.match(/function isSafeLocalPath\(path\) \{[\s\S]*?\n\s*\}/);
  if (safeMatch) helpers.push(safeMatch[0]);
  const windowObj = { location: { search } };
  return new Function(
    'window',
    'URLSearchParams',
    `${helpers.join('\n')}\n${match[0]}; return getNextUrl;`,
  )(windowObj, URLSearchParams);
}

describe('login.html auth flow guards', () => {
  it('allows root-relative next targets and rejects external redirects', () => {
    expect(buildGetNextUrl('?next=/system-evolution.html?panel=items')()).toBe('/system-evolution.html?panel=items');
    expect(buildGetNextUrl('?next=//evil.example/login')()).toBe('/agent-team-config.html');
    expect(buildGetNextUrl('?next=https://evil.example/login')()).toBe('/agent-team-config.html');
    expect(buildGetNextUrl('?next=//host')()).toBe('/agent-team-config.html');
    expect(buildGetNextUrl('')()).toBe('/agent-team-config.html');
  });

  it('defaults login/register/guest/authenticated redirect to Agent Config', () => {
    const source = read('src/frontend/login.html');
    expect(source).toContain("var DEFAULT_AFTER_LOGIN = '/agent-team-config.html'");
    expect(source).toContain('window.location.href = getNextUrl();');
    // login success, register success, guest, authenticated /auth/me
    const redirects = source.match(/window\.location\.href = getNextUrl\(\);/g) || [];
    expect(redirects.length).toBeGreaterThanOrEqual(3);
  });

  it('primes csrf token on both login and register success paths', () => {
    const source = read('src/frontend/login.html');
    const matches = source.match(/window\.api\.setCsrfToken\(data\.csrf_token\);/g) || [];
    expect(matches).toHaveLength(2);
  });

  it('keeps guest login and auth bootstrap on the same sanitized redirect path', () => {
    const source = read('src/frontend/login.html');
    expect(source).toContain("window.guestLogin = function () {");
    expect(source).toContain("localStorage.setItem('ag-user', 'guest');");
    expect(source).toContain("window.location.href = getNextUrl();");
    expect(source).toContain("window.api.request('/api/v1/auth/me').then(function (data) {");
    expect(source).toContain("localStorage.setItem('ag-user', data.username);");
  });

  it('uses StockAgents product keywords only (T002)', () => {
    const source = read('src/frontend/login.html');
    expect(source).toContain('<title>StockAgents — 登录</title>');
    expect(source).toContain('class="seal">投</span>');
    expect(source).toContain('<h1>StockAgents</h1>');
    expect(source).toContain('AI 信息采集与股票投资模拟平台');
    expect(source).toContain('Agentic Market Intelligence Platform');
    expect(source).not.toContain('AgentsGroup2026 — 登录');
    expect(source).not.toContain('class="seal">智</span>');
    expect(source).not.toContain('Standalone Agent Platform');
  });
});
