# StockAgents 重构规划（修订版）

> 修订日期：2026-07-31  
> 状态：可以进入开发  
> 原则：保留原系统的登录、Agent Config、Build System、AI Coding、Plaza 与 Agent 基础设施，在其上增加两支信息团队，并接入最新 AI 原生金融多 Agent 框架。

## 1. 修订后的明确结论

本次重构不再删除 `build_system` 和 `ai_coding`，也不重做登录交互和 Plaza。

系统主流程确定为：

```text
打开系统
  → 原登录页（只替换产品关键词）
  → 登录成功进入 Agent Config
  → 用户配置模型、API Key、Skills、Tools 和团队
  → 运行两支信息采集团队
  → 信息文档发布到信息源站点
  → TradingAgents 驱动投资分析与模拟决策
  → 专用模拟页展示结果；Plaza 同步展示 Agent 自主行动全过程
```

Plaza 是必须保留的核心能力，不是准备删除的旧页面。即使专用模拟画布第一版效果不理想，用户仍然可以在 Plaza 中看到一次完整的 Agent 自主投资模拟：分析师出发采集、回场汇报、多空辩论、风险辩论、组合经理裁决、模拟成交和事后反思。

## 2. 登录页与首个页面

### 2.1 登录页

保留现有 `src/frontend/login.html` 的：

- HTML 结构与浅色视觉样式；
- 登录、注册、访客模式；
- Cookie、CSRF、Token 和错误处理；
- `next` 参数的安全跳转逻辑；
- 所有现有 API 调用。

只更换以下产品关键词：

| 当前文案 | 新文案 |
| --- | --- |
| `AgentsGroup2026 — 登录` | `StockAgents — 登录` |
| 印章 `智` | 印章 `投` |
| `AgentsGroup2026` | `StockAgents` |
| `智能体团队管理平台` | `AI 信息采集与股票投资模拟平台` |
| `Standalone Agent Platform` | `Agentic Market Intelligence Platform` |

不在这个任务中重新设计布局、表单或认证体系。

### 2.2 登录后默认进入 Agent Config

现有代码已经默认跳转 `/agent-team-config.html`，本次只做回归保护：

- 登录、注册、访客模式都默认进入 Agent Config；
- 合法 `next=/...` 仍可覆盖默认页面；
- 已登录用户访问 `/login.html` 时直接进入 Agent Config；
- `/` 继续跳转登录页；
- 新增自动化测试锁定上述行为。

Agent Config 是系统控制台。用户必须先在这里选择/配置：

- Quick Think 模型；
- Deep Think 模型；
- 模型提供商与 API 地址；
- API Key 的环境变量引用；
- Agent 的 Skills、Tools、预算和权限；
- 两支信息团队的来源与运行频率；
- TradingAgents 的分析师组合、辩论轮数和风险轮数。

## 3. 团队加载策略

### 3.1 所有原团队继续保留

现有团队初始化逻辑和持久化优先规则保持不变，包括：

- `build_system`；
- `ai_coding`；
- `energy_first_principle`；
- `d083a568`（公有云 xOPs）；
- `cloud-ops-team`；
- `aws-ops`；
- `pet_squad`；
- 用户在 `storage/teams/teams.json` 创建的团队。

`build_system` 与 `ai_coding` 是启动验收的强制项，不能因为 TradingAgents、某个数据源或新团队加载失败而消失。

### 3.2 新增两支团队

新增 factory：

```text
src/backend/agents/teams/ai_news_60s_team.py
src/backend/agents/teams/dufu_world_intel_team.py
```

启动时遵循现有规则：磁盘已有团队则使用持久化版本；磁盘没有才用 factory 首次播种，避免重启覆盖用户修改。

### 3.3 启动健康检查

新增核心团队断言：

