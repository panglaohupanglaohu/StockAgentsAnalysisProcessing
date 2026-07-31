# StockAgents 开发 TODO（修订版）

## 说明

- `[Codex]`：仓库内实现、测试和交付。
- `[Grok]`：外部研究任务，交付带来源和日期的 Markdown/JSON，不直接修改核心代码。
- `[联合]`：Grok 提供研究输入，Codex 审查后落成代码与测试。
- `DoD`：完成定义；不满足 DoD 不勾选。

## 立即开工顺序

第一批严格按以下顺序执行：

```text
T001 基线
→ T002 登录文案与跳转测试
→ T003 核心团队加载回归
→ T101/T102 两支新团队 factory
→ T301 TradingAgents v0.3.1 安装冒烟
```

完成这五项后，系统仍保持原功能，同时已经出现两支新团队，并具备最新 AI 投资框架的最小可运行入口。

## P0：保护现有系统

- [ ] **T001 [Codex] 建立可运行基线**
  - 盘点 Python/前端依赖、启动命令和测试命令。
  - 补齐根目录 `pyproject.toml`、`.env.example` 和测试配置。
  - 记录当前通过、失败和跳过测试，历史失败不伪装成新回归。
  - DoD：干净虚拟环境能启动 FastAPI；Agent Config、Build、AI Coding、Plaza 冒烟通过。

- [ ] **T002 [Codex] 修改登录页关键词并锁定跳转** ← T001
  - 只修改 `login.html` 的 title、印章、产品名、副标题、footer。
  - 不修改表单、认证 API、CSRF、Cookie、Token、CSS 布局。
  - 伪代码：

    ```javascript
    const DEFAULT_AFTER_LOGIN = '/agent-team-config.html'

    function getNextUrl() {
      const next = params.get('next') || DEFAULT_AFTER_LOGIN
      return isSafeLocalPath(next) ? next : DEFAULT_AFTER_LOGIN
    }
    ```

  - 测试：login、register、guest、authenticated redirect、恶意 `next=//host`。
  - DoD：所有入口默认进入 Agent Config，安全 next 逻辑不退化。

- [ ] **T003 [Codex] 锁定原团队和 Plaza 加载行为** ← T001
  - 增加 startup/API 测试：

    ```python
    assert team("build_system").agents
    assert team("ai_coding").agents
    assert plaza_router_is_mounted()
    assert plaza_engine_has_chat_harness()
    ```

  - 覆盖“磁盘团队优先于 factory”语义。
  - DoD：任何后续任务若破坏 Build System、AI Coding 或 Plaza，CI 立即失败。

- [ ] **T004 [Codex] 增加核心团队启动健康检查** ← T003
  - 核心 IDs：`build_system`、`ai_coding`、`ai_news_60s`、`dufu_world_intel`。
  - 缺少新团队时返回明确诊断；第三方投资运行时缺失不阻止原系统启动。
  - DoD：健康接口能区分 `core_system`、`information_teams`、`trading_runtime` 三层状态。

## P1：两支新团队

- [ ] **T101 [Codex] 创建 60 秒 AI 信息团队 factory** ← T003
  - 新建 `src/backend/agents/teams/ai_news_60s_team.py`。
  - team_id：`ai_news_60s`。
  - 注册 Lead、Scout、Checker、Market Mapper、Editor、Publisher 六名 Agent。
  - 每个 Agent 绑定最小 tools、skills、频道、权限、Quick/Deep 模型角色和 token budget。
  - 伪代码：

    ```python
    def create_ai_news_60s_team() -> AgentTeam:
        team = AgentTeam(team_id="ai_news_60s", ...)
        team.add_model(default_quick_model())
        team.add_model(default_deep_model())
        for agent in build_ai60_agents():
            validate_real_tools(agent.tools)
            team.add_agent(agent)
        return team
    ```

  - DoD：可序列化、持久化、重启恢复，并能在 Agent Config 编辑。

