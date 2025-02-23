import os
import shutil
from pathlib import Path

DOWNLOADS_FOLDER = Path.home() / "Downloads"
TRASH_FOLDER=Path.home() / ".local/share/Trash"
# Define categories and their corresponding file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Compressed": [".zip", ".rar", ".7z", ".tar.gz"],
    "Executables": [".exe", ".msi", ".sh", ".bat", ".app"],
    "Code Files": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"]
}

def organize_files():
    
    # Ensure the Downloads folder exists
    if not DOWNLOADS_FOLDER.exists():
        print(f"Error: {DOWNLOADS_FOLDER} does not exist.")
        return

    # Iterate over all files in the Downloads folder
    for file in DOWNLOADS_FOLDER.iterdir():
        if file.is_file():  # Ignore directories
            move_file(file)
    print("Do you want to delete your trash??")
    i=input()
    if (i=='Y' or i=='y'):
        if not TRASH_FOLDER.exists():
            print(f"Error: {TRASH_FOLDER} does not exist.")
            return
        for file in TRASH_FOLDER.iterdir():
            if file.is_file():
                print(file)

def move_file(file):
    """Moves a file to the appropriate category folder based on its extension."""
    file_extension = file.suffix.lower()  # Get file extension

    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            target_folder = DOWNLOADS_FOLDER / category
            target_folder.mkdir(exist_ok=True)  # Create folder if not exists
            
            try:
                shutil.move(str(file), str(target_folder / file.name))
                print(f"Moved: {file.name} → {category}/")
            except Exception as e:
                print(f"Error moving {file.name}: {e}")
            return
    
    # If the file doesn't match any category, move it to "Others"
    other_folder = DOWNLOADS_FOLDER / "Others"
    other_folder.mkdir(exist_ok=True)
    shutil.move(str(file), str(other_folder / file.name))
    print(f"Moved: {file.name} → Others/")

if __name__ == "__main__":
    organize_files()

