"""AMB — port of MCT-2600027 ambiguity-language-guard. Labels are not facts."""

from __future__ import annotations

from dataclasses import dataclass, asdict
import re

KINDS = (
    "literal",
    "symbolic",
    "brand",
    "person_label",
    "health_claim",
    "technical_claim",
    "speculative",
)

BRANDS = {"novartis", "forbes"}
HEALTH = {"virus", "vermin", "health", "krankheit", "diagnose"}
TECHNICAL = {"reaktor", "fusion", "helios", "gravity"}
PERSON = {"peter", "molyneux", "raphalpha"}
SPECULATIVE = {"schwurbel", "spirit", "galaxy", "blotter"}

DISCLAIMERS = {
    "de": {
        "health_claim": "Gesundheitstokens sind Labels, keine Diagnose.",
        "technical_claim": "Technikbehauptungen brauchen Herkunft, bevor Zustand geschrieben wird.",
        "speculative": "Spekulation bleibt getrennt von geprüften Fakten.",
    },
    "en": {
        "health_claim": "Health tokens are labels only; no diagnosis.",
        "technical_claim": "Technical claims need provenance before they update state.",
        "speculative": "Speculative language stays separate from verified facts.",
    },
    "fr": {
        "health_claim": "Les jetons santé sont des étiquettes, pas un diagnostic.",
        "technical_claim": "Les assertions techniques exigent une provenance.",
        "speculative": "Le langage spéculatif reste séparé des faits vérifiés.",
    },
}


@dataclass
class GuardToken:
    raw: str
    normalized: str
    kind: str
    confidence: float
    requires_evidence: bool
    external_fact: bool = False


def classify(raw: str) -> GuardToken:
    normalized = raw.strip().lower()
    kind = "symbolic"
    confidence = 0.4
    evidence = False
    if normalized in BRANDS:
        kind, confidence = "brand", 0.9
    elif normalized in HEALTH:
        kind, confidence, evidence = "health_claim", 0.8, True
    elif normalized in TECHNICAL:
        kind, confidence, evidence = "technical_claim", 0.8, True
    elif normalized in PERSON:
        kind, confidence = "person_label", 0.8
    elif normalized in SPECULATIVE:
        kind, confidence, evidence = "speculative", 0.5, True
    elif re.fullmatch(r"[\w-]+", normalized, flags=re.UNICODE):
        kind, confidence = "literal", 0.7
    return GuardToken(raw, normalized, kind, confidence, evidence)


def snapshot(text: str, language: str = "de") -> dict:
    lang = language if language in DISCLAIMERS else "en"
    parts = [re.sub(r"^[^\w]+|[^\w-]+$", "", p, flags=re.UNICODE) for p in text.split()]
    tokens = [classify(p) for p in parts if p]
    unresolved = [t.raw for t in tokens if t.requires_evidence or t.kind == "symbolic"]
    notes = []
    for kind in ("health_claim", "technical_claim", "speculative"):
        if any(t.kind == kind for t in tokens):
            notes.append(DISCLAIMERS[lang][kind])
    return {
        "language": lang,
        "tokens": [asdict(t) for t in tokens],
        "unresolved": unresolved,
        "disclaimers": notes,
        "claims_external_state": False,
    }


def snapshot_many(texts: list[str], language: str = "de") -> list[dict]:
    return [
        {"text": text, "snapshot": snapshot(text, language)}
        for text in texts
    ]
