# ATM cells vs SysEx ATM

Telecom ATM: 53-byte cells, VPI/VCI labels, TDM-like mux on a wire.
VPI = path (bundle of circuits). VCI = circuit inside that path. Switch may rewrite both.
SysEx ATM: four verbs. No cells, no VPI, no mux fabric.
Closest SysEx labels: packet.from / packet.to / rc.slot — not a cell header.
