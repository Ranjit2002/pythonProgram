class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split('-')[0], int(string.split('-')[1]))


a = Employee("Ranjit", 130000)
print(a.name)
print(a.salary)
print()

string = 'Steve-150000'
a1 = Employee(string.split('-')[0], string.split('-')[1])
print(a1.name)
print(a1.salary)
print()

meth = 'Elon-1000000'
a2 = Employee.fromStr(meth)     # This is the class method in class Employee() fromStr() method
print(a2.name)
print(a2.salary)
print()

print(string.split('-'))    # Split method is used to separate and converts the whole elements in a list
