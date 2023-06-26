"""
Verificarea unui palindrom
Scrieți un program_exemplu care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""
# Solution

sir = input('Sirul').lower().replace(' ', '')
sir_invers = sir[::-1]
# print(sir_invers)
print(f"{sir} e polindrom: {sir == sir_invers}")
