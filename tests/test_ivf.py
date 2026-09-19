"""Local IVF over rag TF-IDF."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ivf import search, train  # noqa: E402


class IvfTests(unittest.TestCase):
    def test_train_covers_all(self) -> None:
        idx = train(k=4, rounds=3)
        self.assertEqual(idx["k"], 4)
        self.assertEqual(len(idx["cents"]), 4)
        assigned = sum(len(lst) for lst in idx["lists"])
        self.assertEqual(assigned, len(idx["names"]))

    def test_search_hits(self) -> None:
        idx = train(k=4, rounds=3)
        hits = search("HNSW efSearch", idx, nprobe=2, limit=5)
        self.assertTrue(hits)
        self.assertGreater(hits[0]["score"], 0)

    def test_empty_query(self) -> None:
        idx = train(k=2, rounds=1)
        self.assertEqual(search("", idx), [])


if __name__ == "__main__":
    unittest.main()
