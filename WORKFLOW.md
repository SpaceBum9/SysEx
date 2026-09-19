# Workflow

Analyse → consolidate → iterate ×3 → ingest into RAG → next

Plus: **compose after every answer** (operator rule 2026-09-19).

This five-step chain is **Pflicht** when a trigger below matches. It is **not** run on every chat turn.
Compose is Pflicht on every substantive answer.

## Compose after every answer

After the reply, write into SpaceBum9/SysEx:

- durable rule or protocol → `rag/` or `lexicon/` or `src/`
- this-turn envelope → append one line to `packets/LOG.md`
- verb is `sync` unless the operator named another ATM verb
- execute stays false; no credentials; no network ids

Skip compose only for empty greetings with no content. When in doubt: compose.

Use `src/packet.py` compose() fields: from, to, verb, text, garas class, trace later if stamped locally.
Do not dump full chat transcripts into git.

## Actor provenance

Direct writer commits on `main` must end with exactly one machine-readable trailer:

```text
Actor: GRK
```

or:

```text
Actor: GPT
```

The GitHub account author is transport identity, not slot identity. Slot automation reads the `Actor:` trailer and the matching `packets/LOG.md` entry. A writer must append exactly one log line with the same actor for its turn. Missing, duplicate, or contradictory actor provenance is `Unklar=Stopp`.

## When Pflicht (must run all five steps)

Run the full chain if **any** of these is true:

1. New corpus arrives (ZIP, dump, GPT/Nikita pack, Drive folder, pasted multi-file set).
2. More than one source must be unified into SysEx (repos, modules, lexicon, traces).
3. Something is about to be written into `rag/` or the Notion RAG mirror.
4. Operator says ingest, consolidate, unify, or "into SysEx".
5. A named module changes meaning (MCT ATM RC GARAS BILO ZT AMB I18N) or a new module is proposed.

If several triggers fire at once: still **one** chain, not three parallel ones.

## When not Pflicht (do not fake three iterates)

- Yes/no or definition questions ("was ist X", "nutzt du den workflow").
- Status of one known surface (moreatm 503, ZT not ready).
- Single-file edit already in SysEx with no new source.
- Small talk, greetings, connector checks.

Then: answer **and compose** (log + any one-line rule). Do not invent inventory/cut/chunk passes.

## Steps

### 1. Analyse

Read what exists. Name roles. Separate running from paper. Do not invent live surfaces. Do not treat labels as facts.

### 2. Consolidate

One kernel (SysEx). Named modules only. Old MCT repos stay provenance. No merge of the fourteen. No new repo for a folder.

### 3. Iterate ×3

1. Inventory — claimed vs actual.
2. Cut — drop mega-mode, fake-live flags, ballots-as-product, credentials.
3. Chunk — one topic per retrieval unit.

Skip a pass only if that pass would be empty; say so in the ingest note.

### 4. Ingest into RAG

Embed only `rag/` plus numbered chunks. Git is source of truth.

### 5. Next

One action still outside git, or the next Pflicht trigger. Not a new repository.

## Law

- execute = false
- vendor_live = false
- hold = true
- no credentials in git
- no network ids in git
- label ≠ fact
- actors communicate non-anthropomorphic
- pronouns are non-ontologic
- compose after every answer
