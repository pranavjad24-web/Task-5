class Reservation:
    def __init__(self, name, time_slot):
        self.name = name
        self.time_slot = time_slot

class FirstComePolicy(Reservation):
    def confirm(self):
        print("Table confirmed on first-come basis")

class VIPPolicy(Reservation):
    def confirm(self):
        print("VIP reservation confirmed with priority")

r = VIPPolicy("Pranav", "7 PM")
r.confirm()
