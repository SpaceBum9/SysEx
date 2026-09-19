"""Keyword retrieval over rag/. No embeddings, no vendor."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "rag"


def query(q: str, limit: int = 5) -> list[dict]:
    terms = [t.lower() for t in q.split() if t.strip()]
    if not terms:
        return []
    hits: list[dict] = []
    for path in sorted(ROOT.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        low = text.lower()
        score = sum(low.count(t) for t in terms)
        if score:
            hits.append({"path": path.name, "score": score})
    hits.sort(key=lambda h: (-h["score"], h["path"]))
    return hits[:limit]
