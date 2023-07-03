def calc_factorial(terms):
    if terms <= 0:
        raise ValueError('Terms should be positive and > 0')
    fact = 1
    for a in range(1, terms + 1):
        fact *= a
    return fact


def program():
    try:
        terms = int(input("N:"))
    except ValueError:
        print('Input was not a number')
        return
    try:
        result = calc_factorial(terms)
    except ValueError as ex:
        print(print(ex))
        return
    print(result)


if __name__ == '__main__':
    program()
