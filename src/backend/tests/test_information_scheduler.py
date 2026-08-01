# -*- coding: utf-8 -*-
"""Persistent periodic information-task scheduler tests."""

from pathlib import Path

import pytest

from domain.information_sources.scheduler import InformationScheduler, ScheduleStore


def test_schedule_store_round_trip_and_due_fields(tmp_path: Path):
    store = ScheduleStore(tmp_path / "schedules.json")
    item = store.create(
        {
            "name": "AI 早报",
            "team_id": "ai_news_60s",
            "interval_minutes": 30,
            "run_immediately": True,
        }
    )
    loaded = store.get(item.schedule_id)
    assert loaded is not None
    assert loaded.team_id == "ai_news_60s"
    assert loaded.interval_minutes == 30
    assert loaded.next_run_at

    updated = store.update(item.schedule_id, {"enabled": False, "interval_minutes": 45})
    assert updated is not None
    assert updated.enabled is False
    assert updated.interval_minutes == 45
    assert store.delete(item.schedule_id) is True
    assert store.list() == []


def test_schedule_store_uses_thirty_minute_default(tmp_path: Path):
    store = ScheduleStore(tmp_path / "schedules.json")
    item = store.create(
        {
            "name": "默认节奏",
            "team_id": "ai_news_60s",
        }
    )

    assert item.interval_minutes == 30


def test_schedule_api_uses_thirty_minute_default():
    from domain.api_routes import ScheduleCreate

    assert ScheduleCreate(team_id="ai_news_60s").interval_minutes == 30


@pytest.mark.asyncio
async def test_scheduler_runs_pipeline_and_records_result(tmp_path: Path):
    calls = []

    async def fake_runner(team_id, **kwargs):
        calls.append((team_id, kwargs))
        return {"channel": team_id, "run_id": "fixture-run"}

    store = ScheduleStore(tmp_path / "schedules.json")
    item = store.create(
        {
            "name": "世界趋势测试",
            "team_id": "dufu_world_intel",
            "interval_minutes": 5,
            "run_immediately": True,
        }
    )
    scheduler = InformationScheduler(store=store, runner=fake_runner)
    result = await scheduler.run_once(item.schedule_id)
    assert result["ok"] is True
    assert calls[0][0] == "dufu_world_intel"
    saved = store.get(item.schedule_id)
    assert saved is not None
    assert saved.last_status == "success"
    assert saved.run_count == 1
    assert saved.next_run_at
