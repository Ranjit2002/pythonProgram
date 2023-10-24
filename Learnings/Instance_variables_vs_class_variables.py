class Employee:
    CompanyName = "Apple"  # Class variable are defined at the class level and this is same for all class
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name  # Instance variables    this is different for all employee
        self.raise_amount = 0.02  # Instance variables    this is different for all employee
        Employee.noOfEmployees += 1

    def show_details(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized"
              f" {self.CompanyName} is {self.raise_amount}")


# Employee.show_details(a)
emp1 = Employee("Ranjit")
emp1.raise_amount = 10
emp1.CompanyName = "Apple India"
emp1.show_details()
Employee.CompanyName = "Google"
print(Employee.CompanyName)

emp2 = Employee("Elon")
emp2.CompanyName = "Tesla"
emp2.show_details()
