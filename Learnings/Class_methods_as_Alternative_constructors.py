class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


a = Employee("Ranjit", 12000)
print(a.name)
print(a.salary)

string = "John-12000"
a2 = Employee(string.split("-")[0], string.split("-")[1])
print(a2.name)
print(a2.salary)
