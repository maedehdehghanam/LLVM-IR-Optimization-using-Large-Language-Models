import base64
import pandas as pd
import subprocess
import ast
import swifter
import dask
from multiprocessing.pool import ThreadPool

df = pd.read_csv("./llvm-irs-optimized-2.csv")
with open("unopt.txt", "w") as file:
    file.write(df["llvm-ir"].iloc[90])


with open("opt.txt", "w") as file:
    file.write(df["llvm-optimized-ir"].iloc[90])
