# 研究工作台设计说明

本页是 `/data-intelligence.html` 的交互与输出契约。实现吸收三个公开项目的可迁移模式，但不复制其代码或视觉素材：

- [Horizon](https://github.com/Thysrael/Horizon)：来源配置、并发采集、去重/评分、背景补全、双语摘要和定时发布形成完整雷达流水线。
- [Open Researcher](https://github.com/firecrawl/open-researcher)：实时思考/步骤流、聊天与搜索结果分栏、自动引用。
- [ppt-master](https://github.com/hugohe3/ppt-master)：模板化叙事、数据图表、16:9 版式与可复用的演示结构；独夫之心报告当前先输出安全 HTML，后续可接 PPTX 导出。

## 页面怎么用

1. “添加信息源”Tab 注册 Fixture、RSS、网页或 JSON API 来源；右侧“RSS 目录导入助手”支持直接贴 GitHub RSS 列表、OPML 或目录页 URL，先解析、去重，再按需校验前 20 条，最后由用户确认批量添加；左侧“来源库”再选择已启用来源，Fixture 可离线演示。
2. 左侧“定时任务”填写团队、间隔和来源，可选择创建后立即执行；任务持久化后由后端 worker 到期执行。
3. 中间“研究流程”显示采集、去重、Agent 分析和发布步骤；运行失败只显示在本次运行，不隐藏其他来源。
4. `AI 60 秒` 现在是顶部独立主菜单；顶部展示该团队成员，点击 `Start` 或等待 Cron 后，成员状态会按流水线推进，六个信息盒逐个填充。AI60 团队额外执行主题聚类、信号评分、证据综合、业务影响链和反证检查，随后在动态 HTML 中显示研判驾驶舱与完整的 20 卡深度研究报告。
5. `世界趋势` tab 使用同样的团队控制条，但输出为 16:9 深色故事板与同一套 20 卡研究语法：时间线、驱动、数据趋势、反证、三情景和市场传导会分别落入可追溯的图表/数据卡。
6. 页面每 20 秒轮询定时任务与最新文档；因此后台 Cron 完成后，打开的 tab 无需手动刷新即可看到最新盒子和动态 HTML。右侧还显示最近运行状态；“历史文档”可按频道查看不可变版本。

## 定时任务 API

```text
GET    /api/v1/information-schedules
POST   /api/v1/information-schedules
PATCH  /api/v1/information-schedules/{schedule_id}
DELETE /api/v1/information-schedules/{schedule_id}
POST   /api/v1/information-schedules/{schedule_id}/run
```

`interval_minutes` 范围为 1–10080；只允许 `ai_news_60s` 和 `dufu_world_intel`。任务状态包含 `next_run_at`、`last_status`、`last_error`、`run_count`，用于页面轮询和排障。

默认间隔为 **30 分钟**。全新安装会自动创建一个启用的“AI 60 秒每 30 分钟播报” Fixture 任务；它可以在左侧暂停、改频率或删除。已有任务保留用户已配置的频率。

## 20 卡研究报告

每次新运行都会生成一套深色数据新闻风格的卡组：封面、编辑说明、方法、证据版图、来源脉冲、双端比较、主题气泡、来源环图、Top-3、来源排名、双轨/长尾、焦点信号、传导流图、Pareto、证据枢纽、不确定性、跨期代理、风险四象限与收束页。

该语法参考 [ppt-master 的全局 AI 资本格局示例](https://github.com/hugohe3/ppt-master/tree/main/examples/ppt169_global_ai_capital_2026) 的叙事和图表分工；它不复制原项目素材或数据。所有卡片都显示为“已观察 / 推断 / 研究缺口”之一：缺少可对齐的实体、单位、期间或一手数值时，卡片会明确交给 Scout、Checker、Data Analyst 或 Market Mapper 补齐，绝不以虚构估值、营收或 Capex 占位。

## 输出边界

报告只用于研究和模拟，不连接真实券商，也不输出买入/卖出/目标价。图形表达信息关系，不表达交易信号；所有结论必须携带来源、抓取时间、运行 ID 和不确定性。
