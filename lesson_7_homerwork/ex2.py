## Exercise 2: Guessing game

# Write a program that generates a random number between 1 and 100 and lets the user guess the number. The program should
# provide feedback ("higher" or "lower") until the user guesses the correct number. The program should also keep track of
# the number of guesses it takes for the user to guess correctly.

import random

number = random.randint(1, 100)
guess = 0
num_guesses = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    num_guesses += 1

    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("Correct!")
        print("Number of guesses:", num_guesses)


