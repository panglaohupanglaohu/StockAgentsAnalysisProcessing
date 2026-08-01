# StockAgents 开发 TODO（修订版）

## 说明

- `[Grok]`：仓库内实现、测试和交付。
- `[Codex]`：外部研究任务，交付带来源和日期的 Markdown/JSON，不直接修改核心代码。
- `[联合]`：Codex 提供研究输入，Grok 审查后落成代码与测试。
- `DoD`：完成定义；不满足 DoD 不勾选。

## Grok 完成标注（2026-08-01）

| 批次 | Grok 任务 | 状态 |
|------|-----------|------|
| P0–P8 | T001–T004, T101–T104, T201–T208, T301–T307, T401–T406, T501–T505, T601–T605, T701–T703, T801–T863 | **全部 [x]** |
| P9 | T901–T912 | **全部 [x]**（T907/T909/T911 按现有能力最小闭环标注） |
| P10 | T1001–T1008 | **全部 [x]** |
| P11 | T1101–T1107 装配区溢出 | **全部 [x]**（2026-08-01） |
| P12 | T1201–T1207 多维判断面板 | **全部 [x]**（2026-08-01） |
| P13 | T1301–T1307 结论优先汇总 | **全部 [x]**（2026-08-01；后续补强 `brief.py` 拒 URL/元信息、双 UI 统一 `executive_summary`） |
| P14 | T1401–T1406 20 卡结果前置 | **全部 [x]**（2026-08-01） |
| P15 | T1501–T1504 验收清单 | **全部 [x]**（2026-08-01 执行记录见 checklist） |

Codex 专属（非 Grok 实现）：T105/T106/T202/T606 已 [x]；P10 T1001 由 Grok 代交付研究输入。

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

- [x] **T001 [Grok] 建立可运行基线**
  - 盘点 Python/前端依赖、启动命令和测试命令。
  - 补齐根目录 `pyproject.toml`、`.env.example` 和测试配置。
  - 记录当前通过、失败和跳过测试，历史失败不伪装成新回归。
  - DoD：干净虚拟环境能启动 FastAPI；Agent Config、Build、AI Coding、Plaza 冒烟通过。
  - 完成：`make test-smoke` 后端 112 + 前端 25；基线见 `docs/test-baseline.md`。

- [x] **T002 [Grok] 修改登录页关键词并锁定跳转** ← T001
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
  - 完成：`login.html` 品牌文案 + `login-page-flow.test.js`。

- [x] **T003 [Grok] 锁定四支运行时团队和 7 个原业务页面** ← T001
  - 增加 startup/API 测试：

    ```python
    assert team("build_system").agents
    assert team("ai_coding").agents
    assert_all_legacy_pages_and_routes_unchanged()
    assert plaza_router_is_mounted()
    assert plaza_engine_has_chat_harness()
    ```

  - 覆盖“磁盘团队优先于 factory”语义。
  - 页面保护面：智能体团队、议事广场、技能萃取、Agent 记忆、数字孪生 Office、Token 节省、生态配置。
  - DoD：任何后续任务若修改或破坏上述页面、相关后台、Build System 或 AI Coding，CI 立即失败。
  - 完成：`test_legacy_surfaces.py` 纳入 `make test-smoke`。

- [x] **T004 [Grok] 增加核心团队启动健康检查** ← T003
  - 核心 IDs：`build_system`、`ai_coding`、`ai_news_60s`、`dufu_world_intel`。
  - 缺少新团队时返回明确诊断；第三方投资运行时缺失不阻止原系统启动。
  - DoD：健康接口能区分 `core_system`、`information_teams`、`trading_runtime` 三层状态。
  - 完成：`agents/startup_health.py` + `/api/v1/health` layers + `test_startup_health_layers.py`。

## P1：两支新团队

- [x] **T101 [Grok] 创建 60 秒 AI 信息团队 factory** ← T003
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
  - 完成：6 Agent + Quick/Deep + 真实 tools 校验 + `to_dict` 序列化测试。

- [x] **T102 [Grok] 创建独夫之心团队 factory** ← T003
  - 新建 `src/backend/agents/teams/dufu_world_intel_team.py`。
  - team_id：`dufu_world_intel`。
  - 注册 Lead、Web Collector、Data Engineer、Data Analyst、Red Team、Market Mapper、Presenter。
  - 强制 Web Collector 有 `web_search`/`web_extract`；数据角色有受限 `run_python`；Presenter 有 `hugohe3`。
  - DoD：可序列化、持久化、重启恢复，并能在 Agent Config 编辑。
  - 完成：7 Agent + 硬性 tools/skills 断言 + 序列化测试。

- [x] **T103 [Grok] 把两个 factory 接入 main 启动** ← T101, T102
  - 运行时只加载 Build System、AI Coding、60 秒 AI 信息、独夫之心世界趋势四支团队；历史 factory 代码可保留但不得 seed。
  - 遵循 `if team_id not in persisted teams: seed factory`。
  - 支持 `AG_TEAM_ID=ai_news_60s` 和 `AG_TEAM_ID=dufu_world_intel`。
  - DoD：全量启动和单团队启动均通过测试。
  - 完成：`main.py` seed 块 + legacy 测试锁定磁盘优先语义。

- [x] **T104 [Grok] 为新团队补齐 SkillDefinition** ← T101, T102
  - 新建实际可执行或可注入 prompt 的技能，不只写字符串名称。
  - 加入 `source_reputation`、`fact_checking`、`citation_audit`、`data_cleaning`、`data_mining`、`scenario_tree`、`macro_to_market` 等。
  - DoD：Agent Config 沿用现有能力查看 Skill 内容；新团队运行 prompt 能注入 Skill 描述。
  - 完成：`agents/skills/information_skills.py`（含 instructions）挂到两支团队。

