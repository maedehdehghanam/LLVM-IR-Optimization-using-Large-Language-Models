import base64
import pandas as pd
import subprocess
import ast
import swifter
import dask
import tempfile
import os
import re
from multiprocessing.pool import ThreadPool

dask.config.set(pool=ThreadPool(20))


def c_to_llvm_ir(c_code: str) -> str:
    c_file_name = None
    llvm_file_name = None

    try:
        c_file = tempfile.NamedTemporaryFile(suffix=".c", delete=False)
        c_file.write(c_code.encode("utf-8"))
        c_file_name = c_file.name
        print(c_file_name)
        llvm_file = tempfile.NamedTemporaryFile(suffix=".ll", delete=False)
        llvm_file_name = llvm_file.name

        compile_command = [
            "clang",
            "-S",
            "-emit-llvm",
            c_file_name,
            "-Xclang",
            "-disable-O0-optnone",
            "-o",
            llvm_file_name,
        ]
        subprocess.run(compile_command, check=True)

        with open(llvm_file_name, "r") as llvm_file:
            llvm_ir = llvm_file.read()
    finally:
        if c_file_name and os.path.exists(c_file_name):
            os.remove(c_file_name)
        if llvm_file_name and os.path.exists(llvm_file_name):
            os.remove(llvm_file_name)

    return llvm_ir

column_names = ['func_def']
data_types = {'func_def': str}
df = pd.read_csv(
    "exebench_codes.csv", header=None, names=column_names, dtype=data_types
)
df.info()

# Remove rows with null values
df = df.dropna(subset=["func_def"])

# Ensure swifter is used correctly
df["llvm-ir"] = df["func_def"].swifter.apply(lambda x: c_to_llvm_ir(str(x)))

# Save the resulting DataFrame to a new CSV file
df.to_csv("exebench_codes_llvm_ir.csv", index=False)
