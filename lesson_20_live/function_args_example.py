def say_n_times(n=5, message="Message"):
    for a in range(n):
        print(message)


def greet_n_times(n):
    say_n_times(n, "Hello Python")


def goodbye_n_times(n):
    say_n_times(n, "Good Bye, Python")


def greet_5_times():
    greet_n_times(5)


def greet_10_times():
    greet_n_times(10)


def greet_15_times():
    greet_n_times(15)


def goodbye_5_times():
    goodbye_n_times(5)


def goodbye_10_times():
    goodbye_n_times(10)


def say_yes_5_times():
    say_n_times(message="YES!")


def say_yes_10_times():
    # say_n_times(10, "YES")
    say_n_times(message="YES!", n=10)


greet_5_times()
greet_10_times()
goodbye_10_times()

say_yes_5_times()

from unittest.result import TestResult

my_test_result = TestResult()
