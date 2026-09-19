# SysEx

SoS kernel. Unification. execute=false.

```bash
python3 -m unittest discover -s tests -q
python3 scripts/compose.py read health --verb sync
python3 scripts/rag_query.py A4B GARAS
# optional: python3 scripts/health_server.py   # 127.0.0.1:8787/health
```

Modules: MCT ATM RC GARAS BILO AMB A4B I18N ZT.
Packet: A4B → AMB → GARAS → ATM → stamp.
moreatm and ZeroTier stay outside git until ready.
