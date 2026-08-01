# Third-party notices

StockAgents 使用或计划使用多个开源依赖。实际解析版本以 `pyproject.toml`、`package-lock.json` 和上游依赖锁定文件为准；各组件仍遵循其自身许可证。

## TradingAgents runtime (optional)

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents), tag `v0.3.1`, commit `01477f9`, Apache License 2.0.
- Pin location: `pyproject.toml` optional extra `trading` → `git+https://github.com/TauricResearch/TradingAgents.git@01477f9`.
- Integration style: **unmodified** upstream package; StockAgents only adds an adapter boundary under `src/backend/integrations/tradingagents/` (probe, future config mapper / graph adapter). Upstream source is **not** vendored or patched in this repository.
- When the optional extra is not installed, core StockAgents starts normally and health reports `trading_runtime.status=unavailable`.

## Core dependencies

- FastAPI / Starlette / Uvicorn
- Pydantic
- HTTPX / aiohttp
- Vitest / jsdom

发布版本前应生成完整的 dependency SBOM 与许可证报告，并人工确认所有静态资源、字体、图标和数据集的再分发权限。
