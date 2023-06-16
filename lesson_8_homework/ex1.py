# Write a program that generates random numbers between 1 and 10 using a `while` loop. The program should continue
#    generating numbers until it generates a number greater than 8. Once the number is greater than 8, the program should
#    terminate the loop using the `break` statement.

import random

while True:
    random_number = random.randint(1, 10)
    print("Generated number:", random_number)
    if random_number > 8:
        print("Generated number is greater than 8")
        break

