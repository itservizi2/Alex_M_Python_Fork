sirul = input("Introdu o listă de șiruri de caractere separate prin spațiu: ")
lista_siruri = sirul.split()
for sir in lista_siruri:
    if sir.startswith('A'):
        continue
    print(sir)
