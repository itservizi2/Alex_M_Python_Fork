# Utilizarea instrucțiunii break cu buclele while
print()

count = 0
while count < 10:
    if count == 5:
        break
    print(count, end="  ")
    count += 1

    # 0  1  2  3  4
# ------------------------------------
# Utilizarea instrucțiunii break cu buclele for
print()

fruits = ['apple', 'banana', 'orange', 'grape', 'watermelon']
for fruit in fruits:
    if fruit == 'orange':
        break
    print(fruit, end=" ")

    # apple  banana
# ------------------------------------
# Instrucțiunea continue:
print()

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count, end=" ")

    # 1 2 4 5
# ------------------------------------
# Utilizarea instrucțiunii continue cu buclele for
print()

fruits = ['apple', 'banana', 'orange', 'grape', 'watermelon']
for fruit in fruits:
    if fruit == 'orange':
        continue
    print(fruit, end=" ")

# apple banana grape watermelon
# ------------------------------------
