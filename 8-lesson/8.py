# import math
#
# def pain_calc(height, width, coverage):
#     number_of_cans = height * width / coverage
#     round_up_cans = math.ceil(number_of_cans)
#     return print(f"You will need {round_up_cans} cans of paint")
#
# test_h = int(input("test_h = "))
# test_w = int(input("test_w = "))
# coverage = 5
#
# pain_calc(test_h, test_w, coverage)

# -------------------------------
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("This number Prime")
    else:
        print("This is NOT Prime")

n = int(input("Input number "))
prime_checker(number=n)