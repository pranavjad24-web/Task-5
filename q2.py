class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def display(self):
        print("Balance:", self.balance)

acc = BankAccount(101, "Pranav", 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.display()
