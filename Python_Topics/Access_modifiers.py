# By default, all the variables in python are public and can be accessible from inside or outside the class
"""
class Employee:
    def __init__(self):
        self.name = "Ranjit"    # Public access modifier and can be normally accessible from outside the class


a = Employee()
print(a.name)   # Public access modifier
"""


class Employee:
    def __init__(self):
        self.__name = "Ranjit"  # Private access modifier and cannot be normally accessible from outside the class


a = Employee()
# print(a.name)
print(a._Employee__name)    # This is the way that how we can indirectly access the private access modifier
                            # from outside the class
print(a.__dir__())
