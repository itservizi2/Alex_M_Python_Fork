"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**, **înălţimea** şi **ocupaţia** utilizatorului şi adăugaţi aceste valori în lista creată.
"""
date_personale = []

nume = input("Introduceți numele utilizatorului: ")
prenume = input("Introduceți prenumele utilizatorului: ")
varsta = input("Introduceți vârsta utilizatorului: ")
inaltime = input("Introduceți înălțimea utilizatorului: ")
ocupatie = input("Introduceți ocupația utilizatorului: ")

date_personale.append(nume)
date_personale.append(prenume)
date_personale.append(varsta)
date_personale.append(inaltime)
date_personale.append(ocupatie)

print("Lista date_personale:", date_personale)

