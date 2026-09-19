# Keccak-f state permutation (π)

State is a[x][y][z], x,y in Z/5Z, z in Z/wZ. π does not touch z.
FIPS 202: a'[x][y][z] = a[x+3y][x][z]  (mod 5 on x,y).
Equivalent send-map: lane (x,y) moves to (y, 2x+3y).
Lane (0,0) is a fixed point of π — same lane iota later hits.
π is a 24-cycle plus that fixed point on the 25 lanes.
Together with ρ (rotations along z) it sends nearby bits onto different columns so θ in the next round mixes them.
Not used in SysEx stamp().
