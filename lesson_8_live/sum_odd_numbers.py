"""
Write a program that calculates the sum of all odd numbers between 1 and 50 using a list comprehension
"""

print(
    sum(
        [nr for nr in range(0, 51) if nr % 2 != 0]
    )
)

"""
Write a program that asks the user to enter a sentence and counts the number of vowels in it using a for loop.
"""

list_of_vowels = [char for char in input('Cuvant') if char.lower() in 'aioue']

print(len(list_of_vowels))
print(list_of_vowels)

# Echilvaent cu

list_of_vowels = []
for char in input('cuvant'):
    if char.lower() in 'aioue':
        list_of_vowels.append(char)