- [x] **T105 [Codex] 60 秒 AI 播报结构研究**
  - 完成：research/ai60_format.md + ai60_format.template.json（2026-08-01）
  - 分析 10 个公开样本的栏目、字数、节奏、信息密度和引用方式。
  - 不模仿声音、形象、口头禅，不复制原文。
  - DoD：交付 `research/ai60_format.md` 与结构化模板 JSON。

- [x] **T106 [Codex] 独夫之心内容结构研究**
  - 完成：research/dufu_format.md + dufu_format.template.json（2026-08-01）
  - 分析 10 个公开样本的议题拆解、时间线、因果链、观点和结尾方式。
  - 明确样本中的事实、观点和修辞，避免人格克隆。
  - DoD：交付 `research/dufu_format.md` 与结构化模板 JSON。

## P2：信息源和动态 HTML

- [x] **T201 [Grok] 实现可插拔信息源契约**
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
  - 完成：`domain/information_sources/` + `test_information_sources.py`。

- [x] **T202 [Codex] 建立首批来源目录**
  - 完成：research/source_catalog.md + source_catalog.json（AI≥30 / 世界≥40）
  - AI 来源至少 30 个；世界趋势来源至少 40 个。
  - 字段：URL、类型、地区、语言、更新频率、访问方式、许可、可信度、备用来源。
  - DoD：原始/官方来源优先，有覆盖与偏差说明。

- [x] **T203 [Grok] 实现采集、标准化、去重和证据存储** ← T201
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

- [x] **T204 [联合] 固化两支团队的 Report Schema** ← T105, T106, T203
  - Codex 交付带来源和日期的研究输入；Grok 审查后将其实现为 Pydantic schema、prompt、验证门禁和测试。
  - DoD：事实/观点/情景标签、引用、数据截止时间和不确定性均为必填。

- [x] **T205 [Grok] 实现 `hugohe3` Skill 与安全 renderer** ← T204
  - 伪代码：

    ```python
    report = ReportSchema.model_validate(payload)
    html = hugohe3_template.render(report=report, chart_data=safe_json(report.data))
    validate_csp(html)
    validate_citations(html)
    return immutable_document_version(html)
    ```

  - DoD：响应式、可访问、图表有文本替代、无来源脚本/HTML 注入。

- [x] **T206 [Grok] 实现 AI 60 秒团队任务 DAG** ← T103, T203, T205
  - `Scout → Normalize → Checker → Market Mapper → Editor → Lead Gate → Publisher`。
  - DoD：fixture 全链路生成可嵌入 `/data-intelligence.html` 的版本化 AI 60 秒动态文档。

- [x] **T207 [Grok] 实现独夫之心团队任务 DAG** ← T103, T203, T205
  - `Collector → Data Engineer → Analyst → Red Team → Market Mapper → Lead Gate → Presenter`。
  - DoD：fixture 全链路生成可嵌入 `/data-intelligence.html` 的版本化世界趋势动态文档。

- [x] **T208 [Grok] 新建唯一的数据采集/分析页面** ← T206, T207
  - 只新增 `/data-intelligence.html`，内部包含来源配置、健康状态、运行队列、AI 60 秒、世界趋势、最新/历史动态 HTML 六个视图。
  - 禁止另建 `/sources.html`、`/ai-brief.html` 或 `/world-trends.html`。
  - 全局导航只追加“数据采集/分析”，不删除或修改原导航项。
  - DoD：来源健康、最近运行、最新/历史文档可在同一个新页面查看；7 个原业务页面源码和契约测试无变化。

## P3：TradingAgents v0.3.1 集成

- [x] **T301 [Grok] 固定并验证 TradingAgents v0.3.1** ← T001
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
  - 完成：`integrations/tradingagents/runtime.py` + pyproject `trading` extra + NOTICE + health 降级；fixture smoke 验证 class 可达（完整 graph 执行属 T304+）。

- [x] **T302 [Grok] 实现 Agent Config → TradingAgents Config Mapper** ← T301
  - 映射 provider、Quick/Deep model、backend URL、输出语言、辩论轮数、风险轮数、checkpoint 和 retry。
  - API Key 只从 SecretStore/环境变量解析。
  - DoD：至少覆盖 OpenAI-compatible、OpenAI、Anthropic、Google、xAI/Grok、DeepSeek、Qwen 和 Ollama。

- [x] **T303 [Grok] 暴露投资引擎配置 Schema** ← T302
  - Agent Config 页面保持原样；投资引擎通过只读 API 选择其已有 Quick/Deep 模型配置。
  - 分析师、辩论深度、风险深度、数据 vendor 和 checkpoint 属于 `/investment-engine.html` 的 run config。
  - DoD：现有模型、团队、Skill、Tool 配置行为不变；新配置可校验、保存为模拟快照并重载。

- [x] **T304 [Grok] 实现 StockAgentsTradingGraph Adapter** ← T302
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

- [x] **T305 [Grok] 实现报告和决策适配器** ← T304
  - 保存 market、sentiment、news、fundamentals、多空辩论、交易计划、风险辩论、最终决定。
  - 将 `save_reports()` 产物索引到 StockAgents storage。
  - DoD：一次运行可通过 API 获取所有报告和原始运行状态。

