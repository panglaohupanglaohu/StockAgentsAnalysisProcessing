# 测试基线

- 记录日期：2026-08-01
- 本地验证环境：macOS arm64、Python 3.14.4、Node/Vitest 3.2.7
- 目的：区分仓库原有债务与 StockAgents 重构新增回归。

## 强制烟测

后端：150/150 通过（含 P8 engine live cockpit）。

```text
test_main_health.py
test_startup_validator.py
test_team_manager.py
test_plaza_dispatch.py
test_legacy_surfaces.py
test_information_teams.py
test_startup_health_layers.py
test_tradingagents_runtime.py
test_information_sources.py
test_information_pipelines.py
test_investment_engine.py
test_domain_api_and_security.py
test_engine_live_cockpit.py
```

前端：36/36 通过（含 engine-cockpit）。

```text
login-page-flow.test.js
agent-config.test.js
team-unified.test.js
plaza-action-paths.test.js
plaza-runtime-helpers.test.js
new-pages-nav.test.js
engine-cockpit.test.js
```

运行：`make test-smoke`。

## 后端全量复核

2026-08-01 续：`pytest -q src/backend/tests`：**1572+ passed 基线后新增 P9 runs 套件**。

已清零此前 19 项旧债 + **P9 后台 run**：

- 补齐 `scripts/run_tse_paper_experiments.py`、`benchmark-token-per-task.py`、`experiment_agent_memory_adaptation.py`
- `config/deploy_allowlist.json`（含 `./start.sh`）
- evolution 请求模型 bounds（`AutoTriageRequest` / `DatasetGenerateRequest` / `DatasetImportKBRequest`）
- secret 解析：env 优先于 settings 明文；skill_evolver 不可用回退文案；model_router `AG_MODEL_ROUTE_ALLOW_SWITCH`
- P9：`information-runs` 202 入队 / Worker / events / 20 卡契约（`test_information_runs_p9.py`）

强制烟测：`make test-smoke` 后端 150 + 前端 37。失败时 PR 不可合并。

## P15 交付验收门禁（P9–P14）

```bash
make test-accept-p15
# 服务已在 :8080 时：
ACCEPT_LIVE=1 make test-accept-p15
```

- 脚本：`scripts/accept_p15.sh`
- 手工清单：`research/p15-acceptance-checklist.md`
- 自动化含：backend smoke、P9 runs、P13 brief、frontend smoke、sidebar/overflow/judgment/brief/report-output/cockpit/nav
- Live 探针：health、`latest-summary` bullet 不得含 `http`、team run 接受 202

## 前端全量

2026-08-01 续：**234 passed / 0 failed**（48 files）。已修复 global-nav 当前页高亮、Agent Config runtime/分页/批量删除契约、CSRF mutation wrapper。

## 基线规则

- 强制烟测失败时 PR 不可合并。
- Advisory 套件新增失败时，PR 必须修复或更新基线并说明原因。
- 修复一个遗留失败后，从本页删除对应条目。
