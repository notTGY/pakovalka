seqlen = 4096
theoretical_minimum_batches = 14065472 / seqlen

with open("data/babylm-10M.csv", "r") as f:
    lines = f.readlines()
    N = len(lines) - 1
    lengths = [int(s.split(", ")[1]) for s in lines[1:]]

packed = set()
with open("output.txt", "r") as f:
    lines = f.readlines()
    n = len(lines)
    for s in lines:
        seq = [int(s) for s in s.split()]
        assert max(seq) < N or min(seq) < 0, "Index out of range"
        packed.update(seq)
        current_seqlen = sum([lengths[i] for i in seq])
        assert current_seqlen <= seqlen, "Sequence longer than seqlen"

assert packed == set(range(N)), "Not all sequences were packed or output corrupted"

speedup = N / n
theoretical_max = N / theoretical_minimum_batches
print(f"speedup against naive: {speedup}; theoretical max: {theoretical_max}")
