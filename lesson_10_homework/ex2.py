num_guests = int(input("How many guests will be coming? "))
guest_list = []
food_orders = {}

for _ in range(num_guests):
    guest_name = input("Enter the name of the guest: ")
    dish1 = input("Enter the first dish for {}: ".format(guest_name))
    dish2 = input("Enter the second dish for {}: ".format(guest_name))
    guest_list.append(guest_name)
    food_orders[guest_name] = [dish1, dish2]

print("\nThe guests will be:", guest_list)
print("\nFood orders:")
for guest, dishes in food_orders.items():
    print(guest, "ordered", dishes[0], "and", dishes[1])

print("\nYou will have to prepare:")
dish_counts = {}
for dishes in food_orders.values():
    for dish in dishes:
        if dish in dish_counts:
            dish_counts[dish] += 1
        else:
            dish_counts[dish] = 1

for dish, count in dish_counts.items():
    print(dish, "x", count)
