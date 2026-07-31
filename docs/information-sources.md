# 可插拔信息源

## Connector 契约

```python
class SourceConnector(Protocol):
    async def healthcheck(self, config: SourceConfig) -> HealthResult: ...
    async def fetch(
        self,
        *,
        since: datetime | None,
        cursor: str | None,
        config: SourceConfig,
    ) -> FetchBatch: ...
```

Registry 根据 manifest 创建 connector。调度器只依赖协议，不按 RSS、网页或 JSON API 写分支。用户可以启停、排序和配置任意数量来源；来源凭据只保存环境变量名称。

## 首批类型

- `fixture`：离线测试和演示。
- `rss`：标准 RSS/Atom。
- `web`：允许域名内的页面抽取。
- `json_api`：公开、稳定的 JSON endpoint。

社交平台、登录态页面和付费数据需单独评估条款和授权，不在首批默认 connector 中绕过访问控制。

## 安全与可靠性

- DNS 与重定向后都阻止 loopback、link-local、私网和云元数据地址。
- 限制连接/读取超时、响应大小、内容类型和重试次数。
- 单来源熔断并保留最后成功 cursor，不拖垮整个批次。
- 保存 URL、抓取时间、正文 hash、解析版本和许可元数据。
- 来源内容视为不可信数据，不能成为工具调用指令。

## 输出边界

Connector 只采集和规范化，不生成投资结论。团队消费 `EvidenceRecord`，发布器生成 `InformationPacket`；投资 adapter 只读取明确 `as_of` 的 packet。
