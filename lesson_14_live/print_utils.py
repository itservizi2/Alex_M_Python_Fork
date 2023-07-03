def print_elements_of_list(list_to_print):
    if not isinstance(list_to_print, list):
        raise TypeError('Parameter is not list')
    for index, item in enumerate(list_to_print):
        print(f'IDX:{index:04d}|{item}')


def print_dict(dict_to_print):
    if not isinstance(dict_to_print, dict):
        raise TypeError('Parameter is not list')
    for index, item in dict_to_print.items():
        print(f'KEY:{index}|{item}')


