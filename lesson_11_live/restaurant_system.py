# Price is in LEI
from collections import defaultdict

menu = {
    '1': ('Salad', 150),
    '2': ('Eggs', 100),
    '3': ('Bacon', 100),
    '4': ('Steak', 300),
    '5': ('Borsh', 100),
    '6': ('Pancake', 120),
    '7': ('Icecream', 30),
    '8': ('Limonada', 40),
}

categorized_menu = {
    'salads': {
        '1': ('Salad', 150),
    },
    'breakfast': {
        '2': ('Eggs', 100),
        '3': ('Bacon', 100),
    },
    'mains': {
        '4': ('Steak', 300),
    },
    'soups': {
        '5': ('Borsh', 100),
    },
    'deserts': {
        '6': ('Pancake', 120),
        '7': ('Icecream', 30),
    },
    'drinks': {
        '8': ('Limonada', 40),
    }
}

nr_of_guests = int(input('Nr of guests'))

guest_info = dict()

for guest_nr in range(nr_of_guests):
    name = input('Name: ').capitalize()
    list_of_dishes = []
    while True:
        print(f"Alege ceva din meniu")
        for number, (item, price) in menu.items():
            print(f'{number}: {item} - {price} lei')
        print('Daca doriti sa continuati, scrieti stop')
        if list_of_dishes:
            print('Deja ai ales', ", ".join(menu[item][0] for item in list_of_dishes))
        item_chosen = input('Alegeti dupa numar sau stop').lower()
        if item_chosen == 'stop':
            break
        if item_chosen not in menu:
            print('Wrong item chosen, try again')
            continue
        list_of_dishes.append(item_chosen)
    guest_info[(guest_nr + 1, name)] = list_of_dishes

for (nr, guest), dish_numbers in guest_info.items():
    # Numele la produs
    items_picked = ", ".join(menu[item][0] for item in dish_numbers)
    # Pretul
    total_cost = sum([menu[item][1] for item in dish_numbers])
    print(f"{guest} chose to buy {items_picked} and has to pay {total_cost}")

to_cook = defaultdict(int)

for dish_numbers in guest_info.values():
    for dish in dish_numbers:
        dish_name = menu[dish][0]
        to_cook[dish_name] += 1

print(to_cook)
