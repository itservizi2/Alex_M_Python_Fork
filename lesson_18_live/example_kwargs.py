def example(*args, **kwargs):
    print(
        args
    )
    print(
        kwargs
    )


def sum_of_three(a, b, c):
    return a + b + c


def sum_of_three_with_print(*args, **kwargs):
    if 'a' not in kwargs:
        kwargs['a'] = 1
    if 'b' not in kwargs:
        kwargs['b'] = 2
    if 'c' not in kwargs:
        kwargs['c'] = 3
    result = sum_of_three(*args, **kwargs)
    print(result)


if __name__ == '__main__':
    # example(1, 2, 3, example1=1, example2=2, example3=3)
    data = dict(
        a=1,
        b=2,
        c=3
    )
    result = sum_of_three(**data)
    print(result)
    sum_of_three_with_print(a=1, b=2, c=3)
    sum_of_three_with_print()