```python
CORE_TEAM_IDS = {
    "build_system",
    "ai_coding",
    "ai_news_60s",
    "dufu_world_intel",
}

missing = CORE_TEAM_IDS - set(team_manager.team_ids())
if missing:
    report_startup_error(missing)
```

新框架作为可选运行时依赖。即使它暂时不可用，Agent Config、Build System、AI Coding、信息团队配置和 Plaza 仍然能正常打开。

## 4. 新增团队设计

### 4.1 60 秒 AI 信息播报团队 `ai_news_60s`

该团队参考“60 秒播报”的节奏与信息密度，不复制具体账号的声音、形象、口头禅或原文。

| Agent | 核心职责 | Tools | Skills |
| --- | --- | --- | --- |
| `ai60_lead` | 选题、拆解任务、控制时间预算、发布门禁 | `delegate_task`, `schedule_task`, `memory_read`, `publish_event` | `editorial_planning`, `news_ranking`, `quality_gate` |
| `ai60_scout` | 搜索官方发布、论文、开源项目、产品和政策 | `web_search`, `navigate_url`, `web_extract`, `memory_save` | `ai_source_discovery`, `ai_taxonomy`, `source_reputation` |
| `ai60_checker` | 去重、交叉验证、日期/实体/数字核验 | `web_search`, `web_extract`, `run_python`, `memory_read` | `fact_checking`, `deduplication`, `citation_audit` |
| `ai60_market_mapper` | 映射公司、产业链、赛道、机会和风险 | `run_python`, `memory_read`, `read_file` | `entity_resolution`, `market_impact_mapping`, `scenario_analysis` |
| `ai60_editor` | 生成 60 秒版与可展开长版 | `read_file`, `memory_read` | `sixty_second_brief`, `plain_language_editing`, `uncertainty_labeling` |
| `ai60_publisher` | 输出动态 HTML 并发布 | `read_file`, `write_file`, `publish_event` | `hugohe3`, `accessible_html`, `data_visualization` |

固定产物：

```text
一句话总览
→ 5 条 AI 快讯
→ 为什么重要
→ 相关公司/赛道（明确非投资建议）
→ 风险与反证
→ 原始来源、数据截止时间、运行 ID
```

### 4.2 独夫之心团队 `dufu_world_intel`

该团队参考宏观议题、历史纵深、因果链和观点表达方式，但必须把事实、分析、推断和情景清楚分开。

| Agent | 核心职责 | Tools | Skills |
| --- | --- | --- | --- |
| `dufu_lead` | 议题拆解、调度、最终结论门禁 | `delegate_task`, `mixture_of_agents`, `schedule_task`, `publish_event` | `intelligence_planning`, `scenario_tree`, `editorial_gate` |
| `dufu_web_collector` | 多语言公开来源和 WebSearch 采集 | `web_search`, `navigate_url`, `web_extract`, `memory_save` | `multilingual_search`, `timeline_building`, `source_reputation` |
| `dufu_data_engineer` | 清洗、去重、实体对齐、时序对齐 | `run_python`, `read_file`, `write_file` | `data_cleaning`, `entity_resolution`, `timeseries_alignment` |
| `dufu_data_analyst` | 统计分析、数据挖掘、趋势与异常识别 | `run_python`, `memory_read`, `memory_save` | `data_analysis`, `data_mining`, `change_point_detection` |
| `dufu_red_team` | 查找反证、偏差和替代解释 | `web_search`, `web_extract`, `mixture_of_agents` | `claim_challenge`, `bias_detection`, `confidence_calibration` |
| `dufu_market_mapper` | 宏观事件到行业、公司和市场的传导路径 | `run_python`, `memory_read` | `macro_to_market`, `transmission_path`, `scenario_analysis` |
| `dufu_presenter` | 使用 `hugohe3` 生成动态数据页面 | `read_file`, `write_file`, `run_javascript`, `publish_event` | `hugohe3`, `interactive_storytelling`, `accessible_html` |

固定产物：

