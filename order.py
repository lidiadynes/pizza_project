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