# C:\Users\ITSUPPORT\Documents\python_rename_test

import os
import datetime

def sort_by_date(file_info):
    return (file_info[1], file_info[0])

folder_path = input("Enter the path of the folder: ")

if not os.path.isdir(folder_path):
    print("The specified path is not a directory")
else:
    print("\nSelect a renaming option:")
    print("1. Rename files to numbers based on creation date")
    print("2. Add a prefix to the file name")
    option = int(input("Enter your choice (1 or 2): "))

    if option == 1:
        # Rename files to numbers based on creation date
        files = os.listdir(folder_path)
        files_info = []
        for file in files:
            path = os.path.join(folder_path, file)
            ctime = os.path.getctime(path)
            files_info.append((file, ctime))
        files_info.sort(key=sort_by_date)
        for i, (file, _) in enumerate(files_info):
            ext = os.path.splitext(file)[1]
            new_name = f"{i+1}{ext}"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

    elif option == 2:
        # Add a prefix to the file name
        prefix = input("Enter the prefix to add: ")
        files = os.listdir(folder_path)
        for i, file in enumerate(files):
            ext = os.path.splitext(file)[1]
            new_name = f"{prefix}{i+1}{ext}"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

    else:
        print("Invalid option selected")








