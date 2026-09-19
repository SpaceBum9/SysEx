# Branching

GitFlow: main + develop + feature/release/hotfix. Heavy. Two long-lived lines.
GitHub Flow: branch off main, PR, merge, delete branch. CD often implied.
Trunk-based: short branches or direct main, CI on every push.
Release-train: trunk + release/* cut for freeze.

SysEx: trunk = main only. GRK/GPT commit there. No develop. Feature branches not in use.
CI watches main. Delta automation watches main. Second long-lived branch would split the wheel.
