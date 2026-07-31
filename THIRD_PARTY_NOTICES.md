# Third-party notices

StockAgents 使用或计划使用多个开源依赖。实际解析版本以 `pyproject.toml`、`package-lock.json` 和上游依赖锁定文件为准；各组件仍遵循其自身许可证。

## Planned runtime integration

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents), tag `v0.3.1`, commit `01477f9`, Apache License 2.0。当前仅建立集成设计和可选依赖入口，尚未把其源码复制进本仓库。

## Core dependencies

- FastAPI / Starlette / Uvicorn
- Pydantic
- HTTPX / aiohttp
- Vitest / jsdom

发布版本前应生成完整的 dependency SBOM 与许可证报告，并人工确认所有静态资源、字体、图标和数据集的再分发权限。
