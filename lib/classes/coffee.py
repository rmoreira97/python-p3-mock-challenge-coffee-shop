class Coffee:
    def __init__(self, name):
        self._name = name
        self.orders = []

    @property
    def name(self):
        return self._name

    def get_customers(self):
        return [order.customer for order in self.orders]

    def num_orders(self):
        return len(self.orders)

    def average_price(self):
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders) if self.orders else 0
