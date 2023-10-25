class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod  # @classmethod is not necessary, if we use this method then if someone will use this method then
    # that name become the class name
    def changeCompany(new, newCompany):  # We can write anything in place of new
        new.company = newCompany


a = Employee()
a.name = "Ranjit"
a.show()
a.changeCompany("Tesla")
a.show()
print(Employee.company)
