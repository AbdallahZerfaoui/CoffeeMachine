from useful_functions import *
from data import *


def coffee_machine():
    profit = 0
    while True:
        # TODO: 1. Ask the client about what he wants
        choice = input("What would you like? (espresso/latte/cappuccino):")
        # TODO: 2. TurnOff the machine
        if choice.lower() == "off":
            break
        # TODO: 3. Print report
        if choice.lower() == 'report':
            print_report(profit, resources)
            continue
        # TODO: 4. Check resources
        enough_resources = check_resources(MENU, choice, resources)
        if enough_resources:
            # TODO: 5. Precess coins
            money = process_coins()
        else:
            break

        # TODO: 6. Check transaction
        enough_money = check_transaction(MENU, choice, money)[1]
        answer = check_transaction(MENU, choice, money)[2]
        if enough_money:
            profit += MENU[choice]["cost"]
            # TODO: 7. Make Coffee
            Make_coffee(choice, MENU, resources)
        if answer:
            print(answer)


coffee_machine()
