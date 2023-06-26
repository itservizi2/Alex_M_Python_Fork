def generate_fibonacci(terms):
    fibonacci_sequence = [0, 1]

    if terms <= 2:
        return fibonacci_sequence[:terms]

    while len(fibonacci_sequence) < terms:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


terms = int(input("Enter the number of Fibonacci terms to generate: "))

fibonacci_sequence = generate_fibonacci(terms)
print(f"Generated Fibonacci sequence: {fibonacci_sequence}")
