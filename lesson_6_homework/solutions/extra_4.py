"""
Scrieți un program_exemplu care solicită utilizatorului să introducă un număr și afișează toate numerele pare
de la 1 la acel număr.
"""

numar = int(input('Introduceti un numar: '))
for x in range(2, numar + 1, 2):
    print(x)
