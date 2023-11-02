"""
class Parentclass:
    def Parent_method(self):
        print(f"This is parent class method")


class Childclass(Parentclass):
    def Parent_method(self):
        print("Ranjit")
        super().Parent_method()                     # Calling parent class method using super keyword

    def Child_method(self):
        print(f"This is child class method")
        super().Parent_method()                     # Calling parent class method using super keyword


a = Parentclass()
a.Parent_method()
print()

b = Childclass()
b.Child_method()
b.Parent_method()
"""


class Employee:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id


class Programmer(Employee):
    def __init__(self, name, Id, lang):
        super().__init__(name, Id)  # Calling parent class constructor using super keyword
        self.lang = lang


a = Employee("Steve", 234)
print(a.name)
print(a.id)
print()

b = Programmer("Ranjit", 124, "Python")
print(b.name)
print(b.id)
print(b.lang)
print()

# This is from another class

from Magic_Dunder_methods import Employee1

c = Employee1("Ranjit")
print(c)
print(str(c))
print(repr(c))
c()
