def ex1():
    print('I am ex 1')


def ex2():
    print('I am ex 2')


def ex3():
    print('I am ex 3')


my_exercises = {
    '1': ex1,
    '2': ex2,
    '3': ex3,
}

choice = input('Choose your exercise')
# my_exercises[choice]()
match choice:
    case '1':
        ex1()
    case '2':
        ex2()
    case '3':
        ex3()
    case _:
        print('Didn\'t find the exercise')
