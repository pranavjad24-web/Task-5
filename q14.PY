from abc import ABC, abstractmethod

class Auth(ABC):
    @abstractmethod
    def login(self, data):
        pass

class PasswordAuth(Auth):
    def login(self, data):
        if data == "1234":
            print("Login Success")
        else:
            print("Login Failed")

a = PasswordAuth()
a.login("1234")