- [ ] **T102 [Codex] 创建独夫之心团队 factory** ← T003
  - 新建 `src/backend/agents/teams/dufu_world_intel_team.py`。
  - team_id：`dufu_world_intel`。
  - 注册 Lead、Web Collector、Data Engineer、Data Analyst、Red Team、Market Mapper、Presenter。
  - 强制 Web Collector 有 `web_search`/`web_extract`；数据角色有受限 `run_python`；Presenter 有 `hugohe3`。
  - DoD：可序列化、持久化、重启恢复，并能在 Agent Config 编辑。

- [ ] **T103 [Codex] 把两个 factory 接入 main 启动** ← T101, T102
  - 保留现有 Build/AI Coding 和其他团队代码。
  - 遵循 `if team_id not in persisted teams: seed factory`。
  - 支持 `AG_TEAM_ID=ai_news_60s` 和 `AG_TEAM_ID=dufu_world_intel`。
  - DoD：全量启动和单团队启动均通过测试。

- [ ] **T104 [Codex] 为新团队补齐 SkillDefinition** ← T101, T102
  - 新建实际可执行或可注入 prompt 的技能，不只写字符串名称。
  - 加入 `source_reputation`、`fact_checking`、`citation_audit`、`data_cleaning`、`data_mining`、`scenario_tree`、`macro_to_market` 等。
  - DoD：Agent Config 能查看 Skill 内容；Plaza prompt 能注入 Skill 描述。

- [ ] **T105 [Grok] 60 秒 AI 播报结构研究**
  - 分析 10 个公开样本的栏目、字数、节奏、信息密度和引用方式。
  - 不模仿声音、形象、口头禅，不复制原文。
  - DoD：交付 `research/ai60_format.md` 与结构化模板 JSON。

- [ ] **T106 [Grok] 独夫之心内容结构研究**
  - 分析 10 个公开样本的议题拆解、时间线、因果链、观点和结尾方式。
  - 明确样本中的事实、观点和修辞，避免人格克隆。
  - DoD：交付 `research/dufu_format.md` 与结构化模板 JSON。

## P2：信息源和动态 HTML

- [ ] **T201 [Codex] 实现可插拔信息源契约**
  - 首批 connector：fixture、RSS、普通网页/公开 JSON API。
  - 伪代码：

    ```python
    class SourceConnector(Protocol):
        async def healthcheck(config) -> HealthResult: ...
        async def fetch(since, cursor, config) -> FetchBatch: ...

    registry.register(manifest, factory)
    connector = registry.create(source.kind, source.config)
    ```

  - 安全：SSRF、内网地址、重定向、大小、超时、robots/许可元数据。
  - DoD：新 connector 不修改调度器；单一来源失败不影响其他来源。

- [ ] **T202 [Grok] 建立首批来源目录**
  - AI 来源至少 30 个；世界趋势来源至少 40 个。
  - 字段：URL、类型、地区、语言、更新频率、访问方式、许可、可信度、备用来源。
  - DoD：原始/官方来源优先，有覆盖与偏差说明。

- [ ] **T203 [Codex] 实现采集、标准化、去重和证据存储** ← T201
  - 伪代码：

    ```text
    fetch raw
      → normalize timestamps/entities
      → content hash dedupe
      → evidence record
      → source reputation score
      → team task input
    ```

  - DoD：每条发布内容能追溯原始 URL、抓取时间、内容 hash 和运行 ID。

- [ ] **T204 [联合] 固化两支团队的 Report Schema** ← T105, T106, T203
  - Codex 把研究输入变成 Pydantic schema、prompt 和验证门禁。
  - DoD：事实/观点/情景标签、引用、数据截止时间和不确定性均为必填。

- [ ] **T205 [Codex] 实现 `hugohe3` Skill 与安全 renderer** ← T204
  - 伪代码：

    ```python
    report = ReportSchema.model_validate(payload)
    html = hugohe3_template.render(report=report, chart_data=safe_json(report.data))
    validate_csp(html)
    validate_citations(html)
    return immutable_document_version(html)
    ```

  - DoD：响应式、可访问、图表有文本替代、无来源脚本/HTML 注入。

