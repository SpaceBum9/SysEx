"""IVF is rag-only. Packet path stays A4B AMB GARAS ATM stamp."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from packet import compose  # noqa: E402


class PacketNoIvfTests(unittest.TestCase):
    def test_no_ivf_key(self) -> None:
        p = compose("read health", verb="sync")
        self.assertNotIn("ivf", p)
        self.assertIn("a4b", p)
        self.assertIn("garas", p)


if __name__ == "__main__":
    unittest.main()
