class Employee:
    def __init__(self, name, age, Id):
        self.name = name
        self.age = age
        self.id = Id
        self.company = "Apple"

    def details(self):
        print(f"The employee {self.name} is {self.age} years old and his id is {self.id}")

    def phone(self):
        print(f"He works in a {self.company}")


if __name__ == "__main__":  # We use this if we don't want to run all functions
    a = Employee("Ranjit", 23, 76)
    a.details()
    a.phone()
    a.name = "Harry"
    a.age = 29
    a.id = 92
    a.details()
    a.company = "Google"
