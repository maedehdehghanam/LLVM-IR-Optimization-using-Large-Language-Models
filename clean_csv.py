import pandas as pd


def process_csv(file_path, columns_to_keep):
    df = pd.read_csv(file_path)
    print("Columns in the CSV file:")
    print(df.columns.tolist())

    df = df[columns_to_keep]

    print("\nDataFrame after keeping only the specified columns:")
    print(df.head())

    null_rows = df.isnull().any(axis=1)
    if null_rows.any():
        print("\nRows with null values:")
        print(df[null_rows])
    else:
        print("\nNo rows with null values found.")

    zero_rows = (df == 0).any(axis=1)
    if zero_rows.any():
        print("\nRows with zero values:")
        print(df[zero_rows])
    else:
        print("\nNo rows with zero values found.")

    df.to_csv("dataset/cleaned_optimized_llvm_irs_1000.csv", index=False)
    print("\nModified CSV saved as 'cleaned_optimized_llvm_irs_1000.csv'.")


file_path = "dataset/llvm-irs-optimized-1000.csv"
columns_to_keep = [
    "llvm-ir",
    "llvm-optimized-ir",
]

process_csv(file_path, columns_to_keep)
