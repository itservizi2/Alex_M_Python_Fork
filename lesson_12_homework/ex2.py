def generate_fibonacci(termeni):
    fibonacci_secv = [0, 1]
    if termeni == 1:
        fibonacci_secv = [0]
    elif termeni > 1:
        for i in range(2, termeni):
            next_term = fibonacci_secv[i - 1] + fibonacci_secv[i - 2]
            fibonacci_secv.append(next_term)
    return fibonacci_secv


num_terms = int(input("Citi termeni Fibonacci trebuie generati: "))

fibonacci_seq = generate_fibonacci(num_terms)

print(f"Secventa Fibonacci generata este : {fibonacci_seq}")
