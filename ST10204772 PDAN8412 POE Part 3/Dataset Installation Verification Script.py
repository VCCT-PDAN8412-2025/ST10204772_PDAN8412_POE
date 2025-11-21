from pathlib import Path

# Base directory is the folder containing this script
BASE_DIR = Path().resolve()
DATA_DIR = BASE_DIR / "1M_Big_Captcha_Dataset"

# Get all files in the dataset directory
if DATA_DIR.exists():
    file_list = [f.name for f in DATA_DIR.glob("*.*")]  # just file names
    print(file_list[:5])  # print only the first 5 file names
else:
    print("Dataset folder not found! Make sure it's in the same folder as this script.")
