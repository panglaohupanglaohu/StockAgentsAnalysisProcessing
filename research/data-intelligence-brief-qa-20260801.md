# Data Intelligence brief QA — 2026-08-01

## Backend
- `build_run_brief()` in `domain/information_sources/brief.py`
- Attached as `executive_summary` on document payloads
- `GET /api/v1/information-documents/latest-summary`

## Frontend
- Home strip: In Focus + 核心结论 / 热门分析 / 趋势新闻 / 独到见解
- `loadBriefs()` + client-side `insightItems` / `renderExecutiveBrief` dual path
- Process chatter filtered; single-source limits called out

## Tests
- `test_run_brief.py`
- `data-intelligence-brief.test.js`
