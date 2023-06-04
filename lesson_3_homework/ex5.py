"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""
sir = input('insert the text : ')
sir_invers = sir[::-1]
print(f"sirul invers este {sir_invers}")
are_equal = bool(sir == sir_invers)
print(f"Statement that the strings are equal is {are_equal}")
