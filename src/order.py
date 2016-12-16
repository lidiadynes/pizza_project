
# Class for keeping track of an order
class Order:
    def __init__(self, menu, items, number):
        self.menu = menu
        self.items = items
        self.order_number = number
        self.cost = 0
        self.day_ordered = ""
        self.time_ordered = ""
        for name in items:
            self.cost += self.menu.get(name) * items[name]

    # Set quantity of given item
    def set_qty(self, name, qty):
        self.remove_item(name)
        self.items[name] = qty
        self.cost += self.menu.get(name) * qty

    # Set quantity of given item to 0
    def remove_item(self, name):
        if not self.number_of_items(name) == 0:
            qty = self.items[name]
            self.cost -= self.menu.get(name) * qty
            del self.items[name]

    # Get number of given items in order
    def number_of_items(self, name):
        if self.items.keys().count(name) == 1:
            return self.items[name]
        else:
            return 0

    # String representing order, used on order summary page
    def to_string(self):
        string = ""
        for name in self.items:
            price_string = "%.2f" % (self.items[name] * self.menu.get(name))
            string += name.ljust(28) + str(self.items[name]).ljust(12) + unichr(163) + price_string + "\n"
        return string
