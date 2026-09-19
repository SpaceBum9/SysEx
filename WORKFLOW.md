# Workflow

Analyse → consolidate → iterate ×3 → ingest into RAG → next

This is **Pflicht** when a trigger below matches. It is **not** run on every chat turn.

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

Then: answer. Optionally name the **next** trigger. Do not invent inventory/cut/chunk passes.

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

Embed only `rag/`:

- `rag/00-kernel.md`
- `rag/01-modules.md`
- `rag/02-ambiguity.md`
- `rag/03-surfaces.md`
- `rag/04-do-not.md`
- plus new numbered chunks when a pass produces them (`05-trace.md`, …)

Git is source of truth. Notion draft is a mirror, not the index.
Do not embed the old fourteen READMEs unless a chunk cites them as provenance.

### 5. Next

One action still outside git, or the next Pflicht trigger. Not a new repository.

## Law for every Pflicht pass

- execute = false
- vendor_live = false
- hold = true
- no credentials in git
- no network ids in git
- label ≠ fact
