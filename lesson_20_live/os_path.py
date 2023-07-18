import os

PATH_DE_BAZA = os.path.join('C:\\files\\')

if not os.path.exists(PATH_DE_BAZA):
    os.mkdir(PATH_DE_BAZA)

categorie = input('Categorie')
nume_fisier = input('Nume fisier')
date_fisier = input('Date')

cale_spre_mapa = os.path.join(PATH_DE_BAZA, categorie)
cale_spre_fisier = os.path.join(cale_spre_mapa, nume_fisier)

if not os.path.exists(cale_spre_mapa):
    os.mkdir(cale_spre_mapa)
else:
    if not os.path.isdir(cale_spre_mapa):
        raise Exception('Nu putem folsoi categoria ca cale')

with open(cale_spre_fisier, 'w') as fiel:
    fiel.write(date_fisier)
