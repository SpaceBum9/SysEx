import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ambiguity import snapshot_many  # noqa: E402


class AmbiguityBatchTests(unittest.TestCase):
    def test_snapshot_many_keeps_input_order(self) -> None:
        texts = ["virus galaxy", "fusion health"]
        results = snapshot_many(texts, "en")

        self.assertEqual([item["text"] for item in results], texts)
        self.assertEqual(len(results), 2)

    def test_snapshot_many_keeps_guard_posture(self) -> None:
        results = snapshot_many(["virus", "fusion"], "en")

        for item in results:
            snap = item["snapshot"]
            self.assertFalse(snap["claims_external_state"])
            self.assertTrue(snap["unresolved"])
            self.assertTrue(snap["disclaimers"])


if __name__ == "__main__":
    unittest.main()
