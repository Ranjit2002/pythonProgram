# Polymorphism in python is the ability of an object to take many forms
# e.g = (person, rice, milk)
# Python doesn't support method overriding

# len():
Students = ["Emma", "Jessa", "Kelly"]
School = "ABC School"
# Calculate count
# print(len(Students))
# print(len(School))

# e.g:
# "+"
# "a"+"b" = ab
# 3 + 7 = 10

# e.g = Method overriding
# Polymorphism allows us to define methods in the child class that have the same name as the methods in the parent class
# This process of re-implementing the inherited method in the child class is known as method overriding

class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(f"Details: {self.name}, {self.color}, {self.price}")

    def max_speed(self):
        print("Vehicle max speed is 150")

    def change_gear(self):
        print("Vehicle change 6 gear")


class Car(Vehicle):
    def max_speed(self):
        print("Car max speed is 240")

    def change_gear(self):
        print("Car change 7 gear")


# Car object
car = Car("Tesla", "Red", 300000)
# car.show()
# Calls methods from car class
# car.max_speed()
# car.change_gear()
# print()

vehicle = Vehicle("Cyber Truck", "Black", 500000)
# vehicle.show()
# Calls methods from vehicle class
# vehicle.max_speed()
# vehicle.change_gear()


# Polymorphism with iteration
class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type is Petrol")

    def max_speed(self):
        print("Max speed of ferrari is 350")


class BMW:
    def fuel_type(self):
        print("BMW fule type is Diesel")

    def max_speed(self):
        print("Max speed of BMW is 240")


# ferrari = Ferrari()
# bmw = BMW()
#
# for i in ferrari, bmw:
#     i.fuel_type()
#     i.max_speed()
#     print()


class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type is Petrol")

    def max_speed(self):
        print("Max speed of ferrari is 350")


class BMW:
    def fuel_type(self):
        print("BMW fule type is Diesel")

    def max_speed(self):
        print("Max speed of BMW is 240")


def car_details(obj):
    obj.fuel_type()
    obj.max_speed()


# ferrari = Ferrari()
# bmw = BMW()
#
# car_details(ferrari)
# print()
# car_details(bmw)

def addition(a, b):
    c = a + b
    print(c)

def addition(a, b, c):
    d = a + b + c
    print(d)

# The below shows an error
# addition(4, 5)

# This line will call the second product method
addition(3, 7, 5)
