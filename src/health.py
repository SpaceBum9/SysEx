#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from search_algo import LIVE

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "runtime.json"


def load_runtime() -> dict:
    with CONFIG.open(encoding="utf-8") as handle:
        return json.load(handle)


def health() -> dict:
    runtime = load_runtime()
    atm = runtime.get("surfaces", {}).get("moreatm", {})
    zt = runtime.get("zero_tier", {})
    return {
        "ok": True,
        "name": runtime.get("name"),
        "role": runtime.get("role"),
        "purpose": runtime.get("purpose"),
        "execute": bool(runtime.get("execute")),
        "vendor_live": bool(runtime.get("vendor_live")),
        "hold": bool(runtime.get("hold")),
        "default": runtime.get("default"),
        "live_rail": bool(runtime.get("live_rail")),
        "modules": runtime.get("modules", []),
        "languages": runtime.get("languages", []),
        "rag": {
            "ivf": True,
            "vendor": False,
            "live": [name for name in LIVE if name != "flat"],
        },
        "atm": {
            "host": atm.get("host"),
            "ready": bool(atm.get("ready")),
            "reason": atm.get("reason"),
        },
        "zero_tier": {
            "needed": bool(zt.get("needed")),
            "owned": bool(zt.get("owned")),
            "joined": bool(zt.get("joined")),
            "ready": bool(zt.get("ready")),
            "network_id_present": zt.get("network_id") is not None,
            "reason": zt.get("reason"),
        },
    }


def main() -> None:
    print(json.dumps(health(), indent=2))


if __name__ == "__main__":
    main()
