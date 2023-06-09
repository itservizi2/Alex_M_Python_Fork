"""
Write a program that generates a random number between 1 and 100.
 Allow the user to make guesses
 and provide feedback (higher, lower, or correct)
  given they have 10 attempts."""

import random

guess = random.randrange(0, 100)

for a in range(10):
    print(f"Attempt numebr {a + 1} of 10")
    user_guess = int(input('Your guess:'))
    if user_guess > guess:
        print('Lower')
    elif user_guess < guess:
        print('Higher')
    else:
        print('You won!')
        exit()


