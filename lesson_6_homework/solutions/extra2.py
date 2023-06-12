"""
Scrieți un program care solicită utilizatorului să introducă trei numere și afișează cel mai mare număr dintre ele.
"""

nr1 = float(input("Introduceti numarul 1: "))
nr2 = float(input("Introduceti numarul 2: "))
nr3 = float(input("Introduceti numarul 3: "))

if nr1 == nr2 == nr3:
    print(f"Numere egale.")
    exit()

max_nr = nr1
for number in [nr2, nr3]:
    if number > max_nr:
        max_nr = number
print(f"Mai mare este {max_nr}.")
