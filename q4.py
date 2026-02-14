class Employee:
    def __init__(self, name, designation, basic):
        self.name = name
        self.designation = designation
        self.basic = basic

    def calculate_salary(self):
        if self.designation == "Manager":
            return self.basic + 5000
        elif self.designation == "Developer":
            return self.basic + 3000
        return self.basic

e = Employee("Pranav", "Manager", 40000)
print(e.calculate_salary())
