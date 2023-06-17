set_gol = set()

alt_sequence = (1, 2, 3, 's', 1.3, True, None, None, True, 0, False, 0, 1.4)

set_cu_elemente = set([1, 2, 3])
set_cu_elemente = set((1, 2, 3))
set_cu_elemente = {1, 2, 3}

set_de_alceva = set(alt_sequence)
print(set_de_alceva)
set_de_alceva.add((1, 2, 3))
print(set_de_alceva)

# for element in set_de_alceva:
#     print(element)

print(True == 1)

set_de_alceva.add([1, 23])

print(set_de_alceva)
