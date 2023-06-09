"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**,
 **înălţimea** şi **ocupaţia** utilizatorului şi adăugaţi aceste valori în lista creată.
"""
date_personale = list()
info_date = ["nume", "prenume", "varsta", "inaltime", "ocupatie"]
numar_de_persoane = int(input('Nr de persoane'))
for persoana in range(numar_de_persoane):
    persoana_date = []
    for el in info_date:
        info = input(f"Introduceti {el}:")
        persoana_date.append(info)
    date_personale.append(persoana_date)

print(f"Lista cu date personale completata: {date_personale}")

# Other ways
date_personale = []  # Sau list()
date_personale.append(input("Nume:"))
date_personale.append(input("prenume:"))
date_personale.append(input("varsta:"))
date_personale.append(input("inaltime:"))
date_personale.append(input("ocupatie:"))

print(date_personale)
