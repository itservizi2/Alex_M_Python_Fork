#
# # set gol
# my_set = set()
# # set ne gol
# my_set = {1, 2, 3}

# Dict gol
dict_gol = dict()
asemena_dict_gol = {}
print(type(dict_gol))
print(type(asemena_dict_gol))

# Dict cu elemente
dict_cu_stringuri_ca_cheie = dict(nume='Marius', varsta=25)
dict_cu_orice_ca_cheie = {1: 'Marius', 2: 25, 'also_valid': True}
print(dict_cu_stringuri_ca_cheie)
print(dict_cu_orice_ca_cheie)

# Also valid
dict_gol = dict()
nume = input('Numele tau:')
nume_key = 'name'
dict_gol[nume_key] = nume
print(dict_gol)

# nu se poate
# dict_gol[dict()] = nume # produce eroare

nume_nou = input('Nume nou:')
dict_gol[nume_key] = nume_nou
print(dict_gol)
