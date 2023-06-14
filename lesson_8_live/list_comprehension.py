some_list = [5, 1, 20, 7, 8, 3, 4, 5, 12, 13, -10]

pow_list = [el ** 2 for el in some_list]
print(pow_list)

cond_list_comprehension = [el * 2 for el in some_list if el > 10]

print(some_list)
print(cond_list_comprehension)

# some_list = [el for el in some_list if el > 5]
print(some_list)

print(any(el < 0 for el in some_list))

number_list = [2, 3, 4]
print(all(el % 2 == 0 for el in number_list))
print(any(el % 2 == 0 for el in number_list))

print('Even')
are_even_in_list = [el % 2 == 0 for el in number_list]
print(are_even_in_list)
print(all(are_even_in_list))
