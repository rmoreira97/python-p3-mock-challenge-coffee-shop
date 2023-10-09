class Customer:
    def __init__(self, name):
        if not (isinstance(name, str) and 1 <= len(name) <= 15):
            raise Exception("Name must be a string of length 1-15 characters.")
        self._name = name
        self.orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (isinstance(value, str) and 1 <= len(value) <= 15):
            raise Exception("Name must be a string of length 1-15 characters.")
        self._name = value

    def get_coffees(self):
        return [order.coffee for order in self.orders]