- [ ] **T206 [Codex] 实现 AI 60 秒团队任务 DAG** ← T103, T203, T205
  - `Scout → Normalize → Checker → Market Mapper → Editor → Lead Gate → Publisher`。
  - DoD：fixture 全链路生成 `/ai-brief.html` 的版本化动态文档。

- [ ] **T207 [Codex] 实现独夫之心团队任务 DAG** ← T103, T203, T205
  - `Collector → Data Engineer → Analyst → Red Team → Market Mapper → Lead Gate → Presenter`。
  - DoD：fixture 全链路生成 `/world-trends.html` 的版本化动态文档。

- [ ] **T208 [Codex] 实现信息源站点入口** ← T206, T207
  - 新增 `/sources.html`、`/ai-brief.html`、`/world-trends.html`。
  - 增加导航入口，不删除原导航项。
  - DoD：来源健康、最近运行、最新/历史文档可查看。

## P3：TradingAgents v0.3.1 集成

- [ ] **T301 [Codex] 固定并验证 TradingAgents v0.3.1** ← T001
  - 依赖固定为 signed tag `v0.3.1` / commit `01477f9`。
  - 保存 Apache-2.0 attribution/NOTICE。
  - 实现 import smoke；缺失依赖时健康接口降级而不是应用崩溃。
  - 伪代码：

    ```python
    try:
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        runtime_status = "ready"
    except ImportError as exc:
        runtime_status = "unavailable"
        runtime_error = actionable_message(exc)
    ```

  - DoD：可对 fixture ticker 运行最小 graph；原系统在运行时缺失时仍可启动。

- [ ] **T302 [Codex] 实现 Agent Config → TradingAgents Config Mapper** ← T301
  - 映射 provider、Quick/Deep model、backend URL、输出语言、辩论轮数、风险轮数、checkpoint 和 retry。
  - API Key 只从 SecretStore/环境变量解析。
  - DoD：至少覆盖 OpenAI-compatible、OpenAI、Anthropic、Google、xAI/Grok、DeepSeek、Qwen 和 Ollama。

- [ ] **T303 [Codex] 扩展 Agent Config 页面** ← T302
  - 增加 Trading Runtime 配置区：Quick/Deep 模型、分析师选择、辩论深度、风险深度、数据 vendor、checkpoint。
  - 不破坏现有模型、团队、Skill、Tool 配置。
  - DoD：配置保存、重载、校验和错误提示通过前端测试。

- [ ] **T304 [Codex] 实现 StockAgentsTradingGraph Adapter** ← T302
  - 不修改第三方源码；用 subclass/composition 包装。
  - 伪代码：

    ```python
    class StockAgentsTradingGraph(TradingAgentsGraph):
        def resolve_instrument_context(self, ticker, asset_type="stock"):
            base = super().resolve_instrument_context(ticker, asset_type)
            source_context = context_provider.for_ticker(
                ticker=ticker,
                cutoff=self.trade_date,
            )
            return base + source_context.to_prompt(max_tokens=context_budget)
    ```

  - DoD：信息上下文有版本、cutoff 和引用；历史运行不能读取未来文档。

- [ ] **T305 [Codex] 实现报告和决策适配器** ← T304
  - 保存 market、sentiment、news、fundamentals、多空辩论、交易计划、风险辩论、最终决定。
  - 将 `save_reports()` 产物索引到 StockAgents storage。
  - DoD：一次运行可通过 API 获取所有报告和原始运行状态。

- [ ] **T306 [Codex] 实现 TaskEngine 运行封装** ← T304
  - TradingAgents 长任务由现有 TaskEngine 启动、取消、记录成本和错误。
  - checkpoint 支持失败后恢复。
  - DoD：运行状态为 queued/running/completed/failed/cancelled；恢复不会串用不同 graph shape。

