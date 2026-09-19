# ATM cells vs SysEx ATM

Telecom ATM: 53-byte cells, VPI/VCI labels, TDM-like mux on a wire.
SysEx ATM: four verbs on an automaton. No cells, no VPI, no mux fabric.
RC next_slot is the only sequencer. Not a cell scheduler.
