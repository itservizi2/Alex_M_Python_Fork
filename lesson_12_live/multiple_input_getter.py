def multiple_input_getter(prompts: list, times: int):
    result_list = []
    for i in range(times):
        result = dict()
        for prompt in prompts:
            result[prompt] = input(prompt)
        result_list.append(result)
    return result_list


#
#
# def print_dict(dict_to_print: dict):
#     for key, value in dict_to_print.items():
#         print(key, value)
#
#
# result = multiple_input_getter(['numele', 'varsta', 'ocupatia'], 4)
#
# for element in result:
#     print_dict(element)

guest_data = multiple_input_getter(['Guest name', 'Dish 1', 'Dish 2'], int(input('Number of guests')))
print(guest_data)
