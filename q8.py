from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Email sent:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS sent:", message)

n = EmailNotification()
n.send("Welcome User")
