"""
Scrieţi un program_exemplu care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""

sir = input("Introduceți un șir de caractere: ")

if len(sir) >= 2 and sir[1] == 'a':
    print("Litera 'a' se află pe a doua poziție în șirul citit.")
else:
    print("Litera 'a' nu se află pe a doua poziție în șirul citit.")

if len(sir) >= 2:
    if sir[1] == 'a':
        print("Litera 'a' se află pe a doua poziție în șirul citit.")
    else:
        print("Litera 'a' nu se află pe a doua poziție în șirul citit.")
else:
    print('Stringul nu are 2 pozitii')

if len(sir) < 2:
    print('Stringul nu are 2 pozitii')
else:
    if sir[1] == 'a':
        print("Litera 'a' se află pe a doua poziție în șirul citit.")
    else:
        print("Litera 'a' nu se află pe a doua poziție în șirul citit.")
