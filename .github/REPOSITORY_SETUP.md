# GitHub 仓库初始化清单

首次创建远端仓库后，维护者需要完成：

- [x] 项目链接已指向 `panglaohupanglaohu/StockAgentsAnalysisProcessing`。
- [x] 默认分支和 `origin/HEAD` 已指向 `main`。
- [ ] 启用 Private vulnerability reporting。
- [ ] 为 `main` 设置 branch protection，要求 `Backend (Python 3.11/3.12)` 与 `Frontend contracts` 通过。
- [ ] 暂不把两个 `Full ... baseline (advisory)` job 设为必需检查。
- [ ] 启用 Dependabot security updates 和 secret scanning（若账户支持）。
- [ ] 选择项目许可证并新增根目录 `LICENSE`。
- [ ] 配置维护者/审查者；确认后再新增 `CODEOWNERS`。
- [ ] 检查任何准备转为 fixture 的运行数据是否已脱敏；`src/storage/evolution_*` 与 `src/docs` 下的生成 artifacts 默认忽略。

本次只建立 GitHub-ready 文件，不自动创建远端仓库、不推送，也不替维护者选择许可证。
