class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        self.items.pop(item, None)

    @property
    def total_price(self):
        return sum(item.price * qty for item, qty in self.items.items())

    def clear(self):
        self.items = {}