class currency:
    def __init__(self):
        self.America = 83.05
        self.England = 88.22
        self.Kuwait = 268.69
        self.Singapore = 60.75
        self.Australia = 52.82

    def america(self):
        while True:
            try:
                rupee = int(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.America:.2f} US dollars")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def england(self):
        while True:
            try:
                rupee = int(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.England:.2f} EU euros")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def kuwait(self):
        while True:
            try:
                rupee = int(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.Kuwait:.2f} Kuwaiti dinars")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def singapore(self):
        while True:
            try:
                rupee = int(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals {rupee / self.Singapore:.2f} Singapore dollars")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def australia(self):
        while True:
            try:
                rupee = int(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.Australia:.2f} Australian dollars")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")


a = currency()
a.america()
print()
a.england()
print()
a.kuwait()
print()
a.singapore()
print()
a.australia()
