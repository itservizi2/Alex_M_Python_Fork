def print_every_element_in_list(list_to_print):
    list_to_print = list_to_print.copy()
    while list_to_print:
        print(list_to_print.pop())


my_list = [1, 2, 3]
print_every_element_in_list(my_list)
print(my_list)
