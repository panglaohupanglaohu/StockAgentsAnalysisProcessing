# TradingAgents adapter

目标版本：`v0.3.1` / `01477f9`。

本目录只放版本探测、配置映射、输入/输出转换、checkpoint adapter 和错误归一化。上游内部 state 不得直接进入 StockAgents API 或持久化 schema。实现任务见 `TODOS.md` 的 T301 以后。
