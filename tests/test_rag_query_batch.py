"""Keyword batch loads corpus once."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rag_query import query_many  # noqa: E402


class RagQueryBatchTests(unittest.TestCase):
    def test_two_queries(self) -> None:
        rows = query_many(["GARAS", "HNSW"])
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["q"], "GARAS")
        self.assertTrue(rows[0]["hits"])


if __name__ == "__main__":
    unittest.main()
