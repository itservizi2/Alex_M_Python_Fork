def print_sum(a: int, b: int):
    print(a + b)


def print_dif(a: int, b: int):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    print(a - b)


print_sum(1, 2)
print_sum(1.3, 2.4)
print_sum("1", "2")

print_dif(1, 2)
print_dif(1.3, 2.4)
print_dif("1", "2")
print_dif("1", "b")
