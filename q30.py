from abc import ABC, abstractmethod

class DrivingMode(ABC):
    @abstractmethod
    def control(self):
        pass

class EcoMode(DrivingMode):
    def control(self):
        print("Driving in Eco Mode")

class SportMode(DrivingMode):
    def control(self):
        print("Driving in Sport Mode")

mode = SportMode()
mode.control()
