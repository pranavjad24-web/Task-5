from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI(Payment):
    def process(self, amount):
        print(f"Paid ₹{amount} using UPI")

class Order:
    def __init__(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount

    def make_payment(self, payment_method):
        payment_method.process(self.amount)

order = Order(101, "Pranav", 1500)
order.make_payment(UPI())
