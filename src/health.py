#!/usr/bin/env python3
"""Print SoS health from config/runtime.json. No network. No execute."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "runtime.json"


def load_runtime() -> dict:
    with CONFIG.open(encoding="utf-8") as handle:
        return json.load(handle)


def health() -> dict:
    runtime = load_runtime()
    return {
        "ok": True,
        "name": runtime.get("name"),
        "role": runtime.get("role"),
        "execute": bool(runtime.get("execute")),
        "vendor_live": bool(runtime.get("vendor_live")),
        "hold": bool(runtime.get("hold")),
        "default": runtime.get("default"),
        "live_rail": bool(runtime.get("live_rail")),
    }


def main() -> None:
    print(json.dumps(health(), indent=2))


if __name__ == "__main__":
    main()
