# import random
# import my_module

# name_string = input(f"Give me everybody's names, separated by comma. ")
# names = name_string.split(", ")

# lenngth = len(names)
# random_number = random.randint(0, lenngth -1)


# print(f"Names = {names}")
# print(f"Length = {lenngth}")
# print(f"Random number = {random_number}")
# print (f"{names[random_number]} is going to buy the meal today!" )
# # Use only one line of code instead all above
# print (f"{random.choice(names)} is going to buy the meal today!" )

#---------------

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

#---------------

# row1 = ['😂', '😭', '😚']

# row2 = ['❤', '💋', '💕']

# row3 = ['👍', '👌', '🙏']

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where is you simbol? ")
# list1 = position.split(" ")
# print(list1)
# print(map[int(list1[0])][int(list1[1])])

#---------------
import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

my_choice = int(input("Make you choice:\n 1 = Rock\n 2 = Paper\n 3 = Scissers\n "))
com_choice = random.randint(1, 3)

if my_choice == 1 or com_choice == 1:
    

if my_choice == com_choice:
    print(f"Your choice is\n {my_choice}\n Computer choice\n {com_choice}\n Draw")
elif my_coice == 1 and com_choice == 2

# I add ne line in this file 