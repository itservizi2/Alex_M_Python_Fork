def find_name_in_list(list_of_elements: list, name: str):
    for index, elmenet in enumerate(list_of_elements):
        print('Evaluez', elmenet)
        if elmenet == name:
            print('Am Gasit', elmenet)
            return index


result = find_name_in_list(['Marius', 'Ion', 'Dumitru', 'Ion'], 'Mircea')
print(result)


def is_element_on_position(list_of_elements: list, element_to_find: str, position_to_look_for):
    for index, elmenet in enumerate(list_of_elements):
        print('Evaluez', elmenet)
        if elmenet == element_to_find and position_to_look_for == index:
            print('Am Gasit', elmenet)
            return True
    return False


result = is_element_on_position(['Marius', 'Ion', 'Dumitru', 'Ion'], 'Ion', 1)
print(result)
