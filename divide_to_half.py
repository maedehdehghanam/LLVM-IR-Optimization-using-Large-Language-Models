import pandas as pd


csv_file = 'exebench-llvm-irs-loop-optimized.csv'
df = pd.read_csv(csv_file)


midpoint = len(df) // 2

first_half = df.iloc[:midpoint]
second_half = df.iloc[midpoint:]

first_half.to_csv('exebench_first_half.csv', index=False)
second_half.to_csv('exebench_second_half.csv', index=False)

print("CSV file has been split into 'exebench_first_half.csv' and 'exebench_second_half.csv'")
