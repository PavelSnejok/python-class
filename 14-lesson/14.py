from game_data import data
from art import logo, vs
import os
import random

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def check_answer(guess, a_followers, b_followers):
    if guess == "a" and a_followers > b_followers:
        return True
    elif guess == "b" and a_followers < b_followers:
        return True
    else:
        return False

def game():
    whole_answers = 0
    score = 0
    game_should_continue = True
    while game_should_continue:
        os.system('clear')
        dict_A = get_random_account()
        a_followers = dict_A['follower_count']
        # print(dict_A)

        dict_B = get_random_account()
        b_followers = dict_B['follower_count']
        # print(dict_B)

        while dict_A == dict_B:
            dict_B = get_random_account()

        if 5 > whole_answers > 0:
            print(f"Your current score is {score} form {whole_answers}")
        elif whole_answers == 5:
            os.system('clear')
            game_should_continue = False
            return print(f"Your FINAL score is {score} from {whole_answers}")

        print(logo)
        print(f"Compare A: {format_data(dict_A)}")
        print(vs)
        print(f"Against B: {format_data(dict_B)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if check_answer(guess, a_followers, b_followers):
            score += 1
            print(f"Correct!")
            input("Press bottom to continue...")
        else:
            print(f"Your guess is WRONG.")
            input("Press bottom to continue...")
        whole_answers += 1
    return

os.system('clear')
while input("Do you want start Guess game. Type 'y' or 'n':  ").lower() == 'y':
    game()
