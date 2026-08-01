# ADR 0001：使用 TradingAgents v0.3.1 作为 AI 投资运行时

- 状态：Accepted for implementation
- 日期：2026-07-31

## 背景

项目需要 AI 原生、多角色协作的投资研究和模拟流程。需求明确不以传统量化回测框架作为主引擎，同时必须完整保留现有 7 个业务页面。

## 决策

采用 TauricResearch/TradingAgents `v0.3.1`（commit `01477f9`）作为唯一主运行时，并通过 `src/backend/integrations/tradingagents` 隔离。默认安装不包含该可选依赖。

## 原因

- 原生表达多类分析师、多空辩论、风险辩论与组合经理裁决。
- 基于图的 Agent 流程适合向独立投资引擎页面投射可观察事件。
- v0.3.1 明确修复前视数据泄漏与 checkpoint identity 等问题。
- Apache-2.0 适合通过依赖方式集成，但仍需在发布前完成许可证审计。

## 后果

- 必须维护稳定的 StockAgents 输入/输出契约，避免上游 state 渗透。
- 必须固定上游 commit，并为升级建立回放和时序测试。
- 上游不是高可用核心依赖；不可用时原应用继续工作。
- 本决策不等于接入真实交易，也不免除项目自身的数据泄漏测试责任。
