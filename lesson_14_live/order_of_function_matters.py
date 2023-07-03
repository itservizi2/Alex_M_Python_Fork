def program():
    print_hello()


try:
    program()
except Exception as ex:
    print(ex)

def print_hello():
    print("Hello")

