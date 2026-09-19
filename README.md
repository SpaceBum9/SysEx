# SysEx

This is the SoS runtime root.

Not a merge of the old fourteen repositories. Those stay where they are.

## Rules

- `execute`: false
- `vendor_live`: false
- `hold`: true
- No credentials in this repository
- No Dual-Allow ballots in-tree
- moreatm.com is blocked on Cloudflare/origin (503). Do not wait on it.

## Run

```bash
python3 src/health.py
python3 -m unittest discover -s tests -v
```

Done means `/health` JSON prints and tests pass. Nothing else is in scope until that stays true.
