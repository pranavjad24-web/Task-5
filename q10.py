class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

class Light(SmartDevice):
    def turn_on(self):
        super().turn_on()
        print("Light turned ON")

class Fan(SmartDevice):
    def turn_on(self):
        super().turn_on()
        print("Fan started spinning")

l = Light(1)
l.turn_on()
