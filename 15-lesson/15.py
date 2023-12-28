from resource import MENU, resources

def resource_calculation(resource, receipt, money):
    for key in receipt:
        if resource[key] < receipt[key]:
            print(f"Sorry there is not enough {key}")
            return resource
    for key in receipt:
        resource[key] -= receipt[key]
    resource['money'] += money
    return resource

def insert_coins():
    print("Please insert coins")
    money_dict = {"quarter": .25, "dime": .10, "nickle": .05, "pennie": .01}
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money_sum = {"quarter": quarters, "dime": dimes, "nickle": nickles, "pennie": pennies}
    summary = 0
    for key in money_dict:
        summary += money_dict[key] * money_sum[key]
    return round(summary, 2)

def transaction_success(money, summary):
    if money > summary:
        print(f"Sorry that's not enough money. Money refunded. You insert {summary}")
        return False
    else:
        print(f"Here is ${round(summary - money, 2)} dollars in change.")
        return True

def coffe_machine():
    money = 0
    resource = resources
    resource['money'] = money
    should_continue = True
    while should_continue:
        offer_prompt = input("What would you like (espresso/latte/cappuccino): ").lower()
        if offer_prompt == 'off':
            print("Machine is off!")
            should_continue = False
        elif offer_prompt == 'report':
            print(resource)
        elif offer_prompt == 'espresso' or offer_prompt == 'latte' or offer_prompt == 'cappuccino':
            receipt = MENU[offer_prompt]['ingredients']
            money = MENU[offer_prompt]['cost']
            summary = insert_coins()
            if transaction_success(money, summary):
                resource = resource_calculation(resource, receipt, money)
                print("Here is your latte. Enjoy!")
            # print(resource)
        else:
            print("Check your chose and repeat!")

coffe_machine()
# insert_coins()






