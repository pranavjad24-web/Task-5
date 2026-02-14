class Plan:
    def __init__(self, name):
        self.name = name

class BasicPlan(Plan):
    def bill(self):
        return 199

class PremiumPlan(Plan):
    def bill(self):
        return 499

p = PremiumPlan("Premium")
print("Monthly Bill:", p.bill())
