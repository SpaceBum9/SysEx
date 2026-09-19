"""GARAS — protocol function. Door, not truth."""

from __future__ import annotations

import re

DENY_TOKENS = {
    "money": "MONEY",
    "transfer": "MONEY",
    "order": "MONEY",
    "vendor": "VENDOR",
    "credential": "CREDENTIAL",
    "destroy": "DESTROY",
    "execute": "EXECUTE",
}

INTENT_CLASSES = (
    "OBSERVE",
    "SYNC",
    "EXECUTE",
    "MONEY",
    "VENDOR",
    "CREDENTIAL",
    "DESTROY",
    "NOISE",
)


def _hits(intent: str) -> list[str]:
    text = intent.lower()
    found: list[str] = []
    for word in DENY_TOKENS:
        if re.search(rf"\b{re.escape(word)}\b", text):
            found.append(word)
    return found


def classify(intent: str) -> str:
    hits = [DENY_TOKENS[w] for w in _hits(intent)]
    if "EXECUTE" in hits:
        return "EXECUTE"
    if hits:
        return hits[0]
    return "OBSERVE"


def decide(intent: str) -> dict:
    hits = _hits(intent)
    intent_class = classify(intent)
    if hits:
        return {
            "decision": "deny",
            "reason": "gated",
            "hits": hits,
            "intent_class": intent_class,
        }
    return {
        "decision": "allow",
        "reason": "observe_only",
        "hits": [],
        "intent_class": intent_class,
    }
