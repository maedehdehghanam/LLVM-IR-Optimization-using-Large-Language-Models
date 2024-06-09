import csv
import sys


def read_csv_columns(file_path):
    max_int = sys.maxsize
    while True:
        try:
            csv.field_size_limit(max_int)
            break
        except OverflowError:
            max_int = int(max_int / 10)
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        col1, col2 = [], []

        for row in reader:
            if len(row) < 2:
                raise ValueError("CSV file must have at least two columns")
            col1.append(row[0])
            col2.append(row[1])

    return col1, col2


def find_mismatch_index(col1, col2):
    min_len = min(len(col1), len(col2))
    for i in range(min_len):
        if col1[i] != col2[i] and i!=0:
            return i
    # If no mismatch found within the common length, check if lengths are different
    if len(col1) != len(col2):
        return min_len
    return None


def write_columns_to_files(col1, col2, file1_path, file2_path):
    with open(file1_path, "w", newline="") as file1:
        writer = csv.writer(file1)
        for item in col1:
            writer.writerow([item])

    with open(file2_path, "w", newline="") as file2:
        writer = csv.writer(file2)
        for item in col2:
            writer.writerow([item])


def main():
    input_csv = "./dataset/llvm-ir-loop-optimized-llvm-ir-newversion.csv"
    col1, col2 = read_csv_columns(input_csv)

    mismatch_index = find_mismatch_index(col1, col2)

    if mismatch_index is not None:
        print(f"Mismatch found at index: {mismatch_index}")
        write_columns_to_files(col1, col2, "v1.ll", "v2.ll")
    else:
        print(
            "No mismatch found. The columns are of the same length and have the same content."
        )


if __name__ == "__main__":
    main()
