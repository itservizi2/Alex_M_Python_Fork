print(1, 2, 3, sep=' | ')

my_list = [1, 2, [], 'Something', None]

primul_el, al_doilea, *result = my_list
print(primul_el, al_doilea, result)

print(*my_list, sep=' | ')
# Echivalent
print(1, 2, [], 'Something', None, sep=' | ')


# Packing
def function_with_unlimited_args(*my_arguments):
    print(my_arguments)


function_with_unlimited_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def my_sum(*numbers, start_from=0):
    result = start_from
    for number in numbers:
        result += number
    return result


print(my_sum(1, 2, 1, 2, 3, start_from=10))
print(my_sum(1, 2, 4, 5))
