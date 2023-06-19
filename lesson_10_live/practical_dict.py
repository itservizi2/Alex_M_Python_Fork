parametri = ['name', 'age']

nr_de_utilizatori = int(input('Nr'))

utilizatori = []
for a in range(nr_de_utilizatori):
    element = dict()
    # Cream datele utilizatoruli
    for param in parametri:
        val = input(param)
        element[param] = val
    print(element)
    # Adaugam la lista de utilizatori
    utilizatori.append(element)

print(utilizatori)

# Calculam average age

age_sum = 0

for user in utilizatori:
    age_sum += int(user['age'])

print('Avg age', age_sum / len(utilizatori))
