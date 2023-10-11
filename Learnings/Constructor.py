class Person:
    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


# a = Person()    # This will print what's inside the constructor

a = Person("Ranjit", "Developer")
a.info()
b = Person("Divya", "HR")
b.info()
