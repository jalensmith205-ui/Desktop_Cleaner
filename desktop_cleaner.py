import shutil, time
from pathlib import Path

# configuration 
DESKTOP = Path.home() / "Desktop"


EXTENSION_MAP = {
    ".docx": "Documents", ".doc": "Documents", ".txt":"Documents",
    ".pdf": "PDFs",
    ".jpg": "Images", ".png": "Images", ".jpeg": "Images", ".heic": "Images",
    ".zip": "Archives", ".dmg": "Installers", ".pkg": "Installers",
    ".mp4": "Videos", ".mov": "Videos",
    ".xlsx": "Spreadsheets", ".csv": "Spreadsheets"
}

def clean_desktop():
    for item in DESKTOP.iterdir():
        if item.is_dir() or item.name.startswith('.') or item.suffix == ".py":
            continue

        # Determine the target folder 
        dest_folder_name = EXTENSION_MAP.get(item.suffix.lower(), "Misc")
        dest_path = DESKTOP / dest_folder_name
        dest_path.mkdir(exist_ok=True)

        try:
            shutil.move(str(item), dest_path / item.name)
            print(f"Moved {item.name}: {e}")
        except Exception as e:
            print(f"Skipped {item.name}: {e}")
if __name__ == "__main__":
    print("Smart Cleaner Active... Sorting existing and new files.")
    while True:
        clean_desktop()
        time.sleep(10)
