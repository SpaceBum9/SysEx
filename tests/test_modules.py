"""runtime.json module set."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "config" / "runtime.json"
NEED = {"MCT", "ATM", "RC", "GARAS", "BILO", "ZT", "AMB", "A4B", "I18N", "IVF"}


class ModuleSetTests(unittest.TestCase):
    def test_need(self) -> None:
        data = json.loads(RUNTIME.read_text(encoding="utf-8"))
        self.assertFalse(data["execute"])
        self.assertEqual(set(data["modules"]), NEED)


if __name__ == "__main__":
    unittest.main()
