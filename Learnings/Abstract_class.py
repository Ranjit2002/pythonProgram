"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def set_age(self):
        return self.__age

    @set_age.setter
    def set_age(self, New_age):
        self.__age = New_age


a = Employee("Ranjit", 21)
print(f"Name: {a.name}, Age: {a.set_age}")
a.set_age = 50
print(f"Name: {a.name}, Age: {a.set_age}")


class student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.__age = age
        self.__roll_no = roll_no

    def show(self):
        print(f"Name: {self.name}, Age: {self.__age}, Roll no.: {self.__roll_no}")

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, New_roll_no):
        if New_roll_no > 50:
            print("Invalid roll no! Please enter correct roll no")
        else:
            self.__roll_no = New_roll_no


a = student("Steve", 50, 20)
a.show()
print(a._student__roll_no)      # object_name._class_name__variable_name

a.set_roll_no(99)
a.show()

a.set_roll_no(42)
a.show()
"""

from abc import ABC, abstractmethod

class shape(ABC):
    def area(self):
        pass

    def parameter(self):
        pass


class square(shape):
    def __init__(self):
        self.side = 5
        print(self.side)


a = shape()
a1 = square()
