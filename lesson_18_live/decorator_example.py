import time
from functools import wraps


def print_exec_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Function {function.__name__} was called with args {args} and {kwargs}')
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Function {function.__name__} took {end - start} to run")
        return result

    return wrapper


@print_exec_time
def calculate_fib_sequence(nr):
    fib_sequence = [0, 1]
    for a in range(2, nr):
        fib_sequence.append(fib_sequence[a - 1] + fib_sequence[a - 2])
    return fib_sequence


@print_exec_time
def calculate_prime(nr):
    for a in range(2, nr // 2 + 1):
        if nr % a == 0:
            return False
    return True


if __name__ == '__main__':
    print(len(calculate_fib_sequence(150000)))
    print(calculate_prime(1281284812488123))
