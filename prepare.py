import os
import time

import tiktoken
from datasets import load_dataset

start = time.perf_counter_ns()

enc = tiktoken.encoding_for_model("gpt-4o")

ds = load_dataset("nilq/babylm-10M", split="train")

print(f"loaded {len(ds)} samples")

os.makedirs("data", exist_ok=True)

with open("data/babylm-10M.csv", "w") as f:
    f.write("Id, Length\n")
    total = 0
    for index, item in enumerate(ds):
        length = len(enc.encode(item["text"])) + 1  # +1 for EOS separator
        f.write(str(index) + ", " + str(length) + "\n")
        total += length
    print(f"Total {total} tokens")

print(f"took {int((time.perf_counter_ns() - start) / 1_000_000_000)}s")