```text
发生了什么
→ 历史时间线
→ 核心驱动因素
→ 数据与趋势强度
→ 主要观点与反证
→ 乐观/基准/悲观情景
→ 对行业和股票的可能传导路径
→ 引用、更新时间和不确定性
```

当前仓库没有 `hugohe3`，因此实现一个仓库内置的同名 Skill 和 renderer adapter。输入为受控 JSON schema，输出为响应式 HTML。若之后提供外部同名 Skill，只替换 adapter，不改变团队配置。

## 5. 最新 AI 投资框架选择

### 5.1 唯一主框架：TradingAgents v0.3.1

不再采用 LEAN、FinRL-X、Qlib 或 VectorBT 作为本项目主引擎。

本项目集成 [TauricResearch/TradingAgents v0.3.1](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.3.1)，固定到已签名 tag `v0.3.1` / commit `01477f9`。它在 2026-07-05 发布，是当前最新正式版本，使用 Apache-2.0 许可证。

选择原因：

- 原生 LangGraph 多 Agent 金融工作流；
- 市场、情绪、新闻、基本面四类分析师；
- 看多/看空研究员结构化辩论；
- Trader Agent；
- 激进/保守/中性风险辩论；
- Portfolio Manager 最终批准或拒绝；
- 持久化决策日志和收益反思；
- SQLite checkpoint 与按图结构恢复；
- 支持 OpenAI、Claude、Gemini、Grok、DeepSeek、Qwen、GLM、MiniMax、Kimi、Groq、Mistral、NVIDIA NIM、Bedrock、Ollama 和 OpenAI-compatible 本地服务；
- v0.3.x 提供可验证的数据访问契约、FRED、Polymarket、无界面报告输出和未来数据过滤。

官方资料：

