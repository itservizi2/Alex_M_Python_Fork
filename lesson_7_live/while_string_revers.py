"""
Write a program_exemplu that uses a while loop to reverse a given string.
    Example input: "Python"
    Example output: "nohtyP"
"""

string1 = 'Python'
string2 = ''
for index in range(1, len(string1) + 1):
    string2 += string1[-index]

print(string2)

string1 = 'Python'
string2 = ''
for char in string1:
    string2 = char + string2

print(string2)

string1 = 'Python'
string2 = ''
index = len(string1) - 1
while index >= 0:
    string2 += string1[index]
    index -= 1

print(string2)
