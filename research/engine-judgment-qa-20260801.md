# Engine multi-dim judgment QA — 2026-08-01

## Contract
- `judgment_dimensions[]` keys: quant, analyst, consensus, valuation, growth, profitability, momentum, risk, eps_revision, liquidity, event_impact
- `overall_judgment`: score, label, confidence, coverage, bull/bear
- Fixture path is deterministic from ticker+as_of; valuation rationale marked as simulation

## UI
- Panel `#judgment-dimensions-panel` under Live Journey
- Tabs: 评级摘要 / 基本面 / 预期与修正 / 市场行为 / 风险与事件
- Disclaimer: 研究/模拟，非投资建议

## Tests
- `engine-judgment.test.js`
- Existing cockpit tests remain green when judgment script is optional
