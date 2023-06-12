"""
Write a program that uses a while loop to simulate a dice rolling game.
The game continues until the user rolls a 6.
Example output: Rolled a 4/3/2/1/5. Continue? (y/n)
"""

import random

rand_number = 0

should_continue = True
while rand_number != 6 and should_continue:
    rand_number = random.randrange(1, 7)
    print(f"Rolled a {rand_number}")
    if rand_number != 6:
        should_continue = input('Continue ? y/n') == 'y'
