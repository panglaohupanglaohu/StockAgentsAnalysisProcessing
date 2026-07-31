# Agent 团队

## 必须保留的团队

`build_system` 与 `ai_coding` 必须在所有重构阶段正常加载。其他现有 factory 和持久化团队继续遵循原逻辑。磁盘已存在的团队配置优先于 factory 默认值，升级不得覆盖用户修改。

## `ai_news_60s`

目标是产出高密度、可核验的 AI 信息播报页面。建议角色：Lead、Scout、Checker、Market Mapper、Editor、Publisher。

质量门禁：

- 每条事实至少一个可访问来源，重要事实尽量交叉验证。
- 区分事件发生时间、来源发布时间和抓取时间。
- 明确事实、分析、推断和不确定性。
- 页面保留长版内容，60 秒版本只是摘要层。

## `dufu_world_intel`

目标是从公开多语言来源建立世界趋势时间线、因果链、反证和市场传导路径。建议角色：Lead、Web Collector、Data Engineer、Data Analyst、Red Team、Market Mapper、Presenter。

质量门禁：

- 数据清理和实体对齐可重复执行。
- 图表显示数据截止时间、单位、样本范围和来源。
- Red Team 的反证不得被编辑阶段静默删除。
- 乐观、基准、悲观情景必须写出触发条件，而非只给结论。

完整角色、Skills、Tools 和伪代码见 [PLAN.md](../PLAN.md) 与 [TODOS.md](../TODOS.md)。
