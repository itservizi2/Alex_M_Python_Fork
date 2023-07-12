import time


def benchmark_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # start timer
        result = func(*args, **kwargs)  # call the function
        end_time = time.time()  # end timer
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


@benchmark_time
def sum_calculator(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

print(f"Suma numerelor introduse este", sum_calculator(num1, num2, num3, num4))
