## Exercise 1: Factorial calculation

# Write a program that uses a while loop to calculate the factorial of a given positive integer n. The factorial of a
# number is the product of all positive integers from 1 to n.

n = int(input("Enter a positive integer: "))
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    while n > 0:
        factorial *= n
        n -= 1
    print("Factorial of", n, "is", factorial)
