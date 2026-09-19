import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from murmur import murmur3_32, murmur3_32_hex  # noqa: E402


class MurmurTests(unittest.TestCase):
    def test_vectors_seed0(self) -> None:
        self.assertEqual(murmur3_32(b""), 0)
        self.assertEqual(murmur3_32_hex(b"hello"), "248bfa47")
        self.assertEqual(murmur3_32_hex(b"hello world"), "5e928f0f")

    def test_seed_changes(self) -> None:
        self.assertNotEqual(murmur3_32(b"hello", 0), murmur3_32(b"hello", 1))


if __name__ == "__main__":
    unittest.main()
