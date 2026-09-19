"""Keyword retrieval over rag/. No embeddings, no vendor."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "rag"


def _corpus() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for path in sorted(ROOT.glob("*.md")):
        rows.append((path.name, path.read_text(encoding="utf-8", errors="replace").lower()))
    return rows


def _score(low: str, terms: list[str]) -> int:
    return sum(low.count(t) for t in terms)


def query(q: str, limit: int = 5, corpus: list[tuple[str, str]] | None = None) -> list[dict]:
    terms = [t.lower() for t in q.split() if t.strip()]
    if not terms:
        return []
    docs = corpus if corpus is not None else _corpus()
    hits: list[dict] = []
    for name, low in docs:
        score = _score(low, terms)
        if score:
            hits.append({"path": name, "score": score})
    hits.sort(key=lambda h: (-h["score"], h["path"]))
    return hits[:limit]


def query_many(queries: list[str], limit: int = 5) -> list[dict]:
    docs = _corpus()
    return [{"q": q, "hits": query(q, limit=limit, corpus=docs)} for q in queries]
