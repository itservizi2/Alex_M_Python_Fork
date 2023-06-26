"""Scrieți un program_exemplu care utilizează o buclă while pentru a calcula
factorialul unui număr întreg pozitiv dat n.
Factorialul unui număr este produsul tuturor numerelor întregi pozitive de la 1 la n.
"""
n = int(input('Introduceti n ='))
produsul = 1
i = 1
while i <= n:  # in caz in care si n se include in produs
    produsul = produsul * i
    i += 1
if n == 0:
    print('Nu avem ce calcula ')
else:
    print("Produsul este ", produsul)
