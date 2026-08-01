# 原页面冻结保护面

以下页面及其相关前后端功能全部保留。新功能不得改变 DOM 契约、URL/query、现有 API、跨页深链、SSE、3D 状态、存储结构或交互结果。

| 页面 | 地址 | 主要前端保护文件 | 保护重点 |
| --- | --- | --- | --- |
| 智能体团队 | `/agent-team-config.html` | `agent-team-config.html`、`js/agent-team-config.js`、`js/agent-detail.js`、`js/tools-skills.js`、`js/wizard.js` | 团队/模型/Skills/Tools/任务、数字员工配置 |
| 议事广场 | `/plaza.html` | `plaza.html`、`js/plaza.js` | 讨论、共识、派发、SSE、现有 3D 会场与深链 |
| 技能萃取 | `/skill-extract.html` | `skill-extract.html`、`js/skill-extract.js`、`js/skill-extract-timeline.js`、`js/extract-routing.js` | 萃取 DAG、卡片、审核、发布与跨页路径 |
| Agent 记忆 | `/agent-memory.html` | `agent-memory.html`、`js/agent-memory-page.js` | 记忆查看、共享、传递、生命周期与深链 |
| 数字孪生 Office | `/Agent-digital-twin.html?office3d=1` | `Agent-digital-twin.html`、`js/digital-twin/**`、`js/office/**` | Office/3D、演练、生态反馈、关系与通道 |
| Token 节省 | `/cost-dashboard.html` | `cost-dashboard.html`、`js/cost-dashboard.js`、`js/token-workbench.js` | 成本治理、压缩、棘轮、跨页联动 |
| 生态配置 | `/pet-config.html` | `pet-config.html` 及现有配置脚本 | 代谢、学习、声音、生态运行参数 |

主要后端保护面包括 `src/backend/main.py` 中的静态路由、`agent_team_api.py`、`agents/api.py`，以及 `agents/` 下现有 Plaza、memory、extraction、cost、eco、employee、digital-twin 相关 route/service/store。表格不是删改白名单：未列出的依赖同样受现有测试和调用图保护。

## Grok 实现门禁

1. 开发两个新页面前保存 7 页的路由、DOM、API 和关键交互基线。
2. 新后端使用独立 route prefix、领域包和 adapter，不在旧 route 中加条件分支。
3. 旧页面只允许追加两个导航链接；若共享导航能一次完成，不修改页面主体。
4. PR 中若出现保护文件 diff，必须说明为何不是新页面代码可以解决，并单独获得确认。
5. Codex 负责提供外部研究材料；Grok 负责把材料落成代码、测试和交付。
