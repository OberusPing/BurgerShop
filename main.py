from pick import pick
import json

# import json with menu items and load data into objects
with open('menu.json', 'r') as f:
    data = json.load(f)

for category in data['food-item-categories']:
    if category['name'] == 'Burgers':
        burgers = [category['menu-items']]
    if category['name'] == 'Sides':
        sides = [category['menu-items']]
    if category['name'] == 'Drinks':
        drinks = [category['menu-items']]

print(burgers[0][0])

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

    def __init__(self, price: float, name: str, description: str, *condiments) -> None:
        super().__init__(price, name, description)
        self.condiments = condiments


class Drink(FoodItem):
    def __init__(self, price: float, name: str, size='small'):
        super(Drink, self).__init__(price, name)
        self.size = size


    pass


class Side(FoodItem):
    def __init__(self, price: float, name: str):
        super(Drink, self).__init__(price, name)

    pass


class Combo(FoodItem):
    pass


class Order:
    food_items = []
    name = ""
    order_price = 0.0

    def __init__(self, name: str) -> None:
        self.name = name

    def addItem(self, FoodItem: FoodItem) -> None:
        self.food_items.append(FoodItem)
        order_price += FoodItem.price

    def removeItem(self, FoodItem: FoodItem) -> None:
        self.foodItems.remove(FoodItem)
        order_price -= FoodItem.price

    def calculate_price(self) -> float:
        return self.order_price


def user_input_burger():
    b = Burger(option)

    # ask user for input and store it in burger object
    title = 'What burger do you want?'
    options = ['Chicken Burger', 'Vegan Burger']
    option, index = pick(options, title)
    title = 'What size is the drink?'

    return b


def user_input_drink():
    d = Drink()
    # ask user for input and store it in drink object
    return d


def user_input_side():
    s = Side()
    # ask user for input and store it in side object
    return s


def user_input_combo():
    c = Combo()
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
    return c


def take_order():
    # ask user for name for the order
    # repeat taking order until client is done
    # display order details
    # display a thank you message
    name = input("Welcome to Burger Shop! Please enter your name: ")
    o = Order(name)

    while True:
        title = "What would you like to add to your order? Please select from the following: burger, side, drink, or combo."
        options = ['burger', 'side', 'drink', 'combo']
        option, index = pick(options, title)

        match option:
            case 'burger': o.addItem(user_input_burger())
            case 'side': o.addItem(user_input_side())
            case 'drink': o.addItem(user_input_drink())
            case 'combo': o.addItem(user_input_combo())

        loop_exit = input(
            "Would you like to add more items to your order? (Y/N)").lower()

        if loop_exit == "n":
            break


take_order()
