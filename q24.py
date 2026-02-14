class PaymentSource:
    def pay(self, amount):
        pass

class Card(PaymentSource):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")

class Wallet:
    def __init__(self):
        self.sources = []

    def add_source(self, source):
        self.sources.append(source)

    def make_payment(self, source, amount):
        source.pay(amount)

w = Wallet()
c = Card()
w.add_source(c)
w.make_payment(c, 1000)
