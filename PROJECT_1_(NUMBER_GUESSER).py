#PROGRAM THAT LETS THE USER GUESS A RANDOM GENERATED NUMBER BETWEEN 1-100/
#While at the same time it gives the user some tips along the way.

import random

randNum = random.randint(1, 100)
guesses = 0

for i in range(1, 8):
    guesses = guesses + 1
    print("Hi fellow human guess a number 1-100! \n")
    guess = input()

    if guess.isdigit():
        if int(guess) > randNum:
            print("your guess is too high \n")

        elif int(guess) < randNum:
            print("your guess is too low \n")

        elif int(guess) == randNum:
            print("duuude you're a genius \n")
            print("you needed " + str(guesses) + " guesses")

    else:
        print("Invalid Input! Try a number. \n")
