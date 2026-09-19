import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from i18n import t, translate_many  # noqa: E402


class I18NTests(unittest.TestCase):
    def test_translate_many_keeps_order(self) -> None:
        keys = ["hold", "health", "missing"]
        results = translate_many(keys, "de")

        self.assertEqual([item["key"] for item in results], keys)
        self.assertEqual(
            [item["value"] for item in results],
            ["Halten", "Status", "missing"],
        )

    def test_unknown_language_falls_back_to_english(self) -> None:
        self.assertEqual(t("denied", "xx"), "denied")
        self.assertEqual(
            translate_many(["hold", "health"], "xx"),
            [
                {"key": "hold", "value": "Hold"},
                {"key": "health", "value": "health"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
