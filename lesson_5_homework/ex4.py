"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule, iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""

elev1 = []
elev2 = []


# Cream lista goala pu ambii elevi
elev1 = []
elev2 = []

# Citim datele elev1
nume_elev1 = input("Introduceți numele elevului 1: ")
prenume_elev1 = input("Introduceți prenumele elevului 1: ")
nota_elev1 = float(input("Introduceți nota elevului 1: "))

# Adaugam datele primului elev in lista
elev1.append(nume_elev1)
elev1.append(prenume_elev1)
elev1.append(nota_elev1)

# Citim datele elev2
nume_elev2 = input("Introduceți numele elevului 2: ")
prenume_elev2 = input("Introduceți prenumele elevului 2: ")
nota_elev2 = float(input("Introduceți nota elevului 2: "))

# Adaugam datele la al doilea elev in lista
elev2.append(nume_elev2)
elev2.append(prenume_elev2)
elev2.append(nota_elev2)

# vedem care elev are nota mai mare
if nota_elev1 > nota_elev2:
    elev_cu_nota_mai_mare = f"{nume_elev1} {prenume_elev1}"
elif nota_elev2 > nota_elev1:
    elev_cu_nota_mai_mare = f"{nume_elev2} {prenume_elev2}"
else:
    elev_cu_nota_mai_mare = "ambii elevi au aceeași notă"

# vedem care elev are nota mai mica
if nota_elev1 < nota_elev2:
    elev_cu_nota_mai_mica = f"{nume_elev1} {prenume_elev1}"
elif nota_elev2 < nota_elev1:
    elev_cu_nota_mai_mica = f"{nume_elev2} {prenume_elev2}"
else:
    elev_cu_nota_mai_mica = "ambii elevi au aceeași notă"

# Facem conversia la majuscula pu nume si capitalizarea pentru prenume
nume_elev1_majuscule = nume_elev1.upper()
prenume_elev1_prima_majuscula = prenume_elev1.capitalize()
nume_elev2_majuscule = nume_elev2.upper()
prenume_elev2_prima_majuscula = prenume_elev2.capitalize()

# printam rezultatele ca text
print("Datele sub formă de text:")
print("Elevul cu nota mai mare:", elev_cu_nota_mai_mare)
print("Elevul cu nota mai mică:", elev_cu_nota_mai_mica)
print("Numele și prenumele elevului 1 scris cu majuscule:", nume_elev1_majuscule, prenume_elev1_prima_majuscula)
print("Numele și prenumele elevului 2 scris cu majuscule:", nume_elev2_majuscule, prenume_elev2_prima_majuscula)

# printam rezultatele ca tabel
print("Datele sub formă de tabel:")
print("Index  Nume   Prenume   Nota")
print("  1   ", elev1[0], " ", elev1[1], "   ", elev1[2])
print("  2   ", elev2[0], " ", elev2[1], "   ", elev2[2])


