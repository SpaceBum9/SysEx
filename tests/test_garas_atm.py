"""GARAS before ATM on compose(). Sibling to test_pipeline."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from packet import compose  # noqa: E402


class GarasAtmTests(unittest.TestCase):
    def test_sync_has_both(self) -> None:
        p = compose("read health", verb="sync")
        self.assertIn("garas", p)
        self.assertIn("atm", p)
        self.assertEqual(p["garas"]["decision"], "allow")
        self.assertEqual(p["atm"]["status"], "accepted")
        self.assertFalse(p["execute"])

    def test_execute_denied(self) -> None:
        p = compose("read health", verb="execute")
        self.assertEqual(p["garas"]["decision"], "deny")
        self.assertEqual(p["atm"]["status"], "denied")
        self.assertFalse(p["execute"])


if __name__ == "__main__":
    unittest.main()
