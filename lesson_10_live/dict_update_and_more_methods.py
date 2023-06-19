# Update

dict_1 = {'name': 'Marius', 'country': 'MD'}
dict_2 = {'name': 'Ion', 'age': 30}

dict_1.update(dict_2)
print(dict_1)

print(dict_2)

for key, value in dict_1.items():
    print(f'Key {key} has value {value}')

for key in dict_1:
    print(f'Key {key} has value {dict_1[key]}')

dict_2.clear()
print(dict_2)

dict_2 = dict().fromkeys(['name', 'age', 'country'], None)
print(dict_2)

# print(dict_2['occupation']) # Will throw error
print(dict_2.get('occupation'))  # Nu primir eroare
print(dict_2)
print(dict_2.get('occupation', 'unemployed'))  # Primim unemployed
print(dict_2)

dict_2['occupation'] = dict_2.get('occupation', 'unemployed')
print(dict_2)

dict_2['occupation'] = 'Programmer'
print(dict_2.get('occupation', 'unemployed'))
dict_2['occupation'] = dict_2.get('occupation', 'unemployed')
print(dict_2)
