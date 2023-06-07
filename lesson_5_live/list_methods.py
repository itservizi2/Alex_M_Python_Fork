# Remove din lista
example_list = [1, 2, 3, 1]
print(example_list)
example_list.remove(1)
print(example_list)
example_list.remove(1)
print(example_list)
# Produce eroare
# example_list.remove(1)


example_list_str = ['a', 'b', 'c']
example_list_str.remove('a')
# Produce eroare
# example_list_str.remove('B')


# Adaugare
print(example_list_str)
example_list_str.append('d')
print(example_list_str)
example_list_str.insert(0, 'd')
print(example_list_str)
another_list = ['f', 'g', 'h', 'h']
example_list_str.extend(another_list)
print(example_list_str)
print(example_list_str.index('h'))
# Produce eroare
# print(example_list_str.index('o'))