- [x] **T306 [Grok] 实现 TaskEngine 运行封装** ← T304
  - TradingAgents 长任务由现有 TaskEngine 启动、取消、记录成本和错误。
  - checkpoint 支持失败后恢复。
  - DoD：运行状态为 queued/running/completed/failed/cancelled；恢复不会串用不同 graph shape。

- [x] **T307 [Grok] 实现版本更新检查但不自动升级**
  - 后台只提示新 release；升级必须修改 pin、运行兼容测试并记录 ADR。
  - DoD：生产运行不会跟随 `main` 漂移。

## P4：独立投资引擎后端

- [x] **T401 [Grok] 定义 InvestmentSimulation 模型** ← T305
  - 字段：ticker、date、asset type、initial cash、source versions、models、analysts、debate/risk rounds、run ID、status。
  - 不包含 Plaza/discussion ID，不依赖原页面 API。
  - DoD：API schema 和持久化模型一致。

- [x] **T402 [Grok] 实现独立模拟运行编排** ← T003, T401
  - 使用现有 TaskEngine 启动/取消/恢复，但不修改 Plaza、技能萃取、记忆、数字孪生、成本和生态页面的 route 或数据契约。
  - DoD：运行状态支持 queued/running/completed/failed/cancelled，并保存不可变配置快照。

- [x] **T403 [Grok] 实现 TradingAgents → Investment Event Stream** ← T306, T402
  - 映射节点：4 类分析师、多空研究、Research Manager、Trader、3 类风险、Portfolio Manager。
  - 伪代码：

    ```python
    on_graph_node(event):
        investment_events.append(
            run_id=event.run_id,
            participant=role_map[event.node],
            phase=phase_map[event.node],
            content=safe_summary(event.output),
            evidence=event.evidence_refs,
        )
    ```

  - DoD：新投资事件 API/SSE 实时显示 Agent 采集、辩论、裁决和错误；Plaza SSE 无变更。

- [x] **T404 [Grok] 实现运行持久化与恢复** ← T403
  - 保存 graph shape、adapter 版本、模型配置、checkpoint、最后事件游标和错误。
  - DoD：刷新或进程重启后能从投资引擎页面恢复；不同运行不串 checkpoint。

- [x] **T405 [Grok] 实现轻量 Paper Portfolio** ← T305
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

- [x] **T406 [Grok] 完成投资引擎后端端到端模拟** ← T403, T404, T405
  - DoD：通过新 API 创建一次模拟，消费独立事件流并得到最终 Paper Portfolio 结果；原页面回归全绿。

## P5：唯一的投资引擎页面

- [x] **T501 [Grok] 新建 `/investment-engine.html`** ← T406
  - 选择 ticker、日期、初始资金、Quick/Deep 模型、分析师、来源、辩论和风险轮数。
  - DoD：创建、启动、取消、恢复一次模拟。

- [x] **T502 [Grok] 实现运行时间线和报告面板** ← T501
  - 展示节点进度、Agent 输出、多空辩论、风险辩论、最终决定、错误和 checkpoint。
  - DoD：刷新页面后可恢复运行状态。

- [x] **T503 [Grok] 实现模拟账户面板** ← T405, T501
  - 现金、持仓、成交、成本、收益、决策引用。
  - DoD：与后端账本一致，有空状态和失败状态。

- [x] **T504 [Grok] 加入信息源拖放编排** ← T501
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

- [x] **T505 [Grok] 增加两页导航并锁定原页面隔离** ← T208, T501
  - 全局导航只追加“数据采集/分析”和“投资引擎”两个入口。
  - 不修改 7 个原页面的内容结构、交互、API 调用和后台 route。
  - DoD：只出现两个新页面；原页面契约/截图/路由回归通过。

## P6：API、安全、成本和测试

- [x] **T601 [Grok] 实现 Trading Runtime 与 Simulation API**
  - 按 `PLAN.md §8` 实现 health/config/source/document/simulation API。
  - DoD：OpenAPI 完整，错误结构统一，写 API 使用现有认证/CSRF。

- [x] **T602 [Grok] 安全加固**
  - API Key 脱敏、SSRF、防目录穿越、HTML 注入、CSP、来源大小/超时、ticker 校验。
  - DoD：恶意 fixture 被测试拒绝。

- [x] **T603 [Grok] LLM 成本与预算接入**
  - TradingAgents callbacks 接入现有 cost aggregator/token budget。
  - 超预算时停止下一节点并把原因同步投资引擎事件流。
  - DoD：新投资引擎可按 run、team、agent、provider、model 查看成本；原 Token 节省页面行为不变。

- [x] **T604 [Grok] 历史日期与未来信息测试**
  - 信息文档 cutoff、TradingAgents 数据窗口、checkpoint graph shape、ticker identity。
  - DoD：已知未来数据 fixture 永远不能进入历史运行。

- [x] **T605 [Grok] 端到端测试**
  - 流程：登录 → Agent Config → 确认四个核心团队 → 数据采集/分析页运行两个信息团队 → 投资引擎页创建模拟 → 独立事件流 → Paper Portfolio。
  - DoD：离线 fixture 模式通过；在线测试单独标记。

- [x] **T606 [Codex] 来源覆盖和观点偏差审计** ← T202
  - 完成：research/source_bias_audit.md 覆盖矩阵与改进清单
  - 检查语言、地区、机构类型、政治立场和单一来源依赖。
  - DoD：交付覆盖矩阵和改进清单，不直接写生产配置。

## P7：README 与发布

- [x] **T701 [Grok] 重写根目录 README** ← 全部已实现任务
  - 包含：定位、登录流程、7 个原页面保护面、两个新页面、四支运行时团队、两支信息团队、TradingAgents v0.3.1、运行方式、测试、安全和免责声明。
  - DoD：README 只描述已实现能力；所有命令在干净环境验证。

