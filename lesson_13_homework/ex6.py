import math

def calculate_geometric_mean():
    lst = []
    try:
        lst = list(map(float, input("Enter a list of numbers separated by space: ").split()))
    except ValueError:
        print("Invalid input! Please enter a list of numbers separated by space.")
        return calculate_geometric_mean()
    if 0 in lst:
        raise ZeroDivisionError("The list contains zero")
    else:
        product = 1
        for num in lst:
            product *= num
        return math.pow(product, 1/len(lst))

try:
    result = calculate_geometric_mean()
    print("The geometric mean is:", result)
except ZeroDivisionError as e:
    print(e)
