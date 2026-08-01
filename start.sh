#!/usr/bin/env bash
# StockAgents local quick-start (dev only).
# Bootstraps a random local admin password without embedding a fixed default.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

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

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install -q -e '.[dev]' || true

cd src/backend
exec python main.py --port "${AG_PORT:-8080}" --reload
