# Create a function that takes a string as input and checks if it is a palindrome.
# Handle the ValueError if an empty string is provided.
import string


def check_palindrome(string_):
    if not string_:
        raise ValueError('String can not be empty for palindrom check')
    return string_ == string_[::-1]


print(check_palindrome('radar'))
print(check_palindrome('marius'))
try:
    print(check_palindrome(''))
except ValueError as ex:
    print(ex)
