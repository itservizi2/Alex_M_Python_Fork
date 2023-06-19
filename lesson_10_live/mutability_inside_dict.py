notele_lui_marius = [2, 3, 4]

registry = {
    'Marius': notele_lui_marius,
    'Ion': {1, 2, 3}
}

print(registry)

registry['Marius'].append(10)

# Se modifica in ambele
print(registry)
print(notele_lui_marius)

notele_lui_marius.append(5)

# Se modifica in ambele
print(registry)
print(notele_lui_marius)

# Extrag din dict setul
setul = registry['Ion']
# Modifc setul
setul.add(4)
print(registry, setul)

# For other types it's not the same

some_string = 'Hello'
some_dict = dict(message=some_string)

print(some_dict)
some_dict['message'] += ' Python!'
print(some_dict)
print(some_string)


