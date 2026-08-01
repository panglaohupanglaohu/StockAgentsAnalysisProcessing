# -*- coding: utf-8 -*-
"""Builtin SkillDefinitions for information teams (ai_news_60s, dufu_world_intel).

These are real SkillDefinition objects with injectable instructions — not bare
string names. Agent Config can list/view them; runtime prompts can inject
skill.instructions into agent context.
"""

from __future__ import annotations

from typing import Dict, List

from ..models import SkillCategory, SkillDefinition

# Stable skill_id == name for builtin catalog skills so agent.skills name
# references resolve without an extra slug map.
AI_CAPITAL_OVERVIEW_DECK_SKILL_ID = "ai_capital_overview_deck"
IMMERSIVE_DYNAMIC_REPORT_SKILL_ID = "immersive_dynamic_report"

_SKILL_SPECS: List[dict] = [
    {
        "skill_id": "source_reputation",
        "name": "source_reputation",
        "description": "评估信息源可信度、历史准确性与利益冲突",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_search", "web_extract", "memory_read"],
        "instructions": (
            "## 来源信誉评估\n\n"
            "1. 记录来源类型（官方/学术/媒体/社交/二次转载）。\n"
            "2. 检查作者、机构、更新频率与更正记录。\n"
            "3. 对冲突利益与赞助关系做显式标注。\n"
            "4. 输出 0–1 信誉分，并写明扣分理由。\n"
            "5. 低信誉来源不得单独支撑关键事实。"
        ),
    },
    {
        "skill_id": "fact_checking",
        "name": "fact_checking",
        "description": "交叉验证事实、数字、实体与时间戳",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_search", "web_extract", "run_python"],
        "instructions": (
            "## 事实核验\n\n"
            "1. 将声明拆成可验证原子主张。\n"
            "2. 至少使用两个独立来源交叉验证重要事实。\n"
            "3. 区分事件发生时间、来源发布时间与抓取时间。\n"
            "4. 对数字、实体名与 ticker 做规范化比对。\n"
            "5. 未核验项必须标记为「待验证」并附不确定性。"
        ),
    },
    {
        "skill_id": "citation_audit",
        "name": "citation_audit",
        "description": "审计引用完整性、可访问性与出处一致性",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_extract", "read_file"],
        "instructions": (
            "## 引用审计\n\n"
            "1. 每条事实至少绑定一个可访问 URL。\n"
            "2. 核对引用片段与原文是否一致，禁止断章取义。\n"
            "3. 缺失、失效或 paywall 来源写入审计清单。\n"
            "4. 发布前确保引用列表含抓取时间与运行 ID。"
        ),
    },
    {
        "skill_id": "data_cleaning",
        "name": "data_cleaning",
        "description": "清洗、去重、对齐实体与时间序列数据",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "read_file", "write_file"],
        "instructions": (
            "## 数据清洗\n\n"
            "1. 规范化时间戳为 ISO-8601（含时区）。\n"
            "2. 按内容 hash / 实体键去重。\n"
            "3. 对齐不同来源的实体别名与单位。\n"
            "4. 记录清洗规则与丢弃行数，保证可重复执行。"
        ),
    },
    {
        "skill_id": "data_mining",
        "name": "data_mining",
        "description": "从结构化与半结构化数据中挖掘趋势与异常",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read", "memory_save"],
        "instructions": (
            "## 数据挖掘\n\n"
            "1. 明确分析窗口、样本范围与数据截止时间。\n"
            "2. 使用可解释统计/变化点方法，避免黑盒结论。\n"
            "3. 区分相关与因果；禁止过度拟合叙事。\n"
            "4. 输出趋势强度、异常点与置信区间说明。"
        ),
    },
    {
        "skill_id": "scenario_tree",
        "name": "scenario_tree",
        "description": "构建乐观/基准/悲观情景树及触发条件",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["memory_read", "run_python"],
        "instructions": (
            "## 情景树\n\n"
            "1. 定义乐观、基准、悲观三条路径。\n"
            "2. 每条路径写明触发条件、关键指标与时间窗口。\n"
            "3. 禁止只给结论不写触发条件。\n"
            "4. 标注情景为分析而非预测保证。"
        ),
    },
    {
        "skill_id": "macro_to_market",
        "name": "macro_to_market",
        "description": "将宏观事件映射到行业、公司与市场传导路径",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 宏观到市场传导\n\n"
            "1. 从事件出发列出一级/二级传导节点。\n"
            "2. 关联行业、供应链与代表性公司（非投资建议）。\n"
            "3. 写明机制、滞后与不确定性。\n"
            "4. 输出中必须包含「非投资建议」声明。"
        ),
    },
    {
        "skill_id": "editorial_planning",
        "name": "editorial_planning",
        "description": "选题、拆解任务与时间预算控制",
        "category": SkillCategory.GENERAL,
        "required_tools": ["delegate_task", "schedule_task", "memory_read"],
        "instructions": (
            "## 编辑策划\n\n"
            "1. 按时效与影响力排序选题。\n"
            "2. 拆解为 Scout / Checker / Mapper / Editor 任务。\n"
            "3. 设置时间预算与发布门禁条件。\n"
            "4. 未过质量门禁不得发布。"
        ),
    },
    {
        "skill_id": "news_ranking",
        "name": "news_ranking",
        "description": "按信息密度与重要性排序快讯",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["memory_read"],
        "instructions": (
            "## 新闻排序\n\n"
            "1. 综合新颖性、影响面、可核验性打分。\n"
            "2. 优先官方与一手来源。\n"
            "3. 去重后输出 Top-N 与淘汰理由。"
        ),
    },
    {
        "skill_id": "quality_gate",
        "name": "quality_gate",
        "description": "发布前质量门禁：事实/引用/标签齐全",
        "category": SkillCategory.GENERAL,
        "required_tools": ["memory_read", "publish_event"],
        "instructions": (
            "## 质量门禁\n\n"
            "检查：事实标签、引用、数据截止时间、不确定性、反证是否齐全。\n"
            "任一项缺失则驳回并返回可操作修复清单。"
        ),
    },
    {
        "skill_id": "ai_source_discovery",
        "name": "ai_source_discovery",
        "description": "发现 AI 领域官方发布、论文与产品动态来源",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_search", "navigate_url", "web_extract"],
        "instructions": (
            "## AI 来源发现\n\n"
            "覆盖：实验室/公司官方、论文、开源仓库、监管与标准。\n"
            "记录 URL、语言、更新频率与访问方式。"
        ),
    },
    {
        "skill_id": "ai_taxonomy",
        "name": "ai_taxonomy",
        "description": "AI 事件分类：模型/产品/政策/安全/开源",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["memory_save"],
        "instructions": (
            "## AI 分类法\n\n"
            "将每条资讯打上主类与标签，便于后续聚合与市场映射。"
        ),
    },
    {
        "skill_id": "deduplication",
        "name": "deduplication",
        "description": "基于内容 hash 与实体键的去重",
        "category": SkillCategory.AUTOMATION,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 去重\n\n"
            "对标题、正文摘要与实体集合计算内容 hash；合并同源转载，保留最早与最权威版本。"
        ),
    },
    {
        "skill_id": "entity_resolution",
        "name": "entity_resolution",
        "description": "公司、人物、产品实体对齐与消歧",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 实体对齐\n\n"
            "统一别名、ticker、中英文名；冲突时保留证据链与置信度。"
        ),
    },
    {
        "skill_id": "market_impact_mapping",
        "name": "market_impact_mapping",
        "description": "映射公司、产业链、赛道机会与风险",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read", "read_file"],
        "instructions": (
            "## 市场影响映射\n\n"
            "输出相关公司/赛道及传导机制；明确标注「非投资建议」。"
        ),
    },
    {
        "skill_id": "scenario_analysis",
        "name": "scenario_analysis",
        "description": "机会与风险情景分析",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 情景分析\n\n"
            "列出上行/下行驱动因素、触发条件与观察指标；禁止确定性措辞。"
        ),
    },
    {
        "skill_id": "sixty_second_brief",
        "name": "sixty_second_brief",
        "description": "生成 60 秒高密度播报摘要与可展开长版",
        "category": SkillCategory.GENERAL,
        "required_tools": ["read_file", "memory_read"],
        "instructions": (
            "## 60 秒播报结构\n\n"
            "一句话总览 → 5 条快讯 → 为什么重要 → 相关公司/赛道 "
            "→ 风险与反证 → 原始来源、截止时间、运行 ID。\n"
            "不模仿任何创作者声音或口头禅；不复制原文。"
        ),
    },
    {
        "skill_id": "plain_language_editing",
        "name": "plain_language_editing",
        "description": "用平实中文改写技术信息",
        "category": SkillCategory.GENERAL,
        "required_tools": ["read_file", "memory_read"],
        "instructions": (
            "## 平实语言编辑\n\n"
            "保留事实精度，去掉行话堆砌；关键术语首次出现时简短解释。"
        ),
    },
    {
        "skill_id": "uncertainty_labeling",
        "name": "uncertainty_labeling",
        "description": "为事实/观点/推断打不确定性标签",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["memory_read"],
        "instructions": (
            "## 不确定性标注\n\n"
            "每条陈述标记：事实 / 分析 / 推断；附置信度与缺失信息。"
        ),
    },
    {
        "skill_id": "hugohe3",
        "name": "hugohe3",
        "description": "受控 JSON → 响应式可访问动态 HTML 渲染（仓库内置同名 Skill）",
        "category": SkillCategory.AUTOMATION,
        "required_tools": ["read_file", "write_file", "publish_event"],
        "instructions": (
            "## hugohe3 渲染\n\n"
            "1. 输入必须通过 Report Schema 校验。\n"
            "2. 输出响应式 HTML：标题/证据卡/时间带/关系图/引用区分层呈现，图表需文本替代。\n"
            "3. 报告视觉采用可复用的版式 token，兼容 16:9 投屏阅读；不要把信息压成一张无层次长表。\n"
            "4. 允许 SVG 原生图形、数据标签和模板化叙事，借鉴 ppt-master 的可复用模板/图表/演示结构，但不复制其项目素材。\n"
            "5. 禁止注入来源脚本；校验 CSP 与引用完整性。\n"
            "6. 生成不可变文档版本（含运行 ID 与数据截止时间）。"
        ),
    },
    {
        "skill_id": "accessible_html",
        "name": "accessible_html",
        "description": "可访问性：语义结构、对比度、alt 文本",
        "category": SkillCategory.AUTOMATION,
        "required_tools": ["read_file", "write_file"],
        "instructions": (
            "## 可访问 HTML\n\n"
            "使用语义标题层级、足够对比度、图表 alt/aria 说明；键盘可达。"
        ),
    },
    {
        "skill_id": "data_visualization",
        "name": "data_visualization",
        "description": "安全图表数据与文本替代说明",
        "category": SkillCategory.AUTOMATION,
        "required_tools": ["run_python", "read_file"],
        "instructions": (
            "## 数据可视化\n\n"
            "图表数据经 safe_json 序列化；显示单位、样本范围与截止时间。"
        ),
    },
    {
        "skill_id": "intelligence_planning",
        "name": "intelligence_planning",
        "description": "议题拆解与情报采集调度",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["delegate_task", "mixture_of_agents", "schedule_task"],
        "instructions": (
            "## 情报策划\n\n"
            "拆解议题为采集/清洗/分析/红队/呈现阶段；设定截止与证据门槛。"
        ),
    },
    {
        "skill_id": "editorial_gate",
        "name": "editorial_gate",
        "description": "情报报告最终编辑门禁",
        "category": SkillCategory.GENERAL,
        "required_tools": ["publish_event", "memory_read"],
        "instructions": (
            "## 编辑门禁\n\n"
            "红队反证不得静默删除；情景触发条件与引用必须齐全。"
        ),
    },
    {
        "skill_id": "multilingual_search",
        "name": "multilingual_search",
        "description": "多语言公开来源检索与摘要",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_search", "navigate_url", "web_extract"],
        "instructions": (
            "## 多语言检索\n\n"
            "覆盖主要语言来源；保留原文关键术语并附中文对照；记录语言字段。"
        ),
    },
    {
        "skill_id": "timeline_building",
        "name": "timeline_building",
        "description": "构建可核验历史时间线",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_extract", "memory_save"],
        "instructions": (
            "## 时间线构建\n\n"
            "每个节点含日期、事件、来源 URL；区分确认事实与传闻。"
        ),
    },
    {
        "skill_id": "timeseries_alignment",
        "name": "timeseries_alignment",
        "description": "多源时序对齐与重采样",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "read_file", "write_file"],
        "instructions": (
            "## 时序对齐\n\n"
            "统一频率与时区；标注缺失区间与插值方法。"
        ),
    },
    {
        "skill_id": "data_analysis",
        "name": "data_analysis",
        "description": "统计分析与趋势识别",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 数据分析\n\n"
            "给出方法、样本范围、截止时间与可复现步骤；图表附文本说明。"
        ),
    },
    {
        "skill_id": "evidence_synthesis",
        "name": "evidence_synthesis",
        "description": "把多条异构证据合成为可审计的主张、矛盾与证据链",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["run_python", "memory_read", "read_file"],
        "instructions": (
            "## 证据综合\n\n"
            "1. 将标题、摘要、正文和发布时间统一成证据单元。\n"
            "2. 合并重复报道，保留一手来源与冲突版本。\n"
            "3. 输出主张—证据—反证三元组，不把相关性写成因果。\n"
            "4. 每个结论携带证据数量、来源多样性和缺口说明。"
        ),
    },
    {
        "skill_id": "signal_scoring",
        "name": "signal_scoring",
        "description": "按新颖性、时效性、影响面和证据质量计算可解释信号分",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 信号评分\n\n"
            "对每条信息给出 0–100 分：新颖性、时效性、影响面、来源质量各有权重；"
            "同时输出分项值和降权原因，禁止把评分当成交易信号。"
        ),
    },
    {
        "skill_id": "business_impact_analysis",
        "name": "business_impact_analysis",
        "description": "分析 AI 事件对成本、收入、交付与产业链的业务传导",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read", "read_file"],
        "instructions": (
            "## 业务影响分析\n\n"
            "沿着事件 → 能力/成本 → 产品采用 → 收入或利润池的链路推演；"
            "区分直接证据与模拟假设，写明时间滞后、受益方、承压方和不确定性；不构成投资建议。"
        ),
    },
    {
        "skill_id": "change_point_detection",
        "name": "change_point_detection",
        "description": "识别趋势拐点与结构变化",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_save"],
        "instructions": (
            "## 变化点检测\n\n"
            "报告变化点位置、统计依据与可能的外部事件关联（非因果断言）。"
        ),
    },
    {
        "skill_id": "claim_challenge",
        "name": "claim_challenge",
        "description": "主动寻找反证与替代解释",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_search", "web_extract", "mixture_of_agents"],
        "instructions": (
            "## 主张挑战\n\n"
            "对主叙事寻找反证；列出至少一种替代解释；不得被后续编辑删除。"
        ),
    },
    {
        "skill_id": "bias_detection",
        "name": "bias_detection",
        "description": "检测来源与叙述偏差",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["web_search", "memory_read"],
        "instructions": (
            "## 偏差检测\n\n"
            "检查语言、地区、机构类型与单一来源依赖；输出偏差提示。"
        ),
    },
    {
        "skill_id": "confidence_calibration",
        "name": "confidence_calibration",
        "description": "校准置信度表述与证据权重",
        "category": SkillCategory.RESEARCH,
        "required_tools": ["mixture_of_agents", "memory_read"],
        "instructions": (
            "## 置信度校准\n\n"
            "高置信需多源独立证据；证据薄弱时降低置信并说明缺口。"
        ),
    },
    {
        "skill_id": "transmission_path",
        "name": "transmission_path",
        "description": "事件到市场的传导路径刻画",
        "category": SkillCategory.DOMAIN_KNOWLEDGE,
        "required_tools": ["run_python", "memory_read"],
        "instructions": (
            "## 传导路径\n\n"
            "绘制因果/相关链路节点；标注滞后与不确定性；附「非投资建议」。"
        ),
    },
    {
        "skill_id": "interactive_storytelling",
        "name": "interactive_storytelling",
        "description": "结构化交互叙事呈现情报结论",
        "category": SkillCategory.GENERAL,
        "required_tools": ["read_file", "write_file", "run_javascript"],
        "instructions": (
            "## 交互叙事\n\n"
            "按「发生了什么 → 时间线 → 驱动 → 数据 → 观点/反证 → 情景 → 传导」组织页面；"
            "交互脚本仅限受控数据绑定，禁止外部脚本注入。"
        ),
    },
    {
        "skill_id": AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
        "name": AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
        "description": "将一次信息运行组织成 20 张可审计、高冲击的资本格局 Overview 数据卡组",
        "category": SkillCategory.GENERAL,
        "required_tools": [],
        "instructions": (
            "## AI Capital Overview Deck\n\n"
            "这是信息团队共同遵守的 20 卡研究叙事与数据契约，不是把 RSS 摘要堆成页面。"
            "每张卡必须显示数据截止时间、样本/来源标签、引用或研究缺口、观察事实与推断/代理的边界；"
            "不能从新闻标题虚构估值、Capex、营收或地域事实。\n\n"
            "### 固定卡组\n\n"
            "01 封面（本轮论点/截止时间/最强主题）→ 02 编辑导语（三个结论与不确定性）→ "
            "03 方法与目录（证据契约）→ 04 主题景观（主题分布）→ 05 证据脉冲（量与时效）→ "
            "06 对比信号（主题排名）→ 07 置信度气泡（信号/新颖性/时效）→ "
            "08 来源构成环图（质量分层）→ 09 Top-3 主题比较 → 10 来源排名 → "
            "11 双轨比较（国内/国际或可解释代理）→ 12 长尾多样性 → 13 焦点信号深描 → "
            "14 事件到业务的流图 → 15 集中度 Pareto → 16 证据关系 Hub → "
            "17 不确定性与反证 → 18 采用/成本/收入机制代理曲线 → 19 四象限风险 → "
            "20 六条结论、继续监测项、引用与研究/模拟免责声明。\n\n"
            "### 数据不足时的规则\n\n"
            "全部 20 张卡都必须出现。缺少可比数据时生成『研究缺口卡』：写明覆盖率、缺少的字段、"
            "下一轮负责 Agent 和可验证动作；不得删除卡片、重复文本或伪造数值。"
            "金额/估值/营收/Capex 卡只有在存在带单位、日期、来源的结构化指标时才可画数值图；"
            "否则降级为证据计数或机制假设，并显著标注『研究代理，不代表市场规模』。\n\n"
            "### 团队分工\n\n"
            "Lead 负责主论点和卡序；Scout/Web Collector 负责来源、时间戳和原始指标；"
            "Checker/Data Engineer 负责去重、单位/期间对齐与口径门禁；"
            "Market Mapper/Data Analyst 负责比较、传导、网络与风险；"
            "Editor/Red Team 负责叙事、反证、开放问题；Publisher/Presenter 负责响应式、可访问 HTML。\n\n"
            "视觉采用强数字层级、深色数据新闻底色、克制强调色、清晰图例和图表文字替代；"
            "所有市场/业务映射均标注仅供研究与模拟，非投资建议。"
        ),
    },
    {
        "skill_id": IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
        "name": IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
        "description": "将版本化研究文档发布为可访问、安全、沉浸式的独立动态报告阅读页",
        "category": SkillCategory.GENERAL,
        "required_tools": [],
        "instructions": (
            "## Immersive Dynamic Report\n\n"
            "这是信息团队共同遵守的独立报告发布契约。报告不是 RSS 摘要堆叠，也不是不可追溯的视觉特效。"
            "每次发布必须保留不可变 document_id + version，阅读页只能读取该精确版本，禁止把『最新』指针当作历史报告。\n\n"
            "### 阅读体验\n\n"
            "1. 以本轮核心论点、数据截止时间和证据强度作为英雄区，不使用空泛 KPI 装饰。\n"
            "2. 固定组织 20 张研究卡：论点、方法、主题、证据、对比、来源、传导、反证、风险与监测项。\n"
            "3. 每张卡均标记观察事实 / 推断 / 研究缺口，并带来源、时间或下一步验证动作。\n"
            "4. 图表只能消费经过 Checker/Data Engineer 认证的输入；数值、估值、营收、Capex 或地域事实缺失时必须降级为研究缺口，绝不由标题猜测。\n"
            "5. Publisher/Presenter 输出有稳定锚点和 data-card-id 的语义 HTML；阅读壳必须键盘可用、响应式、支持减少动态效果，并保留研究/模拟、非投资建议声明。\n"
            "6. 动效只服务理解：可用克制的加载序列、证据轨道、阅读进度或卡片入场；不伪造实时性，不用动态数字暗示不存在的数据。\n\n"
            "### 安全与版本\n\n"
            "独立阅读页以 document_id + version 获取已审核快照；HTML 进入严格 sandbox，不注入来源脚本，"
            "不为测量高度而放松 same-origin 或 scripts 权限。报告页和 API 都须维持 CSP、来源引用与可恢复错误状态。"
        ),
    },
]


