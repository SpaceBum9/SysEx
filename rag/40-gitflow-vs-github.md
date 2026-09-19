# GitFlow vs GitHub Flow

GitFlow: two long lines (main = prod, develop = integration). feature/* off develop. release/* freeze. hotfix/* off main back to both. Merge traffic high. Good when versions are rare and named.
GitHub Flow: one long line (main). Short topic branch, PR, review, CI, merge, delete. main is always supposed to be deployable. Hotfix is just another short branch.

Delta: GitFlow separates 'what ships' from 'what integrates'. GitHub Flow says they are the same commit on main.
SysEx uses neither ceremony. Direct commits on main (trunk). Closest neighbor is GitHub Flow without the PR step.
