# 系统架构

## 设计原则

1. 保护现有系统：登录、Agent Config、Build System、AI Coding 和 Plaza 是基线能力。
2. 渐进适配：新领域模块不要求一次性搬迁旧代码。
3. 证据优先：信息内容和投资判断必须能回到来源与决策时点。
4. 可降级：TradingAgents 或单一来源失败时，原系统和其他团队继续运行。
5. 仅做模拟：不内置真实券商下单通道。

## 逻辑组件

```mermaid
flowchart TB
    UI["静态 Web UI"] --> API["FastAPI API"]
    API --> CFG["Agent Config / Team Manager"]
    API --> PLAZA["Plaza"]
    CFG --> CORE["现有 Agent Runtime"]
    CORE --> T1["ai_news_60s"]
    CORE --> T2["dufu_world_intel"]
    SOURCES["Source Connector Registry"] --> NORMAL["标准化 / 去重 / 证据存储"]
    NORMAL --> T1
    NORMAL --> T2
    T1 --> REPORTS["Report Schema / HTML Publisher"]
    T2 --> REPORTS
    REPORTS --> PACKET["Time-bounded Information Packet"]
    PACKET --> ADAPTER["TradingAgents Adapter"]
    ADAPTER --> SIM["模拟组合 / 决策 / Checkpoint"]
    SIM --> PLAZA
    SIM --> UI
```

## 分层职责

- `agents/`：现有团队、工具、技能、记忆、调度和 Plaza 行为。
- `domain/information_sources/`：来源定义、抓取批次、证据、游标和发布报告等领域契约。
- `domain/investment_simulation/`：模拟运行、信息快照、订单意图、组合状态和结果。
- `integrations/tradingagents/`：第三方图状态与 StockAgents 领域对象之间的转换。
- `frontend/js/features/`：新页面按功能收拢，旧页面继续运行并逐步接入。

## 关键数据契约

```text
SourceConfig
  → FetchBatch(raw items, cursor, observed_at)
  → EvidenceRecord(source, url, hash, fetched_at)
  → InformationPacket(as_of, claims, evidence, confidence)
  → SimulationRun(run_id, symbol, as_of, config_snapshot)
  → DecisionRecord(action, rationale, debates, risk, provenance)
```

`as_of` 是硬边界：connector、报告团队和投资 runtime 均不得读取该时刻之后才可见的信息。

## 降级矩阵

| 故障 | 行为 |
| --- | --- |
| 单一信息源失败 | 标记来源失败，其他来源继续 |
| 某支新团队失败 | 保存运行记录，另一团队和原团队继续 |
| HTML 发布失败 | 保留结构化报告，可重试发布 |
| TradingAgents 缺失/启动失败 | Agent Config、原团队、信息站点、Plaza 继续可用 |
| 专用模拟页面不可用 | Plaza 作为完整的模拟过程展示入口 |
