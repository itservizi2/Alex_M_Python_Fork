import json

with open("files/dishes.json", "r") as f:
    dishes_data = json.load(f)

    dishes = dishes_data["dishes"]

print("Select an option:")
print("1. List all dishes")
print("2. Add dish")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":

    print("Dishes:")
    for dish in dishes:
        print("-", dish)
elif choice == "2":

    new_dish = input("Enter the name of the new dish: ")

    dishes.append(new_dish)

    with open("files/dishes.json", "w") as f:

        json.dump(dishes_data, f)
        print("New dish added successfully!")
else:

    print("Invalid choice. Please try again.")
