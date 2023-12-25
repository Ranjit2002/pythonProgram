"""
Banking application using encapsulation
    Bank name
    IFSC code
    Branch name
    User_Name
    User_account_number
    User_pin
    User_emailID
    User_bank_balance
"""
import random
class encapsulation_bank:
    def __init__(self, name, bank_name, IFSC_code, branch_name, account_no, account_name, email_Id, bank_balance):
        self._name = name
        self._bank_name = bank_name
        self._IFSC_code = IFSC_code
        self._branch_name = branch_name
        self._account_no = account_no
        self._account_name = account_name
        self._email_Id = email_Id
        self._bank_balance = bank_balance

    def withdraw(self):
        b = random.randrange(1000, 9999)
        i = 1
        while i < 5:
            try:
                print(f"\nPin: {b}\n")
                p = int(input("Enter pin:- "))
                if p == b:
                    print(f"\nVerify your account details\n\nName: {self._name}\nBank: {self._bank_name}\nBranch: {self._branch_name}\nAccount no.: {self._account_no}\nAccount: {self._account_name}\nEmail_Id: {self._email_Id}\n")
                    print(f"\nEnter 1 if this is your account details\nElse enter 2 if this is not your account"
                          f" details\n")
                    new = int(input("Enter your choice:- "))
                    if new == 1:
                        money = int(input("Enter how much rupees you want to withdraw:- "))
                        if money <= 0:
                            print("Please enter number greater than 0\n")
                            continue
                        else:
                            if self._bank_balance > 0 and money <= self._bank_balance:
                                print(f"\nYou withdraw {money} rupees from your account\n")
                                self._bank_balance -= money
                                break
                            else:
                                print("You don't have enough money in your account\n")
                                break
                    elif new == 2:
                        break
                    else:
                        print("Please enter 1 or 2\n")
                        continue
                else:
                    print(f"Oops try again\nYou have {5-i} chance remaining\n")
                    i += 1
            except Exception as er:
                print(type(er))
                print(er, "\n")

    def deposit(self):
        i = 1
        while i < 5:
            try:
                print(f"Account number: {self._account_no}\n\nCheck your details\n")
                print(f"\nVerify your account details\n\nName: {self._name}\nBank: {self._bank_name}\nIFSC code: {self._IFSC_code}\nBranch: {self._branch_name}\nAccount no.: {self._account_no}\nAccount: {self._account_name}\nEmail_Id: {self._email_Id}\nBank_balance: {self._bank_balance}\n")
                acc_no = int(input("Enter account number:- "))
                if acc_no == self._account_no:
                    money = int(input("Enter how much money you want to deposit:- "))
                    if money > 0:
                        self._bank_balance += money
                        print(f"\nSuccessfully deposited {money} rupees in your account\n")
                        break
                    else:
                        print(f"Please enter money greater than 0\n")
                        continue
                else:
                    print(f"Please enter valid account number\nYou have {5-i} chance remaining\n")
                    i += 1
                    continue
            except Exception as ez:
                print(type(ez))
                print(ez, "\n")

    def money_transfer(self):
        ra = random.randint(100000000000, 999999999999)
        i = 1
        while i < 5:
            try:
                print(f"\nRecipient account no.: {ra}\n")
                rec_acc_no = int(input("Enter recipient's account number:- "))
                if ra == rec_acc_no:
                    rec_name = str(input("Enter recipient's name:- "))
                    money = int(input("Enter how much money you want to transfer:- "))
                    print(f"\nCheck recipient's\nAccount number: {rec_acc_no}\nRecipient's name: {rec_name}\n"
                          f"Money to transfer: {money}\n")
                    df = int(input("Enter 1 to transfer after checking all the details:-"))
                    if df == 1:
                        if self._bank_balance > 0 and money <= self._bank_balance:
                            print(f"\nSuccessfully transferred {money} rupees to {rec_name}\n")
                            self._bank_balance -= money
                            break
                        else:
                            print(f"Please enter money greater than 0 or less than bank balance\n")
                            continue
                    else:
                        print(f"Please enter number greater than 0 or less than 2\n")
                        continue
                else:
                    print(f"Please enter correct account number\n"
                          f"You have {5-i} chance remaining\n")
                    i += 1
                    continue
            except Exception as ew:
                print(type(ew))
                print(ew, "\n")

    def account_balance(self):
        print(f"\nYou have {self._bank_balance} rupees in your account\n")

    @property
    def get_bank_name(self):
        return self._bank_name

    @get_bank_name.setter
    def set_bank_name(self, New_bank_name):
        self._bank_name = New_bank_name


my_bank = encapsulation_bank("Ranjit Vishwakarma", "TJSB", 12345678987, 'Louiswadi', 123456789876, "Savings", 'vishranjit43@gmail.com', 150000)

print(f"Current Bank: {my_bank.get_bank_name}")
my_bank.set_bank_name = "HDFC"
print()

while True:
    try:
        print(f"1 --> Withdraw\n2 --> Deposit\n3 --> Account Balance\n4 --> Money Transfer\n5 --> Exit")
        choice = int(input("Enter your choice:- "))
        if choice == 1:
            my_bank.withdraw()
            continue
        elif choice == 2:
            my_bank.deposit()
            continue
        elif choice == 3:
            my_bank.account_balance()
            continue
        elif choice == 4:
            my_bank.money_transfer()
            continue
        elif choice == 5:
            break
        else:
            print("\nPlease enter number between 1 to 5\n")
            continue
    except Exception as e:
        print(type(e))
        print(e, "\n")
