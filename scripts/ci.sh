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
