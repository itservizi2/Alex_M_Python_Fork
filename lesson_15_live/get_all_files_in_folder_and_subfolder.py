import os


def get_all_files_from_folder(path_to_folder, file_ends_with):
    if not os.path.isdir(path_to_folder):
        if path_to_folder.endswith(file_ends_with):
            return [path_to_folder]
        else:
            return []
    files = []
    for file in os.listdir(path_to_folder):
        files_in_path = get_all_files_from_folder(os.path.join(path_to_folder, file), file_ends_with)
        files.extend(files_in_path)
    return files


path = input('search path')
file_extension = input('file ext')
for result in get_all_files_from_folder(path, file_extension):
    print(result)
