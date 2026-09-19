import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from search_algo import pick, run, run_many  # noqa: E402


class SearchAlgoTests(unittest.TestCase):
    def test_pick_live(self) -> None:
        self.assertEqual(pick("flat"), "brute")
        self.assertEqual(pick("ivf"), "ivf")

    def test_hnsw_not_wired(self) -> None:
        with self.assertRaises(RuntimeError):
            pick("hnsw")

    def test_run_brute(self) -> None:
        hits = run("brute", "GARAS")
        self.assertTrue(hits)

    def test_run_many_brute_keeps_query_shape(self) -> None:
        queries = ["GARAS", "keccak permutation"]
        results = run_many("brute", queries, limit=3)

        self.assertEqual([item["q"] for item in results], queries)
        self.assertTrue(all("hits" in item for item in results))
        self.assertTrue(all(len(item["hits"]) <= 3 for item in results))

    def test_run_many_ivf_keeps_query_shape(self) -> None:
        queries = ["GARAS", "A4B"]
        results = run_many("ivf", queries, limit=2)

        self.assertEqual([item["q"] for item in results], queries)
        self.assertTrue(all("hits" in item for item in results))
        self.assertTrue(all(len(item["hits"]) <= 2 for item in results))


if __name__ == "__main__":
    unittest.main()
