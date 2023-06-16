 # Write a program that takes a list of numbers as input. The program should calculate the product of all the numbers in
 #   the list. However, if the product exceeds 100, the program should stop calculating and print a message indicating
 #   that the product is too large. Use a `while` loop and the `break` statement to terminate the loop when necessary.

numbers = list(map(int, input("Enter list of numbers separated by spaces: ").split()))
product = 1
i = 0

while i < len(numbers):
    product *= numbers[i]
    if product > 100:
        print(f"Product is greater than 100, so is too large!")
        break
    i += 1

print(f"The product of the numbers in the list is: {product}")




