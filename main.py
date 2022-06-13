#!/usr/bin/env python3

r"""
__author__  Team 6
__date__ 2022/06/

"""
from pick import pick
import json

# import json with menu items and load data into objects
with open('menu.json', 'r') as f:
    data = json.load(f)

for category in data['food-item-categories']:
    if category['name'] == 'Burgers':
        burgers = category['menu-items']
    if category['name'] == 'Sides':
        sides = category['menu-items']
    if category['name'] == 'Drinks':
        drinks = category['menu-items']
    if category['name'] == 'Condiments':
        condiments = category['menu-items']

# implement the classes listed below


class FoodItem:
    price = None
    name = None
    description = None

    def __init__(self, price: float, name: str, description: str) -> None:
        self.price = price
        self.name = name
        self.description = description


class Burger(FoodItem):
    condiments = []

    def __init__(self, price: float, name: str, description: str, condiments: list) -> None:
        super().__init__(price, name, description)
        self.condiments = condiments


class Drink(FoodItem):
    def __init__(self, price: float, name: str, description: str, size='small'):
        super(Drink, self).__init__(price, name, description)
        self.size = size

    pass


class Side(FoodItem):
    def __init__(self, price: float, name: str, description: str):
        super(Side, self).__init__(price, name, description)

    pass


class Combo(Burger, Drink, Side):
    burger = None
    side = None
    drink = None

    def __init__(self, burger: Burger, drink: Drink, side: Side) -> None:
        self.burger = burger
        self.drink = drink
        self.side = side


class Order:
    food_items = []
    name = ""
    order_price = 0.0

    def __init__(self, name: str) -> None:
        self.name = name

    def add_item(self, FoodItem: FoodItem) -> None:
        self.food_items.append(FoodItem)
        self.order_price += FoodItem.price

    def remove_item(self) -> None:
        item, index = pick(
            self.food_items, "Please select the item to remove.")
        self.foodItems.remove(item)
        self.order_price -= item.price

    def calculate_price(self) -> float:
        return self.order_price

    def review_order(self) -> None:
        print("Your current order is the following: \n")
        for item in self.food_items:
            print(f"{item.name}: {item.price} ({item.description})\n")
        print(f"Current total price: {self.order_price}")


def user_input_burger() -> Burger:
    burger_names = []
    for burger in burgers:
        burger_names.append(burger['name'])

    condiment_names = []
    for condiment in condiments:
        condiment_names.append(condiment['name'])

    # ask user for input and store it in burger object
    option, index = pick(
        burger_names, "Please select a burger to add to your order.")

    b_name = burgers[index]['name']
    b_price = burgers[index]['price']
    b_description = burgers[index]['description']

    # ask user if they want to add condiments
    b_condiments = []

    options = pick(condiment_names, "Please select any condiments to add to your burger (press SPACE to mark, ENTER to continue).",
                   multiselect=True, min_selection_count=0)

    for option in options:
        b_condiments.append(option[0])

    b = Burger(b_price, b_name, b_description, b_condiments)

    return b


def user_input_drink():
    Totalprice = 0
    title = "What is your preference for cup size?"
    Sizes = ['Small', 'Medium', 'Large']
    size, index = pick(Sizes, title)

    if size == "Small":
        pass
    elif size == "Medium":
        Totalprice += 1
    else:
        Totalprice += 2

    drink_names = []
    for drink in drinks:
        drink_names.append(drink['name'])

    name, index = pick(
        drink_names, "Please select a drink to add to your order.")

    Totalprice += float(drinks[index]['price'])
    description = drinks[index]['description']

    d = Drink(Totalprice, name, size, description)
    return d


def user_input_side():
    side_names = []
    for side in sides:
        side_names.append(side['name'])

    name, index = pick(
        side_names, "Please select a side dish to add to your order.")

    price = float(sides[index]['price'])
    description = sides[index]['description']

    s = Side(price, name, description)

    return s


def user_input_combo():
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink

    b = user_input_burger()

    # Do the same for drink

    d = user_input_drink()

    # Do the same for side

    s = user_input_side()

    # Construct combo

    c = Combo(b, d, s)

    # Return combo
    return c


def take_order():
    # ask user for name for the order
    name = input("Welcome to Burger Shop! Please enter your name: ")
    o = Order(name)

    # repeat taking orders until client is done
    while True:
        order_prompt = "What would you like to add to your order? Please select from the following: burger, side, drink, or combo."
        order_options = ['burger', 'side', 'drink', 'combo']
        option, index = pick(order_options, order_prompt)

        match option:
            case 'burger':  o.add_item(user_input_burger())
            case 'side':    o.add_item(user_input_side())
            case 'drink':   o.add_item(user_input_drink())
            case 'combo':   o.add_item(user_input_combo())

        loop_exit_title = "Would you like to add more items to your order, remove items, review your order, or finish your order??"
        order_options = ['I would like to add more items.',
                         'I would like to remove an item.', 'I would like to review my order.', 'I have finished my order']
        option, index = pick(order_options, loop_exit_title)

        match index:
            case 0:
                pass

            case 1:
                o.remove_item(option)

            case 2:
                o.review_order()
                input("Press Enter to continue...")

            case 3:
                break

        # Check automatically if the current list of food items can be put in a combo

    # Display a thank you message and order details


take_order()
