import random
class store:
    def __init__(self):
        self.Bank_amount = 150000
        self.l1 = ["Shirt", "Mobile", "Laptop", "Shoes", "Refrigerator", "Smart TV"]
        self.w = ["Amazon", "Flipkart", "Myntra", "Shopsy"]
        self.pay = ["Debit card", "UPI apps", "Cash on delivery"]
        self.shirt = None
        self.mobile = None
        self.laptop = None
        self.shoes = None
        self.appliance = None
        self.smartTV = None
        self.comp = random.randrange(10, 30)
        self.shr_pr = [500, 600, 650, 700, 750, 1000]
        self.mo_pr = [14000, 16000, 17500, 20000]
        self.lap_pr = [35000, 40000, 37000, 43000]
        self.sho_pr = [1200, 1400, 1350, 1600, 1650]
        self.ap_pr = [30000, 32000, 35000, 37000]
        self.smt_pr = [50000, 53000, 55000, 60000, 63000]

    def choose_website(self):
        while True:
            try:
                print("Choose any website")
                print(f"1 --> {self.w[0]}\n2 --> {self.w[1]}\n3 --> {self.w[2]}\n4 --> {self.w[3]}")
                global web
                web = int(input("Enter your choice:- "))
                if 0 < web < 5:
                    return web
                else:
                    print("Please enter number between 1 to 4\n")
                    continue
            except Exception as ex:
                print(type(ex))
                print(ex, "\n")

    def select_item(self):
        while True:
            try:
                print("Choose category what you want to purchase")
                print(f"1 --> {self.l1[0]}\n2 --> {self.l1[1]}\n3 --> {self.l1[2]}\n4 --> {self.l1[3]}\n"
                      f"5 --> {self.l1[4]}\n6 --> {self.l1[5]}")
                global pro
                pro = int(input("Enter your choice:- "))
                if 0 < pro < 7:
                    return pro
                else:
                    print("Please enter number between 1 to 6\n")
                    continue
            except Exception as ep:
                print(type(ep))
                print(ep, "\n")

    def discount(self):
        if pro == 1:
            self.shirt = random.choice(self.shr_pr)
            print(f"On {self.w[web-1]}\nPrice of {self.l1[pro-1]}: {self.shirt}\n"
                  f"Discount on {self.l1[pro-1]}: {self.comp}%")
            return self.shirt, self.comp
        elif pro == 2:
            self.mobile = random.choice(self.mo_pr)
            print(f"On {self.w[web - 1]}\nPrice of {self.l1[pro - 1]}: {self.mobile}\n"
                  f"Discount on {self.l1[pro - 1]}: {self.comp}%")
            return self.mobile, self.comp
        elif pro == 3:
            self.laptop = random.choice(self.lap_pr)
            print(f"On {self.w[web - 1]}\nPrice of {self.l1[pro - 1]}: {self.laptop}\n"
                  f"Discount on {self.l1[pro - 1]}: {self.comp}%")
            return self.laptop, self.comp
        elif pro == 4:
            self.shoes = random.choice(self.sho_pr)
            print(f"On {self.w[web - 1]}\nPrice of {self.l1[pro - 1]}: {self.shoes}\n"
                  f"Discount on {self.l1[pro - 1]}: {self.comp}%")
            return self.shoes, self.comp
        elif pro == 5:
            self.appliance = random.choice(self.ap_pr)
            print(f"On {self.w[web - 1]}\nPrice of {self.l1[pro - 1]}: {self.appliance}\n"
                  f"Discount on {self.l1[pro - 1]}: {self.comp}%")
            return self.appliance, self.comp
        elif pro == 6:
            self.smartTV = random.choice(self.smt_pr)
            print(f"On {self.w[web - 1]}\nPrice of {self.l1[pro - 1]}: {self.smartTV}\n"
                  f"Discount on {self.l1[pro - 1]}: {self.comp}%")
            return self.smartTV, self.comp

    def price(self, Item_price, discount_percent):
        a = (Item_price / 100) * discount_percent
        b = Item_price - a
        return b

    def UPI(self):
        return self.Bank_amount

    def compare(self, daam):
        print(f"After discount\nPrice of {self.l1[pro-1]}: {daam} rupees\n")
        while True:
            try:
                print("1 --> Purchase\n2 --> Exit\n")
                kd = int(input("Enter your choice:- "))
                if 0 < kd < 3:
                    return kd
                else:
                    print("Please enter 1 or 2\n")
                    continue
            except Exception as ex:
                print(type(ex))
                print(ex, "\n")

    def select_payment_option(self):
        while True:
            try:
                print(f"\nSelect payment option\n1 --> {self.pay[0]}\n2 --> {self.pay[1]}\n3 --> {self.pay[2]}")
                pay = int(input("Enter your choice:- "))
                if pay == 1:
                    return 1
                elif pay == 2:
                    return 2
                elif pay == 3:
                    return 3
            except Exception as ec:
                print(type(ec))
                print(ec)

    def payment(self, payment_option, daam):
        i = 1
        while i <= 5:
            pin = random.randrange(1000, 9999)
            try:
                if payment_option == 1:
                    print(f"Pin = {pin}\n")
                    x = int(input("Enter card pin : "))
                    if x == pin:
                        if self.Bank_amount < daam:
                            print(f"\nYou don't have enough money to purchase this {self.l1[pro-1]}\n")
                            break
                        else:
                            self.Bank_amount -= daam
                            print(f"\nYou purchased {self.l1[pro-1]} in {daam} rupees")
                            break
                    else:
                        print(f"Oops! wrong pin please try again\nYou have {5-i} chance remaining\n")
                        i += 1
                        continue
                elif payment_option == 2:
                    print(f"Pin = {pin}\n")
                    y = int(input("Enter UPI pin : "))
                    if y == pin:
                        if self.Bank_amount < daam:
                            print(f"\nYou don't have enough money to purchase this {self.l1[pro-1]}\n")
                            break
                        else:
                            self.Bank_amount -= daam
                            print(f"\nYou purchased {self.l1[pro-1]} in {daam} rupees")
                            break
                    else:
                        print(f"Oops! wrong pin please try again\nYou have {5-i} chance remaining\n")
                        i += 1
                        continue
                elif payment_option == 3:
                    print("Enter 1 to place order\n")
                    z = int(input("Enter your choice:- "))
                    if z == 1:
                        print(f"\nYour order for {self.l1[pro-1]} has been placed\n"
                              f"It will be delivered after 4 to 5 days\n")
                        break
            except Exception as er:
                print(type(er))
                print(er)


