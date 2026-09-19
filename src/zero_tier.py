"""ZT — overlay declaration. Owned is not joined."""

from __future__ import annotations

from health import load_runtime


def status() -> dict:
    zt = load_runtime().get("zero_tier", {})
    return {
        "needed": bool(zt.get("needed")),
        "owned": bool(zt.get("owned")),
        "joined": False,
        "ready": False,
        "network_id": None,
        "id_suffix": zt.get("id_suffix"),
        "mcp_live": False,
        "reason": zt.get("reason"),
        "note": zt.get("note"),
    }
