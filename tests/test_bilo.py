import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bilo import load, lookup, scan  # noqa: E402


class BiloTests(unittest.TestCase):
    def test_load(self) -> None:
        rows = load()
        self.assertIn("GARAS", rows)
        self.assertFalse(rows["HOLD"]["claims_external_state"])

    def test_lookup(self) -> None:
        row = lookup("atm")
        self.assertIsNotNone(row)
        self.assertEqual(row["token"], "ATM")

    def test_scan(self) -> None:
        hits = scan("hold GARAS execute")
        tokens = {h["token"] for h in hits}
        self.assertIn("GARAS", tokens)
        self.assertIn("HOLD", tokens)


if __name__ == "__main__":
    unittest.main()
