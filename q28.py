from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def interpret(self, raw):
        pass

class TemperatureSensor(Sensor):
    def interpret(self, raw):
        return raw * 0.1  # convert to °C

class PressureSensor(Sensor):
    def interpret(self, raw):
        return raw + 10

s = TemperatureSensor()
print("Temperature:", s.interpret(300))
