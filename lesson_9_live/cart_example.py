products_available = {
    'banana',
    'mar',
    'paine',
    'coffee',
    'apa',
    'bere',
    'carne',
    'cascaval'
}

lista_de_cumparaturi = {
    'coffee', 'carne', 'apa', 'vin'
}

intersection_result = lista_de_cumparaturi.intersection(products_available)

print(intersection_result)
print('Pot cumpara', intersection_result == lista_de_cumparaturi)

print(lista_de_cumparaturi - products_available)
