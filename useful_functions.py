from basic_functions_II import *

def print_report(Profit, resources):
    print("Water :", resources["water"], "ml")
    print("Milk :", resources["milk"], "ml")
    print("Coffee :", resources["coffee"], "g")
    print("Profit :", Profit, "$")


def check_resources(MENU, choice, resources):
    list_ingredients = list(MENU[choice]["ingredients"].keys())
    message = "Sorry there is not enough "
    needs =[MENU[choice]["ingredients"][ing] for ing in list_ingredients]
    stock = [resources[ing] for ing in list_ingredients]

    availabe = [x>=y for x, y in zip(stock, needs)]
    missed_index = [i for i in range(len(availabe)) if availabe[i]==False]
    if not missed_index:
        return True
    else:
        message += list_ingredients[missed_index[0]] + "."
        print(message)
        return False


def process_coins() -> object:
    values =[0.25, 0.1, 0.05, 0.01]
    coins = eval(input("Please insert coins :")) #[1, 1, 1, 1]
    Money= sum_product(coins, values)
    return Money


def check_transaction(MENU, choice, Money):
    #Money = process_coins()
    Price = MENU[choice]["cost"]
    answer = ""
    if Money < Price :
        answer = "Sorry that's not enough money. Money refunded."
        return [0, False, answer]
    elif Money > Price:
        answer = "Here is $"+str(round(Money-Price, 2))+" dollars in change."
        return [Money, True, answer]
    else: # Money = Price
        return [Money, True, answer]


def Make_coffee(choice, MENU, resources):
    list_ingredients = list(MENU[choice]["ingredients"].keys())

    for ing in list_ingredients:
        resources[ing] -= MENU[choice]["ingredients"][ing]
    #print(resources)
    print("Here is your " + choice + ". Enjoy!")


def TurnOff(choice):
    return choice.lower() =="off"

