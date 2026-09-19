# Hash roles in SysEx

| | SHA-256 | FNV-1a-64 | MurmurHash3 x86_32 |
|---|---|---|---|
| file | trace.content_sha256 | trace.chain_fnv | murmur.murmur3_32 |
| job | packet body unchanged | prev\|trace_id chain | fast lookup / bucket |
| bits | 256 | 64 | 32 |
| crypto | yes (preimage/collision resistance for this use) | no | no |
| seed | n/a | fixed offset | optional seed |
| stamp | yes | yes | not wired |
| collision_resistant claim | treat as integrity check | false | false |

Do not swap SHA for FNV or Murmur on verify().
A4B: TRACE marker ≠ hack. Hash match ≠ fact.
