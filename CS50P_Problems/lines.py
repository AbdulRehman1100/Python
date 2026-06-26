import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

count_lines = 0
try:
    with open(sys.argv[1]) as f:
        for x in f:
            if len(x.lstrip()) != 0 and not x.strip().startswith("#"):
                count_lines += 1
except FileNotFoundError:
    sys.exit("File does not exit")
print(count_lines)
    