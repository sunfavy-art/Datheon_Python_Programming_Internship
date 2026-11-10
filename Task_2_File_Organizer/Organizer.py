import os
import shutil
from pathlib import Path

# File extension categories
FILE_TYPES = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}
# Ask the user for the folder to organize
folder_path = input("Enter the folder path to organize: ")

# Convert the folder path into a Path object
folder = Path(folder_path)

# Check whether the folder exists
if not folder.exists():
    print("Error: This folder does not exist.")

elif not folder.is_dir():
    print("Error: The path is not a folder.")

else:
    print("Folder found successfully!")
    print("Ready to organize files.")
    # Count organized files
    moved_files = 0

    # Inspect every item in the selected folder
    for item in os.scandir(folder):

        # Skip folders and process files only
        if item.is_file():

            file_path = Path(item.path)

            # Identify the file extension
            extension = file_path.suffix.lower()

            # Find the correct category
            category = FILE_TYPES.get(extension, "Others")

            # Create the destination folder
            destination_folder = folder / category
            destination_folder.mkdir(exist_ok=True)

            print(f"Found: {file_path.name}")
            print(f"Category: {category}")
            # Choose a safe destination filename
            destination = destination_folder / file_path.name

            # Handle duplicate filenames
            counter = 1

            while destination.exists():
                new_name = (
                    f"{file_path.stem}_{counter}"
                    f"{file_path.suffix}"
                )
                destination = destination_folder / new_name
                counter += 1

            # Move the file safely
            try:
                shutil.move(str(file_path), str(destination))

                moved_files += 1
                print(f"Moved: {file_path.name} -> {category}")

            except PermissionError:
                print(f"Permission denied: {file_path.name}")

            except OSError as error:
                print(f"Could not move {file_path.name}: {error}")
                print("\n================================")
    print("       ORGANIZATION SUMMARY")
    print("================================")
    print(f"Files successfully moved: {moved_files}")
    print("Organization completed!")
    print("================================")