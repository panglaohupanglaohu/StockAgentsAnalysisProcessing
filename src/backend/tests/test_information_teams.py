# -*- coding: utf-8 -*-
"""T101–T104 — Information team factories, skills, serialization."""

from __future__ import annotations

import json

import pytest

from agents.teams.ai_news_60s_team import TEAM_ID as AI60_ID
from agents.teams.ai_news_60s_team import create_ai_news_60s_team
from agents.teams.dufu_world_intel_team import TEAM_ID as DUFU_ID
from agents.teams.dufu_world_intel_team import create_dufu_world_intel_team
from agents.teams._tool_validation import validate_real_tools


class TestAiNews60sFactory:
    def test_team_shape(self):
        team = create_ai_news_60s_team()
        assert team.team_id == AI60_ID
        assert len(team.agents) == 6
        assert "quick_think" in team.models
        assert "deep_think" in team.models

    def test_required_agent_ids(self):
        team = create_ai_news_60s_team()
        expected = {
            "ai60_lead",
            "ai60_scout",
            "ai60_checker",
            "ai60_market_mapper",
            "ai60_editor",
            "ai60_publisher",
        }
        assert set(team.agents.keys()) == expected

    def test_tools_are_real_and_budgets_set(self):
        team = create_ai_news_60s_team()
        for agent in team.agents.values():
            validate_real_tools(agent.tools)
            assert agent.token_budget > 0
            assert agent.model_id in ("quick_think", "deep_think")
            assert agent.skills
            assert agent.channels

    def test_ai60_has_analysis_and_storytelling_skills(self):
        team = create_ai_news_60s_team()
        assert {"evidence_synthesis", "signal_scoring", "business_impact_analysis"}.issubset(set(team.skills))
        assert "mixture_of_agents" in team.agents["ai60_lead"].tools
        assert "interactive_storytelling" in team.agents["ai60_editor"].skills
        assert "run_javascript" in team.agents["ai60_publisher"].tools

    def test_every_agent_binds_shared_overview_and_reader_skills(self):
        from agents.skills.information_skills import (
            AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
            IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
        )

        team = create_ai_news_60s_team()
        assert AI_CAPITAL_OVERVIEW_DECK_SKILL_ID in team.skills
        assert IMMERSIVE_DYNAMIC_REPORT_SKILL_ID in team.skills
        assert all(
            {
                AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
                IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
            }.issubset(set(agent.skills))
            for agent in team.agents.values()
        )

    def test_serializable_roundtrip_dict(self):
        team = create_ai_news_60s_team()
        payload = team.to_dict()
        # JSON serializable (Agent Config / persistence)
        raw = json.dumps(payload, ensure_ascii=False)
        restored = json.loads(raw)
        assert restored["team_id"] == AI60_ID
        assert len(restored["agents"]) == 6
        assert restored["skills"]
        # Skills must carry instructions for prompt injection
        for skill in restored["skills"].values():
            assert skill.get("has_instructions") is True or skill.get("description")


class TestDufuWorldIntelFactory:
    def test_team_shape(self):
        team = create_dufu_world_intel_team()
        assert team.team_id == DUFU_ID
        assert len(team.agents) == 7

    def test_hard_tool_skill_requirements(self):
        team = create_dufu_world_intel_team()
        collector = team.agents["dufu_web_collector"]
        assert "web_search" in collector.tools
        assert "web_extract" in collector.tools

        for aid in ("dufu_data_engineer", "dufu_data_analyst"):
            assert "run_python" in team.agents[aid].tools

        presenter = team.agents["dufu_presenter"]
        assert "hugohe3" in presenter.skills
        assert "run_javascript" in presenter.tools

    def test_serializable(self):
        team = create_dufu_world_intel_team()
        payload = team.to_dict()
        raw = json.dumps(payload, ensure_ascii=False)
        assert DUFU_ID in raw
        assert len(json.loads(raw)["agents"]) == 7

    def test_every_agent_binds_shared_overview_and_reader_skills(self):
        from agents.skills.information_skills import (
            AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
            IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
        )

        team = create_dufu_world_intel_team()
        assert AI_CAPITAL_OVERVIEW_DECK_SKILL_ID in team.skills
        assert IMMERSIVE_DYNAMIC_REPORT_SKILL_ID in team.skills
        assert all(
            {
                AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
                IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
            }.issubset(set(agent.skills))
            for agent in team.agents.values()
        )


class TestInformationSkills:
    def test_required_skill_ids_present_on_teams(self):
        required = {
            "source_reputation",
            "fact_checking",
            "citation_audit",
            "data_cleaning",
            "data_mining",
            "scenario_tree",
            "macro_to_market",
            "hugohe3",
            "ai_capital_overview_deck",
            "immersive_dynamic_report",
        }
        ai60 = create_ai_news_60s_team()
        dufu = create_dufu_world_intel_team()
        combined = set(ai60.skills) | set(dufu.skills)
        missing = required - combined
        assert not missing, f"Missing skill definitions: {missing}"

    def test_skills_have_injectable_instructions(self):
        from agents.skills.information_skills import build_information_skills

        catalog = build_information_skills()
        for sid in (
            "source_reputation",
            "fact_checking",
            "citation_audit",
            "data_cleaning",
            "data_mining",
            "scenario_tree",
            "macro_to_market",
            "hugohe3",
            "ai_capital_overview_deck",
            "immersive_dynamic_report",
        ):
            skill = catalog[sid]
            assert skill.instructions.strip()
            assert skill.name == sid

    @pytest.mark.parametrize(
        "factory",
        [create_ai_news_60s_team, create_dufu_world_intel_team],
    )
    def test_persisted_team_can_be_backfilled_without_replacement(self, factory):
        from agents.skills.information_skills import (
            AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
            IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
            bind_ai_capital_overview_deck,
            bind_immersive_dynamic_report,
        )

        team = factory()
        # Simulate an older disk-backed team which pre-dates this shared skill.
        team.skills.pop(AI_CAPITAL_OVERVIEW_DECK_SKILL_ID)
        for agent in team.agents.values():
            agent.skills.remove(AI_CAPITAL_OVERVIEW_DECK_SKILL_ID)

        team.skills.pop(IMMERSIVE_DYNAMIC_REPORT_SKILL_ID)
        for agent in team.agents.values():
            agent.skills.remove(IMMERSIVE_DYNAMIC_REPORT_SKILL_ID)

        changed = bind_ai_capital_overview_deck(team)
        reader_changed = bind_immersive_dynamic_report(team)

        assert "team" in changed
        assert set(team.agents).issubset(set(changed))
        assert "team" in reader_changed
        assert set(team.agents).issubset(set(reader_changed))
        assert AI_CAPITAL_OVERVIEW_DECK_SKILL_ID in team.skills
        assert IMMERSIVE_DYNAMIC_REPORT_SKILL_ID in team.skills
        assert all(
            {
                AI_CAPITAL_OVERVIEW_DECK_SKILL_ID,
                IMMERSIVE_DYNAMIC_REPORT_SKILL_ID,
            }.issubset(set(agent.skills))
            for agent in team.agents.values()
        )


class TestUnknownToolRejected:
    def test_validate_real_tools_rejects_unknown(self):
        with pytest.raises(ValueError, match="unknown tools"):
            validate_real_tools(["web_search", "not_a_real_tool_xyz"])
