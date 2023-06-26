"""
Write a program_exemplu that uses a while loop to implement a simple calculator.
 The program_exemplu prompts the user for two numbers and an operator (+, -, *, /)
 and performs the corresponding calculation.
    Example input: 5 + 3
    Example output: 8
"""

counter = 0

should_calc = True
while should_calc:
    oper = input("Type in the operation:")
    nr_1 = float(input('Nr1'))
    nr_2 = float(input('Nr2'))
    if oper == '+':
        print(f"{nr_1} + {nr_2} = {nr_1 + nr_2}")
    elif oper == '-':
        print(f"{nr_1} - {nr_2} = {nr_1 - nr_2}")
    elif oper == '*':
        print(f"{nr_1} * {nr_2} = {nr_1 * nr_2}")
    elif oper == '/':
        if nr_2 == 0:
            print('Division by 0 not possible')
            should_calc = False
        else:
            print(f"{nr_1} / {nr_2} = {nr_1 / nr_2}")
    else:
        print('Unknown operation', oper)
    counter += 1
    if should_calc:
        shoudl_calc = input('type exit to stop') != "exit"

print(f'You made {counter} caluclations')