- [ ] **T307 [Codex] 实现版本更新检查但不自动升级**
  - 后台只提示新 release；升级必须修改 pin、运行兼容测试并记录 ADR。
  - DoD：生产运行不会跟随 `main` 漂移。

## P4：Plaza 投资模拟

- [ ] **T401 [Codex] 定义 InvestmentSimulation 模型** ← T305
  - 字段：ticker、date、asset type、initial cash、source versions、models、analysts、debate/risk rounds、plaza/discussion IDs、status。
  - DoD：API schema 和持久化模型一致。

- [ ] **T402 [Codex] 新增 Plaza `investment_simulation` 讨论类型** ← T003, T401
  - 不修改普通 Plaza 讨论行为。
  - 创建模拟时自动新建或绑定一个 Plaza discussion。
  - DoD：普通讨论回归通过；投资讨论显示专属阶段。

- [ ] **T403 [Codex] 实现 TradingAgents → Plaza Event Bridge** ← T306, T402
  - 映射节点：4 类分析师、多空研究、Research Manager、Trader、3 类风险、Portfolio Manager。
  - 伪代码：

    ```python
    on_graph_node(event):
        plaza.publish_message(
            participant=role_map[event.node],
            phase=phase_map[event.node],
            content=safe_summary(event.output),
            evidence=event.evidence_refs,
        )
        plaza.publish_presence(
            state="away" if event.status == "collecting" else "returned"
        )
    ```

  - DoD：Plaza SSE 实时显示 Agent 出发、返回、辩论、裁决和错误。

- [ ] **T404 [Codex] 扩展 Plaza 3D 状态表现** ← T403
  - `seated / away / collecting / debating / deciding / completed / failed`。
  - 使用现有 Three.js 场景，不重写 Plaza。
  - DoD：普通讨论视觉不变；投资模拟能看出当前是谁在行动。

- [ ] **T405 [Codex] 实现轻量 Paper Portfolio** ← T305
  - 伪代码：

    ```python
    decision = parse_structured_decision(final_trade_decision)
    if decision.action == "BUY":
        qty = size_by_risk(cash, price, decision.confidence, max_position)
        portfolio.buy(ticker, qty, price, fees)
    elif decision.action == "SELL":
        portfolio.sell(ticker, allowed_qty, price, fees)
    else:
        portfolio.hold()
    ```

  - DoD：现金、持仓、成交、收益和引用报告可审计；绝不连接真实券商。

- [ ] **T406 [Codex] 完成 Plaza 端到端投资模拟** ← T403, T404, T405
  - DoD：从 Plaza 创建一次模拟，看到全过程并得到最终 Paper Portfolio 结果。

## P5：专用投资模拟页面

- [ ] **T501 [Codex] 新建 `/investment-simulator.html`** ← T406
  - 选择 ticker、日期、初始资金、Quick/Deep 模型、分析师、来源、辩论和风险轮数。
  - DoD：创建、启动、取消、恢复一次模拟。

- [ ] **T502 [Codex] 实现运行时间线和报告面板** ← T501
  - 展示节点进度、Agent 输出、多空辩论、风险辩论、最终决定、错误和 checkpoint。
  - DoD：刷新页面后可恢复运行状态。

- [ ] **T503 [Codex] 实现模拟账户面板** ← T405, T501
  - 现金、持仓、成交、成本、收益、决策引用。
  - DoD：与后端账本一致，有空状态和失败状态。

- [ ] **T504 [Codex] 加入信息源拖放编排** ← T501
  - 左侧来源卡片拖入当前模拟；可拖出、禁用、重排。
  - 第一版只编排“来源选择和优先级”，不重造 TradingAgents 内部 LangGraph。
  - 伪代码：

    ```javascript
    onDrop(source) {
      simulation.sources.push({ sourceId: source.id, priority: nextPriority() })
      saveDraft()
    }
    onRemove(sourceId) {
      simulation.sources = simulation.sources.filter(x => x.sourceId !== sourceId)
      saveDraft()
    }
    ```

  - DoD：拖放结果进入 simulation snapshot，并决定 context provider 使用哪些文档。

