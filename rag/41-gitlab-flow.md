# GitLab Flow advantages

Upstream-first: work lands on main, then is merged into environment branches (staging, production) or into release/*.
Maps branches to environments without GitFlow's develop line.
Issue-to-branch naming is part of the product story.
Hotfixes can go to production then cherry-pick back to main (still explicit).
Less merge theater than GitFlow, more environment truth than GitHub Flow.

Cost: long-lived env branches drift. Needs discipline to merge main into them often.
SysEx has no staging/production deploy, so GitLab Flow adds lines with no environment behind them. Stay on main.
