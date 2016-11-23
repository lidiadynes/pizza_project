import datetime

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