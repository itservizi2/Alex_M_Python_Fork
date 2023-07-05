# def add(a, b):
#     return a + b


add = lambda a, b: a + b

print(add(1, 3))
print(add(1, 6))

print(1 + 3)

list_of_strings = ['Ana', 'Andrei', 'Ion', 'Marius']


def get_second_element(string_):
    return string_[1]


print(sorted(list_of_strings, key=lambda a: a[1]))
print(sorted(list_of_strings, key=get_second_element))
