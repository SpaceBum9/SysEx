"""I18N — RC/BILO language slots."""

from __future__ import annotations

LABELS = {
    "de": {"hold": "Halten", "denied": "abgelehnt", "health": "Status"},
    "en": {"hold": "Hold", "denied": "denied", "health": "health"},
    "fr": {"hold": "Maintien", "denied": "refusé", "health": "état"},
    "pl": {"hold": "Wstrzymanie", "denied": "odrzucone", "health": "stan"},
    "ko": {"hold": "보류", "denied": "거부", "health": "상태"},
    "gs": {"hold": "Haltn", "denied": "oa", "health": "Stand"},
}


def _table(lang: str) -> dict[str, str]:
    return LABELS.get(lang) or LABELS["en"]


def t(key: str, lang: str = "de") -> str:
    return _table(lang).get(key, key)


def translate_many(keys: list[str], lang: str = "de") -> list[dict]:
    table = _table(lang)
    return [{"key": key, "value": table.get(key, key)} for key in keys]
