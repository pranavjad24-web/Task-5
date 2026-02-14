class UpdateStrategy:
    def apply_update(self):
        pass

class AutomaticUpdate(UpdateStrategy):
    def apply_update(self):
        print("Update installed automatically")

class ManualUpdate(UpdateStrategy):
    def apply_update(self):
        print("User confirmed and update installed")

u = AutomaticUpdate()
u.apply_update()
