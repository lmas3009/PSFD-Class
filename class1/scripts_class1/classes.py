class Student:
    def __init__(self, name, rno, phno):
        self.name = name
        self.rno = rno
        self.phno = phno

    def display(self):
        print(self.name, self.rno, self.phno)


Student("amith", 123, 1234567890).display()
