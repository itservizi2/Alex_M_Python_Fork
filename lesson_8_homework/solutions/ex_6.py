sir_caractere = input("Introdu un sir de caractere: ")
litere_majuscule = [caracter for caracter in sir_caractere if caracter.isupper()]
print(litere_majuscule)

print("; ".join(litere_majuscule))
