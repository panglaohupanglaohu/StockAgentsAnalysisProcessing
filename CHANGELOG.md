# Changelog

本项目采用 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) 的结构；稳定版本后遵循语义化版本。

## [Unreleased]

### Added

- GitHub 仓库文档、Issue/PR 模板和 CI 骨架。
- Python 与前端测试项目配置。
- 信息源、投资模拟和 TradingAgents 适配层的目录边界。
- 7 个原业务页面冻结清单，以及仅新增数据采集/分析、投资引擎两页的契约。

### Changed

- 项目文档品牌调整为 StockAgents。
- 重构方案明确保留 Build System、AI Coding、Agent Config 与 Plaza。
- 职责调整为 Codex 提供外部研究输入、Grok 负责代码实现与测试。

### Planned

- `ai_news_60s` 与 `dufu_world_intel` 团队。
- 可插拔信息源和动态 HTML 发布。
- TradingAgents v0.3.1 模拟运行时适配。
