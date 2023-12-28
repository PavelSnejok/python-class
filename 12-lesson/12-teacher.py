from random import randint
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def check_answer(guess, answer, turns):
    """check answer """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it. The answer is {answer}")

def set_difficulty():
    level = input("Choose the difficulty 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Passt, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            return print("You've run of guesses, you lose.")
        elif guess != answer:
            print("Guess again!")

while input("Do you want play game. Type 'y' or 'n': ").lower() == "y":
    os.system('clear')
    game()


