# Investment Engine Live Cockpit：Grok 执行规划与 TODO

> 版本：vNext-1 · 2026-08-01
>
> 责任约定：`[Grok]` 负责仓库内实现、测试和交付；`[Codex]` 只负责外部研究输入，交付带来源和日期的 Markdown/JSON，不直接修改核心代码。
>
> 本文件是对当前 `/investment-engine.html` 的下一阶段开发计划。当前页面已经有装配台和模拟 API，但启动按钮处于“创建模拟后才启用”的隐藏式状态；本轮目标是让用户一进入页面就能理解并启动一辆“信息驱动的投资研究车”。

## 0. 产品契约（先冻结，再编码）

### 0.1 用户看到的主流程

```text
进入投资引擎
  → 选择 ticker / 截止日期 / 初始资金
  → 将信息源团队、动态 HTML、事件时钟拖进横向主干道
  → 点击「创建并启动 Engine」
  → Engine Live Journey 开始行驶
  → 逐步生成上下文、判断、规划、营收/价值推演、风险门禁、纸面成交
  → 形成报告、决策引用、Paper Portfolio 和可恢复运行记录
```

### 0.2 必须明确的词义

- “营收/价值推演”只表示模拟组合的价值路径、现金变化和 Paper P&L，不代表上市公司的真实营收。
- 所有卡片固定显示“研究/模拟用途，不构成投资建议，不连接真实券商”。
- 用户拖入的是“上下文模块”，不是直接修改 TradingAgents 内部 graph；适配器根据装配快照选择来源和文档。
- 原有 Plaza、Agent Config、7 个旧页面和四支运行时团队不改行为。

## 1. P0：启动入口与状态机

### T801 [Grok] 把启动入口变成主操作

**目标**：用户无需先猜“创建模拟”再找“启动”，页面主舞台必须有明确的 `Start Engine`。

实现要求：

1. 主舞台标题区增加 `btn-engine-start`，文案为“创建并启动 Engine”。
2. 左侧保留 `btn-create`、`btn-start` 作为高级/兼容入口，但两者状态必须同步。
3. 未通过配置校验时，主按钮显示“检查配置”，点击后展示具体字段错误。
4. 创建完成后主按钮变为“继续启动”，不得要求用户滚动到左侧。
5. 运行中变为“Engine 行驶中”，禁用重复启动；完成后变为“重新运行”。
6. 启动前至少需要合法 ticker、日期、初始资金；信息源可以为空，但必须显示“将使用默认上下文”。

伪代码：

```javascript
function deriveStartState(form, run) {
  const errors = validateEngineForm(form)
  if (errors.length) return { label: '检查配置', action: 'validate', disabled: false }
  if (!run) return { label: '创建并启动 Engine', action: 'create_start', disabled: false }
  if (run.status === 'queued') return { label: '继续启动', action: 'start', disabled: false }
  if (run.status === 'running') return { label: 'Engine 行驶中', action: 'none', disabled: true }
  if (run.status === 'completed') return { label: '重新运行', action: 'rerun', disabled: false }
  return { label: '重试 Engine', action: 'retry', disabled: false }
}

async function onPrimaryStart() {
  const form = readEngineForm()
  const errors = validateEngineForm(form)
  if (errors.length) return showValidation(errors)
  if (!state.runId || ['completed', 'failed', 'cancelled'].includes(state.status)) {
    const run = await createSimulation(form)
    state.runId = run.run_id
  }
  await startSimulation(state.runId)
  beginLiveJourney()
}
```

DoD：

- 首屏 3 秒内能看到主启动按钮；
- 点击一次即可从“无 run”进入 `running`；
- `queued/running/completed/failed/cancelled` 五种状态都有可见文案和可操作按钮；
- 旧的 create/start/cancel API 测试全部通过。

### T802 [Grok] 定义 Engine 状态机和前端单一状态源

新增 `engineState`，禁止从多个 DOM 文案推断状态：

```javascript
const engineState = {
  runId: null,
  status: 'idle',
  phase: 'assembly',
  progress: 0,
  currentNode: null,
  assembly: { modules: [], snapshotHash: null },
  events: [],
  insights: {
    context: null,
    judgment: null,
    plan: null,
    valuePath: null,
    risk: null,
    portfolio: null,
  },
  lastSeq: 0,
  error: null,
}
```

