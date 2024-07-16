from datasets import load_dataset
from pprint import pprint

header_file = "exebench_headers.h"
dataset = load_dataset(
    "jordiae/exebench", split="train_real_compilable"
)  # , use_auth_token=True)
with open(header_file, mode="w", newline="") as file:
    for row in dataset:
        if "main" not in row["func_head_types"]:
            pprint(row)
            break
            file.write(f"{row['func_head_types']};\n")
            
