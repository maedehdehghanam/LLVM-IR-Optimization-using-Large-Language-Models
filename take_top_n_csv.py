import pandas as pd


def take_first_n_rows(input_csv_path, output_csv_path, n):
    # Read the input CSV file
    df = pd.read_csv(input_csv_path)

    # Take the first n rows
    df_first_n = df.head(n)

    # Write these rows to a new CSV file
    df_first_n.to_csv(output_csv_path, index=False)


# Example usage
input_csv_path = "exebenh_cleaned_ir.csv"
output_csv_path = "top_n_exebench.csv"
n = int(input())

take_first_n_rows(input_csv_path, output_csv_path, n)