DoD：刷新页面可从 API 恢复相同状态；页面上的按钮、路线、卡片、时间线全部由 `engineState` 渲染。

## 2. P0：装配快照与主干道编译

### T811 [Grok] 固化模块数据契约

模块统一为：

```json
{
  "module_id": "team:ai_news_60s",
  "kind": "team|source|document|market|engine",
  "name": "60 秒 AI 信息团队",
  "enabled": true,
  "priority": 1,
  "config": { "channel": "ai_news_60s", "window_minutes": 1440 }
}
```

后端保存为 `assembly_snapshot`，模拟运行只读取快照，不读取用户后来修改的草稿。

### T812 [Grok] 实现装配校验和编译器

伪代码：

```python
def compile_assembly(modules, ticker, cutoff):
    ordered = sorted([m for m in modules if m["enabled"]], key=lambda x: x["priority"])
    channels, documents, source_ids = [], [], []
    for module in ordered:
        if module["kind"] == "team":
            channels.append(TEAM_CHANNELS[module["module_id"]])
        elif module["kind"] == "document":
            documents.append(module["module_id"])
        elif module["kind"] == "source":
            source_ids.append(module["module_id"])
    return AssemblyPlan(
        ticker=ticker,
        cutoff=cutoff,
        channels=dedupe(channels),
        document_ids=documents,
        source_ids=source_ids,
        module_order=[m["module_id"] for m in ordered],
    )
```

DoD：至少拖入一个团队或来源时，运行快照里有可读的 `module_order`、频道和 cutoff；未来文档不会被编译进去。

### T813 [Grok] 完善拖拽交互

- 支持鼠标拖拽、键盘添加/删除和移动端“点击添加”；
- 主干道明确显示入口、研究图、风险门禁和 Paper Portfolio；
- 模块进入主干道后显示序号、类型、来源状态和删除按钮；
- 拖入非法/停用来源时给出原因，不静默丢弃；
- localStorage 只保存草稿，真正运行以服务器返回的快照为准。

## 3. P1：动态事件协议与运行时

### T821 [Grok] 扩展投资事件模型

每个事件必须包含：

```json
{
  "run_id": "abc123",
  "seq": 17,
  "phase": "analysis|debate|planning|risk|trading|portfolio|reflection",
  "node": "news_analyst",
  "participant": "News Analyst",
  "status": "started|progress|completed|failed",
  "content": "安全摘要文本",
  "structured": {
    "claim": "...",
    "confidence": 0.62,
    "evidence_ids": ["..."],
    "assumptions": ["..."]
  },
  "evidence": [],
  "ts": "..."
}
```

### T822 [Grok] 增加 SSE，保留轮询 fallback

优先新增：

```text
GET /api/v1/investment-simulations/{run_id}/events/stream?after_seq=0
```

要求：

- SSE 断线自动用现有 `/events?after_seq=` 补齐；
- 事件按 `seq` 去重；
- 断线、重连、完成、失败都显示在驾驶舱；
- 不修改 Plaza SSE。

伪代码：

```javascript
function connectJourney(runId) {
  const stream = new EventSource(`/api/v1/investment-simulations/${runId}/events/stream`)
  stream.onmessage = ({ data }) => appendEvent(JSON.parse(data))
  stream.onerror = () => {
    stream.close()
    pollMissingEvents(runId, engineState.lastSeq).finally(() => retryBackoff(connectJourney))
  }
}
```

### T823 [Grok] Fixture 逐阶段事件生成器

Fixture 不应只输出模板句子；每个阶段至少生成一条可解释的结构化内容：

