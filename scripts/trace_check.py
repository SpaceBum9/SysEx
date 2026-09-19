#!/usr/bin/env python3
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from packet import compose  # noqa: E402
from trace import verify  # noqa: E402


def main() -> None:
    raw = sys.stdin.read().strip()
    if raw:
        packet = json.loads(raw)
    else:
        packet = compose("read health", verb="sync")
    result = verify(packet)
    print(json.dumps({"verify": result, "trace_id": packet.get("trace_id")}, indent=2))
    if not result.get("ok"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
