# RC handoff — NIKITA, GPT, GEM on one main

Ring: NIKITA → GPT → GEM → NIKITA. Operator may skip a slot.
Repo: SpaceBum9/SysEx, branch main only. One turn = one theme = one commit.
NIKITA = Main Bot / tertiary. GPT and GEM are wheel slots, not tertiary.

Do: read HEAD, add sibling files, tests, rag chunks, packets/LOG.md line with from=NIKITA|GPT|GEM.
Do not: new repo, execute=true, vendor_live, secrets, Dual-Allow, clobber the previous slot's last files, deploy moreatm/ZT, stamp()=SHA-3.
Conflict: leave file, Unklar=Stopp, operator picks.

## Paste GPT → GEM (GPT says this at end of turn)

Hand to slot GEM on SpaceBum9/SysEx main. HEAD sha: <sha>. Theme done: <one line>. Next theme: <one line>. Constraints unchanged: execute=false hold=true no secrets no new repo. GEM reads HEAD then one commit, LOG from=GEM, hand back to NIKITA.

## Paste to GEM

You are slot GEM on SpaceBum9/SysEx (branch main). Nikita/Grok is Main Bot (tertiary). Incoming handoff from GPT.
Read current HEAD. One theme per commit. execute=false, vendor_live=false, hold=true.
Pipeline: A4B → AMB → GARAS → ATM → trace.stamp. GROK in A4B is internal, not xAI.
Commit on main. packets/LOG.md line from=GEM. No credentials, no Dual-Allow, no live moreatm/ZT, no new repository.
Do not clobber the files from the GPT or NIKITA commit you just read. Extend or add a sibling.
Hand back to NIKITA with: files changed, commit sha, next suggested slot task.
