import os
import time

import tiktoken
from datasets import load_dataset

seqlen = 4096

start = time.perf_counter_ns()

enc = tiktoken.encoding_for_model("gpt-4o")

ds = load_dataset("HuggingFaceFW/fineweb-edu", "sample-10BT", data_files={"train": [f"sample/10BT/{i:03d}_00000.parquet" for i in range(3)]}, split="train")

print(f"loaded {len(ds)} samples")


def tokenize(batch):
    return {
        "length": [
            len(enc.encode(text, disallowed_special=())) + 1  # +1 for EOS separator
            for text in batch["text"]
        ]
    }


ds = ds.map(tokenize, batched=True, num_proc=1, remove_columns=ds.column_names)

os.makedirs("data", exist_ok=True)

with open("data/lengths.csv", "w") as f:
    f.write("Length\n")
    total = 0
    for item in ds:
        length = item["length"]
        if length > seqlen:
            continue
        f.write(str(length) + "\n")
        total += length
    print(f"Total {total} tokens")

print(f"took {int((time.perf_counter_ns() - start) / 1_000_000_000)}s")
