# Trace integrity

trace_id = TR- + 16 hex. Random per packet. MUST NOT be derived from anchor text, lyrics, or body.
prev = previous trace_id or null.
content_sha256 = SHA-256 of canonical JSON body excluding trace_id, content_sha256, chain_fnv.
chain_fnv = FNV-1a-64 over prev|trace_id. Collision-resistant: false. Correlation only.
verify fails on bad prefix or body mismatch.
A valid trace does not make a speculative token a fact. AMB still runs first.
W3C traceparent is the public cousin; SysEx keeps TR- locally.
No credentials, no network ids in the packet.
