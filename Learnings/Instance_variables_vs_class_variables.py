class Employee:
    CompanyName = "Apple"               # Class variable        this is same for all employee

    def __init__(self, name):
        self.name = name                # Instance variables    this is different for all employee
        self.raise_amount = 0.02        # Instance variables    this is different for all employee

    def show_details(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.CompanyName}"
              f" is {self.raise_amount}")


# Employee.show_details(a)
emp1 = Employee("Ranjit")
emp1.raise_amount = 10
emp1.CompanyName = "Apple India"
emp1.show_details()
emp2 = Employee("Elon")
emp2.show_details()
