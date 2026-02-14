class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

class BusTicket(Ticket):
    def fare(self, distance):
        return distance * 5

class TrainTicket(Ticket):
    def fare(self, distance):
        return distance * 3

t = BusTicket("A","B")
print(t.fare(10))
