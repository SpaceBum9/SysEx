import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ambiguity import snapshot  # noqa: E402
from atm import handle  # noqa: E402
from garas import decide  # noqa: E402
from health import health  # noqa: E402
from i18n import t  # noqa: E402
from rc import next_slot  # noqa: E402
from zero_tier import status as zt_status  # noqa: E402


class UnificationTests(unittest.TestCase):
    def test_health(self) -> None:
        payload = health()
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["name"], "SysEx")
        self.assertEqual(payload["purpose"], "unification")
        self.assertFalse(payload["execute"])
        self.assertTrue(payload["hold"])
        self.assertIn("ZT", payload["modules"])
        self.assertFalse(payload["atm"]["ready"])
        self.assertFalse(payload["zero_tier"]["joined"])
        json.dumps(payload)

    def test_atm_execute_denied(self) -> None:
        self.assertEqual(handle("initialize")["status"], "accepted")
        self.assertEqual(handle("execute")["status"], "denied")

    def test_garas_denies_money(self) -> None:
        self.assertEqual(decide("transfer funds")["decision"], "deny")
        self.assertEqual(decide("read health")["decision"], "allow")

    def test_rc_and_i18n(self) -> None:
        self.assertEqual(next_slot(0)["slot"], "GPT")
        self.assertEqual(t("hold", "de"), "Halten")

    def test_ambiguity_no_external_fact(self) -> None:
        snap = snapshot("virus galaxy", "en")
        self.assertFalse(snap["claims_external_state"])
        self.assertTrue(snap["disclaimers"])

    def test_zero_tier_not_fake_live(self) -> None:
        z = zt_status()
        self.assertTrue(z["needed"])
        self.assertFalse(z["joined"])
        self.assertFalse(z["mcp_live"])


if __name__ == "__main__":
    unittest.main()
