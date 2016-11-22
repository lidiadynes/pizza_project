import datetime
import bst

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