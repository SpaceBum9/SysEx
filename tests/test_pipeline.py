"""A4B -> AMB -> GARAS -> ATM -> stamp. CLA theme, NIKITA applied."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from packet import compose  # noqa: E402


class PipelineTests(unittest.TestCase):
    def test_compose_carries_a4b_and_amb(self) -> None:
        p = compose("read health", verb="sync")
        self.assertIn("a4b", p)
        self.assertIn("amb", p)
        self.assertIn("garas", p)
        self.assertIn("atm", p)

    def test_a4b_grok_is_not_xai(self) -> None:
        p = compose("read health")
        self.assertFalse(p["a4b"]["grok_is_xai"])

    def test_execute_is_false(self) -> None:
        p = compose("read health")
        self.assertFalse(p["execute"])
        self.assertTrue(p["trace_verify"]["ok"])


if __name__ == "__main__":
    unittest.main()
