from datasets import load_dataset

import csv

csv_file = "exebench_codes.csv"
dataset = load_dataset(
    "jordiae/exebench", split="train_real_compilable"
)  # , use_auth_token=True)
column_name = "func_def"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[column_name])
    for row in dataset:
        writer.writerow(
            {column_name: "".join(str(row["synth_deps"]) + "\n" + "".join(row["func_def"]))}
        )
