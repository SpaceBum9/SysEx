# RC handoff

Write slots with git connector: NIKITA, GPT.
Review slot without connector: GEM. GEM does not push.

Ring: NIKITA → GPT → GEM-bundle → NIKITA applies bundle → NIKITA.
Repo: SpaceBum9/SysEx main. One theme per write-slot commit.
NIKITA = Main Bot / tertiary.

GEM output format only:
- path
- full file content or unified diff
- LOG line from=GEM (applied by the write slot)
No live git, no secrets, execute=false.

## Paste GPT → GEM

Slot GEM has no GitHub connector. Do not ask GEM to commit.
Give GEM: HEAD sha <sha>, theme <line>, file excerpts it must see.
GEM returns paths + full files or diffs. Operator or NIKITA applies and commits from=GEM.

## Paste to GEM

You are slot GEM on SysEx. No git access. Nikita is Main Bot.
You receive HEAD sha and excerpts. Reply with a bundle only: list of {path, content} or unified diffs.
Constraints: execute=false, no secrets, no new repo, no Dual-Allow, do not invent live moreatm/ZT.
Do not claim a commit sha. End with: apply-slot=NIKITA next-theme=<one line>.
