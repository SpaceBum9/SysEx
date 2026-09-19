import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from a4b import route, route_many  # noqa: E402
from packet import compose  # noqa: E402


class A4BTests(unittest.TestCase):
    def test_selfhood_blocked(self) -> None:
        r = route("I AM alive")
        self.assertEqual(r["class"], "SELFHOOD_BLOCKED")
        self.assertEqual(r["next"], "drop_claim")
        self.assertFalse(r["grok_is_xai"])

    def test_exec_boundary(self) -> None:
        self.assertEqual(route("please execute now")["next"], "deny_execute")

    def test_route_many_keeps_order_and_shape(self) -> None:
        texts = ["please execute now", "rag context", "xx"]
        results = route_many(texts)

        self.assertEqual([item["text"] for item in results], texts)
        self.assertEqual(results[0]["route"]["next"], "deny_execute")
        self.assertEqual(results[1]["route"]["class"], "SOURCE_RAG")
        self.assertFalse(results[2]["route"]["grok_is_xai"])

    def test_compose_carries_a4b(self) -> None:
        p = compose("read health")
        self.assertIn("a4b", p)
        self.assertTrue(p["trace_verify"]["ok"])


if __name__ == "__main__":
    unittest.main()
