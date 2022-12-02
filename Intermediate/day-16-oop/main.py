from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine() 
coffee_maker = CoffeeMaker()
menu = Menu()
no_coffee = False
while not no_coffee:
  print(menu.get_items())
  ask = input("What would you like?: ")
  drink = menu.find_drink(ask)
  if ask == "report":
    coffee_maker.report()
    money_machine.report()
  elif ask == "off":
    no_coffee = True
  elif coffee_maker.is_resource_sufficient(drink):
    if money_machine.make_payment(drink.cost):
      print('Success')
