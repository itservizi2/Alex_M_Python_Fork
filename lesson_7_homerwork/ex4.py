## Exercise 4: Prime number check

# Write a program that uses a while loop to check if a given positive integer n is a prime number. A prime number is a
# positive integer greater than 1 that has no positive divisors other than 1 and itself. The program should output whether
# the number is prime or not.

n = int(input("Enter a positive integer: "))
if n <= 1:
    print(n, "is not a prime number")
else:
    i = 2
    is_prime = True
    while i*i <= n:
        if n % i == 0:
            is_prime = False
        i += 1
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")


