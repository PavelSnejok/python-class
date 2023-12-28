import random
import os
import importlib


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "Win, with a BlackJack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score >21:
        return "Opponent went over, You win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You lose"

def play_game():
    file_logo = importlib.import_module("11-logo")
    logo = file_logo.logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for deal in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score:  {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_game = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_game == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        while computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f" Your final hand {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_cards}")
    print(compare(user_score, computer_score))

while input(f"Do you want to play in BlackJack? Type 'y' or 'n': ").lower() == "y":
    os.system("clear")
    play_game()