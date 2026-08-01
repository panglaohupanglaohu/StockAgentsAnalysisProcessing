# StockAgents

StockAgents 是一个以 Agent 团队为核心的市场情报与股票投资**模拟**平台。项目完整保留原有 AgentsGroup 七个业务页面及其前后端能力，并新增：

1. **数据采集/分析**（`/data-intelligence.html`）
2. **投资引擎**（`/investment-engine.html`）

数据采集页内置 RSS 目录 Chat：粘贴 GitHub RSS 列表、OPML 或目录页后，系统会解析表格/链接、去重、按需校验前 20 条，待用户确认后批量写入来源库，并可指定 60 秒 AI、独夫之心或两支团队。

两支信息团队的新报告使用 20 卡深度研究语法：从来源覆盖、主题/信号、比较、传导、风险到下一轮研究缺口，所有卡片都标明“已观察 / 推断 / 待补”，不会用虚构财务数字填图。默认 Cron 间隔为 **30 分钟**；“AI 60 秒”保留的是播报栏目名称，而不是刷新频率。

> 状态：核心重构链路已落地（见 [TODOS.md](TODOS.md)）。Codex 外部研究任务（来源目录、格式样本审计）已交付于 [`research/`](research/README.md)，不阻塞本仓库运行。

**免责声明：全部输出仅供研究与模拟，不构成投资建议；Paper Portfolio 永不连接真实券商。**

## 产品流程

```text
登录（StockAgents 品牌文案）
  → Agent Config（默认跳转）
  → 七个原业务页面（完整保留）
  → 数据采集/分析：运行 ai_news_60s / dufu_world_intel → 版本化动态 HTML
  → 投资引擎：fixture 或 TradingAgents 模拟 → 事件流 + Paper Portfolio
```

### 原页面保护面（不得删除/改写）

| 页面 | 路径 |
| --- | --- |
| 智能体团队 | `/agent-team-config.html` |
| 议事广场 | `/plaza.html` |
| 技能萃取 | `/skill-extract.html` |
| Agent 记忆 | `/agent-memory.html` |
| 数字孪生 Office | `/Agent-digital-twin.html?office3d=1` |
| Token 节省 | `/cost-dashboard.html` |
| 生态配置 | `/pet-config.html` |

全局导航**只追加**「数据采集/分析」「投资引擎」两个入口。

## 团队

| 团队 | 状态 | 说明 |
| --- | --- | --- |
| `build_system` | 既有 | 启动强制项；磁盘优先于 factory |
| `ai_coding` | 既有 | 启动强制项 |
| `ai_news_60s` | factory + DAG | 6 Agent；证据综合、信号评分、业务影响分析、反证与动态研判驾驶舱 |
| `dufu_world_intel` | factory + DAG | 7 Agent；含 Red Team / hugohe3 Presenter |

运行时团队白名单固定为以上四支；历史团队记录会在启动时清理，不会出现在 Agent Config 下拉框。

## 投资运行时

- 主适配：[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) **v0.3.1** / commit **`01477f9`**（Apache-2.0）
- 可选安装：`python -m pip install -e '.[trading]'`
- 未安装时：`GET /api/v1/trading-runtime/health` → `trading_runtime=unavailable`，原系统仍可启动
- 默认模拟模式：`mode=fixture`（离线确定性 graph，无需外部 API Key）
- 版本检查：仅提示新 release，**永不自动升级**

## 快速开始

环境：Python 3.11+、Node.js 20+。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
cp .env.example .env

cd src/backend
python main.py --port 8080
```

打开 `http://127.0.0.1:8080/login.html`。

前端测试：

```bash
npm ci
npm run test:frontend
```

核心保护烟测：

```bash
make test-smoke
```

全量：`make test`（已知遗留失败见 [docs/test-baseline.md](docs/test-baseline.md)）。

## 主要 API（新增）

```text
GET  /api/v1/trading-runtime/health
GET  /api/v1/trading-runtime/config-schema
POST /api/v1/trading-runtime/config/validate

GET/POST /api/v1/information-sources
POST     /api/v1/information-sources/import-directory/preview
POST     /api/v1/information-sources/import-directory/commit
POST     /api/v1/information-sources/{id}/test
POST     /api/v1/information-sources/teams/{team_id}/run
GET/POST /api/v1/information-schedules
PATCH/DELETE /api/v1/information-schedules/{schedule_id}
POST     /api/v1/information-schedules/{schedule_id}/run

GET  /api/v1/information-documents
GET  /api/v1/information-documents/latest/{channel}

GET/POST /api/v1/investment-simulations
POST     /api/v1/investment-simulations/{run_id}/start
POST     /api/v1/investment-simulations/{run_id}/cancel
GET      /api/v1/investment-simulations/{run_id}/events
GET      /api/v1/investment-simulations/{run_id}/reports
GET      /api/v1/investment-simulations/{run_id}/portfolio
```

投资事件流**独立于 Plaza**，不修改 Plaza API/SSE。

数据采集/分析工作台的交互说明见 [docs/research-workbench.md](docs/research-workbench.md)。

## 仓库结构（增量）

```text
src/backend/
  agents/teams/ai_news_60s_team.py
  agents/teams/dufu_world_intel_team.py
  agents/skills/information_skills.py
  agents/startup_health.py
  domain/information_sources/   # connectors, evidence, hugohe3, pipelines
  domain/investment_simulation/ # simulation store, portfolio, orchestrator
  domain/api_routes.py
  integrations/tradingagents/   # pin probe, mapper, graph adapter
src/frontend/
  data-intelligence.html
  investment-engine.html
  js/data-intelligence.js
  js/investment-engine.js
```

## 安全要点

- 信息源 SSRF：拒绝 loopback/私网/元数据/凭据 URL；重定向再校验
- 密钥仅 `env:VAR` 引用；不落浏览器明文
- hugohe3：无 `<script>` / 行内事件 / `javascript:`；引用 URL 必须出现在 HTML
- 历史模拟 `as_of` 截止：禁止注入未来文档
- ticker 校验；目录穿越类 ticker 拒绝

## 协作

- **Grok**：仓库实现、测试、交付（本 README 描述范围）
- **Codex**：外部研究（T105/T106/T202/T606 等），交付带日期的 Markdown/JSON

详见 [CONTRIBUTING.md](CONTRIBUTING.md)、[SECURITY.md](SECURITY.md)、[PLAN.md](PLAN.md)、[TODOS.md](TODOS.md)。

## 许可证

项目许可证待维护者选定。第三方见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
