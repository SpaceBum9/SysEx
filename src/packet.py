"""SysEx packet: envelope + A4B/AMB + GARAS + ATM + trace."""

from __future__ import annotations

from ambiguity import snapshot
from atm import handle as atm_handle
from garas import decide as garas_decide
from rc import next_slot
from trace import stamp, verify


def compose(
    text: str,
    verb: str = "sync",
    sender: str = "operator",
    lang: str = "de",
    prev: str | None = None,
    slot_index: int = 0,
) -> dict:
    amb = snapshot(text, lang)
    policy = garas_decide(f"{verb} {text}")
    atm = atm_handle(verb)
    rc = next_slot(slot_index)
    raw = {
        "schema": "sysex.packet.v0",
        "from": sender,
        "to": rc["slot"],
        "tertiary": "NIKITA",
        "lang": lang,
        "verb": verb,
        "text": text,
        "amb": amb,
        "garas": policy,
        "atm": atm,
        "rc": rc,
        "execute": False,
        "live_write": False,
    }
    packet = stamp(raw, prev=prev)
    packet["trace_verify"] = verify(packet)
    return packet
