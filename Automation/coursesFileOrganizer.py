from pathlib import Path
import re

parent_dir = Path(r"C:\Users\Abdul Rehman\Downloads")
files_paths = [entry for entry in parent_dir.iterdir() if entry.is_file()]
files_paths_with_codes = [file for file in files_paths if re.search(r"([A-Z]{2,3}\d{3})", str(file))]


def extract_code(path):
    match = re.search(r"([A-Z]{2,3}\d{3})", path.name)
    if match:
        return match.group(1)


def is_validate_code(code):
    valid_codes ={"CS101", "ENG101", "ETH202", "ISL 202", "MTH101", "PAK301", "PHY101", "PHY301",
        "VU001", "CS201", "CS201P", "CS302", "CS302P", "MGT211", "ECO401", "ENG201", "MTH301", "CS304",
        "CS304P", "CS403", "CS403P", "CS601", "MGT301", "MGT503", "MTH202", "CS301", "CS301P",
        "CS401", "CS401P", "CS504", "CS610", "CS610P", "MGT602", "MGT501", "CS205", "CS402",
        "CS502", "MCM301", "MTH401", "STA301", "CS602", "CS605", "CS407", "CS411", "CS435",
        "CS603", "CS604", "CS604P", "CS606", "MTH501", "CS609", "CS501", "CS611", "CS506",
        "CS619", "CS621", "MGT502", "MGT610", "MTH603", "CS607", "CS607P", "CS612", "CS625"}
    if code in valid_codes:
           return True


for path in files_paths_with_codes:
    code = extract_code(path)
    if is_validate_code(code):
        new_folder = parent_dir / code
        new_folder.mkdir(exist_ok = True)
        path.rename(new_folder / path.name)