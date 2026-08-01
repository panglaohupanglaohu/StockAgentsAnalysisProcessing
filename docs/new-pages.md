# 两个新页面

本轮前端只允许新增两个顶层页面。动态报告、来源目录、运行时间线等都作为这两个页面的内部视图，不再拆分更多 HTML 页面。

## 1. `/data-intelligence.html` — 数据采集/分析

内部视图：

- 信息源目录与任意数量来源的启停、排序、配置；
- 独立“添加信息源”Tab：Fixture、RSS、网页、JSON API、options JSON 和环境变量引用；
- RSS 目录导入 Chat：粘贴目录 URL 后解析表格/Markdown/OPML，去重、可选健康检查，确认后批量加入来源库，并可指定 60 秒 AI、独夫之心或两者；
- 来源健康、调度、运行队列和错误隔离；
- `ai_news_60s` 团队运行、版本化结果和动态 HTML；
- `dufu_world_intel` 团队运行、数据分析、版本化结果和动态 HTML；
- 来源证据、抓取时间、内容 hash、运行 ID 和历史版本。

页面只调用新的 `/api/v1/information-sources` 与 `/api/v1/information-documents` API，不改写原页面 API。

## 2. `/investment-engine.html` — 投资引擎

内部视图：

- 行业板块、股票/ETF 标的、日期、初始资金和 Agent Config 现有模型的选择；
- 横向主干道式装配画布：60 秒 AI 团队、独夫之心团队、动态 HTML、事件时钟和可插拔来源作为上下游零件拖入、移除、排序并写入配置快照；
- Engine Live Journey 动态 HTML 驾驶舱：运行时沿信息上下文、判断、规划、风险门禁、纸面成交路线推进，实时填充判断、规划、价值推演、风险、组合和证据卡；
- TradingAgents 分析师、多空辩论、风险辩论和 Portfolio Manager 时间线；
- 报告、证据、最终模拟决定、Paper Portfolio、成本和 checkpoint；
- 启动、暂停、取消、恢复与错误诊断。

页面只调用新的 `/api/v1/trading-runtime` 与 `/api/v1/investment-simulations` API。它不创建 Plaza discussion，不修改 Plaza SSE 或 3D 场景。

## 导航规则

现有 7 个导航项保持顺序、地址与行为；在其后只追加：

```javascript
{ id: 'data-intelligence', label: '数据采集/分析', href: '/data-intelligence.html' }
{ id: 'investment-engine', label: '投资引擎', href: '/investment-engine.html' }
```

如果旧页面存在多套导航实现，Grok 应先增加共享导航契约测试，再以最小改动追加相同两个入口；不得借机迁移或重写旧页面。
