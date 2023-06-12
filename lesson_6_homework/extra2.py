## Exercițiul 2:

# Scrieți un program care solicită utilizatorului să introducă trei numere și afișează cel mai mare număr dintre ele.

a, b, c = input("Introduceți trei numere: ").split()
a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c:
    print("Cel mai mare număr este:", a)
elif b >= a and b >= c:
    print("Cel mai mare număr este:", b)
else:
    print("Cel mai mare număr este:", c)

