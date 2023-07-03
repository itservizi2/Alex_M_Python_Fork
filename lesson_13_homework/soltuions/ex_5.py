class AgeError(Exception):
    pass


def input_age():
    value = input('Input your age:')
    while True:
        try:
            age_value = int(value)
            break
        except ValueError:
            print('Entered value is not a number, please try again')
            value = input('Input your age:')
    if 0 <= age_value < 150:
        print('Thankyou')
        return age_value
    raise AgeError('Age value should be between 0 and 150')


def program():
    try:
        print(input_age())
    except AgeError as err:
        print(err)


if __name__ == '__main__':
    program()
