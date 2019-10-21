#Program for guessing a number between 1 and 30.
#Using random import and setting guesses_input = 0 to calculate the times the user entered the numbers.

import random
guesses_input = 0
number = random.randint(1, 30)

#Main Body and asking for the user's imput.

print("Hello! What is your name?")
user_name = input()
print("Greetings", user_name, "I am thinking of a number between 1 and 30.")
print("You have only 5 guesses on this so don't waste them.")

#Defining if the number is too high or too low.

for i in range(1, 6):
    guesses_input = (guesses_input + 1)
    print("Guess the number within 5 guesses...")
    guess_number = input()

    if guess_number.isdigit():
        if int(guess_number) > number:
            print("Too high, try again.")

        elif int(guess_number) < number:
            print("Too low try again.")

        elif int(guess_number) == number:
            print("Well Done,", user_name, "you managed to guess my number in ", guesses_input, "guesses!")
            break

    else:
        print("Wrong input, try giving me numbers instead.")
        
if int(guess_number) != number:
            print("Sorry, out of guesses. The number I was thinking of is, ", number, "!")
