numere = input("Introdu o listă de numere separate prin spațiu: ").split()
produs = 1
for numar in numere:
    numar = int(numar)
    produs *= numar
    if produs > 100:
        print("Produsul este prea mare!")
        break
else:
    print("Produsul tuturor numerelor din listă este:", produs)
