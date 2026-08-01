# Engine Sidebar Patterns — Research Input

- **Date:** 2026-08-01
- **Author role:** research synthesis (Grok standing in for T1001 Codex deliverable)
- **Scope:** Information architecture and accessible interaction for a research-terminal style left rail on `/investment-engine.html`
- **Non-goals:** Copy Seeking Alpha / Bloomberg brand assets, logos, or proprietary chrome

## Public references (patterns only)

| # | Source | URL | Accessed | What we extract |
|---|--------|-----|----------|-----------------|
| 1 | MDN: Navigation landmarks | https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/navigation_role | 2026-08-01 | `<nav aria-label>`, current page via `aria-current` |
| 2 | WAI-ARIA Authoring Practices: Disclosure / Tree | https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ | 2026-08-01 | Collapsed groups, `aria-expanded`, keyboard |
| 3 | GOV.UK side navigation | https://design-system.service.gov.uk/components/side-navigation/ | 2026-08-01 | Active item indicator, grouping, mobile drawer |
| 4 | GitHub Docs / product rails (generic) | https://docs.github.com | 2026-08-01 | Dark rail + content contrast; collapse to icons |
| 5 | TradingView / research terminals (generic IA) | public product UX observation | 2026-08-01 | Dense left groups: overview / analysis / news / portfolio |

## Design decisions for StockAgents Engine

1. **Internal rail only** — does not replace global nav; lives inside investment-engine page.
2. **Dark rail + light/deep cockpit** — sidebar `#0b1220` / accent `#f97316` (orange current bar); does not restyle existing Live Journey HUD beyond shared focus rings.
3. **Items map to existing anchors** — no second config form; “分析” expands/focuses the same `#sector`…`#btn-cancel` controls.
4. **Badges are soft** — counts from information-sources / documents / runs; failure shows `—`, never blocks Engine start.
5. **Persistence** — `localStorage` key `sa_engine_sidebar_v1` stores only UI: `{ collapsed, expandedMore, active, drawerOpen }`.
6. **Mobile** — ≤960px: hamburger + drawer + dim overlay; ESC and overlay click close.

## Anti-patterns (do not ship)

- Hard-coding Seeking Alpha / “Authors” brand copy as product identity
- Loading remote icon fonts or third-party CSS
- Saving API keys, report HTML, or simulation snapshots in sidebar storage
- Removing or renaming existing control IDs used by tests
- Making sidebar required for fixture create/start/cancel

## Recommended item map

| id | Label (zh) | Target anchor | Badge |
|----|------------|---------------|-------|
| overview | 首页 | `#engine-overview` | — |
| analysis | 分析 | `#engine-config` | — |
| news | 信息流 | `#engine-context` | AI docs count |
| performance | 市场表现 | `#engine-dashboard` | — |
| authors | 我的 Agent | `#engine-assembly` | team modules selected |
| research | 研究组 | `#engine-assembly` | selected sources |
| more | 显示更多 | expands secondary | — |
| portfolio | 纸面组合 | `#engine-portfolio` | runs (optional) |

## Accessibility checklist

- [x] `nav[aria-label="投资引擎研究导航"]`
- [x] Buttons, not bare divs
- [x] `aria-current="page"` on active item
- [x] `aria-expanded` on collapse / show-more / drawer
- [x] Visible `:focus-visible` ring
- [x] `prefers-reduced-motion: reduce` disables transform animations
