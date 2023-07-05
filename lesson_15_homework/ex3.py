import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2, dice1+dice2

while True:
    user_input = input("Press ENTER to roll the dice (q to quit): ")
    if user_input.lower() == 'q':
        break
    dice1, dice2, total = roll_dice()
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {total}")

