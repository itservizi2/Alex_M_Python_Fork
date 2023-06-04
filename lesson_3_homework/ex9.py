"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""
sir = input("introduceti sirul de caractere : ")
caractere_de_exclus = ".?!,"
sir_prelucrat = sir
for char in caractere_de_exclus:
    sir_prelucrat = sir_prelucrat.replace(char, "")
print(f"Sirul fara caracterele excluse este {sir_prelucrat}")

