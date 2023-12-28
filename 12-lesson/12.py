import random
import os
import importlib

number_of_attempts = 0
random_number = 0

def welcome_message():
    file_logo = importlib.import_module('12-logo')
    logo = file_logo.logo
    print(logo)
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    choose_level = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()
    global number_of_attempts, random_number
    if choose_level == "easy":
        number_of_attempts = 10
    else:
        number_of_attempts = 5

    random_number = random.choice(range(1, 100))
    return random_number

def main_game():
    welcome_message()
    global number_of_attempts
    while number_of_attempts >= 0:
        if number_of_attempts == 0:
            return print(f"You loose the game. Right answer is {random_number}")
        your_guess_number = int(input("Make a guess: "))
        if your_guess_number > random_number:
            number_of_attempts -= 1
            print(f"Too high.\nGuess again.\nYou have {number_of_attempts} attempts remaining to guess the number.")
        elif your_guess_number < random_number:
            number_of_attempts -= 1
            print(f"Too low.\nGuess again.\nYou have {number_of_attempts} attempts remaining to guess the number.")
        else:
            return print("Your guess is right. You Win!")

while input("Do you want to palay the guess game. Type 'y' or 'n': ").lower() == "y":
    os.system('clear')
    main_game()




