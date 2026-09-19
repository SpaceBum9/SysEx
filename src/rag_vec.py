"""In-memory TF-IDF over rag/. Not Pinecone. Not embeddings-as-a-service."""

from __future__ import annotations

import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "rag"
TOKEN = re.compile(r"[a-z0-9äöüß]+", re.I)


def _tok(text: str) -> list[str]:
    return [m.group(0).lower() for m in TOKEN.finditer(text)]


def _load() -> list[tuple[str, list[str]]]:
    docs: list[tuple[str, list[str]]] = []
    for path in sorted(ROOT.glob("*.md")):
        docs.append((path.name, _tok(path.read_text(encoding="utf-8", errors="replace"))))
    return docs


def _tfidf(docs: list[tuple[str, list[str]]]) -> tuple[list[str], list[dict[str, float]]]:
    df: dict[str, int] = {}
    for _, toks in docs:
        for w in set(toks):
            df[w] = df.get(w, 0) + 1
    n = max(len(docs), 1)
    idf = {w: math.log((n + 1) / (c + 1)) + 1.0 for w, c in df.items()}
    vecs: list[dict[str, float]] = []
    for _, toks in docs:
        tf: dict[str, int] = {}
        for w in toks:
            tf[w] = tf.get(w, 0) + 1
        length = max(len(toks), 1)
        vecs.append({w: (tf[w] / length) * idf[w] for w in tf})
    names = [name for name, _ in docs]
    return names, vecs


def _cos(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values())) or 1.0
    nb = math.sqrt(sum(v * v for v in b.values())) or 1.0
    return dot / (na * nb)


def query(q: str, limit: int = 5) -> list[dict]:
    terms = _tok(q)
    if not terms:
        return []
    docs = _load()
    if not docs:
        return []
    names, vecs = _tfidf(docs)
    qv = {t: 1.0 for t in terms}
    ranked = sorted(
        ({ "path": names[i], "score": round(_cos(qv, vecs[i]), 4) } for i in range(len(names))),
        key=lambda h: (-h["score"], h["path"]),
    )
    return [h for h in ranked if h["score"] > 0][:limit]


def query_many(queries: list[str], limit: int = 5) -> list[dict]:
    results: list[dict] = []
    for q in queries:
        hits = query(q, limit=limit)
        results.append({"q": q, "hits": hits})
    return results
