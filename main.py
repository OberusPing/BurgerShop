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

    def add_item(self, FoodItem: FoodItem) -> None:
        self.food_items.append(FoodItem)
        self.order_price += FoodItem.price

    def remove_item(self, FoodItem: FoodItem) -> None:
        self.foodItems.remove(FoodItem)
        self.order_price -= FoodItem.price

    def calculate_price(self) -> float:
        return self.order_price

    def return_order(self) -> str:
        pass


def user_input_burger() -> Burger:
    burger_names = []
    for burger in burgers[0]:
        burger_names.append(burger['name'])

    # ask user for input and store it in burger object
    option, index = pick(
        burger_names, "Please select a burger to add to your order.")

    b_name = burgers[0][index]['name']
    b_price = burgers[0][index]['price']
    b_description = burgers[0][index]['description']

    # ask user if they want to add condiments
    b_condiments = []

    options = pick(["ketchup", "mustard"], "Please select any condiments to add to your burger (press SPACE to mark, ENTER to continue).",
                   multiselect=True, min_selection_count=0)

    for option in options:
        b_condiments.append(option[0])

    b = Burger(b_price, b_name, b_description, b_condiments)

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
    name = input("Welcome to Burger Shop! Please enter your name: ")
    o = Order(name)

    # repeat taking orders until client is done
    while True:
        order_prompt = "What would you like to add to your order? Please select from the following: burger, side, drink, or combo."
        order_options = ['burger', 'side', 'drink', 'combo']
        option, index = pick(order_options, order_prompt)

        match option:
            case 'burger': o.add_item(user_input_burger())
            case 'side': o.add_item(user_input_burger())
            case 'side': o.add_item(user_input_side())
            case 'drink': o.add_item(user_input_drink())
            case 'combo': o.add_item(user_input_combo())

        loop_exit_title = "Would you like to add more items to your order, remove items, review your order, or finish your order??"
        order_options = ['I would like to add more items.',
                         'I would like to remove an item.', 'I would like to review my order.', 'I have finished my order']
        option, index = pick(order_options, loop_exit_title)

        match index:
            case 0:
                pass

            case 1:
                option, index = pick(
                    o.food_items, "Please select the item to remove.")
                o.remove_item(option)

            case 2:
                print(o.food_items.__str__)
                input("Press Enter to continue...")

            case 3:
                break

    # Display a thank you message and order details


take_order()
