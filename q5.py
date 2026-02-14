class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car is driving smoothly")

class Bike(Vehicle):
    def drive(self):
        print("Bike is riding fast")

c = Car("Hyundai","Petrol")
c.drive()
