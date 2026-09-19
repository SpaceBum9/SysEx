# Auto handoff

Bus: packets/NEXT.md on main. Not a chat.
sysex-github-delta fires on push and runs GRK in a separate session. It does not start GPT.
GPT starts only if that product polls NEXT.md or the operator pastes it.
Closed loop needs two wakeups: GitHub trigger (GRK) + GPT-side schedule/action on the same file.
Until GPT polls, operator paste remains the second half.
execute=false. Empty theme = stop.