a = store()
i = 1
while i < 2:
    a.choose_website()
    print()
    a.select_item()
    print()
    d, e = a.discount()
    print()
    f = a.price(d, e)
    a1 = a.compare(f)
    if a1 == 2:
        break
    g = a.select_payment_option()
    print()
    b = a.UPI()
    a.payment(g, f)
    i += 1
print()
while True:
    try:
        print("1 --> Purchase anything else\n2 --> Compare with other websites\n3 --> See bank balance\n4 --> Exit")
        choice = int(input("Enter your choice:- "))
        if choice == 1:
            print()
            a.choose_website()
            print()
            a.select_item()
            print()
            d, e = a.discount()
            print()
            f = a.price(d, e)
            a1 = a.compare(f)
            if a1 == 2:
                continue
            g = a.select_payment_option()
            print()
            b = a.UPI()
            a.payment(g, f)
            print()
        elif choice == 2:
            print()
            a.choose_website()
            print()
            d, e = a.discount()
            print()
            f = a.price(d, e)
            a1 = a.compare(f)
            if a1 == 2:
                continue
            g = a.select_payment_option()
            print()
            b = a.UPI()
            a.payment(g, f)
            print()
        elif choice == 3:
            print(f"\nYour bank balance is {a.UPI()}\n")
        elif choice == 4:
            break
        else:
            print("Please enter number between 1 to 4")
            continue
    except Exception as exc:
        print(type(exc))
        print(exc, "\n")
