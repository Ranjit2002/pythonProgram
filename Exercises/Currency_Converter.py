# Create a currency converter which converts Indian currency into any 5 country currency
class Currency:
    def __init__(self):
        self.Dollar = 83.28
        self.Euro = 88.93
        self.Dinar = 269.73
        self.Rial = 216.35
        self.Franc = 92.42

    def Dollar_to_Inr(self):
        while True:
            try:
                print()
                rupee = float(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.Dollar:.2f} Dollars\n")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def Euro_to_Inr(self):
        while True:
            try:
                print()
                rupee = float(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.Euro:.2f} Euros\n")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def Dinar_to_Inr(self):
        while True:
            try:
                print()
                rupee = float(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.Dinar:.2f} Dinar\n")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def Rial_to_Inr(self):
        while True:
            try:
                print()
                rupee = float(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals {rupee / self.Rial:.2f} Rial\n")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def Franc_to_Inr(self):
        while True:
            try:
                print()
                rupee = float(input("Enter how many rupees:- "))
                print(f"{rupee} Indian rupees is equals to {rupee / self.Franc:.2f} Franc\n")
                break
            except Exception as e:
                print(type(e))
                print(e, "\n")


if __name__ == '__main__':
    a = Currency()
    while True:
        try:
            print("1 --> Dollar to Rupees\n2 --> Euro to Rupees\n3 --> Dinar to Rupees\n4 --> Rial to Rupees\n"
                  "5 --> Franc to Rupees\n6 --> Exit")
            choice = float(input("Enter your choice:- "))
            if choice == 1:
                a.Dollar_to_Inr()
            elif choice == 2:
                a.Euro_to_Inr()
            elif choice == 3:
                a.Dinar_to_Inr()
            elif choice == 4:
                a.Rial_to_Inr()
            elif choice == 5:
                a.Franc_to_Inr()
            elif choice == 6:
                break
            else:
                print("\nPlease enter number between 1 to 6\n")
                continue
        except Exception as ex:
            print()
            print(type(ex))
            print(ex, "\n")
