class Student:
    def __init__(self, name, dept, cgpa, year):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        self.year = year

    def is_eligible(self):
        if self.cgpa >= 7.0 and self.year >= 3:
            return "Eligible for placements"
        return "Not Eligible"

s = Student("Pranav", "CSE", 8.2, 3)
print(s.is_eligible())