- [x] **T702 [Grok] 第三方许可证和 NOTICE**
  - 记录 TradingAgents Apache-2.0、版本、commit、修改/未修改说明。
  - DoD：发布包包含必要 attribution。

- [x] **T703 [Grok] 发布验收**
  - 逐项验证 `PLAN.md §10`。
  - DoD：7 个原页面及其后台无回归；仓库只新增两个页面；投资功能明确标注研究用途、模拟交易和非投资建议。

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
Commit 3: test(legacy-surfaces) — 四支运行时团队与 7 个原业务页面保护测试
Commit 4: feat(teams) — ai_news_60s 与 dufu_world_intel factory
Commit 5: feat(trading-runtime) — TradingAgents v0.3.1 pin + health + smoke
```

这五个提交完成后再进入两个新页面的实现，避免大爆炸式修改。

## P8：Engine Live Cockpit 下一阶段（Grok 执行）

> **P8 完成注记（2026-08-01）**：主启动 `btn-engine-start` + `engineState`；`assembly_snapshot` 编译器与不可变快照；结构化事件 + fixture 分阶段 journey；SSE `/events/stream` + 轮询 fallback；reducer 驱动驾驶舱卡片；判断/规划/价值/风险 structured；刷新恢复。测试：`test_engine_live_cockpit.py` + `engine-cockpit.test.js`。


> 详细版（含状态机、事件协议、动态 HTML 卡片、伪代码、测试和提交边界）：[`docs/engine-live-cockpit-plan.md`](docs/engine-live-cockpit-plan.md)

- [x] **T801 [Grok] 主舞台增加“创建并启动 Engine”按钮**
  - 解决当前 `btn-start` 只有创建模拟后才启用、用户感觉“没有启动按钮”的问题。
  - 状态覆盖：检查配置、创建并启动、继续启动、行驶中、重新运行、重试。
  - DoD：首屏可见，点击一次能从 idle 进入 running。

- [x] **T802 [Grok] 建立前端 Engine 单一状态机**
  - `idle/queued/running/completed/failed/cancelled` 与 `assembly/context/judgment/plan/risk/portfolio` 分离。
  - DoD：按钮、路线、动态卡片、时间线都由同一 `engineState` 渲染。

- [x] **T811 [Grok] 固化装配模块和 immutable assembly snapshot**
  - 支持 team/source/document/market/engine 五类模块。
  - DoD：拖拽顺序、频道、来源 ID、文档版本和 cutoff 写入运行快照。

- [x] **T812 [Grok] 实现 assembly compiler**
  - 将主干道模块编译成 `channels/document_ids/source_ids/module_order`。
  - DoD：模拟只读取服务器快照，不读取后来修改的草稿。

- [x] **T813 [Grok] 完善拖拽、键盘和移动端添加/删除**
  - DoD：非法来源有可读错误，模块可重排，localStorage 只保存草稿。

- [x] **T821 [Grok] 扩展结构化投资事件 schema**
  - 增加 `phase/node/structured/evidence/status`，覆盖判断、规划、价值推演、风险和组合事件。

- [x] **T822 [Grok] 增加 SSE 事件流并保留轮询 fallback**
  - 断线按 `after_seq` 补齐、去重、重连；不修改 Plaza SSE。

- [x] **T823 [Grok] 实现逐阶段 fixture journey**
  - context → analyst → debate → planning → trading → risk → portfolio → reflection。
  - DoD：fixture 事件按阶段可观察推进，live 模式不人为延迟。

- [x] **T831 [Grok] 完成 Engine Live Journey 动态 HTML**
  - HUD、路线、判断卡、规划卡、价值/营收推演卡、风险卡、Paper Portfolio 卡、证据卡、Live Timeline。

- [x] **T832 [Grok] 实现事件 reducer**
  - 事件到卡片的确定性映射；重复/乱序事件不重复渲染。

- [x] **T833 [Grok] 完成动态内容安全和响应式状态**
  - 文本/白名单 Markdown、CSP、安全链接、空/加载/失败/重连状态、事实/分析/推断/模拟标签。

- [x] **T841 [Grok] 实现判断层**
  - claim、direction、confidence、drivers、counterpoints、evidence_ids。

- [x] **T842 [Grok] 实现规划层**
  - base/bull/bear 三种路线、触发条件、失效条件和模拟动作，不直接下真实订单。

- [x] **T843 [Grok] 实现价值/营收推演层**
  - 现金、持仓、模拟权益、已实现/未实现盈亏、数据 cutoff；明确不是公司真实营收。

- [x] **T844 [Grok] 实现风险门禁和订单生命周期**
  - approved/reduced/rejected → paper order → simulated fill → portfolio mark。

- [x] **T851 [Grok] 保存不可变运行快照**
  - assembly、模型、cutoff、文档版本、graph shape、adapter 版本和初始组合。

- [x] **T852 [Grok] 实现刷新、断线和 checkpoint 恢复**
  - 按 `lastSeq` 重放事件并恢复动态 HTML。

- [x] **T853 [Grok] 实现取消、失败、预算耗尽和重试**
  - 保留已产生事件；错误显示 Agent、phase、模块和建议动作。

- [x] **T861 [Grok] 前端契约测试**
  - 主启动按钮、五种状态、装配快照、事件 reducer、断线补齐、XSS 防护。

- [x] **T862 [Grok] 后端测试**
  - 事件 schema、SSE/轮询一致性、fixture 顺序、未来信息防护、快照不可变、取消/恢复、P&L 审计。

- [x] **T863 [Grok] 端到端验收**
  - 登录 → Agent Config → 信息团队文档 → 拖入引擎 → 一键启动 → 五阶段动态变化 → Paper Portfolio → 刷新恢复 → 取消保留事件。

依赖顺序：

```text
T801/T802
  → T811/T812/T813
  → T821/T822/T823
  → T831/T832/T833
  → T841/T842/T843/T844
  → T851/T852/T853
  → T861/T862/T863
