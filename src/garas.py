"""GARAS — policy. Default deny on money, vendor, destroy."""

from __future__ import annotations

DENY = ("money", "transfer", "order", "vendor", "credential", "destroy", "execute")


def decide(intent: str) -> dict:
    text = intent.lower()
    hits = [word for word in DENY if word in text]
    if hits:
        return {"decision": "deny", "reason": "gated", "hits": hits}
    return {"decision": "allow", "reason": "observe_only", "hits": []}
