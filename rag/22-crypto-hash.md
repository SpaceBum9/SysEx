# Cryptographic hash

Needed properties: preimage resistance, second-preimage resistance, collision resistance.
SHA-256 (stdlib hashlib) is the only function in SysEx treated as cryptographic. Used for content_sha256.
SHA-3 / SHA-512 / BLAKE2b / BLAKE3 would also qualify; not wired.
MD5 and SHA-1 are broken for collisions — do not add.
FNV-1a and MurmurHash3 are not cryptographic hashes.
A digest is not a signature. Signing would need a key (HMAC or pubkey) and is not in stamp().
