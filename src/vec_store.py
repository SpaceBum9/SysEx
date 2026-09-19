"""Vector store port. Only memory is live. Vendor names raise."""

from __future__ import annotations

import math

DENIED = {
    "pinecone",
    "weaviate",
    "qdrant",
    "chroma",
    "milvus",
    "pgvector",
    "lancedb",
    "faiss",
    "annoy",
    "scann",
}


def _cos(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values())) or 1.0
    nb = math.sqrt(sum(v * v for v in b.values())) or 1.0
    return dot / (na * nb)


class MemoryStore:
    def __init__(self) -> None:
        self.rows: list[tuple[str, dict[str, float]]] = []

    def add(self, doc_id: str, vec: dict[str, float]) -> None:
        self.rows.append((doc_id, dict(vec)))

    def search(self, vec: dict[str, float], k: int = 5) -> list[dict]:
        ranked = sorted(
            (
                {"id": doc_id, "score": round(_cos(vec, item), 4)}
                for doc_id, item in self.rows
            ),
            key=lambda h: (-h["score"], h["id"]),
        )
        return [h for h in ranked if h["score"] > 0][:k]


def open_store(name: str = "memory"):
    key = name.lower().strip()
    if key in DENIED:
        raise RuntimeError("vendor_live=false")
    if key != "memory":
        raise RuntimeError("unknown_store")
    return MemoryStore()