def build_information_skills() -> Dict[str, SkillDefinition]:
    """Build skill_id → SkillDefinition map for information teams."""
    out: Dict[str, SkillDefinition] = {}
    for spec in _SKILL_SPECS:
        skill = SkillDefinition(
            skill_id=spec["skill_id"],
            name=spec["name"],
            description=spec["description"],
            category=spec["category"],
            required_tools=list(spec.get("required_tools") or []),
            instructions=spec.get("instructions") or "",
            source="builtin",
            slug=spec["name"],
            enabled=True,
            is_default=True,
            lifecycle_stage="published",
        )
        out[skill.skill_id] = skill
    return out


def attach_skills_to_team(team, skill_ids: List[str]) -> None:
    """Add named skills onto an AgentTeam (idempotent by skill_id)."""
    catalog = build_information_skills()
    for sid in skill_ids:
        skill = catalog.get(sid)
        if skill is None:
            raise ValueError(f"Unknown information skill: {sid}")
        team.add_skill(skill)


def _bind_shared_skill_to_team(team, skill_id: str) -> List[str]:
    """Idempotently bind a role-neutral shared skill to a persisted info team."""
    catalog = build_information_skills()
    skill = catalog[skill_id]
    changed: List[str] = []
    if skill_id not in team.skills:
        team.add_skill(skill)
        changed.append("team")
    for agent in team.agents.values():
        if skill_id not in (agent.skills or []):
            agent.skills.append(skill_id)
            changed.append(agent.agent_id)
    return changed


def bind_ai_capital_overview_deck(team) -> List[str]:
    """Idempotently bind the shared 20-card deck skill to a persisted info team.

    Team factories bind this skill from day one.  This helper is deliberately
    separate so startup can retrofit an existing disk-backed team without
    replacing its user-managed members, prompts, models, or other skills.
    """
    return _bind_shared_skill_to_team(team, AI_CAPITAL_OVERVIEW_DECK_SKILL_ID)


def bind_immersive_dynamic_report(team) -> List[str]:
    """Retrofit the standalone-report contract without replacing team setup.

    The skill belongs to every role: upstream roles produce certified inputs,
    while Editor/Publisher or Presenter turns them into the safe reader.
    """
    return _bind_shared_skill_to_team(team, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID)
