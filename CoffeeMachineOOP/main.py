from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

if __name__ == '__main__':
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == 'off':
            sys.exit(0)
        elif choice == 'report':
            coffee_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_machine.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_machine.make_coffee(drink)
