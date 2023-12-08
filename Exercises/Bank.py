import random

class Eng_bank:
    def __init__(self):
        self.amount = 500000

    def account(self):
        while True:
            try:
                print("Please select account")
                print("1 --> Current account\n2 --> Saving account\n")
                a = int(input("Enter your choice:-"))
                if a == 1:
                    return "Current"
                elif a == 2:
                    return "Saving"
                else:
                    print("Please enter number greater than 0 or less than 3\n")
            except Exception as ef:
                print(type(ef))
                print(ef)

    def with_depo(self):
        while True:
            try:
                global widp
                print("Please select what to do")
                print("1 --> Withdraw\n2 --> Deposit\n")
                widp = int(input("Enter your choice:-"))
                if widp == 1:
                    return 1
                elif widp == 2:
                    return 2
                else:
                    print("Please enter number greater than 0 or less than 3\n")
            except Exception as ep:
                print(type(ep))
                print(ep)

    def rem_sub(self, y):
        code = random.randrange(1000, 4000)
        i = 1
        while True:
            try:
                if widp == 1:
                    print(f"Pin {code}\n")
                    a = int(input("Enter pin "))
                    if a == code:
                        how = int(input("How much money you want to withdraw:-"))
                        if 0 < how <= self.amount:
                            self.amount -= how
                            print(f"You withdraw {how} rupees from your {y} account")
                            break
                        elif how < 0:
                            print("Please enter amount greater than 0\n")
                            continue
                        elif how > self.amount:
                            print(f"Please enter amount less than {self.amount} rupees\n")
                            continue
                    elif i == 5:
                        return True
                    else:
                        print(f"You have {5 - i} chance remaining")
                        i += 1
                        print("Oops wrong pin please try again\n")
                        continue
                else:
                    dipo = int(input("How much money you want to deposit:-"))
                    if dipo > 0:
                        self.amount += dipo
                        print(f"You deposited {dipo} rupees in your {y} account")
                        break
                    elif dipo < 0:
                        print("Please enter amount in positive\n")
                        continue
            except Exception as ex:
                print(type(ex))
                print(ex)

    def account_balance(self):
        print(f"Your account balance is {self.amount} rupees\n")


if __name__ == '__main__':
    a = Eng_bank()

    while True:
        try:
            print(f"1--> Select Account\n2--> Withdraw/Deposit\n3--> See account balance\n4--> Exit")
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                print()
                b = a.account()
                a.with_depo()
                a.rem_sub(b)
                print()
            elif choice == 2:
                print()
                a.with_depo()
                a.rem_sub(a.account())
                print()
            elif choice == 3:
                print()
                a.account_balance()
                print()
            elif choice == 4:
                break
            else:
                print("\nPlease enter Number between 1 to 4\n")
                continue
        except Exception as e:
            print('\n', type(e))
            print(e, '\n')


