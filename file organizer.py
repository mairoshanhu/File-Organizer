import os, shutil

#Folder path input
FOLDER_PATH = r"Folder's Path"

# File  groups
EXT_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Docs": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php", ".rb"],
}


def organize(folder):
    if not os.path.isdir(folder):
        print("❌ Invalid folder path!")
        return

    files = os.listdir(folder)
    for f in files:
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            ext = os.path.splitext(f)[1].lower()
            moved = False
            for category, exts in EXT_MAP.items():
                if ext in exts:
                    target_dir = os.path.join(folder, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(path, os.path.join(target_dir, f))
                    moved = True
                    break
            if not moved:
                other_dir = os.path.join(folder, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(path, os.path.join(other_dir, f))
    print("Organizing of files is done!")


if __name__ == "__main__":
    print(f"Organizing files in: {FOLDER_PATH}")
    organize(FOLDER_PATH)
