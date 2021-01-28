from abc import ABC, abstractmethod


class X(ABC):

    @abstractmethod
    def hi(self):
        pass

    def hello(self):
        pass


class Y(X):
    def hi(self):
        print("Hello from Y")


class Z(Y):
    def hello(self):
        print("Hello from Z")


obj = Z()
obj.hi()
obj.hello()
