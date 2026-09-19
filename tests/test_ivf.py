"""Local IVF over rag TF-IDF."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ivf import search, train  # noqa: E402


class IvfTests(unittest.TestCase):
    def test_train_and_hit(self) -> None:
        idx = train(k=4, rounds=3)
        self.assertEqual(len(idx["lists"]), 4)
        hits = search("HNSW efSearch", idx, nprobe=2, limit=5)
        self.assertTrue(hits)
        self.assertGreater(hits[0]["score"], 0)


if __name__ == "__main__":
    unittest.main()
