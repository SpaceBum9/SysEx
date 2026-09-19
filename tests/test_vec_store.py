"""Memory store only."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from vec_store import open_store  # noqa: E402


class VecStoreTests(unittest.TestCase):
    def test_memory_search(self) -> None:
        store = open_store("memory")
        store.add("a", {"hnsw": 1.0})
        store.add("b", {"garas": 1.0})
        hits = store.search({"hnsw": 1.0}, k=1)
        self.assertEqual(hits[0]["id"], "a")

    def test_vendor_denied(self) -> None:
        with self.assertRaises(RuntimeError):
            open_store("pinecone")


if __name__ == "__main__":
    unittest.main()
