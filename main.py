from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    options = menu.get_items()
    action = input(f"What would you like to do drink? ({options}): ")
    if action == "off":
        machine_is_on = True
    elif action == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

