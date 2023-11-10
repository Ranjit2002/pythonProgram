# x = [1, 2, 3]
# print(dir(x))
# print(x.__add__)
# print()
#
# y = (1, 2, 3)
# print(dir(y))
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


# a = Person("Ranjit", 21)
# print(a.__dict__)                       # This will give all data in the form of dictionary
                                          # like this = {'name': 'Ranjit', 'age': 21, 'version': 1}

# print(help(Person))                       # Use this if you want to know everything about that
print(help(list))
