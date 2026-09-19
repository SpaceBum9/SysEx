# efConstruction

Build-time candidate width. Higher: better edges, slower build, more RAM during insert.
Typical start 100-200. Sweep 64, 100, 200, 400 against a frozen efSearch.
If recall still low after high efSearch: raise M first, then efConstruction, rebuild once.
SysEx does not set it.
