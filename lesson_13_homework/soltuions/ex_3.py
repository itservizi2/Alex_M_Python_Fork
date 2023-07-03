def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division by 0 is not allowed")


def program():
    print("This is a program that divides 2 numbers")
    a = float(input('First number'))
    b = float(input('Second number'))
    divide(a=a, b=b)


if __name__ == '__main__':
    try:
        program()
    except Exception as ex:
        print('Something unexepcted happened')
