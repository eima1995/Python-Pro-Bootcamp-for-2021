from config import resources
from config import MENU
import sys


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources_sufficient(selected_drink):
    enough = True
    for ingredient in selected_drink['ingredients']:
        if resources[ingredient] < drink['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough = False
    return enough


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(drink_cost, payment):
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(selected_drink):
    for item in selected_drink['ingredients']:
        resources[item] -= selected_drink['ingredients'][item]


profit = 0
if __name__ == '__main__':
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == 'off':
            sys.exit(0)
        elif choice == 'report':
            print_report()
        else:
            err = False
            try:
                drink = MENU[choice]
            except:
                print(f"Unknown drink {choice}")
                err = True
            if not err:
                if check_resources_sufficient(drink):
                    if transaction(drink['cost'], process_coins()):
                        make_coffee(drink)
                        print(f"Here is your {choice}. Enjoy!")