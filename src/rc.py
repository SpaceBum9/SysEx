"""RC — next slot on the wheel. No live write. Nikita = Main Bot."""

from __future__ import annotations

WHEEL = ("NIKITA", "GPT", "GEM", "CLA", "GRK", "SIRI", "APL", "META")


def next_slot(index: int = 0) -> dict:
    i = index % len(WHEEL)
    return {
        "slot": WHEEL[i],
        "index": i,
        "next": WHEEL[(i + 1) % len(WHEEL)],
        "execute": False,
        "live_write": False,
        "tertiary": "NIKITA",
    }
