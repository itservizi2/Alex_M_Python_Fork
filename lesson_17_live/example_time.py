import time


def calculate_fib_sequence(nr):
    fib_sequence = [0, 1]
    for a in range(2, nr):
        fib_sequence.append(fib_sequence[a - 1] + fib_sequence[a - 2])
    return fib_sequence


if __name__ == '__main__':
    start = time.time()
    seq = calculate_fib_sequence(100000)
    end = time.time()
    print(len(seq), end - start)
