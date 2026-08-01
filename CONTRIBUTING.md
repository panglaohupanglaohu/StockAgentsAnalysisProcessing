# 贡献指南

感谢参与 StockAgents。当前阶段优先保护原系统行为，再以小步、可回滚的方式加入信息源与投资模拟能力。

## 开发环境

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
npm ci
cp .env.example .env
```

启动服务：

```bash
cd src/backend
python main.py --port 8080 --reload
```

## 开发流程

1. 从一个明确的 TODO 或 Issue 开始，并写清完成定义。
2. 保持改动聚焦；结构重排与功能修改不要混在同一个 PR。
3. 为行为变化增加测试。7 个原业务页面及其后台接口是冻结保护面，不在新页面任务中顺手改造。
4. 至少运行 `make test-smoke`；同时运行 `make test`，并把已知基线以外的失败说明清楚。
5. 更新用户可见行为对应的 README、文档或 CHANGELOG。

推荐分支名：`feat/<topic>`、`fix/<topic>`、`docs/<topic>`。提交信息建议采用 Conventional Commits，例如 `feat(teams): add ai news team factory`。

## 架构边界

- 现有 Agent 内核保留在 `src/backend/agents`。
- 新领域规则进入 `src/backend/domain`，不依赖 FastAPI 页面层。
- 第三方系统进入 `src/backend/integrations`，必须由 adapter 隔离。
- 信息源 connector 不得直接调用投资引擎；统一产出规范化 information packet。
- 前端新功能放在 `src/frontend/js/features`，避免继续扩大单页全局脚本。

## Pull Request 检查

- [ ] 没有提交 API Key、Cookie、用户数据、运行日志或生成报告。
- [ ] 7 个原业务页面及其相关后台功能仍可加载，且行为未改变。
- [ ] 前端只新增 `/data-intelligence.html` 与 `/investment-engine.html`。
- [ ] 新来源包含超时、大小限制、SSRF 与错误隔离策略。
- [ ] 投资逻辑没有使用决策时刻之后的数据。
- [ ] 新增事实输出能追溯来源、抓取时间与运行 ID。
- [ ] 测试和文档已同步。

安全问题请遵循 [SECURITY.md](SECURITY.md)，不要在公开 Issue 中披露漏洞细节。
