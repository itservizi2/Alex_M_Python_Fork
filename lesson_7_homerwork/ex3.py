## Exercise 3: Fibonacci sequence

# Write a program that uses a while loop to generate the Fibonacci sequence up to a given number of terms. The Fibonacci
# sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence starts with 0 and 1.

terms = int(input("Enter the number of terms to generate: "))
a, b = 0, 1

if terms == 0:
    print("No terms to generate")
elif terms == 1:
    print("Fibonacci sequence:", a)
else:
    print("Fibonacci sequence:", a, b, end=" ")
    count = 2
    while count < terms:
        c = a + b
        print(c, end=" ")
        a, b = b, c
        count += 1
