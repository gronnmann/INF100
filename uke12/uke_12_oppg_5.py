import csv


def write_to_csv(file, rows, newline=""):
    with open(file, "w") as f:
        csv.writer(f).writerows(rows)
