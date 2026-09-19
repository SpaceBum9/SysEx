# Collision resistance

Birthday bound ~ 2^(n/2) random trials for n-bit output.

SHA-256: n=256 → ~2^128 work. No practical collision published. Used for content_sha256 / verify().
FNV-1a-64: n=64 → ~2^32 random; adversarial collisions cheap. Flag collision_resistant=false. Chain only.
MurmurHash3 x86_32: n=32 → ~2^16 random; crafted keys collide on purpose (hash-flood). Seed mitigates buckets, not an attacker who picks both messages.

Packet implication: two different bodies sharing chain_fnv or murmur is expected at scale. Two different canonical bodies sharing content_sha256 is the event verify() treats as impossible for this system.
Excluded stamp fields (trace_id, fnv meta, trace_verify) are not in the SHA body — that is domain split, not a SHA break.
