# -*- coding: utf-8 -*-
"""60 秒 AI 信息播报团队 factory — team_id: ai_news_60s.

参考公开「60 秒播报」的栏目节奏与信息密度，不复制创作者声音、形象、口头禅或原文。
磁盘已持久化的团队配置优先于本 factory（main 启动时仅 seed 缺失团队）。
"""

from __future__ import annotations

from typing import List

from ..models import (
    AccessLevel,
    AgentChannelConfig,
    AgentPermission,
    AgentPersonality,
    AgentProfile,
    AgentTeam,
    AgentTemplateType,
    ModelConfig,
    Visibility,
)
from ..skills.information_skills import (
    AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
    IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
    attach_skills_to_team,
)
from ._tool_validation import validate_real_tools

TEAM_ID = "ai_news_60s"
CHANNEL = "ai_news_60s_bus"

# Quick Think / Deep Think model roles used by Agent Config and future pipelines.
QUICK_MODEL_ID = "quick_think"
DEEP_MODEL_ID = "deep_think"

# role, agent_id, name, description, template, tools, skills, token_budget, model_id
_AI60_ROLES = [
    (
        "lead",
        "ai60_lead",
        "Lead 编辑",
        "选题、拆解任务、控制时间预算、发布门禁",
        AgentTemplateType.COORDINATOR,
        ["delegate_task", "mixture_of_agents", "schedule_task", "memory_read", "publish_event"],
        ["editorial_planning", "intelligence_planning", "news_ranking", "confidence_calibration", "quality_gate", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        80_000,
        DEEP_MODEL_ID,
    ),
    (
        "scout",
        "ai60_scout",
        "Scout 采集",
        "搜索官方发布、论文、开源项目、产品和政策",
        AgentTemplateType.RESEARCHER,
        ["web_search", "navigate_url", "web_extract", "memory_save"],
        ["ai_source_discovery", "multilingual_search", "timeline_building", "ai_taxonomy", "source_reputation", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        120_000,
        QUICK_MODEL_ID,
    ),
    (
        "checker",
        "ai60_checker",
        "Checker 核验",
        "去重、交叉验证、日期/实体/数字核验",
        AgentTemplateType.ANALYST,
        ["web_search", "web_extract", "run_python", "memory_read"],
        ["fact_checking", "deduplication", "evidence_synthesis", "citation_audit", "bias_detection", "confidence_calibration", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        100_000,
        DEEP_MODEL_ID,
    ),
    (
        "market_mapper",
        "ai60_market_mapper",
        "Market Mapper",
        "映射公司、产业链、赛道、机会和风险（非投资建议）",
        AgentTemplateType.ANALYST,
        ["run_python", "memory_read", "read_file"],
        ["entity_resolution", "data_analysis", "signal_scoring", "change_point_detection", "business_impact_analysis", "market_impact_mapping", "transmission_path", "scenario_analysis", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        90_000,
        DEEP_MODEL_ID,
    ),
    (
        "editor",
        "ai60_editor",
        "Editor 撰稿",
        "生成 60 秒版与可展开长版",
        AgentTemplateType.CUSTOM,
        ["read_file", "memory_read", "run_javascript"],
        ["sixty_second_brief", "plain_language_editing", "uncertainty_labeling", "interactive_storytelling", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        70_000,
        QUICK_MODEL_ID,
    ),
    (
        "publisher",
        "ai60_publisher",
        "Publisher 发布",
        "输出动态 HTML 并发布版本化文档",
        AgentTemplateType.ENGINEER,
        ["read_file", "write_file", "run_javascript", "publish_event"],
        ["hugohe3", "accessible_html", "data_visualization", "interactive_storytelling", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        60_000,
        QUICK_MODEL_ID,
    ),
]


def default_quick_model() -> ModelConfig:
    return ModelConfig(
        model_id=QUICK_MODEL_ID,
        provider="deepseek",
        name="deepseek-chat",
        max_tokens=4096,
        temperature=0.3,
        is_default=True,
        api_base_url="https://api.deepseek.com",
    )


def default_deep_model() -> ModelConfig:
    return ModelConfig(
        model_id=DEEP_MODEL_ID,
        provider="deepseek",
        name="deepseek-reasoner",
        max_tokens=8192,
        temperature=0.2,
        is_default=False,
        api_base_url="https://api.deepseek.com",
    )


def _system_prompt(name: str, description: str) -> str:
    return (
        f"你是 60 秒 AI 信息团队的「{name}」。\n"
        f"职责：{description}。\n"
        "团队目标：产出高密度、可核验的 AI 信息播报，并生成可嵌入数据采集/分析页的动态 HTML。\n"
        "约束：\n"
        "1. 不模仿任何创作者的声音、形象、口头禅，不复制原文。\n"
        "2. 事实/分析/推断必须分标签；重要事实尽量交叉验证。\n"
        "3. 每条事实至少一个可访问来源；记录事件时间、来源发布时间和抓取时间。\n"
        "4. 不只做摘要：必须完成主题聚类、信号评分、证据综合、业务影响链和反证检查。\n"
        "5. 相关公司/赛道映射必须标注「非投资建议」，收入/成本推演必须标注为模拟假设。\n"
        "6. 每轮都要为 20 卡 AI Capital Overview 准备可引用数据；数据不足时交付明确研究缺口，不得编造数值。\n"
        "7. 报告必须可按 document_id + version 独立打开；卡片具备稳定锚点，动效仅服务理解，严格保留来源、截止时间和非投资建议声明。\n"
        "8. 请用中文回答，简洁、可核验、可追溯；发布前交付结构化 JSON 和动态 HTML 所需的数据。\n"
    )


def _build_agent(
    role: str,
    agent_id: str,
    name: str,
    description: str,
    template_type: AgentTemplateType,
    tools: List[str],
    skills: List[str],
    token_budget: int,
    model_id: str,
) -> AgentProfile:
    validate_real_tools(tools)
    return AgentProfile(
        agent_id=agent_id,
        name=name,
        role=role,
        description=description,
        template_type=template_type,
        model_id=model_id,
        fallback_model_id=QUICK_MODEL_ID if model_id == DEEP_MODEL_ID else DEEP_MODEL_ID,
        system_prompt=_system_prompt(name, description),
        personality=AgentPersonality(
            tone="analytical",
            language="zh-CN",
            expertise_areas=["ai_news", "fact_checking", "briefing"],
            response_style="structured",
            creativity=0.35,
        ),
        permissions=[
            AgentPermission(
                resource="docs",
                access_level=AccessLevel.WRITE,
                channels=[CHANNEL],
            ),
            AgentPermission(
                resource="web",
                access_level=AccessLevel.READ,
                channels=[CHANNEL],
            ),
        ],
        channels=[
            AgentChannelConfig(
                channel_name=CHANNEL,
                subscribe=True,
                publish=True,
                priority=8 if role == "lead" else 5,
            ),
        ],
        tools=list(tools),
        skills=list(skills),
        token_budget=token_budget,
        metadata={
            "team_type": "ai_news_60s",
            "role": role,
            "model_role": "deep_think" if model_id == DEEP_MODEL_ID else "quick_think",
        },
    )


def build_ai60_agents() -> List[AgentProfile]:
    return [
        _build_agent(role, aid, name, desc, tmpl, tools, skills, budget, mid)
        for role, aid, name, desc, tmpl, tools, skills, budget, mid in _AI60_ROLES
    ]


def create_ai_news_60s_team() -> AgentTeam:
    """Create the 60-second AI news briefing team."""
    team = AgentTeam(
        team_id=TEAM_ID,
        name="60 秒 AI 信息团队",
        description=(
            "高密度 AI 快讯采集、核验与动态 HTML 发布团队。"
            "产物结构：总览 → 5 条快讯 → 为什么重要 → 公司/赛道 → 风险反证 → 来源与运行 ID。"
        ),
        visibility=Visibility.INTERNAL,
        metadata={
            "team_type": "information",
            "pipeline": "ai_news_60s",
            "output_surface": "data-intelligence",
        },
    )
    team.add_model(default_quick_model())
    team.add_model(default_deep_model())

    skill_ids: List[str] = []
    for agent in build_ai60_agents():
        validate_real_tools(agent.tools)
        skill_ids.extend(agent.skills)
        team.add_agent(agent)

    attach_skills_to_team(team, sorted(set(skill_ids)))
    return team
