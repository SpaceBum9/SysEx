# Preimage

Preimage: given h, find m with H(m)=h. Generic cost ~2^n.
Second-preimage: given m, find m'!=m with H(m')=H(m). Generic ~2^n for SHA-2.

SHA-256: no practical preimage. content_sha256 does not reveal the body. verify() is second-preimage style on the canonical JSON.
FNV-1a-64: not one-way. 64-bit ceiling 2^64 brute; structure of xor-then-multiply is invertible per byte if you walk backwards with a target. chain_fnv is not a secret and is computed over prev|trace_id which already sit in the packet.
Murmur3-32: 2^32 brute is cheap. Mixer for tables, not hiding.

Do not store credentials under any of these hashes. A4B RISK_TRACE: hash present != recovered secret != hack.
