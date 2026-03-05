# generally just google python 3 <what i want to do>, works mostly
# specifically look at https://docs.python.org/3/library/functions.html

import os
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Parse CSVs")
    parser.add_argument("file", help="The CSV-file")
    args = parser.parse_args()

    filepath = Path(args.file)
    if not filepath.exists():
        print("File does not exist")
        sys.exit(1)

    fd = filepath.open("r")
    data = fd.read()
    fd.close()

    csv_data = dict()

    for line in data.splitlines(keepends=False):
        values = line.split(",")
        values = [v.strip() for v in values]
        csv_data[len(csv_data)] = values

    if not csv_data:
        print("Empty file")
        sys.exit(1)

    for line_number, values in csv_data.items():
        print(f"{line_number}: {'\t\t'.join(values)}")

if __name__ == "__main__":
    main()