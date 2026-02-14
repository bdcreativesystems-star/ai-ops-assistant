import os
import shutil

def organize_files():
    folder = input("Enter folder path: ")

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = file.split(".")[-1]
            dest = os.path.join(folder, ext)

            os.makedirs(dest, exist_ok=True)
            shutil.move(path, os.path.join(dest, file))

    print("Files organized.")
