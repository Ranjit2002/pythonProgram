import functools
import time


@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print("Done for 20")

print(fx(2))
print("Done for 2")

print(fx(6))
print("Done for 6")

print(fx(20))
print("Done for 20")

print(fx(2))
print("Done for 2")

print(fx(6))
print("Done for 6")

"""
class MyClass:
    def __init__(self):
        self.__private_variable = 42

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()


# Creating an instance of the class
obj = MyClass()

# Accessing public method and variable
obj.public_method()

# Accessing private variable and method (not recommended, but possible)
print(obj._MyClass__private_variable)
obj._MyClass__private_method()
"""