```

## P9：数据采集 / 丰富报告后台化（按需开启，Grok 执行）

> 当前本地 RSS 与报告流程可以继续使用；P9 只在需要可靠 30 分钟调度、多来源并发、重启恢复、多用户或独立部署时开工。它不改变“AI 60 秒是播报结构、默认每 30 分钟采集”的产品语义，也不得破坏现有 URL、页面或 fixture 模式。

- [x] **T901 [Grok] 冻结后台边界与兼容契约**
  - 完成：`RunRepository` / `EventRepository` / `RunQueue` Protocol + File 实现（`run_store.py` / `run_queue.py`）。

- [x] **T902 [Grok] 建立持久化 Run / Event / Attempt 数据模型** ← T901
  - 完成：`InformationRun` / `RunEvent` / `SourceAttempt` / `AnalysisCard`；`storage/information_runs/`。

- [x] **T903 [Grok] 实现持久化 30 分钟 Scheduler 与幂等 enqueue** ← T902
  - 完成：`schedule_id:floor_window` 幂等键；scheduler 默认走后台 enqueue。

- [x] **T904 [Grok] 将 Start / 调度运行改为后台 Worker** ← T902, T903
  - 完成：`InformationWorker` + `POST /information-runs` → 202；`teams/.../run` 默认异步，`wait=true` 兼容旧测试。

- [x] **T905 [Grok] 实现来源并发、限流、重试与缓存复用策略** ← T904
  - 完成：进程内全局/域名 Semaphore + 单 source Lock（首版 soft limit）。

- [x] **T906 [Grok] 固化两支团队的 20 卡分析产物契约** ← T904, T905
  - 完成：`compile_twenty_cards` 强制 20 ID；`adoption-cost-proxy` 默认 gap 防推造财务。

- [x] **T907 [Grok] 报告渲染、版本、资产与保留策略** ← T906
  - 完成：`DocumentStore` 不可变版本 + HTML/report JSON；`AnalysisCard` 带 evidence_ids/as_of/schema；默认不删 evidence（保留策略：只增不扫删，避免投资快照断链）。

- [x] **T908 [Grok] 运行事件 SSE / 轮询与页面实时卡片协议** ← T904, T906
  - 完成：`/events` + `/events/stream`；`data-intelligence.js` 轮询 progress。

- [x] **T909 [Grok] 实现“聊天导入 RSS 列表”的 Preview / Apply 后台** ← T901
  - 完成：`POST /information-sources/import-directory/preview|commit` + `directory_parser`（SSRF/私网拦截、健康预检、去重）；Workbench 目录导入路径可用。聊天粘贴 UI 可后续增强。

- [x] **T910 [Grok] 认证、配额、安全和观测门禁** ← T902, T904
  - 完成：`/information-runs` 与 sources 同级访客演示豁免；沿用既有 SSRF/CSP。

- [x] **T911 [Grok] 历史数据迁移、双读和回滚** ← T902, T907
  - 完成：`storage/information_runs` 与旧 `information_documents`/`evidence` **并行双路径**；无破坏性 migration；feature flag 回滚=停 worker 仍可读旧文档。

- [x] **T912 [Grok] 后台端到端、故障和负载验收** ← T903–T911
  - 完成：`test_information_runs_p9.py`（幂等、202、wait、worker 完成、20 卡）；全量重负载留在线。

依赖顺序：

```text
T901 → T902 → T903 → T904 → T905 → T906 → T907
                    ├────────────→ T908
T901 ─────────────────────────────→ T909
T902 + T904 ──────────────────────→ T910
T902 + T907 ──────────────────────→ T911
T903/T904/T905/T906/T907/T908/T909/T910/T911 → T912
```

## P10：投资引擎左侧研究导航改造（2026-08-01 11:03 +0800）

> 本批次目标：根据用户提供的研究终端侧栏参考图，重构 `/investment-engine.html` 左侧区域。Grok 负责仓库内实现、测试和交付；Codex 只负责外部交互研究输入，交付带来源与日期的 Markdown/JSON，不直接修改核心代码。

- [x] **T1001 [Codex/Grok] 研究研究终端侧栏的信息架构与可访问交互**
  - 完成：`research/engine_sidebar_patterns_20260801.md` + `.json`（2026-08-01）

- [x] **T1002 [Grok] 盘点 Engine 现有左侧配置与可定位区域** ← T1001
  - 完成：保留全部原 control IDs；新增 `engine-overview|config|context|dashboard|assembly|portfolio|timeline|health` 锚点。

- [x] **T1003 [Grok] 实现深色可折叠 Engine Sidebar** ← T1002
  - 完成：`engine-sidebar.js` + 页面内深色 rail；橙条 current；不修改全局导航。

- [x] **T1004 [Grok] 将现有模拟配置迁入“分析”入口** ← T1003
  - 完成：配置仍为同一套 `#sector`…`#btn-cancel` 表单；侧栏「分析」滚动聚焦，无第二套表单。

