import csv
import sys

from stats import is_empty, pretty_print


def load_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        return [float(row["value"]) for row in reader if row["value"].strip()]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_dataset.py <path-to-csv>")
        sys.exit(1)

    path = sys.argv[1]
    numbers = load_csv(path)

    if is_empty(numbers):
        print(f"Dataset '{path}' is empty — nothing to compute.")
    else:
        print(f"Dataset: {path}\n")
        pretty_print(numbers)
