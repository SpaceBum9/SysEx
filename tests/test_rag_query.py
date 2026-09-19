import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rag_query import query  # noqa: E402


class RagQueryTests(unittest.TestCase):
    def test_a4b_hits_arch(self) -> None:
        hits = query("A4B router")
        names = [h["path"] for h in hits]
        self.assertTrue(any("a4b" in n or "13" in n for n in names))

    def test_empty(self) -> None:
        self.assertEqual(query(""), [])


if __name__ == "__main__":
    unittest.main()
