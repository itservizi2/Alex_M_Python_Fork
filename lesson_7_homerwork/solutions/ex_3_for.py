nr = int(input('nr:'))

fib_sequence = [0, 1]
for a in range(2, nr):
    fib_sequence.append(fib_sequence[a - 1] + fib_sequence[a - 2])
print(fib_sequence)