- [项目与架构](https://github.com/TauricResearch/TradingAgents)
- [v0.3.1 Release](https://github.com/TauricResearch/TradingAgents/releases/tag/v0.3.1)
- [Changelog](https://github.com/TauricResearch/TradingAgents/blob/main/CHANGELOG.md)
- [Apache-2.0 License](https://github.com/TauricResearch/TradingAgents/blob/main/LICENSE)

### 5.2 集成方式

TradingAgents 不替换现有 AgentsGroup 内核。两者职责如下：

| 层 | 负责内容 |
| --- | --- |
| 现有 StockAgents | 登录、Agent Config、团队、Skills、Tools、任务、预算、记忆、证据、Plaza、页面与 API |
| TradingAgents | 股票研究 Agent 图、多空辩论、风险辩论、Trader、Portfolio Manager 和决策反思 |
| Adapter | 模型映射、信息上下文注入、事件转换、报告保存、Plaza 同步和错误隔离 |

新增适配层：

```text
src/backend/integrations/tradingagents/
  config_mapper.py
  graph_adapter.py
  context_provider.py
  event_bridge.py
  report_adapter.py
  health.py
```

不直接修改第三方源码。版本升级只在 adapter 边界处理。

### 5.3 Agent Config 到 TradingAgents 的模型映射

```python
def map_agent_config(team_config, model_pool):
    return {
        "llm_provider": normalize_provider(team_config.provider),
        "deep_think_llm": model_pool[team_config.deep_model_id].name,
        "quick_think_llm": model_pool[team_config.quick_model_id].name,
        "backend_url": model_pool[team_config.deep_model_id].api_base_url,
        "output_language": "zh-CN",
        "max_debate_rounds": team_config.debate_rounds,
        "max_risk_discuss_rounds": team_config.risk_rounds,
        "checkpoint_enabled": True,
        "data_cache_dir": project_storage / "tradingagents/cache",
        "results_dir": project_storage / "tradingagents/results",
    }
```

API Key 只在服务端通过现有 SecretStore/环境变量解析，不写入团队 JSON，不传到浏览器。

### 5.4 两支信息团队如何进入 TradingAgents

在每次模拟前，系统先读取两个团队最新且已通过门禁的文档版本，按 ticker、行业、主题和时间窗口筛选上下文，再注入 TradingAgents 的运行 state：

```python
class StockAgentsTradingGraph(TradingAgentsGraph):
    def resolve_instrument_context(self, ticker, asset_type="stock"):
        base = super().resolve_instrument_context(ticker, asset_type)
        context = source_context_provider.for_ticker(
            ticker=ticker,
            before=self.trade_date,
            channels=["ai_news_60s", "dufu_world_intel"],
        )
        return base + context.to_prompt(max_tokens=CONTEXT_BUDGET)
```

只注入当时已经发布的信息，保留文档版本、来源和时间，防止历史模拟读取未来文档。

## 6. 投资模拟的产品形态

### 6.1 第一阶段：AI 决策模拟

TradingAgents 生成结构化研究和最终交易决定，StockAgents 增加一个轻量 Paper Portfolio：

- 初始现金；
- 股票与数量；
- BUY/SELL/HOLD；
- 模拟成交价格；
- 现金和持仓变化；
- 已实现/未实现收益；
- 每次决定引用的 Agent 报告；
- 下一次同 ticker 运行时的结果反思。

这是 AI Agent 投资决策模拟，不承诺传统量化回测的逐笔撮合精度。

### 6.2 第二阶段：专用模拟页面

新增 `/investment-simulator.html`：

- 选择 ticker、日期、初始资金；
- 选择 Quick/Deep 模型；
- 选择启用的 TradingAgents 分析师；
- 选择 AI 快报/世界趋势信息源；
- 设置多空辩论轮数和风险轮数；
- 启动、暂停、取消、恢复；
- 查看 Agent 时间线、研究报告、最终决定、模拟持仓和收益；
- 后续加入拖放式来源选择。

### 6.3 Plaza 兜底且同步存在

Plaza 页面和当前 API、SSE、讨论、共识、任务分配、3D 会场全部保留。

新增 `investment_simulation` 讨论类型，TradingAgents 每个节点转换为 Plaza 事件：

```text
Market/Sentiment/News/Fundamentals Analyst 离席采集
→ 回场提交报告
→ Bull 与 Bear 研究员辩论
→ Research Manager 总结
→ Trader 提交交易计划
→ Aggressive/Neutral/Conservative 风险辩论
→ Portfolio Manager 裁决
→ Paper Portfolio 模拟成交
→ 结果写入记忆并进入下一轮反思
```

```python
async for event in trading_graph.stream(run):
    plaza_bridge.publish(
        plaza_id=run.plaza_id,
        discussion_id=run.discussion_id,
        agent_role=map_role(event.node),
        status=map_status(event),
        content=safe_summary(event.output),
        evidence_refs=event.evidence_refs,
    )
```

专用模拟页面不成熟时，Plaza 就是正式的第一版投资模拟页面，而不是临时假页面。

## 7. 页面保留与新增

| 页面 | 处理方式 |
| --- | --- |
| `/login.html` | 保留结构，只改关键词 |
| `/agent-team-config.html` | 登录后首页；扩展 TradingAgents 配置区 |
| `/plaza.html` | 完整保留，增加投资模拟讨论模式 |
| `/skill-extract.html` | 保留 |
| `/agent-memory.html` | 保留，并展示投资决策反思 |
| `/cost-dashboard.html` | 保留，统计 TradingAgents LLM 成本 |
| `/sources.html` | 新增信息源与动态文档入口 |
| `/ai-brief.html` | 新增 60 秒 AI 快报页面 |
| `/world-trends.html` | 新增独夫之心趋势页面 |
| `/investment-simulator.html` | 新增 AI 投资模拟页 |

全局导航只增加新入口，不移除旧入口。

## 8. API 规划

```text
/api/v1/trading-runtime
  GET  /health
  GET  /config-schema
  POST /config/validate

/api/v1/information-sources
  GET/POST /
  GET/PATCH/DELETE /{id}
  POST /{id}/test
  POST /teams/{team_id}/run

/api/v1/information-documents
  GET /
  GET /latest/{channel}
  GET /{id}/versions/{version}

/api/v1/investment-simulations
  GET/POST /
  GET /{run_id}
  POST /{run_id}/start
  POST /{run_id}/cancel
  GET /{run_id}/events
  GET /{run_id}/reports
  GET /{run_id}/portfolio

/api/v1/agent-config/plaza
  保留全部现有端点
  新增 investment_simulation 类型与运行绑定
```

## 9. 实施阶段

### Phase 0：保护原系统

- 建立当前测试基线；
- 锁定登录跳转、Build System、AI Coding 和 Plaza 行为；
- 补齐可复现依赖。

### Phase 1：登录文案与两支新团队

- 修改登录关键词；
- 新增两个 team factory；
- 增加启动注册与强制团队健康检查；
- Agent Config 能配置新团队的模型、Skills、Tools。

### Phase 2：信息采集和动态 HTML

- 实现可插拔来源；
- 实现两支团队的任务 DAG；
- 实现 `hugohe3`；
- 发布 AI 快报和世界趋势页面。

### Phase 3：TradingAgents v0.3.1

- 固定依赖和许可证；
- 实现 config mapper、graph adapter、context provider、event bridge；
- Agent Config 驱动 Quick/Deep 模型；
- 保存报告、决策和 checkpoint。

### Phase 4：Plaza 投资模拟

- 新增投资模拟讨论类型；
- 流式同步每个 TradingAgents 节点；
- 实现 Paper Portfolio；
- 在 Plaza 完成端到端模拟。

### Phase 5：专用投资模拟页

- 实现专用页面；
- 选择信息源和模型；
- 展示时间线、辩论、报告、决策和模拟账户；
- 评估并加入拖放式来源编排。

### Phase 6：测试、README 和发布

- 安全、失败隔离、历史日期和成本测试；
- 重写 README，所有命令按实际代码验证；
- 明确研究用途与非投资建议。

## 10. 验收标准

1. 登录页布局和功能不变，只显示 StockAgents 新关键词。
2. 登录、注册、访客和已登录重定向默认进入 Agent Config。
3. `build_system` 和 `ai_coding` 每次正常加载，持久化版本不被 factory 覆盖。
4. `ai_news_60s` 与 `dufu_world_intel` 能在 Agent Config 查看和编辑。
5. Plaza 的现有创建、讨论、SSE、共识、任务分配和 3D 功能继续通过测试。
6. 两支新团队能从 fixture 完成采集到动态 HTML 的全链路。
7. TradingAgents 固定为 v0.3.1，并能使用 Agent Config 中的 Quick/Deep 模型运行。
8. 两个信息团队的已发布文档能作为带版本和时间边界的上下文进入 TradingAgents。
9. TradingAgents 节点事件能实时出现在 Plaza 投资模拟讨论中。
10. 模型或 TradingAgents 不可用时，原系统和 Plaza 不崩溃，并给出可操作错误。
11. 一次模拟能产生分析报告、多空辩论、风险辩论、最终决定和 Paper Portfolio 变化。
12. README 只描述实际完成的功能，启动命令在干净环境验证通过。

## 11. 责任划分

- **Codex**：全部仓库代码、框架集成、团队、页面、API、测试、迁移和 README。
- **Grok**：两种内容风格的样本研究、外部信息源目录、来源覆盖与偏差审计。
- **联合**：Grok 提供带来源的研究材料，Codex 将其转换为 schema、Skill、Prompt、配置和测试。

当前环境没有 Grok 执行器，因此所有 Grok 工作都作为可并行的外部分工，不阻塞 Codex 从 Phase 0 开工。
