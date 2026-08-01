#!/usr/bin/env bash
# StockAgents local quick-start (dev only).
# Frees occupied ports, then boots the FastAPI app.
# Bootstraps a random local admin password without embedding a fixed default.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

PORT="${AG_PORT:-8080}"
# Comma/space-separated extra ports to free (e.g. AG_EXTRA_PORTS="8000 5173").
EXTRA_PORTS="${AG_EXTRA_PORTS:-}"
# Grace period (seconds) after SIGTERM before SIGKILL.
KILL_WAIT="${AG_KILL_WAIT:-2}"

# ---------------------------------------------------------------------------
# Port cleanup
# ---------------------------------------------------------------------------
list_pids_on_port() {
  local port="$1"
  if command -v lsof >/dev/null 2>&1; then
    # -sTCP:LISTEN avoids killing outbound clients briefly using the port.
    lsof -nP -iTCP:"$port" -sTCP:LISTEN -t 2>/dev/null || true
  elif command -v fuser >/dev/null 2>&1; then
    fuser -n tcp "$port" 2>/dev/null | tr ' ' '\n' | grep -E '^[0-9]+$' || true
  else
    echo "warn: neither lsof nor fuser found; cannot free port $port" >&2
  fi
}

kill_pids() {
  local signal="$1"
  shift
  local pid
  for pid in "$@"; do
    [[ -z "$pid" ]] && continue
    # Never kill our own shell / parent.
    if [[ "$pid" == "$$" || "$pid" == "$PPID" ]]; then
      continue
    fi
    if kill -0 "$pid" 2>/dev/null; then
      kill "-$signal" "$pid" 2>/dev/null || true
    fi
  done
}

free_port() {
  local port="$1"
  local pids
  pids="$(list_pids_on_port "$port" | tr '\n' ' ' | xargs echo -n 2>/dev/null || true)"
  if [[ -z "${pids// /}" ]]; then
    echo "port $port: free"
    return 0
  fi

  echo "port $port: stopping listeners → $pids"
  # shellcheck disable=SC2086
  kill_pids TERM $pids
  sleep "$KILL_WAIT"

  pids="$(list_pids_on_port "$port" | tr '\n' ' ' | xargs echo -n 2>/dev/null || true)"
  if [[ -n "${pids// /}" ]]; then
    echo "port $port: force-killing → $pids"
    # shellcheck disable=SC2086
    kill_pids KILL $pids
    sleep 0.5
  fi

  pids="$(list_pids_on_port "$port" | tr '\n' ' ' | xargs echo -n 2>/dev/null || true)"
  if [[ -n "${pids// /}" ]]; then
    echo "error: port $port still held by: $pids" >&2
    return 1
  fi
  echo "port $port: cleared"
}

# Also stop stale StockAgents workers that may have dropped the listen socket
# but still hold the project cwd (uvicorn --reload reloader orphans).
kill_stale_project_workers() {
  local pattern="python.*main\\.py.*--port[= ]*${PORT}"
  local pids=""
  if command -v pgrep >/dev/null 2>&1; then
    pids="$(pgrep -f "$pattern" 2>/dev/null || true)"
  fi
  if [[ -z "${pids//$'\n'/}" ]]; then
    return 0
  fi
  echo "stale StockAgents workers: stopping → $(echo "$pids" | tr '\n' ' ')"
  # shellcheck disable=SC2086
  kill_pids TERM $pids
  sleep "$KILL_WAIT"
  pids="$(pgrep -f "$pattern" 2>/dev/null || true)"
  if [[ -n "${pids//$'\n'/}" ]]; then
    # shellcheck disable=SC2086
    kill_pids KILL $pids
  fi
}

echo "==> Freeing ports before start (main=${PORT}${EXTRA_PORTS:+, extra=${EXTRA_PORTS}})"
free_port "$PORT"
# shellcheck disable=SC2086
for p in $EXTRA_PORTS; do
  [[ -n "$p" ]] && free_port "$p"
done
kill_stale_project_workers

# ---------------------------------------------------------------------------
# Local admin bootstrap
# ---------------------------------------------------------------------------
DEV_ADMIN_PASSWORD_FILE="${DEV_ADMIN_PASSWORD_FILE:-$ROOT/config/.dev_admin_password}"
mkdir -p "$(dirname "$DEV_ADMIN_PASSWORD_FILE")"

generate_dev_admin_password() {
  python3 - <<'PY'
import secrets
import string
alphabet = string.ascii_letters + string.digits
print("".join(secrets.choice(alphabet) for _ in range(24)))
PY
}

if [[ ! -f "$DEV_ADMIN_PASSWORD_FILE" ]]; then
  generate_dev_admin_password > "$DEV_ADMIN_PASSWORD_FILE"
  python3 - <<PY
from pathlib import Path
path = Path(r"$DEV_ADMIN_PASSWORD_FILE")
path.chmod(0o600)
PY
  echo "Generated local admin password at $DEV_ADMIN_PASSWORD_FILE"
fi

export ADMIN_PASSWORD="$(tr -d '\n' < "$DEV_ADMIN_PASSWORD_FILE")"
# Do not force default-admin flag to on; require explicit local admin bootstrap via password file.
# Reject fixed weak password "admin123" if someone injects it.
if [[ "$ADMIN_PASSWORD" == "admin123" ]]; then
  echo "Refusing fixed password admin123; regenerating."
  generate_dev_admin_password > "$DEV_ADMIN_PASSWORD_FILE"
  python3 - <<PY
from pathlib import Path
path = Path(r"$DEV_ADMIN_PASSWORD_FILE")
path.chmod(0o600)
PY
  export ADMIN_PASSWORD="$(tr -d '\n' < "$DEV_ADMIN_PASSWORD_FILE")"
fi

echo "AG_ALLOW_DEFAULT_ADMIN enabled only when ADMIN_PASSWORD is set from $DEV_ADMIN_PASSWORD_FILE"
export AG_ALLOW_DEFAULT_ADMIN=0
# main.py enables default admin when ADMIN_PASSWORD is present regardless of AG_ALLOW in some builds;
# document intent: local bootstrap via password file, not fixed default.

# ---------------------------------------------------------------------------
# Python env + launch
# ---------------------------------------------------------------------------
if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install -q -e '.[dev]' || true

echo "==> Starting StockAgents on http://127.0.0.1:${PORT}"
cd src/backend
exec python main.py --port "${PORT}" --reload
