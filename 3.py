# size = input("What is pizza size do you want? S, M, or L ")

# bill = 0
# while size not in ["S", "M", "L"]:
#     size = input("Repear and chose correct size? S, M, or L ")

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     size = input("Make sure that you choose a correct size? S, M, or L ")

# add_papperoni = input("Do you want papperoni? Y or N ")
# if add_papperoni == "Y" and size == "S":
#     bill += 2
# elif add_papperoni == "Y" and (size == "M" or size == "L"):
#     bill += 3

# extra_cheese = input("Do you want extra cheese? Y or N ")
# if extra_cheese == "Y":
#     bill += 1
    
# print(f"Your total bill for pizza is {bill} for Pizza Size {size}, and you addition papperoni is {add_papperoni}, and extra cheese is {extra_cheese}")


# -----------------------------------------------

  
# name1 = input("What is your name1? \n")
# name2 = input("What is your name2? \n")

# lower_name1 = name1.lower()
# lower_name2 = name2.lower()

# love = "LOVE"
# true = "TRUE"

# lower_love = love.lower()
# lower_true = true.lower()

# names = lower_name1 + lower_name2
# list_of_words = [lower_true, lower_love]

# love_score_str = ""

# for word in list_of_words:
#     total = 0
#     for i in word:
#         if i in names:
#             total += names.count(i)
#             print(f"{i} occurs {names.count(i)} times")
#         else:
#             print(f"{i} occurs 0 times")
#     print(f"Total in letters in {word} = {total}")
#     love_score_str += str(total)
# love_score = int(love_score_str)

# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score > 40 and love_score < 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}")


#-------------------------------------


choice = input('You\'re at a crlssroad, where do you want to go? Type "left" or "right".\n').lower()

