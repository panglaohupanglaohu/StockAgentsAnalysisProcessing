# 首批信息源目录（T202）

- 建立日期：2026-08-01
- 原则：**原始/官方优先**；社交与二手转载降权；字段完整（URL、类型、地区、语言、频率、访问、许可、可信度、备用）
- 覆盖说明见文末；机器可读清单：`research/source_catalog.json`

## AI 来源（≥30）

涵盖实验室/公司官方、论文、开源、标准、安全与基准。完整表见 JSON 中 `ai_sources`。

摘要类别：

1. 模型与研究实验室官方博客（OpenAI, DeepMind, Anthropic, Meta AI, Mistral, Cohere 等）
2. 论文：arXiv cs.AI / cs.LG / cs.CL
3. 开源：Hugging Face blog/docs、主要框架 release notes
4. 云与芯片：AWS/Azure/GCP AI 博客、NVIDIA 开发者博客
5. 标准与安全：NIST AI、OECD AI、CISA AI 相关公开页
6. 基准与评测：公开 leaderboard 更新说明

## 世界趋势来源（≥40）

涵盖国际组织、央行、能源、贸易、统计、多语种官方通讯。完整表见 JSON `world_sources`。

摘要类别：

1. 国际组织：UN / IMF / World Bank / WTO / OECD / WHO 新闻
2. 能源：IEA / EIA
3. 统计：Eurostat、各国统计局公开发布页
4. 央行：Fed / ECB / BoE / BoJ 公开沟通
5. 区域多语：EU 新闻室、ASEAN、主要国家外交/商务部英文页
6. 航运与大宗：公开运价/现货指数说明页（只读）

## 覆盖与偏差说明

| 维度 | 现状 | 风险 | 改进 |
| --- | --- | --- | --- |
| 语言 | 英/中为主 | 非英语区低估 | 后续加 FR/ES/AR/RU 官方源 |
| 地区 | 北美/欧洲/东亚偏多 | 全球南方不足 | 增补非盟、拉美开发银行 |
| 机构类型 | 官方+实验室强 | 公民社会弱 | 增补独立监察组织 RSS |
| 政治立场 | 官方叙述偏中性包装 | 单一官方依赖 | 强制双源 + Red Team |
| 更新频率 | 日/周混杂 | 突发滞后 | 调度按 source.update_interval |

**偏差声明**：本目录不代表全面中立；运行时必须用 `source_reputation` + 交叉验证，禁止单一来源支撑关键事实。
