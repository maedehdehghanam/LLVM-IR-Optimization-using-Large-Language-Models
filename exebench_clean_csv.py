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

import pandas as pd

df = pd.read_csv('exebench_codes_llvm_ir.csv')
df.drop(columns=['func_def'], inplace=True)
df = df[df['llvm-ir'].notna()]
df = df[df['llvm-ir'] != 'null']
df.to_csv('exebenh_cleaned_ir.csv', index=False)