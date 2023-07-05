import random

num_dice = int(input("Enter the number of dice to roll: "))
num_sides = int(input("Enter the number of sides for each dice: "))

while True:
    total = 0
    rolls = []

    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
        total += roll

    print("Rolls: ", rolls)
    print("Total: ", total)

    user_choice = input("Press ENTER to roll again, or type 'STOP' to end the game. ")

    if user_choice.upper() == "STOP":
        break

print("Thanks for playing!")


