"""ATM — public automaton. execute stays closed."""

from __future__ import annotations

VERBS = ("initialize", "sync", "halt", "execute")


def handle(verb: str) -> dict:
    name = verb.strip().lower()
    if name not in VERBS:
        return {"ok": False, "verb": name, "status": "unknown"}
    if name == "execute":
        return {
            "ok": False,
            "verb": name,
            "status": "denied",
            "reason": "execute_gated",
        }
    return {"ok": True, "verb": name, "status": "accepted", "side_effects": False}
