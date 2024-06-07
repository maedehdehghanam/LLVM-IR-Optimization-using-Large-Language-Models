import base64
import pandas as pd
import subprocess
import ast 
import swifter
import dask
from multiprocessing.pool import ThreadPool
dask.config.set(pool = ThreadPool(20))
def dis(bytecode:str) -> str:
    bytecode_b = ast.literal_eval(bytecode)
    dis_command_vector = ['llvm-dis', '-']
    with subprocess.Popen(
    dis_command_vector,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    stdin=subprocess.PIPE) as dis_process:
        output = dis_process.communicate(input= (bytecode_b))[0].decode('utf-8')
        return output
column_names = ['content', 'language', 'package_source'] 
data_types = {'content': str, 'language':str , 'package_source':str}
df = pd.read_csv("dataset/bytecodes.csv", header=None, names=column_names,dtype=data_types)
df.info()
df['llvm-ir'] =  df['content'].apply(dis)
df = df.drop('content', axis = 1)
df.to_csv('dataset/llvm-irs.csv', index=False)
