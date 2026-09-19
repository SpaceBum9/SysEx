import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from garas import classify, decide  # noqa: E402


class GarasBoundaryTests(unittest.TestCase):
    def test_border_is_not_order(self) -> None:
        self.assertEqual(classify("border check"), "OBSERVE")
        self.assertEqual(decide("border check")["decision"], "allow")

    def test_order_still_denies(self) -> None:
        self.assertEqual(decide("place order")["decision"], "deny")


if __name__ == "__main__":
    unittest.main()
