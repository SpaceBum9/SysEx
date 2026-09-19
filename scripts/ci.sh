#!/bin/sh
set -e
cd "$(dirname "$0")/.."
python3 - <<'PY'
import json
from pathlib import Path
r = json.loads(Path("config/runtime.json").read_text())
assert r.get("execute") is False
assert r.get("vendor_live") is False
assert r.get("hold") is True
print("hold ok")
PY
python3 -m unittest discover -s tests -v
if git rev-parse --is-inside-work-tree >/dev/null 2>&1 && [ "${GITHUB_EVENT_NAME:-}" != "pull_request" ]; then
  msg=$(git log -1 --pretty=%B)
  actor_count=$(printf '%s\n' "$msg" | grep -Ec '^Actor: (GRK|GPT)$' || true)
  test "$actor_count" -eq 1
  echo "actor trailer ok"
fi
