

class Order:
    def __init__(self, menu, items, number):
        self.menu = menu
        self.items = items
        self.order_number = number
        self.cost = 0
        self.day_ordered = ""
        self.time_ordered = ""
        for name in items:
            self.cost += self.menu.get_menu_price(name) * items[name]

    def set_qty(self, name, qty):
        self.remove_item(name)
        self.items[name] = qty
        self.cost += self.menu.get_menu_price(name) * qty

    def remove_item(self, name):
        if not self.number_of_items(name) == 0:
            qty = self.items[name]
            self.cost -= self.menu.get_menu_price(name) * qty
            del self.items[name]

    def number_of_items(self, name):
        if self.items.keys().count(name) == 1:
            return self.items[name]
        else:
            return 0

    def to_string(self):
        string = ""
        for name in self.items:
            price_string = "%.2f" % (self.items[name] * self.menu.get_menu_price(name))
            string += name.ljust(28) + str(self.items[name]).ljust(12) + unichr(163) + price_string + "\n"
        return string

    def items_to_string(self):
        for key in self.items.keys():
            print key, " : ", dict[key]
