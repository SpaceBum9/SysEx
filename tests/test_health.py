import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from health import health  # noqa: E402


class HealthTests(unittest.TestCase):
    def test_health_shape(self) -> None:
        payload = health()
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["name"], "SysEx")
        self.assertEqual(payload["role"], "sos-root")
        self.assertFalse(payload["execute"])
        self.assertFalse(payload["vendor_live"])
        self.assertTrue(payload["hold"])
        self.assertEqual(payload["default"], "denied")
        self.assertFalse(payload["live_rail"])
        json.dumps(payload)


if __name__ == "__main__":
    unittest.main()
