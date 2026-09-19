# IVF tune

k ~ sqrt(n) is a common start on large sets. nprobe trades recall vs lists scanned.
Retrain after the corpus shifts. Empty lists: lower k or change init.
On SysEx rag size, default --k 4 --nprobe 2 is a sketch. Brute remains default.
