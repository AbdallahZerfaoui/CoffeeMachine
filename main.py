from useful_functions import *
from basic_functions_II import *
from data import *


Profit = 0
Money = 0

while (True):
    # TODO: 1. Ask the client about what he wants
    choice = input("What would you like? (espresso/latte/cappuccino):")
    # TODO: 2. TurnOff the machine
    if (choice =="OFF" or choice =="off"):
        break
    # TODO: 3. Print report
    if (choice == 'report'):
        print_report(Money, resources)
        continue
    # TODO: 4. Check resources
    enough_resources = check_resources(MENU, choice, resources)
    if (enough_resources):
        # TODO: 5. Precess coins
        Money = process_coins()
        #print(Money)
    else:
        break

    # TODO: 6. Check transaction
    enough_money = check_transaction(MENU, choice, Money)[1]
    answer = check_transaction(MENU, choice, Money)[2]
    if (enough_money):
        Profit += check_transaction(MENU, choice, Money)[0]
        # print(Profit)
    if (answer != ""):
        print(answer)
    # TODO: 7. Make Coffee
    Make_coffee(choice, MENU, resources)

