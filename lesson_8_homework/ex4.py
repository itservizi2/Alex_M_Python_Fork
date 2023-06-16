# Write a program that takes a list of strings as input. The program should print each string on a separate line.
#    However, if a string starts with the letter 'A', the program should skip that string and move on to the next one
#    using the `continue` statement.

string_list = []
n = int(input("Enter the number of strings: "))

for i in range(n):
    string = input(f"Enter string {i+1}: ")
    string_list.append(string)

for string in string_list:
    if string.startswith('A'):
        continue
    print(string)


