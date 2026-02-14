class Package:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.status = "Pending"

class ExpressDelivery(Package):
    def update_status(self):
        self.status = "Delivered in 1 Day"

class NormalDelivery(Package):
    def update_status(self):
        self.status = "Delivered in 5 Days"

pkg = ExpressDelivery("A","B")
pkg.update_status()
print(pkg.status)
