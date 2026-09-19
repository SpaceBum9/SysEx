"""ZT — overlay declaration. Does not join a network. Does not invent live MCP."""

from __future__ import annotations

from health import load_runtime


def status() -> dict:
    zt = load_runtime().get("zero_tier", {})
    return {
        "needed": bool(zt.get("needed")),
        "joined": False,
        "network_id": None,
        "mcp_live": False,
        "note": zt.get("note"),
    }
