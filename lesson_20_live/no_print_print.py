def add(a, b):
    print(a + b)


def add_rt(a, b):
    return a + b


def something(a, b):
    return "HEllo"


# print(add(1, 2) + add(2, 3))
print(add_rt(1, 2) + add_rt(2, 3))
results_sum = something(1, 2) + something(1, 2)
print(results_sum)
