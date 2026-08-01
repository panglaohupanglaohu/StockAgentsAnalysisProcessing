# TradingAgents adapter

目标版本：`v0.3.1` / `01477f9`（Apache-2.0）。

## 已实现（T301）

- `runtime.py` — pin 常量、`probe_trading_runtime()`、import smoke、fixture ticker smoke。
- 可选安装：`python -m pip install -e '.[trading]'`。
- 缺失依赖时健康层 `trading_runtime` 降级为 `unavailable`，不阻止原系统启动。

## 规划

配置映射、graph adapter、context provider、event bridge 见 `TODOS.md` T302+。

上游内部 state 不得直接进入 StockAgents API 或持久化 schema。
