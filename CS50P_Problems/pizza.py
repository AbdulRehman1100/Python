import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

table = []
try:
    with open(sys.argv[1]) as f:
        # for x in f:
        #     table.append(x.split(","))
        reader = csv.reader(f)
        for row in reader:
            table.append(row)
except FileNotFoundError:
    sys.exit("File does not exit")

print(tabulate(table, headers = "firstrow", tablefmt = "grid"))
    