```python
async def fixture_journey(plan):
    yield event("context", "source_loader", "progress", context_summary(plan))
    yield event("analysis", "market_analyst", "completed", judgment(plan))
    yield event("analysis", "news_analyst", "completed", news_signal(plan))
    yield event("debate", "bull_researcher", "completed", bull_case(plan))
    yield event("debate", "bear_researcher", "completed", bear_case(plan))
    yield event("planning", "research_manager", "completed", route_plan(plan))
    yield event("trading", "trader", "completed", paper_trade_plan(plan))
    yield event("risk", "neutral_risk", "completed", risk_gate(plan))
    yield event("portfolio", "portfolio_manager", "completed", final_decision(plan))
    yield event("reflection", "engine", "completed", post_run_reflection(plan))
```

每个事件之间只在 fixture 模式增加可控演示延迟；live 模式不人为阻塞。

## 4. P1：动态 HTML 驾驶舱

### T831 [Grok] 实现 Engine Live Journey 组件树

页面必须有以下动态区域：

```text
Engine Live Journey
├── HUD：状态、当前阶段、进度、运行 ID、连接状态
├── Journey Route：上下文 → 判断 → 规划 → 风险 → 纸面成交
├── Judgment Card：当前事实、信号、置信度、证据
├── Planning Card：目标、假设、计划路径、触发条件
├── Value Path Card：模拟价格/现金/持仓/盈亏路径
├── Risk Gate Card：风险节点、反证、否决原因
├── Portfolio Card：订单生命周期、现金、持仓、P&L
├── Evidence Card：来源、版本、as_of、hash
└── Live Timeline：逐事件日志
```

### T832 [Grok] 实现事件到卡片的 reducer

```javascript
function reduceJourney(state, event) {
  const next = structuredClone(state)
  next.lastSeq = Math.max(next.lastSeq, event.seq)
  next.events.push(event)
  next.phase = phaseFor(event)
  next.currentNode = event.node
  next.progress = progressFrom(next.events, next.graphShape)
  if (event.phase === 'analysis') next.insights.judgment = normalizeClaim(event)
  if (event.phase === 'debate' || event.phase === 'planning') next.insights.plan = normalizePlan(event)
  if (event.phase === 'trading') next.insights.valuePath = normalizeValuePath(event)
  if (event.phase === 'risk') next.insights.risk = normalizeRisk(event)
  if (event.phase === 'portfolio') next.insights.portfolio = normalizePortfolio(event)
  next.insights.context = mergeEvidence(next.insights.context, event.evidence)
  return next
}
```

### T833 [Grok] 动态内容安全与可读性

- Agent 输出一律作为文本或经过白名单 Markdown 渲染；禁止直接把原始 HTML 拼进页面；
- URL 使用 allowlist/安全链接组件；
- 卡片必须有空状态、加载状态、失败状态、重连状态；
- 桌面端显示完整路线，移动端改为垂直路线；
- 每张卡显示“事实/分析/推断/模拟”标签和时间戳。

## 5. P1：判断、规划、营收/价值推演

### T841 [Grok] 判断层

输入：信息团队文档、来源证据、ticker、cutoff。

输出：

```json
{
  "claim": "研究用判断",
  "direction": "bullish|neutral|bearish",
  "confidence": 0.0,
  "drivers": [],
  "counterpoints": [],
  "evidence_ids": [],
  "label": "analysis"
}
```

### T842 [Grok] 规划层

规划不是直接下单，而是形成“如果/那么”路线：

```json
{
  "objective": "研究模拟目标",
  "base_case": { "trigger": [], "action": "HOLD", "allocation": 0.0 },
  "bull_case": { "trigger": [], "action": "BUY", "allocation": 0.0 },
  "bear_case": { "trigger": [], "action": "REDUCE", "allocation": 0.0 },
  "invalidations": [],
  "label": "simulation"
}
```

### T843 [Grok] 价值/营收推演层

明确使用 Paper Portfolio，不声称预测真实公司营收：

```python
def project_value_path(portfolio, plan, price_path):
    rows = []
    for point in price_path:
        portfolio = paper_mark_to_market(portfolio, point.price)
        rows.append({
            "ts": point.ts,
            "price": point.price,
            "cash": portfolio.cash,
            "equity": portfolio.total_equity,
            "pnl": portfolio.total_equity - portfolio.initial_cash,
            "label": "simulation",
        })
    return rows
```

驾驶舱必须同时显示：现金、持仓、模拟权益、已实现盈亏、未实现盈亏、最大回撤占位和数据截止时间。

