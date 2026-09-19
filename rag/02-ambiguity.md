# Ambiguity for SysEx RAG

Do not treat labels as facts.
Pipeline: utterance -> AMB.snapshot -> unresolved stays open -> GARAS.decide -> resolve only if an ATM verb needs it -> persist only with evidence.
Health and technical and speculative tokens require evidence.
Lyric or metaphor tokens stay speculative. Do not write them into runtime state.
Underspecification is allowed. Do not invent a finish.
If two readings remain, RC may ask the next slot. RC may not execute.
Bos levels used here: underspecify, resolve, infer — shrunk to AMB then GARAS then ATM.
Source-grounding alone is not enough; authority must pick which reading may dominate.
