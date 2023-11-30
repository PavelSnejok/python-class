import os
import importlib

file_logo = importlib.import_module("10-logo")
logo = file_logo.logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(logo)

    num1 = float(input("What the first number: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        choice = input("Choose the method: '+' '-' '*' '/' ")
        num2 = float(input("What the next number: "))

        for key in operations:
            if choice == key:
                result = operations[key](num1, num2)
                print(f"{num1} {key} {num2} = {result}")

        end_or_continue = input("Do you want to continue with another number: ").lower()
        if end_or_continue == "no":
            should_continue = False
            os.system('clear')
        else:
            num1 = result

calculation()





