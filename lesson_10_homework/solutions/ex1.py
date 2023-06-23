"""
De la consola se va introduce o bucata de text.
Calculati de cate ori fiecare cuvant a fost folosit.
Afisati informatia.
"""
import string

propozitia = input('Input:')

for char in string.punctuation:
    propozitia = propozitia.replace(char, '')

# Cleanup V2
clean_propozitia = ''
for char in propozitia:
    if char in string.punctuation:
        continue
    clean_propozitia += char

propozitia = propozitia.lower()

cuvinte = propozitia.split()

# V1

cuvinte_count = dict()

for cuvant in cuvinte:
    if cuvant in cuvinte_count:
        cuvinte_count[cuvant] += 1
    else:
        cuvinte_count[cuvant] = 1


# V2 no if
cuvinte_count = dict()
for cuvant in cuvinte:
    cuvinte_count[cuvant] = cuvinte_count.get(cuvant, 0) + 1

# Access info V1
for cuvant, count in cuvinte_count.items():
    print(f"Cuvantul \"{cuvant}\" a fost gasit de {count} ori")

# Access info V2
for cuvant in cuvinte_count:
    print(f"Cuvantul \"{cuvant}\" a fost gasit de {cuvinte_count[cuvant]} ori")
