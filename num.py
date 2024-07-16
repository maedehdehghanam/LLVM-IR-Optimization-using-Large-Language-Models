import csv

with open("exebench_codes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))
        break
