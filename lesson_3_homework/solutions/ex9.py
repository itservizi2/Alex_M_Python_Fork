"""
Eliminați semnele de punctuație
Scrieți un program_exemplu care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""
from string import punctuation

# Solution
# Pentru alte semne de bunctuatie ce nu sunt incluse procedam la fel.
propozitie = input()
print(
    propozitie.replace('.', '')
    .replace(',', '')
    .replace('?', '')
    .replace('!', '')
    .replace("'", '')
    .replace('"', '')
    .replace(':', '')
    .replace(';', '')
    .replace('-', '')
    .replace('(', '')
    .replace(')', '')
    .replace('{', '')
    .replace('}', '')
)


# Cu FOR e mai usor
# clean = propozitie
# for char in punctuation:
#     clean = clean.replace(char, "")
# print(clean)
