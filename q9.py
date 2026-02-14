class Course:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def register(self, course):
        if course.name not in self.courses:
            self.courses.append(course.name)
            print("Registered successfully")
        else:
            print("Already registered")

c1 = Course("AI")
s1 = Student("Pranav")
s1.register(c1)
s1.register(c1)
