cuvant = "Python"
print(cuvant[0])
print(cuvant[1])
print(cuvant[2])
print(cuvant[3])
print(cuvant[4])
print(cuvant[5])

# Va produce eroare
# print(cuvant[6])

propozitie = "Hello, this is a long sentence"
print(len(propozitie))
print(propozitie[len(propozitie) // 2])

print(propozitie[-1])
print(propozitie[-2])
print(propozitie[-3])
# Produce eroare
# print(propozitie[-31])

cuvantul_hello = propozitie[0:5]
# Aceias, 0 este subinteles
cuvantul_hello = propozitie[:5]
print(cuvantul_hello)

sentence = propozitie[-8:]
# Aceias chestie, ultimul caracter este subinteles
sentence = propozitie[22:]
# Aceias chestie
sentence = propozitie[-8:len(propozitie)]
print(sentence)

small_word = "hello"
# Sliece-ul nu produce index error
print(small_word[-123812831:3000])
