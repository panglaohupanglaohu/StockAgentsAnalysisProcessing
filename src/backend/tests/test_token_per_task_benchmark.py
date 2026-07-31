# -*- coding: utf-8 -*-
"""P1-4 token/任务基准：确定性双跑 ±10% 与 G2/G3 列。"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "scripts" / "benchmark-token-per-task.py"


@pytest.mark.parametrize("twice", [False, True])
def test_deterministic_benchmark_cli(tmp_path: Path, twice: bool):
    out = tmp_path / "reports"
    cmd = [
        sys.executable,
        str(SCRIPT),
        "--mode",
        "deterministic",
        "--seeds",
        "7,42",
        "--output-dir",
        str(out),
    ]
    if twice:
        cmd.append("--twice")
    env = {"PYTHONPATH": str(ROOT / "src" / "backend")}
    # inherit rest of env
    import os

    full_env = {**os.environ, **env}
    proc = subprocess.run(cmd, capture_output=True, text=True, env=full_env, cwd=str(ROOT))
    assert proc.returncode == 0, proc.stderr + proc.stdout
    payload = json.loads(proc.stdout.strip().splitlines()[-1])
    assert payload["ok"] is True
    assert payload["status"] == "completed"
    assert payload["G2"] is not None and payload["G2"] > 0
    assert payload["G3"] is not None and payload["G3"] >= 0.9

    report_path = out / "token-per-task-benchmark.json"
    assert report_path.is_file()
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["n_tasks"] >= 5 * 2  # 6 scenarios × 2 seeds
    s = report["summary"]
    assert "G2_tokens_per_task" in s
    assert "G3_success_rate" in s
    assert len(s["by_scenario"]) >= 5
    md = (out / "token-per-task-benchmark.md").read_text(encoding="utf-8")
    assert "G2" in md and "G3" in md

    if twice:
        assert report["repro"]["pass"] is True
        assert report["repro"]["g2_delta_pct"] <= 10.0
        assert payload["repro_pass"] is True


def test_deterministic_import_run_once():
    sys.path.insert(0, str(ROOT / "scripts"))
    # load module by path
    import importlib.util

    spec = importlib.util.spec_from_file_location("bench_tok", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    import asyncio

    r = asyncio.run(
        mod.run_once(
            mode="deterministic",
            seeds=[7],
            scenario_ids=[s["id"] for s in mod.SCENARIOS],
            team_id=mod.FIXED_TEAM_ID,
        )
    )
    assert r["status"] == "completed"
    assert r["summary"]["G3_success_rate"] == 1.0
    assert r["summary"]["G2_tokens_per_task"] > 0
    # 同 seed 再跑一次应数值相同
    r2 = asyncio.run(
        mod.run_once(
            mode="deterministic",
            seeds=[7],
            scenario_ids=[s["id"] for s in mod.SCENARIOS],
            team_id=mod.FIXED_TEAM_ID,
        )
    )
    assert r["summary"]["G2_tokens_per_task"] == r2["summary"]["G2_tokens_per_task"]
    assert r["summary"]["G3_success_rate"] == r2["summary"]["G3_success_rate"]
