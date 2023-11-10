class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, Dance):
        self.Dance = Dance

    def show(self):
        print(f"The Dance is {self.Dance}")


class DancerEmployee(Employee, Dancer):
    def __init__(self, name, Dance):
        self.name = name
        self.Dance = Dance


a = DancerEmployee("Ranjit", "Kathak")
print(a.name)
print(a.Dance)
a.show()
print(DancerEmployee.mro())
