"""Named ANN families. Only brute and ivf run here."""

from __future__ import annotations

from ivf import search, search_many, train
from rag_vec import query, query_many

KNOWN = ("brute", "ivf", "hnsw", "lsh", "pq", "scann", "flat")
LIVE = ("brute", "ivf", "flat")


def pick(name: str) -> str:
    key = name.lower().strip()
    if key == "flat":
        key = "brute"
    if key not in KNOWN:
        raise ValueError("unknown_algo")
    if key not in LIVE:
        raise RuntimeError("algo_not_wired")
    return key


def run(name: str, q: str, limit: int = 5) -> list[dict]:
    algo = pick(name)
    if algo == "ivf":
        return search(q, train(), limit=limit)
    return query(q, limit=limit)


def run_many(name: str, queries: list[str], limit: int = 5) -> list[dict]:
    algo = pick(name)
    if algo == "ivf":
        return search_many(queries, limit=limit)
    return query_many(queries, limit=limit)
