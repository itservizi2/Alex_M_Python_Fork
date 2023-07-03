# Varianta intiala fara functii
# string_of_numbers = input('Numere prin virgula').split(',')
#
# list_of_numbers = [int(a) for a in string_of_numbers]
#
# print(sum(list_of_numbers))


def sum_of_numbers(numbers):
    if not isinstance(numbers, list):  # type(numbers) == list
        raise TypeError('Parameter is not list')
    return sum(numbers)


#
#
# print(sum_of_numbers([1, 2, 3]))
# # try:
# #     print(sum_of_numbers(['1', '2']))
# # except TypeError as error:
# #     print(error)
# #     print('Ai folosit altceva in loc de numere')
# #
# # try:
# #     print(sum_of_numbers({1, 2, 3}))
# # except TypeError as error:
# #     print(error)
# #     print('Ai folosit altceva in loc de numere')
# try:
#     print(sum_of_numbers(['1', '2']))
# except TypeError:
#     print('SUm is 0 because we could not calculate it')
# print(sum_of_numbers([0, 0, 0]))


def sum_of_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Parameter is not list')
    return sum(numbers)


# string_of_numbers = input('Numere prin virgula').split(',')
# try:
#     list_of_numbers = [int(a) for a in string_of_numbers]
#     print(sum_of_numbers(list_of_numbers))
# except ValueError:
#     print('Nu am putut transforma valorile')


if __name__ == '__main__':
    from input_utils import input_list_of_numbers_safe
    print(sum_of_numbers(input_list_of_numbers_safe()))
