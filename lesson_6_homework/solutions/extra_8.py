"""
Scrieți un program care solicită utilizatorului să introducă un șir de caractere și verifică dacă acesta
este un palindrom (adică se citește la fel de la stânga la dreapta și de la dreapta la stânga).
"""

sir = input('Introduceti un sir de caractere: ').lower().replace(' ', '')
sir_invers = sir[::-1]
if sir == sir_invers:
    print(f"Sirul este un polindrom.")
else:
    print(f"Sirul nu este polindrom.")