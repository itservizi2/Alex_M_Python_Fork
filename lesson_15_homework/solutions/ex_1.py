import os


class FolderDoesNotExist(Exception):
    pass


class PathIsNotAFolder(Exception):
    pass


def list_dir_files(dir_path):
    if not os.path.exists(dir_path):
        raise FolderDoesNotExist(f"{dir_path} nu exista")
    # if not os.path.isdir()
    if os.path.isfile(dir_path):
        raise PathIsNotAFolder(f'{dir_path} nu este o mapa')
    list_of_paths = []
    for sub_path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, sub_path)):
            list_of_paths.append(sub_path)
    return list_of_paths


if __name__ == '__main__':
    result = list_dir_files('C:\\Users\\mtricolici\\PycharmProjects\\tekwillLive\\lesson_13_live\\')
    for el in result:
        print(el)
    # list_dir_files('C:\\Users\\mtricolici\\PycharmProjects\\tekwillLive\\lesson_13_live\\hello')
