lista = [1, 2, 3]
lista[0] = 2
print(lista)

lista = ['Marius', 'Ion']
lista[0].replace('a', '')
print(lista)
lista[0] = lista[0].replace('a', '')
print(lista)

result = lista.remove('Mrius')
print(result)
result = lista.pop(0)
print(result)

# Iterare si modificare
# for el in lista:
#     # Nu e bine sa modifici lista in timpul parcurgerii
#     lista.append('100')
#     print(lista)

