"""Lexicon lookup. Not statute. claims_external_state false."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "lexicon" / "BILO.md"


def load() -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for line in ROOT.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---") or "Token" in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4:
            continue
        token = parts[0].upper()
        rows[token] = {
            "token": token,
            "de": parts[1],
            "en": parts[2],
            "job": parts[3],
            "claims_external_state": False,
        }
    return rows


def lookup(token: str) -> dict | None:
    return load().get(token.strip().upper())


def scan(text: str) -> list[dict]:
    table = load()
    found: list[dict] = []
    upper = text.upper()
    for token, row in table.items():
        if token and token in upper.split() or token in upper:
            if row not in found:
                found.append(row)
    return found
