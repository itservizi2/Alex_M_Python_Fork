"""
Creaza un program care va inregistra o lista de oaspeti si comenzile lor la un restaurant.

Utilizatorul va introduce la consola cati oaspeti vor fi inregistrati.

Pentru fiecare oaspete, utilizatorul va introduce Numele Oaspetelui si 2 feluri de mancare.

La sfarsit, programul va trebui sa afiseze lista cu oaspeti,
 ce au comandat, si cat in total va trebui restaurantul sa pregateasca.

Folositi dict
"""

nr_guests = int(input('Guest nr:'))

guest_info = dict()

for nr in range(nr_guests):
    name = input('Guest name').capitalize()
    # Formam un tuplu cu 2 elemente (string) din input
    dishes = input('Dish 1').capitalize(), input('Dish 2').capitalize()
    guest_key = name
    # Determining suffix
    if guest_key in guest_info:
        all_similar_keys = [key for key in guest_info if key.startswith(guest_key + '_')]
        guest_key = f"{name}_{len(all_similar_keys)}"
    guest_info[guest_key] = dishes

print(guest_info)

for customer_name, (dish1, dish_2) in guest_info.items():
    print(f'Customer {customer_name} ordered {dish1} and {dish_2}')

cook_info = dict()
for comanda in guest_info.values():
    for dish in comanda:
        cook_info[dish] = cook_info.get(dish, 0) + 1

print(cook_info)

for dish, number in cook_info.items():
    print(f"Need to cook {number} of {dish}")
