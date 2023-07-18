def is_prime(n):
    """
    Verifica daca N este numar prim
    :param n:
    :return: boolean
    """
    if n < 2:
        return False
    for a in range(2, n // 2 + 1):
        if n % a == 0:
            return False
    return True


def find_first_n_prime_numbers(n):
    """
    Gasim, pan la n numere prime
    :param n:
    :return: o lista de numere prime
    """
    prime_numbers = []
    checking = 2
    while len(prime_numbers) < n:
        if is_prime(checking):
            prime_numbers.append(checking)
        checking += 1
    return prime_numbers


def print_first_n_prime_numbers(n):
    if n < 0:
        print('N este negativ')
        return
    for number in find_first_n_prime_numbers(n):
        print(number)


print(print_first_n_prime_numbers(-1))
