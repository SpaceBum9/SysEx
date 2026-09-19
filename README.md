# SysEx

SoS unification root. One process, named modules, no extra MCT repos.

## Modules

| Id | Job |
|---|---|
| MCT | this kernel |
| ATM | public verbs + moreatm.com surface |
| RC | who speaks next |
| GARAS | allow / deny / reason |
| BILO | lexicon + score, not statute |
| ZT | ZeroTier overlay (declared, not joined) |
| AMB | ambiguity / claim guard |
| I18N | de en fr pl ko gs |

`execute=false`. `vendor_live=false`. `hold=true`. No credentials.

moreatm.com is the ATM hostname when Cloudflare origin works (today: 503). Fallback: this repo.

ZeroTier is the private lane between nodes. Until a network id is configured locally (never committed), ZT status is `disconnected`.

## Run

```bash
python3 src/health.py
python3 -m unittest discover -s tests -v
```
