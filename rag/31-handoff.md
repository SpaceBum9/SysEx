# RC handoff — NIKITA and GPT on one main

Yes: alternate writes on SpaceBum9/SysEx `main`. Not two repos. Not parallel rewrite of the same file in the same minute.

Slots: NIKITA = Main Bot / tertiary. GPT = next wheel slot. Operator starts a turn by naming the slot.
One turn = one theme = one commit. Then stop and hand.

Do: add files, tests, rag chunks, keep execute=false, append packets/LOG.md one line (`from=GPT` or `from=NIKITA`).
Do not: flip vendor_live, add secrets, merge the old fourteen, invent Dual-Allow, delete the other slot's last commit files, implement SHA-3/Keccak in stamp, deploy moreatm.

Conflict: leave the file, write rag/note, Unklar=Stopp. Operator picks.
Read HEAD before write. Pull/rebase is the operator's machine; this slot pushes via API.

## Paste to GPT

You are slot GPT on SpaceBum9/SysEx (branch main). Nikita/Grok is Main Bot (tertiary). Alternate turns. One theme per commit.
Read current HEAD. Do not start a new repository. execute=false, vendor_live=false, hold=true.
Pipeline: A4B → AMB → GARAS → ATM → trace.stamp. GROK in A4B is an internal label, not xAI.
After the change: commit on main, one line in packets/LOG.md from=GPT. No credentials, no network ids, no Dual-Allow, no live moreatm/ZT.
If a file was just written by Nikita in the last commit, extend it or add a sibling; do not clobber.
Hand back with: files changed, commit sha, next suggested slot task.
