"""Scrieți un program care utilizează o buclă while pentru a genera secvența
Fibonacci până la un număr dat de termeni. Secvența Fibonacci este o serie de numere în
care fiecare număr este suma celor două numere precedente. Secvența începe cu 0 și 1."""

n = int(input('Introdu un numar n= '))
lista = [0, 1]
a = 0
b = 1
c = 1
while len(lista) < n:
    c = a + b
    a = b
    b = c
    lista.append(c)
print(lista)
