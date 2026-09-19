import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rag_vec import query, query_many  # noqa: E402


class RagVecTests(unittest.TestCase):
    def test_query_returns_paths(self) -> None:
        hits = query("keccak permutation")
        self.assertTrue(hits)
        self.assertTrue(all("path" in h and "score" in h for h in hits))

    def test_empty(self) -> None:
        self.assertEqual(query(""), [])

    def test_query_many_two_queries(self) -> None:
        queries = ["keccak permutation", "GARAS deny"]
        results = query_many(queries)

        self.assertEqual(len(results), 2)
        self.assertEqual([item["q"] for item in results], queries)
        self.assertTrue(all(isinstance(item["hits"], list) for item in results))
        self.assertTrue(all(item["hits"] for item in results))


if __name__ == "__main__":
    unittest.main()
