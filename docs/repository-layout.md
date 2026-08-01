# 仓库目录规范

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/         可复现的 Bug/功能请求模板
│   ├── workflows/              GitHub Actions
│   └── pull_request_template.md
├── docs/                       稳定设计文档与 ADR
├── scripts/                    可复用的开发、迁移和验证脚本
├── src/
│   ├── backend/
│   │   ├── agents/             现有 Agent 平台实现
│   │   ├── domain/             新领域契约与纯业务规则
│   │   ├── integrations/       外部框架 adapter
│   │   └── tests/              现有后端测试
│   ├── frontend/
│   │   ├── js/features/        仅含 data-intelligence / investment-engine 新模块
│   │   └── __tests__/          前端契约测试
│   └── storage/                当前已有状态/样例数据
├── PLAN.md                     设计与范围
├── TODOS.md                    可执行开发清单
├── pyproject.toml              Python 构建与测试配置
└── package.json                前端测试配置
```

## 放置规则

- 业务上可独立测试的数据结构和规则放入 `domain`。
- FastAPI route 只负责输入输出转换、鉴权和调用应用服务。
- 第三方对象不得越过 `integrations` 泄漏到页面 API。
- 只允许新增 `data-intelligence.html` 与 `investment-engine.html`；其他信息/报告视图必须作为这两页内部组件。
- 原 7 个业务页面及其既有脚本是冻结保护面，除独立修复任务外不得修改。
- 生成的报告、日志、缓存与真实用户数据不得提交；示例数据必须去敏并明确标注 fixture。
- 新的长期文档放 `docs`；阶段任务写 `TODOS.md`；已经确认的架构决策写 `docs/decisions`。

当前不移动既有文件，避免破坏其顶层 import 和静态文件路径。后续若迁移目录，必须单独 PR，并同时修正启动、导入和测试。
