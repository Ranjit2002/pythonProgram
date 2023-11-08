# 1. Write a python function that lists and return a new list with district elements from first list
import random
def duplicate_elements(list):
    s = set(list)
    return s


d = (1, 3, 3, 2, 2, 4, 5, 5, 6, 7, 7)
f = duplicate_elements(d)
print(f)
print()

# 2. Make a bank management system using inheritance. Account holder should be able to add amount,
# remove amount and transfer amount

class Add:
    def __init__(self):
        self.Bank_amount = 150000

    def add_amount(self):
        while True:
            try:
                amount = int(input("\nEnter amount to add:- "))
                if amount > 0:
                    self.Bank_amount += amount
                    print(f"\n{amount} rupees credited to your bank account\n")
                    break
                else:
                    print("\nPlease enter number greater than 0\n")
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")


class Withdraw(Add):
    def withdraw_amount(self):
        pin = random.randrange(1000, 9999)
        i = 1
        while i <= 5:
            try:
                print(f"\nPin:- {pin}\n")
                account_pin = int(input("Enter pin:- "))
                if account_pin == pin:
                    amount = int(input("Enter amount:- "))
                    if 0 < amount <= self.Bank_amount:
                        self.Bank_amount -= amount
                        print(f"\n{amount} rupees has been debited from your account\n")
                        break
                    else:
                        print("\nPlease enter amount greater than 0 or less than bank amount\n")
                        continue
                else:
                    print(f'\nOops wrong pin, please try again\n'
                          f'You have {5 - i} chance remaining\n')
                    i += 1
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def see_amount(self):
        print(f"\nYou have {self.Bank_amount} rupees in your bank account\n")

class Transfer(Withdraw):
    def transfer_amount(self):
        pin = random.randrange(1000, 9999)
        i = 1
        while i <= 5:
            try:
                print(f"\nPin:- {pin}\n")
                account_pin = int(input("Enter pin:- "))
                if account_pin == pin:
                    name = str(input("Enter receiver name:- "))
                    amount = int(input("Enter amount:- "))
                    if 0 < amount <= self.Bank_amount:
                        self.Bank_amount -= amount
                        print(f"\n{amount} rupees has been transferred to {name}\n")
                        break
                    else:
                        print(f"\nPlease enter amount greater than 0 or less than bank amount\n")
                        continue
                else:
                    print(f'\nOops wrong pin, please try again\n'
                          f'You have {5 - i} chance remaining\n')
                    i += 1
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")


if __name__ == '__main__':
    a = Transfer()
    while True:
        try:
            print("1 --> Add amount\n2 --> Remove amount\n3 --> Transfer amount\n4 --> Bank amount\n5 --> Exit")
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                a.add_amount()
            elif choice == 2:
                a.withdraw_amount()
            elif choice == 3:
                a.transfer_amount()
            elif choice == 4:
                a.see_amount()
            elif choice == 5:
                break
            else:
                print("Please enter number between 1 to 4")
                continue
        except Exception as ex:
            print(type(ex))
            print(ex, "\n")
print()

# 4. Create a currency converter which converts Indian currency into any 5 country currency
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


# 5. Create a pyramid

def pyramid(n):
    c = 1
    for i in range(1, n+1):
        for j in range(i):
            print(c, end=" ")
            c += 1
        print()


print()
k = int(input("Enter how many lines of pyramid to print:- "))
pyramid(k)
