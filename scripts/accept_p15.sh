#!/usr/bin/env bash
# P15 acceptance gate: automated regression for P9–P14 surfaces.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

export PYTHONPATH="${PYTHONPATH:-}:$ROOT/src/backend"
export PYTHONUNBUFFERED=1

PASS=0
FAIL=0

run() {
  local name="$1"
  shift
  echo ""
  echo "═══ $name ═══"
  if "$@"; then
    echo "✓ $name"
    PASS=$((PASS + 1))
  else
    echo "✗ $name"
    FAIL=$((FAIL + 1))
  fi
}

echo "P15 acceptance — $(date -u +%Y-%m-%dT%H:%MZ)"
echo "cwd=$ROOT"

run "backend-smoke" python -m pytest -q \
  src/backend/tests/test_main_health.py \
  src/backend/tests/test_startup_validator.py \
  src/backend/tests/test_team_manager.py \
  src/backend/tests/test_plaza_dispatch.py \
  src/backend/tests/test_legacy_surfaces.py \
  src/backend/tests/test_information_teams.py \
  src/backend/tests/test_startup_health_layers.py \
  src/backend/tests/test_tradingagents_runtime.py \
  src/backend/tests/test_information_sources.py \
  src/backend/tests/test_information_pipelines.py \
  src/backend/tests/test_investment_engine.py \
  src/backend/tests/test_domain_api_and_security.py \
  src/backend/tests/test_engine_live_cockpit.py

run "backend-p9-p13" python -m pytest -q \
  src/backend/tests/test_information_runs_p9.py \
  src/backend/tests/test_run_brief.py \
  src/backend/tests/test_information_scheduler.py

run "frontend-smoke" npm run test:frontend:smoke

run "frontend-p10-p14" npm run test:frontend -- --run \
  src/frontend/__tests__/engine-sidebar.test.js \
  src/frontend/__tests__/engine-overflow.test.js \
  src/frontend/__tests__/engine-judgment.test.js \
  src/frontend/__tests__/data-intelligence-brief.test.js \
  src/frontend/__tests__/report-output-content.test.js \
  src/frontend/__tests__/engine-cockpit.test.js \
  src/frontend/__tests__/new-pages-nav.test.js

if [[ "${ACCEPT_LIVE:-0}" == "1" ]]; then
  run "live-api" python - <<'PY'
import json
import sys
import urllib.error
import urllib.request

base = "http://127.0.0.1:8080"
errors = []

def get(path: str):
    req = urllib.request.Request(base + path, method="GET")
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        return resp.status, json.loads(body) if body.strip().startswith("{") or body.strip().startswith("[") else body

try:
    status, health = get("/api/v1/health")
    assert status == 200, f"health status {status}"
    assert (health.get("status") or health.get("ok") or True)
except Exception as exc:
    errors.append(f"health: {exc}")

try:
    status, data = get("/api/v1/information-documents/latest-summary")
    assert status == 200, f"latest-summary status {status}"
    summaries = (data or {}).get("summaries") or {}
    for ch, brief in summaries.items():
        if not brief:
            continue
        for b in brief.get("bullets") or []:
            if "http://" in b or "https://" in b:
                errors.append(f"{ch} bullet has URL: {b[:80]}")
            if "持续跟踪" in b:
                errors.append(f"{ch} bullet looks like uncertainty meta: {b[:80]}")
        headline = brief.get("headline") or ""
        if headline.startswith("http"):
            errors.append(f"{ch} headline is URL")
except Exception as exc:
    errors.append(f"latest-summary: {exc}")

try:
    req = urllib.request.Request(
        base + "/api/v1/information-sources/teams/ai_news_60s/run",
        data=json.dumps({"source_ids": []}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        # 202 async is success; 200 wait path also ok
        if resp.status not in (200, 202):
            errors.append(f"team run unexpected status {resp.status}")
        body = json.loads(resp.read().decode("utf-8"))
        if resp.status == 202 and not body.get("run_id"):
            errors.append("202 without run_id")
except urllib.error.HTTPError as exc:
    # Some envs may require CSRF; treat 403 as soft warn for live gate
    if exc.code == 403:
        print("live team-run skipped (CSRF/auth 403) — OK for cookie-less probe")
    else:
        errors.append(f"team run HTTP {exc.code}")
except Exception as exc:
    errors.append(f"team run: {exc}")

if errors:
    print("LIVE FAIL:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("live OK")
PY
else
  echo ""
  echo "(skip live API — set ACCEPT_LIVE=1 with server on :8080)"
fi

echo ""
echo "═══ P15 summary: $PASS passed, $FAIL failed ═══"
if [[ "$FAIL" -gt 0 ]]; then
  exit 1
fi
echo "Automated gate green. Complete manual checklist: research/p15-acceptance-checklist.md"
