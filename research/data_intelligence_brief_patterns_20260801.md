# Data Intelligence 结论优先汇总模式

- 研究日期：2026-08-01（Asia/Shanghai）
- 交付角色：Codex（外部研究输入）
- 目标消费者：Grok（仓库内实现 P13 / T1301–T1307）
- 适用页面：`src/frontend/data-intelligence.html`

## 结论

Data Intelligence 首屏应先回答“这批信息说明了什么”，再展开“Agent 如何得到这个结论”。推荐采用四层信息层级：

1. **结论层**：一句话 headline、3 条关键发现、影响对象、方向和置信度。
2. **信号层**：In Focus、热门分析、趋势新闻、主题聚类和变化方向。
3. **证据层**：来源域名、发布时间、`as_of`、证据数、引用链接、冲突和反证。
4. **过程层**：采集、清洗、核验、聚类、市场映射等 Agent 运行步骤。

过程层不应占据首屏结论的位置；它是可展开的解释和可追溯依据。

## 可落地的 UI / 内容模式

### 1. In Focus 横向重点条

顶部展示 3–5 个当前最重要的标题，每项包含频道、变化方向、时间和点击后的证据定位。横向滚动只发生在条内，不撑破页面。

### 2. 结论卡片

每张卡至少包含：`标题`、`事实/分析/推断`标签、`why it matters`、影响行业/公司、置信度、证据数、`as_of` 和“查看证据”。

### 3. 热门分析与趋势新闻

热门分析按主题支持度、跨来源数量、影响分排序；趋势新闻按新近度、变化方向和影响分排序。不要只按抓取顺序展示。

### 4. 独到见解

独到见解必须是跨来源组合后的推断。至少显示“支持证据”和“反证/限制”；只有单一来源时明确标注“单一来源推断”，不能使用确定性措辞。

### 5. 渐进披露

首屏展示简洁结论；点击卡片后展开事实 → 分析 → 推断 → 反证链，并定位到历史文档或完整动态 HTML。这样既保持信息密度，也不牺牲可审计性。

## 对 StockAgents 的具体决策

- `latest-summary` 不应只显示版本和打开链接，应渲染 `RunBrief` 的 headline、bullets、confidence 和 evidence limits。
- AI 60 秒团队的结论卡固定为：钩子、事实核验、为什么重要、产业映射、风险反证。
- 独夫之心团队的结论卡固定为：时间线、关键驱动、数据趋势、三情景摘要、市场传导。
- 运行状态仍保留在“研究流程”Tab；完成后将结论层提升到团队 Tab 的首屏。
- 无新数据、证据冲突或时效不足时显示“暂无可确认结论”，而不是回退到方法描述。
- 页面所有输出需保留“研究/模拟用途，非投资建议”。

## 反模式

- 只显示“正在采集/清洗/聚类/分析”，没有回答结果。
- 只有一个总分，没有来源、时间截点和理由。
- 用固定新闻文本冒充动态数据。
- 证据不足时生成“确定上涨/确定下跌”等投资建议式措辞。
- 将全部原始 HTML 塞进首屏，导致用户找不到摘要。

## 外部来源（访问日期均为 2026-08-01）

1. Google Analytics Help，报告以卡片承载指标并允许调整维度/可视化与仪表板布局：<https://support.google.com/analytics/answer/9925281?hl=en>
2. Material Design Cards，建议用 dashboard-style card collection 在同一屏承载多个主题/功能：<https://m2.material.io/components/cards/android>
3. Evidence Docs，将数据产品定义为报告、决策支持工具和嵌入式仪表板，强调从数据到可读交付：<https://docs.evidence.dev/>
4. Data Provenance Initiative，强调从源数据到部署使用的 provenance 记录：<https://www.dataprovenance.org/>
5. Google Data Cards Playbook，提供数据集概览、范围、快照、内容描述和可追溯结构：<https://sites.research.google/datacardsplaybook/activities/assemble-template.pdf>
6. Nielsen Norman Group Site Map Usability，强调信息层级应限制在能清晰展示的深度，并在必要时使用 progressive disclosure：<https://s3.amazonaws.com/media.nngroup.com/media/reports/free/Site_Map_Usability_2nd_Edition.pdf>

## 给 Grok 的实现提示

先实现 `RunBrief` 数据模型和 fixture，再实现首屏结论组件，最后接入真实运行事件。不要先堆更多“分析步骤”卡片；每增加一个过程卡，都必须能回链到一个结论或证据。
