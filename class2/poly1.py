class Cat:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def info(self):
        print(
            f"This is cat and my name is {self.name} and age is {self.value}")


class Dog:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def info(self):
        print(
            f"This is dog and my name is {self.name} and age is {self.value}")


cat1 = Cat("Luccy", 1.4)
dog1 = Dog("tommy", 2)

for i in (cat1, dog1):
    i.info()
