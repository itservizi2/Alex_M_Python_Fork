import os

path = input("Please enter the path you want to list files from: ")

if not os.path.exists(path):
    print("Provided path does not exist.")
elif not os.path.isdir(path):
    print("Provided path is not a folder.")
else:
    # cerem lista elementelor inauntru la o mapa
    all_items = os.listdir(path)

    # cream o lista goala ca sa stocam in ea elementele doar
    files = []

    # pu fiecare element in mapa vedem daca e un file
    for item in all_items:
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            files.append(item)

    print(f"Files inside {path}:")
    for file in files:
        print(file)
