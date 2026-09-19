import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from trace import content_sha256, fnv1a_64, is_trace_id, stamp, verify  # noqa: E402


class TraceTests(unittest.TestCase):
    def test_fnv_vectors(self) -> None:
        self.assertEqual(fnv1a_64(b""), "cbf29ce484222325")
        self.assertEqual(fnv1a_64(b"a"), "af63dc4c8601ec8c")
        self.assertEqual(fnv1a_64(b"foobar"), "85944171f73967e8")

    def test_id_not_from_body(self) -> None:
        a = stamp({"text": "hallo", "verb": "sync"})
        b = stamp({"text": "hallo", "verb": "sync"})
        self.assertTrue(is_trace_id(a["trace_id"]))
        self.assertNotEqual(a["trace_id"], b["trace_id"])
        self.assertEqual(a["text"], b["text"])

    def test_verify_roundtrip(self) -> None:
        p = stamp({"text": "hallo", "from": "operator"})
        self.assertTrue(verify(p)["ok"])

    def test_tamper_detected(self) -> None:
        p = stamp({"text": "hallo"})
        p["text"] = "hallos"
        self.assertFalse(verify(p)["ok"])
        self.assertEqual(verify(p)["reason"], "content_mismatch")

    def test_same_body_same_hash(self) -> None:
        p = {"text": "x", "verb": "halt", "prev": None}
        self.assertEqual(content_sha256(p), content_sha256(dict(p)))

    def test_fnv_not_claimed_strong(self) -> None:
        p = stamp({"text": "x"})
        self.assertFalse(p["chain_fnv_collision_resistant"])


if __name__ == "__main__":
    unittest.main()
