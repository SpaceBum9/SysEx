# GARAS impl

src/garas.py: token scan on lowercased intent. Hits money|transfer|order|vendor|credential|destroy|execute -> deny.
classify prefers EXECUTE if present else first mapped class else OBSERVE.
decide returns decision, reason, hits, intent_class.
Wired in packet.compose before ATM. No ledger. No chain. Door only.