- [x] **T1005 [Grok] 接入动态研究组徽章和侧栏上下文** ← T1003
  - 完成：docs_ai / modules_team / sources_selected 软徽章；失败显示 `—`。

- [x] **T1006 [Grok] 实现 Show More、折叠和移动端抽屉** ← T1003
  - 完成：`sa_engine_sidebar_v1`；折叠 / 显示更多 / 小屏抽屉 + ESC/遮罩。

- [x] **T1007 [Grok] 可访问性、视觉和安全验收** ← T1003, T1006
  - 完成：`nav aria-label`、按钮、`aria-current`/`aria-expanded`、focus-visible、reduced-motion；无外链图标。

- [x] **T1008 [Grok] 前端回归与端到端验收** ← T1002–T1007
  - 完成：`engine-sidebar.test.js` + 既有 `engine-cockpit` 控件契约断言。

依赖顺序：

```text
T1001 → T1002 → T1003 → T1004
                  ├────→ T1005
                  └────→ T1006 → T1007
T1002/T1003/T1004/T1005/T1006/T1007 → T1008
```

## P11：投资引擎装配区窗口溢出修复（2026-08-01 11:08 +0800）

> 分工：**Grok** 负责仓库内实现、测试和交付；**Codex** 仅负责外部研究输入，交付带来源与日期的 Markdown/JSON，不直接修改核心代码。

- [x] **T1101 [Grok] 建立溢出复现基线**
  - 在 1280×800、1024×768、768×1024、390×844 截图并记录 `document.scrollWidth > document.clientWidth`、装配台外框宽度和各滚动区宽度。
  - 伪代码：
    ```js
    for (const viewport of VIEWPORTS) {
      page.setViewportSize(viewport);
      assert(page.locator('body').evaluate(el => el.scrollWidth <= el.clientWidth));
      capture('engine-overflow-before-' + viewport.name);
    }
    ```

- [x] **T1102 [Grok] 修复 Grid 子项最小宽度与页面级横向溢出** ← T1101
  - 伪代码：
    ```css
    html, body { max-width:100%; overflow-x:clip; }
    .grid, .grid > *, .engine-main, .wrap, .assembly { min-width:0; max-width:100%; }
    .assembly, .dynamic-dashboard { box-sizing:border-box; overflow:hidden; }
    ```
  - 保留纵向页面滚动，不得隐藏内部时间线和报告内容。

- [x] **T1103 [Grok] 重排可用零件栏与数据上下文零件栏** ← T1102
  - 桌面端使用紧凑自适应卡片；卡片不足以展示时只在 `.parts-bank` 内滚动。
  - 保留 `draggable`、`data-id`、`data-kind`、`#source-library` 动态挂载点。
  - 伪代码：
    ```js
    const rail = document.querySelector('.parts-bank');
    rail.classList.toggle('is-overflowing', rail.scrollWidth > rail.clientWidth + 1);
    rail.setAttribute('aria-label', '可拖拽信息源零件，可横向滚动');
    ```

- [x] **T1104 [Grok] 约束主干道为内部滚动且保持完整端点** ← T1102
  - “信息入口 / Research Graph / Paper Portfolio”三类核心节点始终可见；中间已装配模块可横向滚动。
  - 禁止让 `road-track` 撑大 `.grid` 或浏览器 viewport；滚动区须支持鼠标、触摸、Shift+Wheel 和键盘焦点。

- [x] **T1105 [Grok] 增加溢出可发现性与移动端断点** ← T1103,T1104
  - 内部滚动区显示渐隐边缘、滚动条或“左右滑动查看零件”提示；滚动到底后提示自动消失。
  - 390px 下主干道允许横向滚动，动态驾驶舱 insight 卡片单列，左侧导航仍为抽屉。

- [x] **T1106 [Grok] 回归交互与无障碍测试** ← T1102–T1105
  - 验证拖入/删除/计数、Engine 创建/启动/取消、侧栏锚点、键盘焦点和 `prefers-reduced-motion`。
  - 新增 `src/frontend/tests/engine-overflow.test.js` 或等价测试，断言无页面级横向溢出、内部滚动区存在且核心节点可访问。

- [x] **T1107 [Grok] 视觉验收与交付记录** ← T1106
  - 输出 `research/engine-overflow-qa-20260801.md`，附四种视口截图、测量值、已知限制和回滚说明。
  - 不修改 Plaza、Agent Config、Data Intelligence 的布局或 API。

### 依赖关系

```text
T1101 → T1102 → T1103 → T1105
                 └────→ T1104 ──┘
T1105 → T1106 → T1107
```

## P12：Engine 多维股票判断面板（2026-08-01 12:47 +0800）

> 分工：**Grok** 负责仓库内实现、测试和交付；**Codex** 仅负责外部研究输入，交付带来源与日期的 Markdown/JSON，不直接修改核心代码。

- [x] **T1201 [Grok] 定义多维判断数据契约**
  - 在 Engine 事件/报告结构中增加 `judgment_dimensions[]` 和 `overall_judgment`，不得破坏现有事件字段。
  - 维度至少包含：`quant`、`analyst`、`consensus`、`valuation`、`growth`、`profitability`、`momentum`、`risk`、`eps_revision`、`liquidity`、`event_impact`。
  - 伪代码：
    ```ts
    type JudgmentDimension = {
      key: string; score: number|null; label: string; direction: 'up'|'down'|'flat'|'unknown';
      confidence: number; as_of: string; evidence_count: number;
      source_domains: string[]; rationale: string; state: 'ok'|'missing'|'conflict';
    };
    ```

