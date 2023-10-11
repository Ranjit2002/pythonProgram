"""
class Employee:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id

    def details(self):
        print(f"The name of the employee: {self.id} is {self.name}")

class Programmer(Employee):     # Class programmer inherits Employee
    def language(self):
        print(f"The default language is Python")

class Expert(Programmer):
    def fibonacci(self, n):
        list1 = list()
        first, second, third = 0, 1, 0
        for i in range(n):
            list1.append(first)
            first = first + second
            second = third
            third = first
        print(list1)


a = Employee("Ranjit", 456)
a.details()
print()

b = Programmer("Elon", 346)
b.details()
b.language()
print()

c = Expert("Steve", 785)
c.details()
c.language()
c.fibonacci(20)
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent class: {self.name}")


class Child(Parent):                                # By using super() function
    def __init__(self, name, additional_info):
        # Using super() to call the constructor of the parent class
        super().__init__(name)
        self.additional_info = additional_info

    def display(self):
        # Using super() to call the display method of the parent class
        super().display()
        print(f"Child class: {self.additional_info}")


# Creating an instance of the Child class
child_obj = Child("John", "Likes Python")

# Calling the display method of the Child class
child_obj.display()
