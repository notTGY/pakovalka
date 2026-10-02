import os
import time

import tiktoken
from datasets import load_dataset

seqlen = 4096

start = time.perf_counter_ns()

enc = tiktoken.encoding_for_model("gpt-4o")

ds = load_dataset("HuggingFaceFW/fineweb-edu", "sample-10BT", data_files={"train": [f"sample/10BT/{i:03d}_00000.parquet" for i in range(3)]}, split="train")

print(f"loaded {len(ds)} samples")

os.makedirs("data", exist_ok=True)

with open("data/lengths.csv", "w") as f:
    f.write("Length\n")
    total = 0
    for item in ds:
        length = len(enc.encode(item["text"], disallowed_special=())) + 1  # +1 for EOS separator
        if length > seqlen:
            continue
        f.write(str(length) + "\n")
        total += length
    print(f"Total {total} tokens")

print(f"took {int((time.perf_counter_ns() - start) / 1_000_000_000)}s")
