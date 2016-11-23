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