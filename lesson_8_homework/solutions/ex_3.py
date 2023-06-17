numere = input("Introdu o listă de numere separate prin spațiu: ").split()
produs = 1
index = 0

while index < len(numere):
    produs *= int(numere[index])
    if produs > 100:
        print("Produsul este prea mare!")
        break
    index += 1

if produs <= 100:
    print("Produsul tuturor numerelor din listă este:", produs)
