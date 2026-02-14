class StoragePlan:
    def __init__(self, limit):
        self.limit = limit  # in MB

    def can_upload(self, size):
        return size <= self.limit

class FreePlan(StoragePlan):
    def __init__(self):
        super().__init__(100)  # 100MB limit

class PremiumPlan(StoragePlan):
    def __init__(self):
        super().__init__(1000)  # 1GB limit

plan = FreePlan()
print("Upload allowed:", plan.can_upload(50))
