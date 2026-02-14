from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass

class LinearModel(MLModel):
    def train(self, data):
        print("Training Linear Model")

    def predict(self, x):
        return x * 2

class TreeModel(MLModel):
    def train(self, data):
        print("Training Tree Model")

    def predict(self, x):
        return x + 10

model = LinearModel()
model.train([1,2,3])
print(model.predict(5))
