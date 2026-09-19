"""Table names in modules/UNIFICATION.md stay inside runtime.modules."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class UnificationMapTests(unittest.TestCase):
    def test_table_subset(self) -> None:
        runtime = json.loads((ROOT / "config" / "runtime.json").read_text(encoding="utf-8"))
        names = []
        for line in (ROOT / "modules" / "UNIFICATION.md").read_text(encoding="utf-8").splitlines():
            if line.startswith("|") and not line.startswith("|---") and "Module" not in line:
                names.append(line.split("|")[1].strip())
        self.assertTrue(names)
        self.assertTrue(set(names) <= set(runtime["modules"]))


if __name__ == "__main__":
    unittest.main()
