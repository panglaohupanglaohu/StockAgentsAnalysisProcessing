# P15 验收清单（手工 + 自动化）

- **日期：** 2026-08-01
- **范围：** P9–P14 落地后的回归与产品验收
- **原则：** 自动化可 CI；手工覆盖视觉/交互；失败项必须可复现

## A. 自动化（CI / 本地一键）

```bash
# 推荐
make test-accept-p15

# 或
./scripts/accept_p15.sh
```

覆盖：

| 套件 | 路径 |
|------|------|
| 后端烟测 | `make test-backend-smoke` |
| P9 runs | `test_information_runs_p9.py` |
| P13 brief | `test_run_brief.py` |
| 前端烟测 | `make test-frontend-smoke` |
| P10–P14 FE | overflow / judgment / brief / report-output / sidebar / cockpit |

可选在线（服务已起在 `:8080`）：

```bash
ACCEPT_LIVE=1 ./scripts/accept_p15.sh
```

检查：`/api/v1/health`、`latest-summary` bullet 无 `http`、无「持续跟踪」元信息。

## B. 手工验收（约 15–20 分钟）

### B1 Data Intelligence（结论优先）

1. 硬刷新 `/data-intelligence.html`（注意 JS cache bust）
2. 首屏 **In Focus** / 核心结论条有可读中文结论（**不是**裸 URL）
3. 深色 **executive-brief** 与浅色 **brief-strip** 结论一致方向
4. 点 **Start AI 60 秒**（fixture 或少量源）
   - 出现「已入队 run_id=…」或进度，而非整页卡死
   - 完成后结论条刷新，bullet 仍无 URL
5. 切换「世界趋势」tab → 结论条跟随频道
6. 打开完整动态 HTML → 编辑结论卡有 headline / as_of / 证据数；方法在折叠区

**通过准则：** 任一结论 bullet 含 `http://` 或 `https://` → 失败。

### B2 投资引擎（装配 + 多维判断）

1. 打开 `/investment-engine.html`
2. 1280 / 1024 / 390 三宽度：页面 **无横向滚动条**；零件栏/主干道可内部横滚
3. 拖入 `ai_news_60s` 团队 → 计数更新
4. **创建并启动 Engine**（fixture）→ Live Journey 推进
5. **多维判断**面板：11 维、分组 Tab、as_of、免责声明可见
6. 研究侧栏：折叠 / 显示更多 / 点击「分析」「纸面组合」可定位

**通过准则：** `document.scrollWidth > document.clientWidth` 在 1280 宽为 false。

### B3 后台 run / 定时

1. `POST /api/v1/information-sources/teams/ai_news_60s/run` 默认 **202** + `run_id`
2. `GET /api/v1/information-runs/{id}` 终态 `completed|degraded`
3. `GET .../events` 有 started/progress/delivered
4. 定时任务「立即运行」不 403（访客演示路径）

### B4 回归保护面

1. 登录默认进 Agent Config（安全 next）
2. 7 原业务页导航仍在；仅多「数据采集/分析」「投资引擎」
3. Plaza 不依赖投资引擎 API

## C. 已知边界（不记为失败）

- TradingAgents **live** 未装 extra → health 显示 unavailable，fixture 仍可用
- 大量 RSS 同时跑会慢；P9 限流为进程内 soft limit
- 旧文档可能仍含低质量 raw bullet，但 **brief 读路径会改写**；新 run 更好

## D. 记录模板

| 项 | 结果 | 备注 |
|----|------|------|
| accept_p15.sh | ✅ pass | 2026-08-01 15:55 CST；`ACCEPT_LIVE=1` → 5/5 |
| DI 结论无 URL | ✅ | latest-summary 双频道 bullets 无 http / 无「持续跟踪」 |
| Engine HTML 契约 | ✅ | start / judgment / overflow-clip / road-scroll / sidebar |
| 异步 202 + 终态 | ✅ | enqueue 202 → run completed + 6 events + 20 cards |
| 原页面 / 新页面可达 | ✅ | login / agent-team-config / DI / investment-engine 200 |
| DI executive-brief | ✅ | 已恢复 `#executive-brief` 与 strip 双区 |

### 本轮执行（T1503）

- **执行者：** Grok（自动化 + 在线探针）
- **时间：** 2026-08-01T07:55Z–07:57Z
- **命令：** `ACCEPT_LIVE=1 make test-accept-p15` + extended Python probes
- **结果：** 自动化绿；扩展探针 **12/12 passed**
- **修复：** 验收中发现 DI 缺 `id="executive-brief"`，已补回并再验
- **人工浏览器视觉：** 未截图（无头浏览器）；结构/API 契约已覆盖。若需四视口截图可再补。

签字 / 日期：Grok / 2026-08-01