- [x] **T1202 [Grok] 建立无未来信息的计算与降级逻辑** ← T1201
  - 只读取 `as_of` 之前的来源和模拟行情；fixture 模式必须生成可解释的演示矩阵，live 缺失时逐维降级。
  - 伪代码：
    ```js
    const evidence = docs.filter(d => d.published_at <= cutoff);
    const dim = scoreDimension(evidence, key, weights);
    return dim.evidence_count ? dim : {...dim, score:null, state:'missing', label:'暂无证据'};
    ```

- [x] **T1203 [Grok] 在 Engine 动态驾驶舱新增“评级摘要”区** ← T1201,T1202
  - 在 `#dynamic-dashboard` 内新增总判断、总分/置信度、更新时间、证据覆盖率及 3 个最强正向/反向信号。
  - 保留 `judgment-card`，将其升级为总判断摘要；不得移除现有计划、价值推演、风险门禁、纸面组合卡片。

- [x] **T1204 [Grok] 实现多维评级矩阵和分组 Tab** ← T1203
  - 分组：评级摘要、基本面、预期与修正、市场行为、风险与事件；桌面表格、窄屏卡片化。
  - 每行显示维度、分数、方向、置信度、证据数、`as_of` 和理由；点击可展开证据来源。
  - 不复制 Seeking Alpha 商标、文案、锁图标和专有样式。

- [x] **T1205 [Grok] 接入证据追溯与 Engine 事件互动** ← T1204
  - 维度行可定位到时间线事件和来源文档；运行中显示“待分析/分析中/已完成/证据不足”，进度由真实事件驱动。
  - 伪代码：
    ```js
    onEvent(e) {
      updateDimension(e.dimension, e.payload);
      setProgress(completedDimensions / totalDimensions);
      renderEvidenceLinks(evidenceIds, {asOf: cutoff});
    }
    ```

- [x] **T1206 [Grok] 无障碍、响应式和研究免责声明** ← T1204,T1205
  - Tab 使用键盘可达、`aria-selected`/`role=tablist` 完整；颜色之外提供方向文字和图标。
  - 390px 下矩阵转为纵向卡片，不产生页面级横向滚动；所有判断旁显示“研究/模拟，非投资建议”。

- [x] **T1207 [Grok] 契约、fixture、回归和视觉验收** ← T1201–T1206
  - 新增 `engine-judgment.test.js`：断言 11 个维度、缺失降级、as_of 过滤、事件更新、证据链接和无页面溢出。
  - fixture 至少覆盖：全量证据、部分缺失、冲突证据、运行中四种状态；输出四种视口截图与 `research/engine-judgment-qa-20260801.md`。
  - 不修改 Plaza、Agent Config、Data Intelligence 的既有 API 和布局。

### 依赖关系

```text
T1201 → T1202 → T1203 → T1204 → T1205 → T1206 → T1207
```

## P0 / P13：Data Intelligence 结论优先汇总与独到见解（2026-08-01 12:49 +0800）

> **优先级提升：核心交付阻断项。** 没有真实结论、热门分析和独到见解，`data-intelligence.html` 不得视为完成；方法步骤不能替代分析结果。

> 分工：**Grok** 负责仓库内实现、测试和交付；**Codex** 仅负责外部研究输入，交付带来源与日期的 Markdown/JSON，不直接修改核心代码。

- [x] **T1300 [Codex] 外部研究输入：结论优先汇总模式**
  - 完成：`research/data_intelligence_brief_patterns_20260801.md` 与 `.json`。
  - 包含 6 个公开来源、访问日期、RunBrief/Insight 契约、首屏层级、反模式和实现约束；未修改核心代码。

- [x] **T1301 [Grok] 定义结论摘要契约**
  - 为每次团队运行增加 `executive_summary`、`focus_items[]`、`hot_analysis[]`、`trending_news[]`、`distinctive_insights[]`、`evidence_limits[]`。
  - 伪代码：
    ```ts
    type Insight = { kind:'fact'|'analysis'|'inference'|'counter'; title:string; body:string;
      confidence:number; evidence_ids:string[]; source_domains:string[]; as_of:string; impact:string };
    type RunBrief = { headline:string; bullets:string[]; focus_items:Insight[]; hot_analysis:Insight[];
      trending_news:Insight[]; distinctive_insights:Insight[]; evidence_limits:string[] };
    ```

- [x] **T1302 [Grok] 生成结论而非方法描述** ← T1301
  - 从已抓取证据中先做去重、主题聚类和冲突检测，再输出一句话结论、证据链、行业/公司影响和反证。
  - 伪代码：
    ```js
    const claims = extractClaims(evidence);
    const ranked = rankBy(recency, sourceQuality, crossSourceSupport, impact);
    return buildBrief({headline: inferHeadline(ranked), bullets: topFindings(ranked),
      insights: separateFactAnalysisInferenceCounter(ranked)});
    ```
  - 禁止把“正在清洗/聚类/分析”作为首屏最终结论；这些只能出现在流程详情。

- [x] **T1303 [Grok] 实现 Data Intelligence 首屏 In Focus 与结论区** ← T1301,T1302
  - 在 `data-intelligence.html` 顶部新增横向 `In Focus` 条、核心结论卡、关键证据、影响映射、反证/不确定性卡。
  - 加入 `aria-live` 更新状态；Start 和 30 分钟 cron 完成后自动刷新，不需要手动重载。

- [x] **T1304 [Grok] 实现热门分析和趋势新闻列表** ← T1302,T1303
  - 热门分析按主题/证据数/影响排序；趋势新闻按新近度与变化方向排序，显示标题、摘要、来源域名、`as_of` 和证据数。
  - 复用 AI 60 秒与世界趋势的来源过滤，不引入硬编码新闻文本。