- [ ] **T505 [Codex] 保持 Plaza 深链入口** ← T501
  - 每个运行提供“在 Plaza 查看自主行动”链接；Plaza 提供“打开模拟详情”链接。
  - DoD：两页面状态和同一 run ID 对齐。

## P6：API、安全、成本和测试

- [ ] **T601 [Codex] 实现 Trading Runtime 与 Simulation API**
  - 按 `PLAN.md §8` 实现 health/config/source/document/simulation API。
  - DoD：OpenAPI 完整，错误结构统一，写 API 使用现有认证/CSRF。

- [ ] **T602 [Codex] 安全加固**
  - API Key 脱敏、SSRF、防目录穿越、HTML 注入、CSP、来源大小/超时、ticker 校验。
  - DoD：恶意 fixture 被测试拒绝。

- [ ] **T603 [Codex] LLM 成本与预算接入**
  - TradingAgents callbacks 接入现有 cost aggregator/token budget。
  - 超预算时停止下一节点并把原因同步 Plaza。
  - DoD：按 run、team、agent、provider、model 查看成本。

- [ ] **T604 [Codex] 历史日期与未来信息测试**
  - 信息文档 cutoff、TradingAgents 数据窗口、checkpoint graph shape、ticker identity。
  - DoD：已知未来数据 fixture 永远不能进入历史运行。

- [ ] **T605 [Codex] 端到端测试**
  - 流程：登录 → Agent Config → 确认四个核心团队 → 运行两个信息团队 → 创建模拟 → Plaza 流式展示 → Paper Portfolio。
  - DoD：离线 fixture 模式通过；在线测试单独标记。

- [ ] **T606 [Grok] 来源覆盖和观点偏差审计** ← T202
  - 检查语言、地区、机构类型、政治立场和单一来源依赖。
  - DoD：交付覆盖矩阵和改进清单，不直接写生产配置。

## P7：README 与发布

- [ ] **T701 [Codex] 重写根目录 README** ← 全部已实现任务
  - 包含：定位、登录流程、Agent Config、所有团队、两支信息团队、TradingAgents v0.3.1、Plaza 投资模拟、信息源、运行方式、测试、安全和免责声明。
  - DoD：README 只描述已实现能力；所有命令在干净环境验证。

- [ ] **T702 [Codex] 第三方许可证和 NOTICE**
  - 记录 TradingAgents Apache-2.0、版本、commit、修改/未修改说明。
  - DoD：发布包包含必要 attribution。

- [ ] **T703 [Codex] 发布验收**
  - 逐项验证 `PLAN.md §10`。
  - DoD：原系统无回归；投资功能明确标注研究用途、模拟交易和非投资建议。

## 依赖图

```text
T001 → T002 → T003 → T004
                ├→ T101 → T103 → T104
                └→ T102 ───────┘

T201 → T203 → T204 → T205 → T206/T207 → T208
  ↑              ↑
T202            T105/T106

T301 → T302 → T303
          └→ T304 → T305 → T306

T305 → T401 → T402
T306 + T402 → T403 → T404
T305 → T405
T403 + T404 + T405 → T406

T406 → T501 → T502/T503/T504/T505
→ T601/T602/T603/T604/T605
→ T701/T702/T703
```

## 第一批提交建议

```text
Commit 1: chore — 可复现依赖与基线测试
Commit 2: feat(auth-ui) — 登录页关键词与 Agent Config 默认跳转回归
Commit 3: test(teams-plaza) — Build System、AI Coding、Plaza 保护测试
Commit 4: feat(teams) — ai_news_60s 与 dufu_world_intel factory
Commit 5: feat(trading-runtime) — TradingAgents v0.3.1 pin + health + smoke
```

这五个提交完成后再进入信息源与 Plaza 投资流程，避免大爆炸式修改。
