"""GARAS — protocol function. Door, not truth."""

from __future__ import annotations

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


def classify(intent: str) -> str:
    text = intent.lower()
    hits = [DENY_TOKENS[w] for w in DENY_TOKENS if w in text]
    if "EXECUTE" in hits:
        return "EXECUTE"
    if hits:
        return hits[0]
    return "OBSERVE"


def decide(intent: str) -> dict:
    text = intent.lower()
    hits = [word for word in DENY_TOKENS if word in text]
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
