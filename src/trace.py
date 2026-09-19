"""Trace integrity. Correlation is not proof. Hash is not a secret."""

from __future__ import annotations

import hashlib
import json
import secrets
from typing import Any

PREFIX = "TR-"
FNV64_OFFSET = 0xCBF29CE484222325
FNV64_PRIME = 0x100000001B3

EXCLUDE_FROM_HASH = frozenset(
    {
        "content_sha256",
        "trace_id",
        "chain_fnv",
        "chain_fnv_collision_resistant",
        "trace_verify",
    }
)


def new_trace_id() -> str:
    return PREFIX + secrets.token_hex(8)


def is_trace_id(value: str) -> bool:
    if not value.startswith(PREFIX):
        return False
    hexpart = value[len(PREFIX) :]
    return len(hexpart) == 16 and all(c in "0123456789abcdef" for c in hexpart)


def canonical_body(packet: dict[str, Any]) -> bytes:
    body = {k: v for k, v in packet.items() if k not in EXCLUDE_FROM_HASH}
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def content_sha256(packet: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_body(packet)).hexdigest()


def fnv1a_64(data: bytes) -> str:
    h = FNV64_OFFSET
    for byte in data:
        h ^= byte
        h = (h * FNV64_PRIME) & 0xFFFFFFFFFFFFFFFF
    return f"{h:016x}"


def stamp(packet: dict[str, Any], prev: str | None = None) -> dict[str, Any]:
    out = dict(packet)
    out["prev"] = prev
    out["execute"] = False
    out["trace_id"] = new_trace_id()
    out["chain_fnv"] = fnv1a_64(f"{prev or ''}|{out['trace_id']}".encode("utf-8"))
    out["chain_fnv_collision_resistant"] = False
    out["content_sha256"] = content_sha256(out)
    return out


def verify(packet: dict[str, Any]) -> dict[str, Any]:
    tid = packet.get("trace_id")
    if not isinstance(tid, str) or not is_trace_id(tid):
        return {"ok": False, "reason": "bad_trace_id"}

    expected = content_sha256(packet)
    got = packet.get("content_sha256")
    if got != expected:
        return {"ok": False, "reason": "content_mismatch", "expected": expected}

    prev = packet.get("prev")
    expected_chain = fnv1a_64(f"{prev or ''}|{tid}".encode("utf-8"))
    if packet.get("chain_fnv") != expected_chain:
        return {
            "ok": False,
            "reason": "chain_mismatch",
            "expected": expected_chain,
        }

    return {"ok": True, "trace_id": tid, "content_sha256": expected}
