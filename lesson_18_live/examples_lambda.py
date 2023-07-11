number_sum = lambda *args: sum(args)

try:
    number_sum(1, 2, 3)
except ValueError:
    print('err')

my_Str = 'example'


def example_sum(a, b):
    """
    Calculates sum of 2 objects
    :param a: int object a
    :param b:
    :return:
    """
    print(a + b)


print(example_sum.__doc__)


def function_that_uses_another_function(function, *args):
    function(*args)


function_that_uses_another_function(example_sum, 1, 2)


