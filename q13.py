from abc import ABC, abstractmethod

class Exam(ABC):
    def __init__(self, subject, max_marks):
        self.subject = subject
        self.max_marks = max_marks

    @abstractmethod
    def evaluate(self, marks):
        pass

class TheoryExam(Exam):
    def evaluate(self, marks):
        return marks

class PracticalExam(Exam):
    def evaluate(self, marks):
        return marks + 5  # Grace

e = PracticalExam("Python", 100)
print(e.evaluate(80))
