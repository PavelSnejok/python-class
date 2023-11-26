import os
import importlib
file_logo = importlib.import_module("9-bit-logo")
logo = file_logo.logo
print(logo)

def people_bid(name, bid, dictionary):
    os.system('clear')
    dictionary[name] = bid

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        if bidding_record[key] > highest_bid:
            highest_bid = bidding_record[key]
            winner = key
    os.system('clear')
    print(logo)
    print(f"The winner is {winner} with the bit of {highest_bid}")

bids = {}
should_continue = True
while should_continue:
    name_input = input("Enter the name for vote: ")
    bid_input = int(input("What is the money bid: "))

    people_bid(name=name_input, bid=bid_input, dictionary=bids)
    choose = input("Do you want to continue: ").lower()

    if choose == "no":
        should_continue = False
        find_highest_bidder(bidding_record=bids)