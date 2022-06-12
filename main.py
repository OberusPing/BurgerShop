from pick import pick

# implement the classes listed below


class FoodItem:
    price = None
    name = None

    def __init__(self, price: float, name: str) -> None:
        self.price = price
        self.name = name


class Burger(FoodItem):
    condiments = []

    def __init__(self, price: float, name: str, *condiments) -> None:
        super().__init__(price, name)
        self.condiments = condiments


class Drink(FoodItem):
    pass


class Side(FoodItem):
    pass


class Combo(FoodItem):
    pass


class Order:
    foodItems = []
    name = ""

    def __init__(self, name: str) -> None:
        self.name = name

    def addItem(self, FoodItem: FoodItem) -> None:
        self.foodItems.append(FoodItem)

    def removeItem(self, FoodItem: FoodItem) -> None:
        self.foodItems.remove(FoodItem)


def user_input_burger():
    b = Burger()

    # ask user for input and store it in burger object
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
