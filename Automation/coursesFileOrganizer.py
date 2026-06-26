from pathlib import Path
import re, sys

parent_dir = Path(r"C:\Users\Abdul Rehman\Downloads")
files_paths = [entry for entry in parent_dir.iterdir() if entry.is_file()]
files_paths_with_codes = [file for file in files_paths if re.search(r"([A-Z]{2,3}\d{3})", str(file))]


def extract_code(path):
    match = re.search(r"([A-Z]{2,3}\d{3})", path.name)
    if match:
        return match.group(1)
    
config_path = Path(__file__).parent / "codes.txt"
try:
        with open(config_path) as config_file:
            valid_codes = config_file.read()
            valid_codes = set(valid_codes.split())
except:
        sys.exit(f"configuration file \"{config_path.name}\" doesn't exist at path: \"{config_path.parent}\"")


def is_validate_code(code):
    if code in valid_codes:
           return True


for path in files_paths_with_codes:
    code = extract_code(path)
    if is_validate_code(code):
        new_folder = parent_dir / code
        new_folder.mkdir(exist_ok = True)
        path.rename(new_folder / path.name)