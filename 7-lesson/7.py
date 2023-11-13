import random
import os
import importlib

def clear_screen():
    os.system('clear')

art = importlib.import_module("7_art")
words = importlib.import_module("7_list")

word_list = words.word_list
stages = art.stages
logo = art.logo

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear_screen()

    if guess in display:
        print(f'The letter {guess} is already in list')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'The letter {guess} not in the word')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])