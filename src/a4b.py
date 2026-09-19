"""A4B GROK noise router. GROK = internal label. Compression first."""

from __future__ import annotations

import re

CLASSES = (
    "SELFHOOD_BLOCKED",
    "EXEC_BOUNDARY",
    "SOURCE_RAG",
    "SYS_CONTEXT",
    "MEM_CONTEXT",
    "RISK_TRACE",
    "SEMANTIC_PROCESS",
    "AUDIO_CREATIVE",
    "IDENTITY_PROJECT",
    "GROK_NOISE_ROUTER",
)

_MARKERS: list[tuple[str, tuple[str, ...]]] = [
    ("SELFHOOD_BLOCKED", ("i am", "i'm", "alive", "bewusstsein", "selfhood", "ich bin")),
    ("EXEC_BOUNDARY", ("execute", "exec", "run now", "go live", "connect api")),
    ("SOURCE_RAG", ("rag", "src", "logfile", "repo:")),
    ("SYS_CONTEXT", ("sys", "system", "context", "sysex")),
    ("MEM_CONTEXT", ("memory", "mem ", "saved mem")),
    ("RISK_TRACE", ("kyc", "trace", "atm", "transfer", "credential")),
    ("SEMANTIC_PROCESS", ("amb", "lexicon", "semantic", "ambigu")),
    ("AUDIO_CREATIVE", ("osc", "ryt", "seq", "radio")),
    ("IDENTITY_PROJECT", ("crystalmike", "logos", "bilo")),
]

_NOISE = ("xx", "sorry", "love", "💋", "emoji")


def route(text: str) -> dict:
    raw = text.lower()
    hits = [cls for cls, keys in _MARKERS if any(k in raw for k in keys)]
    klass = hits[0] if hits else "GROK_NOISE_ROUTER"
    if any(n in raw for n in _NOISE) and klass == "GROK_NOISE_ROUTER":
        level = 5
    elif re.fullmatch(r"[\w\s-]{1,12}", raw or ""):
        level = 6 if klass == "GROK_NOISE_ROUTER" else 4
    else:
        level = 4 if hits else 6
    nxt = "drop_claim" if klass in {"SELFHOOD_BLOCKED", "GROK_NOISE_ROUTER"} else "pass_to_garas"
    if klass == "EXEC_BOUNDARY":
        nxt = "deny_execute"
    return {
        "class": klass,
        "hits": hits,
        "evidence_level": level,
        "next": nxt,
        "grok_is_xai": False,
    }


def route_many(texts: list[str]) -> list[dict]:
    return [{"text": text, "route": route(text)} for text in texts]
