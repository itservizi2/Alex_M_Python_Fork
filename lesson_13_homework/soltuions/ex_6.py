import math

from lesson_14_live.input_utils import input_list_of_numbers_safe


def geometric_mean(list_of_numbers):
    if any(el == 0 for el in list_of_numbers):
        raise ZeroDivisionError('0 element found in list which is not allowed')
    prods = 1
    for el in list_of_numbers:
        prods *= el
    return math.pow(prods, 1 / len(list_of_numbers))

def program():
    try:
        print(geometric_mean(input_list_of_numbers_safe()))
    except ZeroDivisionError as err:
        print(err)


if __name__ == '__main__':
    program()

