def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

try:
    n = int(input("Enter a positive integer: "))
    print("Factorial is :", factorial(n))
except ValueError as valerr:
    print(valerr)


