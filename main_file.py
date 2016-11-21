import datetime
import bst_file

PIZZA_MENU = {'1': ['tomato', 'garlic', 'oregano'], '2': ['tomato', 'mozzarella', 'basil'], '3': ['broccoli', 'mozzarella', 'sausage'],
              '4': ['ham', 'mozzarella', 'ricotta', 'mushrooms'], '5': ['tomato', 'oregano', 'garlic', 'capers', 'olives', 'anchovies', 'mozarella'],
              '6': ['tomato', 'chorizo', 'mozarella']}

PIZZA_PRICES = {'1': 4.50, '2': 5.90, '3': 6.85, '4': 6.85, '5': 6.70, '6': 6.95}

TOPPING_PRICES = {'olives': 1.25, 'mozarella': 0.90, 'ham': 1.50, 'chorizo': 1.75, 'capers': 0.90}

DRINKS_PRICES = {'ten_bianco750': 14.95, 'ten_bianco175': 3.90, 'ten_rosso750': 14.95, 'ten_rosso175': 3.90,
                 'car_bianco750': 15.95, 'car_bianco175': 4.15, 'car_rosso750': 15.95, 'car_rosso175': 4.15,
                 'fra_bianco750': 17.95, 'fra_bianco175': 4.50, 'fra_rosso750': 17.95, 'fra_rosso175': 4.50, 'fra_rose750': 17.95, 'fra_rose175': 4.50,
                 'bub_bianco750': 19.50, 'bub_bianco175': 5.00, 'bub_lambrusco750': 19.50, 'bub_lambrusco175': 5.00,
                 'lemonade': 2.20, 'orange_juice': 2.55, 'apple_juice': 2.55, 'sparkling_water': 2.00, 'beans': 1.60}

SALAD_PRICES = {'mixed_salad': 2.45, 'franco_salad': 3.55}

def item_price(item):
    if item in PIZZA_PRICES:
        return PIZZA_PRICES[item]
    elif item in TOPPING_PRICES:
        return TOPPING_PRICES[item]
    elif item in DRINKS_PRICES:
        return DRINKS_PRICES[item]
    else:
        return SALAD_PRICES[item]

class Order:
    def __init__(self, number):
        self.number = number
        self.items = []
        self.cost = 0

    def time_ordered(self):
        return datetime.datetime

    def add_item(self, item):
        self.items.append(item)
        self.cost += item_price(item)

    def remove_item(self, item):
        self.items.remove(item)
        self.cost -= item_price(item)

    def order_total(self):
        return self.cost

    def dump(self):
        s = 'You have ordered: %s , The total comes to %s' % \
            (self.items, self.order_total)
        print s

    def confirm(self):
        #restaurant class puts it in the queue

class Restaurant:
    def __init__(self):
        self.orders = []
        self.total_restaurant_orders = 0
        self.customers = []
        self.number_of_customers = 0

    def restaurant_customers(self, customer):
        s = set(self.customers)
        if customer in s:
            customer.number_of_orders += 1
        else:
            customer = Customer(customer)
            self.number_of_customers += 1

    def orders(self, customer):
        self.restaurant_orders += 1
        n = self.total_restaurant_orders
        customer = Order(n)

    def isEmpty(self):
        return self.orders == []

    def enqueue(self, order):
        self.orders.insert(0,order)
        self.total_restaurant_orders += 1

    def dequeue(self):
        return self.orders.pop()

    def size_of_queue(self):
        return len(self.orders)

class Customer:
    def __init__(self, first_name, last_name, postcode, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.postcode = postcode
        self.phone_no = phone_no
        self.number_of_orders = 0
        self.money_spent = 0

    def orders(self):
        if customer:
            self.number_of_orders += 1
            self.money_spent += order_total()

    def dump(self):
        s = '%s, %s, Address: %s, Contact Number: %s, Number of orders: %s, Money spent at the restaurant: %s' % \
            (self.last_name, self.first_name, self.postcode, self.phone_no, self.number_of_orders, self.money_spent)
        print s

def create_customers_bst(number_of_orders):
    bst = binary_search_tree.bst_file.BinarySearchTree()
    for name in last_names:
        bst[name.last_name] = name
    return bst

def create_popular_menu_items_bst(times_ordered):
    bst = binary_search_tree.bst_file.BinarySearchTree()
    for item in items:
        bst[item.times_ordered] = item
    return bst