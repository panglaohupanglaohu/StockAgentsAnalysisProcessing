# Information sources domain

本包将承载 `SourceConfig`、`SourceManifest`、`FetchBatch`、`EvidenceRecord`、`InformationPacket` 与 connector protocol。

依赖方向：connector adapter 可以依赖这里；这里不能依赖 FastAPI、具体网页解析器或 TradingAgents。实现入口见 `TODOS.md` 的 T201—T206。
