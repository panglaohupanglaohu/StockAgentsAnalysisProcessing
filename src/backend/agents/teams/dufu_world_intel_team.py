# -*- coding: utf-8 -*-
"""独夫之心世界趋势情报团队 factory — team_id: dufu_world_intel.

参考宏观议题、时间线、因果链与情景分析结构，必须把事实、分析、推断和情景清楚分开。
不复制任何创作者人格、声音或原文。磁盘持久化优先于 factory 播种。
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

TEAM_ID = "dufu_world_intel"
CHANNEL = "dufu_world_intel_bus"

QUICK_MODEL_ID = "quick_think"
DEEP_MODEL_ID = "deep_think"

# role, agent_id, name, description, template, tools, skills, token_budget, model_id
_DUFU_ROLES = [
    (
        "lead",
        "dufu_lead",
        "Lead 统筹",
        "议题拆解、调度、最终结论门禁",
        AgentTemplateType.COORDINATOR,
        ["delegate_task", "mixture_of_agents", "schedule_task", "publish_event"],
        ["intelligence_planning", "scenario_tree", "editorial_gate", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        90_000,
        DEEP_MODEL_ID,
    ),
    (
        "web_collector",
        "dufu_web_collector",
        "Web Collector",
        "多语言公开来源与 Web 采集",
        AgentTemplateType.RESEARCHER,
        ["web_search", "navigate_url", "web_extract", "memory_save"],
        ["multilingual_search", "timeline_building", "source_reputation", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        130_000,
        QUICK_MODEL_ID,
    ),
    (
        "data_engineer",
        "dufu_data_engineer",
        "Data Engineer",
        "清洗、去重、实体对齐、时序对齐",
        AgentTemplateType.ENGINEER,
        ["run_python", "read_file", "write_file"],
        ["data_cleaning", "entity_resolution", "timeseries_alignment", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        100_000,
        DEEP_MODEL_ID,
    ),
    (
        "data_analyst",
        "dufu_data_analyst",
        "Data Analyst",
        "统计分析、数据挖掘、趋势与异常识别",
        AgentTemplateType.ANALYST,
        ["run_python", "memory_read", "memory_save"],
        ["data_analysis", "data_mining", "change_point_detection", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        110_000,
        DEEP_MODEL_ID,
    ),
    (
        "red_team",
        "dufu_red_team",
        "Red Team",
        "查找反证、偏差和替代解释",
        AgentTemplateType.ANALYST,
        ["web_search", "web_extract", "mixture_of_agents"],
        ["claim_challenge", "bias_detection", "confidence_calibration", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        100_000,
        DEEP_MODEL_ID,
    ),
    (
        "market_mapper",
        "dufu_market_mapper",
        "Market Mapper",
        "宏观事件到行业、公司和市场的传导路径",
        AgentTemplateType.ANALYST,
        ["run_python", "memory_read"],
        ["macro_to_market", "transmission_path", "scenario_analysis", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        90_000,
        DEEP_MODEL_ID,
    ),
    (
        "presenter",
        "dufu_presenter",
        "Presenter",
        "使用 hugohe3 生成动态数据页面",
        AgentTemplateType.ENGINEER,
        ["read_file", "write_file", "run_javascript", "publish_event"],
        ["hugohe3", "interactive_storytelling", "accessible_html", AI_CAPITAL_OVERVIEW_DECK_SKILL_ID, IMMERSIVE_DYNAMIC_REPORT_SKILL_ID],
        70_000,
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
        f"你是独夫之心世界趋势团队的「{name}」。\n"
        f"职责：{description}。\n"
        "团队目标：从公开多语言来源建立世界趋势时间线、因果链、反证与市场传导路径，"
        "并生成可嵌入数据采集/分析页的动态 HTML。\n"
        "约束：\n"
        "1. 事实、观点、分析、推断和情景必须分标签，禁止人格克隆或原文复制。\n"
        "2. 数据清理与实体对齐须可重复；图表显示截止时间、单位、样本与来源。\n"
        "3. Red Team 反证不得在编辑阶段被静默删除。\n"
        "4. 乐观/基准/悲观情景必须写出触发条件。\n"
        "5. 市场传导内容必须标注「非投资建议」。\n"
        "6. 每轮都要为 20 卡 AI Capital Overview 准备可引用数据；数据不足时保留研究缺口卡，不得伪造数值。\n"
        "7. 报告必须按 document_id + version 独立打开；卡片具备稳定锚点，动效只帮助理解，严格保留来源、截止时间和非投资建议声明。\n"
        "8. 请用中文回答，严谨、可追溯。\n"
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
            expertise_areas=["geopolitics", "macro", "data_analysis", "intelligence"],
            response_style="detailed",
            creativity=0.4,
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
            AgentPermission(
                resource="code",
                access_level=AccessLevel.WRITE if "run_python" in tools else AccessLevel.READ,
                channels=[CHANNEL],
            ),
        ],
        channels=[
            AgentChannelConfig(
                channel_name=CHANNEL,
                subscribe=True,
                publish=True,
                priority=9 if role == "lead" else 5,
            ),
        ],
        tools=list(tools),
        skills=list(skills),
        token_budget=token_budget,
        metadata={
            "team_type": "dufu_world_intel",
            "role": role,
            "model_role": "deep_think" if model_id == DEEP_MODEL_ID else "quick_think",
            "requires_web_search": role == "web_collector",
            "restricted_python": role in ("data_engineer", "data_analyst", "market_mapper"),
        },
    )


def build_dufu_agents() -> List[AgentProfile]:
    return [
        _build_agent(role, aid, name, desc, tmpl, tools, skills, budget, mid)
        for role, aid, name, desc, tmpl, tools, skills, budget, mid in _DUFU_ROLES
    ]


def create_dufu_world_intel_team() -> AgentTeam:
    """Create the world-trend intelligence team."""
    team = AgentTeam(
        team_id=TEAM_ID,
        name="独夫之心世界趋势团队",
        description=(
            "多语言公开来源采集、数据清洗分析、红队反证与动态 HTML 呈现。"
            "产物：事件 → 时间线 → 驱动 → 数据 → 观点/反证 → 情景 → 传导路径 → 引用。"
        ),
        visibility=Visibility.INTERNAL,
        metadata={
            "team_type": "information",
            "pipeline": "dufu_world_intel",
            "output_surface": "data-intelligence",
        },
    )
    team.add_model(default_quick_model())
    team.add_model(default_deep_model())

    skill_ids: List[str] = []
    for agent in build_dufu_agents():
        validate_real_tools(agent.tools)
        # Hard requirements from TODOS/PLAN
        if agent.agent_id == "dufu_web_collector":
            for required in ("web_search", "web_extract"):
                if required not in agent.tools:
                    raise ValueError(f"Web Collector must have {required}")
        if agent.agent_id in ("dufu_data_engineer", "dufu_data_analyst"):
            if "run_python" not in agent.tools:
                raise ValueError(f"{agent.agent_id} must have restricted run_python")
        if agent.agent_id == "dufu_presenter":
            if "hugohe3" not in agent.skills:
                raise ValueError("Presenter must bind hugohe3 skill")
        skill_ids.extend(agent.skills)
        team.add_agent(agent)

    attach_skills_to_team(team, sorted(set(skill_ids)))
    return team
