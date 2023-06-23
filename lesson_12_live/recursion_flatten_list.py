def flatten_list(list_to_flatten: list):
    result = []
    for element in list_to_flatten:
        if type(element) == list:
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result


example_list = [
    1,
    'asd',
    [1, 2, 3, [91, 23, 10]],
    None,
    ['askd', 'asdk', ['ask', 'iii']]
]
print(example_list)
print(flatten_list(example_list))


