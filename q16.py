from abc import ABC, abstractmethod

class GradingPolicy(ABC):
    @abstractmethod
    def compute_grade(self, marks):
        pass

class NormalGrading(GradingPolicy):
    def compute_grade(self, marks):
        if marks >= 90: return "A"
        elif marks >= 75: return "B"
        elif marks >= 50: return "C"
        return "Fail"

class StrictGrading(GradingPolicy):
    def compute_grade(self, marks):
        if marks >= 95: return "A"
        elif marks >= 85: return "B"
        elif marks >= 60: return "C"
        return "Fail"

policy = StrictGrading()
print(policy.compute_grade(88))
