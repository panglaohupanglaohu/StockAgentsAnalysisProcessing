# Report output content QA — 2026-08-01 (P14)

## Mapping
| card_id | primary sources | empty/gap |
|---------|-----------------|-----------|
| cover | headline / what_happened | gap title |
| editor-note | bullets + why + KPI (count/score/as_of) | gap if no evidence |
| contents | TOC status + implications | gap |
| signal-landscape…closing | analysis.* / citations | `_deck_gap` |

## Checks
- Executive finding shows headline, confidence band, evidence count, as_of
- Method text is in collapsed `<details>`
- 20 card ids stable; no fabricated revenue series without timeline

## Tests
- `report-output-content.test.js`
- pipeline fixture tests already assert research-deck presence
