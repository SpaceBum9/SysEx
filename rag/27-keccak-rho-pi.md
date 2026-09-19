# Keccak-f ρ and π

ρ: rotate lane (x,y) along z by r[x,y] bits. Lane (0,0) rotates 0.
FIPS 202 r[x,y] (rows y=0..4, cols x=0..4):
 y\\x  0  1  2  3  4
 0     0  1 62 28 27
 1    36 44  6 55 20
 2     3 10 43 25 39
 3    41 45 15 21  8
 4    18  2 61 56 14
Offsets = t(t+1)/2 mod w walking the same lane cycle π uses.

π: a'[x,y,z] = a[x+3y, x, z]. Send (x,y) -> (y, 2x+3y). (0,0) fixed.
Order in the round: ρ then π. Bits move in z, then the whole lane jumps on the 5x5.
Next θ sees those bits on new columns.
Not used in SysEx stamp().