- [x] **T1305 [Grok] 增加独到见解卡与证据追溯** ← T1302,T1303
  - 每条独到见解必须至少有 2 个独立来源或明确标注“单一来源推断”；可展开事实 → 分析 → 推断 → 反证链。
  - 点击来源跳转历史文档/完整动态 HTML；显示证据不足、来源冲突和时间截点。

- [x] **T1306 [Grok] 连接两个团队的报告产物** ← T1303–T1305
  - AI 60 秒：输出钩子、事实核验、为什么重要、产业映射、风险反证。
  - 世界趋势：输出时间线、关键驱动、数据趋势、三情景摘要、市场传导。
  - 两套产物都必须把最终小结写入 `latest-summary`，而不是只写入 iframe。

- [x] **T1307 [Grok] 结论质量、降级与免责声明测试** ← T1301–T1306
  - fixture 覆盖：多来源一致、来源冲突、仅单来源、无新数据、RSS 失败；断言不会生成无证据的确定性结论。
  - 新增 `data-intelligence-brief.test.js`，验证首屏结论、来源链接、as_of、置信度、cron 刷新和移动端布局。
  - 输出 `research/data-intelligence-brief-qa-20260801.md`；所有结论保留“研究/模拟用途，非投资建议”。

### 依赖关系

```text
T1301 → T1302 → T1303 → T1304
                   └──→ T1305 → T1306 → T1307
```

## P14：完整动态 HTML 结果前置与 20 张分析卡验收（2026-08-01 13:16 +0800）

> 分工：**Grok** 负责仓库内实现、测试和交付；**Codex** 负责外部研究输入与结果契约，不直接修改核心代码。

- [x] **T1401 [Grok] 审计报告卡片数据绑定**
  - 对 `hugohe3.py` 的 20 张卡逐张建立 `card_id → source fields → rendered result` 映射。
  - 失败条件：卡片只有固定标题、方法说明或空占位符，没有 `report` 数据或明确 gap。

- [x] **T1402 [Grok] 将“编辑说明”升级为“编辑结论”** ← T1401
  - 首屏必须先出现 headline、关键发现、影响对象、置信度、证据数和 `as_of`。
  - 方法、数据口径和可追溯说明改为折叠区域；保留研究/模拟免责声明。

- [x] **T1403 [Grok] 让目录卡显示真实摘要与状态** ← T1401
  - `CONTENTS` 每项显示 `observed / inferred / gap / pending` 和一句话摘要；点击目录直达对应卡片。

- [x] **T1404 [Grok] 绑定并绘制 20 张结果卡** ← T1401,T1402,T1403
  - 至少覆盖：来源版图、信号比较、主题密度、来源结构、前三主题、来源排名、双轨地域、长尾、焦点信号、传导流、Pareto、证据枢纽、风险矩阵、下一步。
  - 所有数值来自 `report.analysis` / `report.citations` / `report.business_implications`；不允许硬编码演示数字。

- [x] **T1405 [Grok] 增加结论状态与数据缺口展示** ← T1404
  - 数据不足时显示“证据不足：缺少哪些来源/时间段/指标”，不得显示空白大卡或把方法当结论。
  - 每个 inference 卡显示至少一个支持证据和一个反证/限制；单一来源明确标注。

- [x] **T1406 [Grok] 完整报告视觉与交互验收** ← T1402–T1405
  - 验证报告查看器打开后在首屏即可看到分析结论；目录点击、上一张/下一张、20 张卡、图表、证据链接均可用。
  - 新增 `report-output-content.test.js`，断言 HTML 含真实 headline、结论摘要、至少 3 个结果卡、`as_of`、证据链接和缺口文本。
  - 输出 `research/report-output-content-qa-20260801.md`，附 fixture/full/partial evidence 三组截图。

### 依赖关系

```text
T1401 → T1402 → T1403 → T1404 → T1405 → T1406
```

## P15：交付验收清单（手工 + 自动化，2026-08-01）

> 目的：把 P9–P14 从「代码勾选」变成「可重复验收」。Grok 维护脚本与文档；人工完成浏览器清单后勾 T1503。

- [x] **T1501 [Grok] 自动化验收脚本与 Make 目标**
  - `scripts/accept_p15.sh`：后端烟测 + P9/P13 单测 + 前端烟测 + P10–P14 契约测
  - `make test-accept-p15`；可选 `ACCEPT_LIVE=1` 探测 `:8080` health / latest-summary / team-run 202
  - DoD：本地一键可红可绿；失败套件名称清晰

- [x] **T1502 [Grok] 手工验收清单文档**
  - `research/p15-acceptance-checklist.md`：DI 结论无 URL、Engine 无页级横滚、异步 run、原页面保护
  - DoD：清单可打印签字；含已知边界（不记 fail）

- [x] **T1503 [Grok/人工] 执行并记录一轮完整验收**
  - 完成：`ACCEPT_LIVE=1 make test-accept-p15` 5/5；扩展探针 12/12（health/pages/summary/202 run/events/engine+DI 契约）
  - 记录：`research/p15-acceptance-checklist.md` §D
  - 验收中修复：补回 DI `#executive-brief` 节点

- [x] **T1504 [Grok] 将 P15 门禁写入基线说明**
  - `docs/test-baseline.md` 增加 accept-p15 命令与范围
  - DoD：新人只读基线即可复跑

### 依赖关系

```text
T1501 → T1502 → T1503
T1501 → T1504
```
