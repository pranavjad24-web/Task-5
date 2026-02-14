class Ride:
    def __init__(self, pickup, drop, distance):
        self.pickup = pickup
        self.drop = drop
        self.distance = distance

class StandardRide(Ride):
    def fare(self):
        return self.distance * 10

class PremiumRide(Ride):
    def fare(self):
        return self.distance * 20

r = PremiumRide("A","B",15)
print("Fare:", r.fare())
