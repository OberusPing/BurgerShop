#!/usr/bin/env python3

"""
__author__  Team 6
__date__ 2022/06/

"""
from pick import pick
import pandas as pd
from tabulate import tabulate
from datetime import datetime
import json
#from json2html import *
import os

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


class Side(FoodItem):
    def __init__(self, price: float, name: str, description: str):
        super(Side, self).__init__(price, name, description)


class Combo(Burger, Drink, Side):
    name = ""
    burger = None
    side = None
    drink = None
    price = 0.0
    description = ""

    def __init__(self, burger: Burger, drink: Drink, side: Side) -> None:
        self.burger = burger
        self.drink = drink
        self.side = side
        self.name = f"{burger.name}, {side.name}, {drink.name}"
        self.description = "A delicious combo!"
        self.price = float("{:.2f}".format(
            (burger.price + drink.price + side.price)*0.9))


class Order:
    food_items = []
    name = ""
    order_price = 0.0

    def __init__(self, name: str) -> None:
        self.name = name

    def add_item(self, FoodItem: FoodItem) -> None:
        self.food_items.append(FoodItem)
        self.order_price += FoodItem.price

    def get_item_name(item): return item.name

    def remove_item(self) -> None:
        item_names = []
        for item in self.food_items:
            item_names.append(item.name)

        item, index = pick(item_names, "Please select the item to remove.")
        self.order_price -= self.food_items[index].price
        del self.food_items[index]

    def calculate_price(self) -> float:
        return self.order_price

    def review_order(self) -> None:
        print("Your current order is the following: \n")
        for item in self.food_items:
            print(f"{item.name}: {item.price} ({item.description})\n")
        print(f"Current total price: {self.order_price}")

    def add_to_order(self) -> None:
        order_prompt = "What would you like to add to your order? Please select from the following: burger, side, drink, or combo."
        order_options = ['burger', 'side', 'drink', 'combo']
        option, index = pick(order_options, order_prompt)

        match option:
            case 'burger':  self.add_item(user_input_burger())
            case 'side':    self.add_item(user_input_side())
            case 'drink':   self.add_item(user_input_drink())
            case 'combo':   self.add_item(user_input_combo())

    def build_receipt(self) -> None:
        now = datetime.now()
        df = pd.DataFrame(data, columns=['Name', 'Quantity', 'Price'])
        for item in self.food_items:
            if ((df['Name'] == item.name.split(':')[0]) & (df['Price'] == item.price)).any():
                df['Quantity'][((df['Name'] == item.name.split(
                    ':')[0]) & (df['Price'] == item.price))] += 1
            else:
                df = pd.concat(
                    [pd.DataFrame({'Name': [item.name.split(':')[0]], 'Quantity': [1], 'Price': [item.price]}),
                     df.loc[:]]).reset_index(drop=True)

        if self.promo_code():
            order_price_promo = float('{:.2f}'.format((self.order_price)*0.85))
        else:
            order_price_promo = self.order_price

        os.system('cls||clear')

        print("--------------------------------------------------------------------------")
        print("-------------------WELCOME TO Data Diggers Burger Shop--------------------")
        print(f"                                 {now.strftime('%d/%m/%Y')}")
        print(f"                                  {now.strftime('%H:%M:%S')}")
        print("--------------------------------------------------------------------------")

        print(tabulate(df, tablefmt="pipe", numalign="center",
                       headers=['       Name       ', '      Quantity      ', '     Price     ']))
        print("--------------------------------------------------------------------------")
        print(
            f"                                 Subtotal = {self.order_price}$")
        print(
            f"                          Subtotal after promotion= {order_price_promo}$")
        print("--------------------------------------------------------------------------")
        print(
            f"            Thank you for shopping at the Burger Shop {self.name}!")
        print("--------------------------------------------------------------------------")

    def promo_code(self) -> None:
        promo = "abc123"
        response, idx = pick(
            ['Yes', 'No'], "Do you want to use your promo code?")
        while True:
            if idx == 0:
                in_promo = input("Please enter Promo Code: ").lower()
                if promo != in_promo:
                    response, idx = pick(
                        ['Yes', 'No'], "Sorry, Promo Code does not exist! Do you want to try again?")
                    continue
                else:
                    return True
                    break
            else:
                return False
                break


def user_input_burger() -> Burger:
    burger_names = []
    for burger in burgers:
        burger_names.append(
            f"{burger['name']}: {burger['price']} ({burger['description']})")

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

    options = pick(condiment_names, "Please select any condiments to add to your burger (press SPACE to mark, ENTER to continue). Multiple condiments can be chosen.",
                   multiselect=True, min_selection_count=0)

    for option in options:
        b_condiments.append(option[0])

    b = Burger(b_price, b_name, b_description, b_condiments)

    return b


def user_input_drink():
    drink_names = []
    for drink in drinks:
        drink_names.append(
            f"{drink['name']}: {drink['price']}")

    name, index = pick(
        drink_names, "Please select a drink to add to your order.")

    description = drinks[index]['description']
    d_name = drinks[index]['name']
    d_price = drinks[index]['price']

    size_desc, index = pick(['Small', 'Medium (+ $1)', 'Large (+ $2)'],
                            "What is your preference for cup size?")

    if index == 0:
        size = 'Small'
    elif index == 1:
        d_price += 1
        size = 'Medium'
    else:
        size = 'Large'
        d_price += 2

    d = Drink(d_price, d_name, size, description)
    return d


def user_input_side():
    side_names = []
    for side in sides:
        side_names.append(
            f"{side['name']}: {side['price']} ({side['description']})")

    options, index = pick(
        side_names, "Please select a side dish to add to your order.")

    s_name = sides[index]['name']
    price = float(sides[index]['price'])
    description = sides[index]['description']

    s = Side(price, s_name, description)

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
    o.add_to_order()

    # repeat taking orders until client is done
    while True:
        os.system('cls||clear')
        loop_exit_title = "Would you like to add more items to your order, remove items, review your order, or finish your order??"
        order_options = ['I would like to add more items.',
                         'I would like to remove an item.', 'I would like to review my order.', 'I have finished my order']
        option, index = pick(order_options, loop_exit_title)

        match index:
            case 0:
                o.add_to_order()

            case 1:
                o.remove_item()

            case 2:
                o.review_order()
                input("Press Enter to continue...")

            case 3:
                break

        # Check automatically if the current list of food items can be put in a combo

    # Display a thank you message and order details
    o.build_receipt()


if __name__ == "__main__":
    take_order()
