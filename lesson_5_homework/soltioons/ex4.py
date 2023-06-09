"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi
**nota** obţinută la examen şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule,
iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk",
rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor,
ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""

elev1 = list()
elev2 = list()
info_elevi = ["nume", "prenume", "nota"]

for index, lista in enumerate([elev1, elev2]):
    for el in info_elevi:
        info = input(f"Introduceti {el} elev:")
        lista.append(info)
    print(f"Date elev {index + 1} sunt: ", lista)

if elev1[2] > elev2[2]:
    print(f"Elevul {elev1[0]} {elev1[1]} are nota mai mare")
    print(f"Elevul {elev2[0]} {elev2[1]} are nota mai mica")
elif elev1[2] < elev2[2]:
    print(f"Elevul {elev2[0]} {elev2[1]} are nota mai mare")
    print(f"Elevul {elev1[0]} {elev1[1]} are nota mai mica")
else:
    print("Ambii elevi au aceeasi nota.")

print("Elevii afisati in tabel:")
print(f"| {elev1[0].capitalize()} | {elev1[1].upper()} | {elev1[2]} |")
print("|------|------|-----|")
print(f"| {elev2[0].capitalize()} | {elev2[1].upper()} | {elev1[2]} |")
