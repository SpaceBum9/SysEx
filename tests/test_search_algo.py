import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from search_algo import pick, run  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
