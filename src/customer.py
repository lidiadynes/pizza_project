# Class for keeping track of customer information
class Customer:
    def __init__(self, first_name, last_name, postcode, phone, email, order_numbers=[], total_orders=0, money_spent=0):
        self.first_name = first_name
        self.last_name = last_name
        self.postcode = postcode
        self.phone = phone
        self.email = email
        self.order_numbers = order_numbers
        self.total_orders = total_orders
        self.money_spent = money_spent

    # Add order data to customer object
    def add_customer_order(self, order):
        self.order_numbers.append(order.order_number)
        self.total_orders += 1
        self.money_spent += order.cost
