import time
from functools import wraps


def decorator_1(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Function {function.__name__} was called from decorator 1')
        result = function(*args, **kwargs)
        return result

    return wrapper


def decorator_2(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Function {function.__name__} was called from decorator 2')
        result = function(*args, **kwargs)
        return result

    return wrapper


@decorator_2
@decorator_1
def calculate_prime(nr):
    for a in range(2, nr // 2 + 1):
        if nr % a == 0:
            return False
    return True


if __name__ == '__main__':
    print(calculate_prime(1281284812488123))
