# Keccak-f permutation

State: 5x5 lanes of w bits. Width b=25w. SHA-3 uses Keccak-f[1600]: w=64, 24 rounds.
Round R = iota ∘ chi ∘ pi ∘ rho ∘ theta.
theta: column parity mix (diffusion).
rho: lane rotations by fixed offsets.
pi: lane permutation (x,y) -> (y, 2x+3y).
chi: nonlinear, bitwise ~a & b in each row.
iota: XOR round constant into lane (0,0).
Sponge: absorb into rate r, permute, squeeze. SHA3-256: r=1088, c=512, 256-bit out.
Not wired in SysEx stamp(). hashlib.sha3_256 is the stdlib sponge if ever swapped.
