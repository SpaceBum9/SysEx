"""packets/NEXT.md is the handoff bus."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEXT = ROOT / "packets" / "NEXT.md"
SLOTS = {"GRK", "GPT", "NIKITA"}


class NextBusTests(unittest.TestCase):
    def test_keys(self) -> None:
        text = NEXT.read_text(encoding="utf-8")
        fields = {}
        for line in text.splitlines():
            if ":" in line and not line.startswith("#"):
                key, _, val = line.partition(":")
                fields[key.strip()] = val.strip()
        self.assertIn(fields.get("to"), SLOTS)
        self.assertIn(fields.get("from"), SLOTS)
        self.assertTrue(fields.get("theme"))
        self.assertIn("execute=false", fields.get("constraints", ""))


if __name__ == "__main__":
    unittest.main()
