import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as input_f:
        with open(sys.argv[2], "w") as output_f:
            reader = csv.reader(input_f) # return iterator
            next(reader) # skip header of input file
            writer = csv.writer(output_f)
            writer.writerow(["first", "last", "house"])
            for row in reader:
                first_name, last_name = row[0].split(",")
                writer.writerow([first_name, last_name.strip(), row[1]])

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")