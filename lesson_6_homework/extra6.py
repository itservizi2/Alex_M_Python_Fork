## Exercițiul 6:

# Scrieți un program care solicită utilizatorului să introducă o propoziție și numără numărul de vocale din acea propoziție.

data = input('Please enter a sentence: ')
data = data.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0

for char in data:
    if char in vowels:
        vowelCount += 1

print(f'The sentence contains {vowelCount} vowels.')
