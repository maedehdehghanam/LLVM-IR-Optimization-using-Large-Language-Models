import base64
import pandas as pd
import subprocess
import ast
import swifter
import dask
from multiprocessing.pool import ThreadPool

df = pd.read_csv("dataset/llvm-irs.csv")

"""
Explanation of the Order:
    loop-simplify: Prepares loops by simplifying them, making the structure easier for subsequent passes to handle.
    lcssa: Converts loops into a form that is more amenable to transformation.
    loop-rotate: Adjusts the loop to expose opportunities for unrolling and other transformations.
    loop-unroll: Unrolls loops to reduce the overhead and expose more optimization opportunities.
    loop-unroll-and-jam: Further optimizes nested loops by interleaving iterations.
    loop-reduce: Applies strength reduction to optimize arithmetic operations within loops.
    loop-deletion: Cleans up unnecessary loops that might have been simplified out of existence by previous transformations.
This ordering aims to set up the loops for effective transformations and then apply those transformations in a logical sequence that maximizes their effectiveness.
"""


def optimize(llvm_ir: str) -> str:
    pass_pipeline = "loop-simplify,lcssa,loop-rotate,loop-unroll,loop-unroll-and-jam,loop-reduce,loop-deletion"
    command_vector = [
        "opt",
        f"-passes={pass_pipeline}",
        "-S",
    ]
    try:
        with subprocess.Popen(
            command_vector,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
        ) as process:
            # Ensure the input is bytes
            output = process.communicate(input=llvm_ir.encode("utf-8"))[0]
            if process.returncode != 0:
                raise RuntimeError(f"Optimization failed: {errors.decode('utf-8')}")

            return output.decode("utf-8")
    except Exception as e:
        raise RuntimeError(f"An error occurred during optimization: {str(e)}")


df["llvm-optimized-ir"] = df["llvm-ir"].apply(optimize)

df.to_csv("dataset/llvm-irs-loop-optimized.csv", index=False)
