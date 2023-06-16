# Write a list comprehension that generates a list of the uppercase letters in a given string. For example, if the
#    string is "Hello World", the list comprehension should produce ['H', 'W'].

string = input("Enter a string: ")
uppercase_letters = [char for char in string if char.isupper()]
print(uppercase_letters)



