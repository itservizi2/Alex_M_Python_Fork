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
    '9': ('Ceai', 30),
}

menu_seara = {
    '1': ('Salad', 150),
    '4': ('Steak', 300),
    '5': ('Borsh', 100),
    '7': ('Icecream', 30),
    '8': ('Limonada', 40),
    '9': ('Ceai', 30),
}


def print_menu(menu_dict):
    print(f"Alege ceva din meniu")
    for number, (item, price) in menu_dict.items():
        print(f'{number}: {item} - {price} lei')
    print('Daca doriti sa continuati, scrieti stop')


def print_guest_info(guest_info, selected_menu):
    for (nr, guest), dish_numbers in guest_info.items():
        # Numele la produs
        items_picked = ", ".join(selected_menu[item][0] for item in dish_numbers)
        # Pretul
        total_cost = sum([selected_menu[item][1] for item in dish_numbers])
        print(f"{guest} chose to buy {items_picked} and has to pay {total_cost}")


def choose_item_from_menu(menu_dict):
    print_menu(menu_dict)
    item_chosen = input('Alegeti dupa numar sau stop').lower()
    if item_chosen == 'stop':
        return 'stop'
    if item_chosen not in menu_dict:
        print('Wrong item chosen, try again')
        return -1
    return item_chosen


def register_guests(number_of_guests, selected_menu):
    guest_info = dict()
    for guest_nr in range(number_of_guests):
        name = input('Name: ').capitalize()
        list_of_dishes = []
        while True:
            if list_of_dishes:
                print('Deja ai ales', ", ".join(selected_menu[item][0] for item in list_of_dishes))
            item_chosen = choose_item_from_menu(selected_menu)
            if item_chosen == -1:
                continue
            if item_chosen == 'stop':
                break
            list_of_dishes.append(item_chosen)
        guest_info[(guest_nr + 1, name)] = list_of_dishes
    return guest_info


def get_cook_order_from_guest_info(guest_info, selected_menu):
    to_cook = defaultdict(int)
    for dish_numbers in guest_info.values():
        for dish in dish_numbers:
            dish_name = selected_menu[dish][0]
            to_cook[dish_name] += 1
    return to_cook


def start_program():
    nr_of_guests = int(input('Nr of guests'))
    selected_menu = menu_seara
    info = register_guests(nr_of_guests, selected_menu)
    print_guest_info(info, selected_menu)
    cook_info = get_cook_order_from_guest_info(info, selected_menu)
    print(cook_info)


start_program()
