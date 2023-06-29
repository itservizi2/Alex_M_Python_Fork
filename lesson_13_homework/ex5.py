class AgeError(Exception):
    pass

def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0 or age > 150:
                raise AgeError("Age must be between 0 and 150")
            return age
        except ValueError:
            print("Invalid input. Please enter a number.")
        except AgeError as err:
            print(err)

try:
    age = get_age()
    print(f"Your age is {age}")
except AgeError as e:
    print(e)
