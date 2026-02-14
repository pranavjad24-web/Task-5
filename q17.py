class UtilityBill:
    def __init__(self, customer, units):
        self.customer = customer
        self.units = units

class ElectricityBill(UtilityBill):
    def calculate(self):
        return self.units * 6

class WaterBill(UtilityBill):
    def calculate(self):
        return self.units * 2

bill = ElectricityBill("Pranav", 100)
print("Bill Amount:", bill.calculate())
