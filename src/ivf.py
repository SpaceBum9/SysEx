"""Tiny IVF over rag_vec TF-IDF. In-process. No vendor."""

from __future__ import annotations

from rag_vec import _cos, _load, _tfidf, _tok


def _mean(vecs: list[dict[str, float]]) -> dict[str, float]:
    acc: dict[str, float] = {}
    if not vecs:
        return acc
    for vec in vecs:
        for key, val in vec.items():
            acc[key] = acc.get(key, 0.0) + val
    scale = 1.0 / len(vecs)
    return {key: val * scale for key, val in acc.items()}


def _farthest_init(vecs: list[dict[str, float]], k: int) -> list[dict[str, float]]:
    if not vecs:
        return [{} for _ in range(k)]
    chosen = [0]
    while len(chosen) < k:
        best_i = 0
        best_gap = -1.0
        for i, vec in enumerate(vecs):
            if i in chosen:
                continue
            nearest = max(_cos(vec, vecs[c]) for c in chosen)
            gap = 1.0 - nearest
            if gap > best_gap:
                best_gap = gap
                best_i = i
        chosen.append(best_i)
    return [dict(vecs[i]) for i in chosen]


def train(k: int = 4, rounds: int = 4) -> dict:
    names, vecs = _tfidf(_load())
    k = max(1, min(k, len(vecs) or 1))
    cents = _farthest_init(vecs, k)
    lists: list[list[int]] = [[] for _ in range(k)]
    for _ in range(rounds):
        lists = [[] for _ in range(k)]
        for i, vec in enumerate(vecs):
            best = max(range(k), key=lambda c: _cos(vec, cents[c]))
            lists[best].append(i)
        for c in range(k):
            if lists[c]:
                cents[c] = _mean([vecs[i] for i in lists[c]])
    return {
        "names": names,
        "vecs": vecs,
        "cents": cents,
        "lists": lists,
        "k": k,
    }


def search(q: str, index: dict, nprobe: int = 2, limit: int = 5) -> list[dict]:
    terms = _tok(q)
    if not terms or not index["vecs"]:
        return []
    qv = {t: 1.0 for t in terms}
    nlist = len(index["cents"])
    order = sorted(range(nlist), key=lambda c: -_cos(qv, index["cents"][c]))
    seen: list[int] = []
    for c in order[: max(1, min(nprobe, nlist))]:
        seen.extend(index["lists"][c])
    ranked = sorted(
        (
            {
                "path": index["names"][i],
                "score": round(_cos(qv, index["vecs"][i]), 4),
            }
            for i in seen
        ),
        key=lambda h: (-h["score"], h["path"]),
    )
    return [h for h in ranked if h["score"] > 0][:limit]
