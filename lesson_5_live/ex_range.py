# Vreau sa inregistrez prezenta

prezenti = []
numar_prezneti = int(input('Nr de studenti:'))
for numar in range(numar_prezneti):
    persoana = input(f"Nume persoana nr: {numar + 1}:")
    print(persoana)
    prezenti.append(persoana)

print(prezenti)

for index, persoana in enumerate(prezenti):
    print(f'{index + 1} {persoana} mersi pentru atentie')