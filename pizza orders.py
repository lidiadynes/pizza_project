import datetime

PIZZA_MENU = {'1': ['tomato', 'garlic', 'oregano'], '2': [tomato, mozzarella, basil], '3': [broccoli, mozzarella, sausage],
               '4': [ham, mozzarella, ricotta, mushrooms], '5': [tomato, oregano, garlic, capers, olives, anchovies, mozarella],
               '6': [tomato, chorizo, mozarella]}

PIZZA_PRICES = {'1': 4.50, '2': 5.90, '3': 6.85, '4': 6.85, '5': 6.70, '6': 6.95}

TOPPING_PRICES = {}

DRINKS_PRICES = {'ten_bianco750': 14.95, 'ten_bianco175': 3.90, 'ten_rosso750': 14.95, 'ten_rosso175': 3.90,
                 'car_bianco750': 15.95, 'car_bianco175': 4.15, 'car_rosso750': 15.95, 'car_rosso175': 4.15,
                 'fra_bianco750': 17.95, 'fra_bianco175': 4.50, 'fra_rosso750': 17.95, 'fra_rosso175': 4.50, 'fra_rose750': 17.95, 'fra_rose175': 4.50
                 'bub_bianco750': 19.50, 'bub_bianco175': 5.00, 'bub_lambrusco750': 19.50, 'bub_lambrusco175': 5.00
                 'ale': 3.40, 'lager': 3.40
                 'lemonade': 2.20, 'orange_juice': 2.55, 'apple_juice': 2.55, 'sparkling_water': 2.00, 'beans': 1.60}

SALAD_PRICES = {'mixed_salad': 2.45, 'franco_salad': 3.55}

class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Pizza(Item):

    def __init__(self, name, price, toppings):
        Item.__init__(self, name, price)
        self.toppings = toppings

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        self.toppings.remove(topping)

class Order:

    def __init__(self):
        self.items = []

    def time_ordered(self):
        return datetime.datetime

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_drink(self, drink):
        self.items.append(drink)

    def remove_drink(self, drink):
        self.items.remove(drink)

    def add_salad(self, salad):
        self.items.append(salad)

    def remove_salad(self, salad):
        self.items.remove(salad)

    def add_pizza(self, pizza):
        self.items.append(pizza)

    def remove_pizza(self, pizza):
        self.items.remove(pizza)

class Customer:

    def __init__(self, name):
        self.first_name = name
