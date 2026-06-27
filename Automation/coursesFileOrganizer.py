from pathlib import Path
import sys

# Read valid course codes from codes.txt config file
config_path = Path(__file__).parent / "codes.txt"
try:
        with open(config_path) as config_file:
            valid_codes = config_file.read()
            valid_codes = set(valid_codes.split())
except:
        sys.exit(f"configuration file \"{config_path.name}\" doesn't exist at path: \"{config_path.parent}\"")


# Get all files in the target directory
if len(sys.argv) < 2:
     sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
     sys.exit("Too many command-line arguments")
parent_dir = Path(sys.argv[1])
if not parent_dir.exists():
    sys.exit(f"Path doesn't exist: {parent_dir}")
if not parent_dir.is_dir():
    sys.exit(f"Path is not a directory: {parent_dir}")
files_paths = [entry for entry in parent_dir.iterdir() if entry.is_file()]

# Move each file to its matching course code folder
for file_path in files_paths:
    for code in valid_codes:
        if code in str(file_path.name):
            new_folder = parent_dir / code
            new_folder.mkdir(exist_ok = True)
            file_path.rename(new_folder / file_path.name)
            break