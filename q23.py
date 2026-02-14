from abc import ABC, abstractmethod

class Attendance(ABC):
    @abstractmethod
    def mark(self, name):
        pass

class ManualAttendance(Attendance):
    def mark(self, name):
        print(f"{name} marked present manually")

class FaceRecognitionAttendance(Attendance):
    def mark(self, name):
        print(f"{name} marked present via Face Recognition")

a = ManualAttendance()
a.mark("Pranav")
