import random
class Eng_bank:
    def __init__(self):
        self.amount = 500000
        self.code = random.randrange(1000, 4000)

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
        i = 1
        while True:
            try:
                if widp == 1:
                    print(f"Pin {self.code}\n")
                    a = int(input("Enter pin "))
                    if a == self.code:
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
                        print(f"You have {5-i} chance remaining")
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

    def next(self):
        while True:
            try:
                print("What you want to do next")
                print("1 --> See account balance\n2 --> Exit\n")
                a = int(input("Enter your choice:-"))
                if a == 1:
                    print(f"{self.amount}\n")
                elif a < 0:
                    print("Please enter number greater than 0 or less than 3\n")
                    continue
                else:
                    break
            except Exception as er:
                print(type(er))
                print(er)


class Hin_bank:
    def __init__(self):
        self.paise = 500000
        self.code = random.randrange(1000, 4000)

    def account(self):
        while True:
            try:
                print("Account chune")
                print("1 --> Current account\n2 --> Saving account\n")
                a = int(input("choice enter kare:-"))
                if a == 1:
                    return "Current"
                elif a == 2:
                    return "Saving"
                else:
                    print("0 se zada aur 3 se kam no enter kare\n")
            except Exception as e:
                print(type(e))
                print(e)

    def with_depo(self):
        while True:
            try:
                global widp
                print("koi option chune")
                print("1 --> Withdraw\n2 --> Deposit\n")
                widp = int(input("choice enter kare:-"))
                if widp == 1:
                    return 1
                elif widp == 2:
                    return 2
                else:
                    print("0 se zada aur 3 se kam no enter kare\n")
            except Exception as ep:
                print(type(ep))
                print(ep)

    def rem_sub(self, y):
        i = 1
        while True:
            try:
                if widp == 1:
                    print(f"Pin {self.code}\n")
                    a = int(input("Pin enter kare "))
                    if a == self.code:
                        how = int(input("kitna paisa nikalna hai enter kare:-"))
                        if 0 < how <= self.paise:
                            self.paise -= how
                            print(f"Aapne {how} rupay apne {y} account se nikale")
                            break
                        elif how < 0:
                            print("0 se bada number enter kare\n")
                            continue
                        elif how > self.paise:
                            print(f"{self.paise} se kam paise enter kare\n")
                            continue
                        else:
                            print("Phir prayas kare\n")
                            continue
                    elif i == 5:
                        return True
                    else:
                        i += 1
                        print("Phir kosis kare\n")
                        continue
                else:
                    dipo = int(input("Kitna paisa zama karna chahata hai enter kare:-"))
                    if dipo > 0:
                        self.paise += dipo
                        print(f"You deposited {dipo} rupees in your {y} account")
                        break
                    elif dipo < 0:
                        print("0 se bada number enter kare\n")
                        continue
            except Exception as ex:
                print(type(ex))
                print(ex)

    def next(self):
        while True:
            try:
                print("Aap ab kya karna chahate hai")
                print("1 --> See account balance\n2 --> Exit\n")
                a = int(input("Apni choice enter kare:-"))
                if a == 1:
                    print(f"{self.paise}\n")
                elif a < 0:
                    print("0 se bada aur 3 se kam number enter kare\n")
                    continue
                else:
                    break
            except Exception as er:
                print(type(er))
                print(er)

class Mar_bank:
    def __init__(self):
        self.amount = 500000
        self.code = random.randrange(1000, 4000)

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
            except Exception as e:
                print(type(e))
                print(e)

    def with_depo(self):
        while True:
            try:
                global widp
                print("Please select to do")
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
        i = 1
        while True:
            try:
                if widp == 1:
                    print(f"Pin {self.code}\n")
                    a = int(input("Enter pin "))
                    if a == self.code:
                        how = int(input("How much money you want to withdraw:-"))
                        if 0 < how <= self.amount:
                            self.amount -= how
                            print(f"You withdraw {how} rupees from your {y} account")
                            break
                        elif how < 0:
                            print("Please enter amount in positive\n")
                            continue
                        elif how > self.amount:
                            print(f"Please enter amount less than {self.amount} rupees\n")
                            continue
                        else:
                            print("Please try again\n")
                            continue
                    elif i == 5:
                        return True
                    else:
                        i += 1
                        print("Oops please try again\n")
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

    def next(self):
        while True:
            try:
                print("What you want to do next")
                print("1 --> See account balance\n2 --> Exit\n")
                a = int(input("Enter your choice:-"))
                if a == 1:
                    print(f"{self.amount}\n")
                elif a < 0:
                    print("Please enter number greater than 0 or less than 3\n")
                    continue
                else:
                    break
            except Exception as er:
                print(type(er))
                print(er)


while True:
    print("Select language:-\n1 --> English\n2 --> Hindi\n3 --> Marathi\n4 --> Exit")
    a = int(input("Enter your choice:-"))
    if a < 0 or a >= 4:
        print("Please enter number greater than 0 and less than 5")
        continue
    elif a == 1:
        print()
        b = Eng_bank()
        d = b.account()
        print()
        e = b.with_depo()
        print()
        c = b.rem_sub(d)
        if c:
            print("You don't have any chance remaining")
            break
        else:
            print()
            b.next()
            break
    elif a == 2:
        print()
        b = Eng_bank()
        d = b.account()
        print()
        e = b.with_depo()
        print()
        c = b.rem_sub(d)
        if c:
            print("You don't have any chance remaining")
            break
        else:
            print()
            b.next()
            break
    elif a == 3:
        print()
        b = Eng_bank()
        d = b.account()
        print()
        e = b.with_depo()
        print()
        c = b.rem_sub(d)
        if c:
            print("You don't have any chance remaining")
            break
        else:
            print()
            b.next()
            break
    elif a == 4:
        break
