import os.path

from lesson_15_homework.solutions.ex_1 import list_dir_files


def rename_files_in_folder(folder_path, prefix):
    all_files_in_the_folder = list_dir_files(folder_path)
    all_files_with_included_path = [os.path.join(folder_path, file) for file in all_files_in_the_folder]
    sorted_files = sorted(
        all_files_with_included_path,
        key=os.path.getmtime
    )
    for index, file_path in enumerate(sorted_files):
        filename = os.path.split(file_path)[-1]
        file_extention = os.path.splitext(filename)[-1]
        new_file_name = f"{prefix}{index + 1}{file_extention}"
        os.rename(file_path, os.path.join(folder_path, new_file_name))


if __name__ == '__main__':
    rename_files_in_folder('C:\\Users\\mtricolici\\PycharmProjects\\tekwillLive\\lesson_13_live\\', 'script')