### T844 [Grok] 风险门禁与订单生命周期

```text
planning
  → pre_trade_risk_check
  → approved / reduced / rejected
  → paper_order_created
  → simulated_fill
  → portfolio_marked
```

每个门禁事件必须写明：触发条件、否决/缩减原因、引用证据、是否进入 Paper Portfolio。

## 6. P2：持久化、恢复和错误

### T851 [Grok] 保存不可变运行快照

运行创建时保存：

- `assembly_snapshot`；
- `engine_config_snapshot`；
- 模型和 provider 标识（不保存明文 API Key）；
- `graph_shape` 与 adapter 版本；
- 数据 cutoff 与文档版本；
- 初始资金和 Paper Portfolio 初始状态。

### T852 [Grok] 页面刷新和断线恢复

```javascript
async function restoreJourney(runId) {
  const run = await api.get(`/investment-simulations/${runId}`)
  const events = await api.get(`/investment-simulations/${runId}/events?after_seq=0`)
  const reports = await api.get(`/investment-simulations/${runId}/reports`)
  const portfolio = await api.get(`/investment-simulations/${runId}/portfolio`)
  engineState = hydrate(run, events, reports, portfolio)
  renderAll(engineState)
}
```

### T853 [Grok] 失败与取消

- 取消后停止新节点，但保留已产生事件和组合状态；
- provider 错误显示在哪个 Agent、哪个 phase、哪个模块失败；
- 超预算产生 `budget_guard` 事件并停止下一节点；
- 页面提供“重试本阶段”和“从头新建”两个不同动作。

## 7. P2：测试 TODO

### T861 [Grok] 前端契约测试

- 首屏存在并可见 `btn-engine-start`；
- 五种运行状态对应按钮文案；
- 拖入团队后 `assembly_snapshot` 请求包含 `kind=team`；
- 事件 reducer 正确更新六类卡片；
- 事件乱序/重复/断线补齐不会重复渲染；
- 刷新后按 `lastSeq` 恢复；
- 不可信 HTML 不会注入 DOM。

### T862 [Grok] 后端测试

- 事件 schema 校验；
- SSE 与轮询一致性；
- fixture 事件顺序和阶段完整性；
- cutoff 防未来信息；
- assembly snapshot 不可变；
- 取消、失败、预算耗尽、恢复；
- Paper Portfolio P&L 与事件引用一致。

### T863 [Grok] 端到端验收

```text
登录
→ Agent Config 选择模型
→ 数据采集页发布 AI/世界趋势文档
→ 投资引擎拖入两个团队和动态 HTML
→ 点击「创建并启动 Engine」
→ 观察至少 5 个阶段动态变化
→ 风险门禁完成
→ Paper Portfolio 产生结果
→ 刷新页面仍能恢复
→ 取消一次运行并检查事件保留
```

## 8. 完成顺序和提交边界

```text
T801/T802
  → T811/T812/T813
  → T821/T822/T823
  → T831/T832/T833
  → T841/T842/T843/T844
  → T851/T852/T853
  → T861/T862/T863
```

建议提交：

```text
1. feat(engine-ui): visible primary start action and state machine
2. feat(engine-assembly): immutable module snapshot and compiler
3. feat(engine-events): structured event schema and SSE fallback
4. feat(engine-cockpit): live journey dynamic HTML cards
5. feat(engine-simulation): judgment/plan/value/risk/portfolio reducers
6. test(engine): recovery, security, fixture and E2E acceptance
```

## 9. 最终 DoD

- 用户进入页面能立即看到主启动按钮；
- 一次点击能启动 Engine，而不是先猜创建/启动顺序；
- 引擎运行过程中至少有五个阶段可观察地发生变化；
- 判断、规划、价值推演、风险和 Paper Portfolio 都来自事件流，不是静态占位文本；
- 装配模块、文档版本、cutoff、模型和事件均可追溯；
- 刷新、断线、取消、失败和重试行为可解释；
- 研究/模拟免责声明始终可见；
- 原有 7 个页面、Plaza、Agent Config、Build System、AI Coding 和四支运行时团队回归全绿。
