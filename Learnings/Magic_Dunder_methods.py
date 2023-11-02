class Employee1:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i

    def __str__(self):
        return f"The name of the employee is Ranjit str"

    def __repr__(self):
        return f"Employee ('{self.name}')"

    def __call__(self):
         print(f"Hey there I am Ranjit")


a = Employee1("Elon")
print(a.name)
print(len(a))
