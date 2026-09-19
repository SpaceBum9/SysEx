# Unification map

SysEx owns the names. Old repos stay provenance only.

| Module | Needed for work | Source not copied |
|---|---|---|
| MCT | kernel runtime + health posture | `config/runtime.json` + `src/health.py` |
| ZT | overlay between operator nodes | `packages/zero-tier-connectors` stub (do not reuse fake active MCP flags) |
| ATM | public hostname + four verbs | `moreatm` + `schema/automaton_command.json` |
| AMB | GPT/BILO claim guard | `MCT-2600027/ambiguity-language-guard.ts` rewritten here |
| I18N | RC packet languages | `MCT-2700026` packet.lang |
| GARAS | deny money / vendor / destroy | paper finance ledger left behind |
| RC | next_slot() | PROTOCOL.json wheel, without live_write |
| BILO | lexicon/BILO.md | Universe 05 + lyrics as mnemonic only |
| IVF | local TF-IDF candidate pruning | `scripts/rag_vec.py --ivf`; no vendor index |
| A4B | routing notes and packet boundary | `src/a4b.py` presence, not a live router |

Unification means one health document listing all 10 table rows. It does not mean joining ZeroTier from CI or binding moreatm while it 503s.
