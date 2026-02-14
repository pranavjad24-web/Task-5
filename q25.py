from abc import ABC, abstractmethod

class InferenceStrategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class RuleBased(InferenceStrategy):
    def execute(self, data):
        return "Rule-based result"

class NeuralNetwork(InferenceStrategy):
    def execute(self, data):
        return "Neural Network result"

engine = NeuralNetwork()
print(engine.execute("input data"))
