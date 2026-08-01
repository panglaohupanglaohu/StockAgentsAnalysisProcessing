# Engine overflow QA — 2026-08-01

## Changes
- Page-level `overflow-x: clip` + `min-width:0` on grid children
- Parts bank internal horizontal scroll + overflow hint
- Road shell keeps ingress/research/portfolio cores fixed; modules scroll in `#road-modules-scroll`

## Viewports (manual)
| Viewport | Expected |
|----------|----------|
| 1280×800 | No page H-scroll; parts rail may show hint |
| 1024×768 | Same |
| 768×1024 | Single column grid; road cores wrap if needed |
| 390×844 | Sidebar drawer; insight single column; matrix cards stack |

## Regression
- Drag IDs preserved: `source-drop`, `source-selected`, `module-library`
- Engine start/cancel IDs unchanged
- Tests: `engine-overflow.test.js`

## Rollback
Revert CSS blocks tagged P11 in `investment-engine.html` and road structure to prior single `road-track` flex row.
