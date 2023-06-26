'''
Write a Python function called generate_fibonacci
that generates the Fibonacci sequence up to a given number of terms.
The function should take one argument: terms (integer) indicating the number of Fibonacci terms to generate.
The function should return a list containing the Fibonacci sequence.

Hint: The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.

Write a program_exemplu that uses the generate_fibonacci function to do the following:

Prompt the user to enter the number of Fibonacci terms to generate.
Call the generate_fibonacci function with the provided input.
Print the generated Fibonacci sequence.
'''


def generate_fibonacci(terms: int):
    if terms <= 1:
        return (terms)
    return generate_fibonacci(terms - 1) + generate_fibonacci(terms - 2)



termps = int(input("Introdu nr-ul din fibonacci care vrei sa-l afli "))
# range(5 + 1) = [0, 1, 2, 3, 4, 5]
fibonacci_terms = [generate_fibonacci(i) for i in range(termps + 1)]
print(f"Fibonacci Terms: {fibonacci_terms}")
