class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price

class VegFood(Food):
    def final_price(self):
        return self.price * 0.9  # 10% discount

class NonVegFood(Food):
    def final_price(self):
        return self.price * 1.1  # 10% extra tax

f = VegFood("Paneer", 200)
print(f.final_price())
