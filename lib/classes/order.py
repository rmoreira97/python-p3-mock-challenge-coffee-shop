class Order:
    def __init__(self, customer, coffee, price):
        if not (isinstance(price, (int, float)) and 1 <= price <= 10):
            raise Exception("Price must be a number between 1 and 10.")
        self._price = price
        self._customer = customer
        self._coffee = coffee
        coffee.orders.append(self)
        customer.orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not (isinstance(value, (int, float)) and 1 <= value <= 10):
            raise Exception("Price must be a number between 1 and 10.")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise Exception("Customer must be an instance of Customer class.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise Exception("Coffee must be an instance of Coffee class.")
        self._coffee = value
