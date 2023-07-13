import numbers


def validate_numeric(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValueError:
            print("Error: Result is not numeric")

        else:
            if isinstance(result, numbers.Number):
                print("The inserted character is a number")
                return result
            else:
                print("Error: Result is not numeric")

    return wrapper


@validate_numeric
def get_input():
    return float(input('Enter a number: '))


print('Testing the decorator...')

get_input()

print("Continuing...")

get_input()

print("Continuing...")

get_input()

print("Done!")
