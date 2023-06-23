"""
De la consola se va introduce o bucata de text.
Calculati de cate ori fiecare cuvant a fost folosit.
Afisati informatia.
"""
import string
from collections import defaultdict

propozitia = input('Input:')

for char in string.punctuation:
    propozitia = propozitia.replace(char, '')
propozitia = propozitia.lower()
cuvinte = propozitia.split()

cuvinte_count = defaultdict(int)

for cuvant in cuvinte:
    cuvinte_count[cuvant] += 1

for cuvant, count in cuvinte_count.items():
    print(f"Cuvantul \"{cuvant}\" a fost gasit de {count} ori")
