"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""
sir = input("introduceti sirul de caractere : ")
caracter_cautat = input("introduceti caracterul cautat : ")
numar = sir.lower().count(caracter_cautat.lower())
print(f"caracterul {caracter_cautat} apare in sir de {numar} ori ")
