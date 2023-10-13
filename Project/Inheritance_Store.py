import random
class website:
    def __init__(self):
        self.web = ["Amazon", "Flipkart", "Myntra", "Shopsy"]

    def choose_website(self):
        while True:
            try:
                print(f"1 --> {self.web[0]}\n2 --> {self.web[1]}\n3 --> {self.web[2]}\n4 --> {self.web[3]}")
                global w
                w = int(input("Enter your choice:- "))
                if 0 < w < 5:
                    return self.web[w - 1]
                else:
                    print("Please enter number between 1 to 4\n")
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")


class items(website):
    def __init__(self):
        super().__init__()
        self.items = ["Shirt", "Mobile", "Laptop", "Shoes", "Fridge", "Smart TV"]

    def choose_items(self):
        while True:
            try:
                print(f"1 --> {self.items[0]}\n2 --> {self.items[1]}\n3 --> {self.items[2]}\n4 --> {self.items[3]}\n"
                      f"5 --> {self.items[4]}\n6 --> {self.items[5]}")
                global tem
                tem = int(input("Enter your choice:- "))
                if 0 < tem < 7:
                    return self.items[tem - 1]
                else:
                    print("Please enter number between 1 to 6\n")
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")


class price_discount(items):
    def __init__(self):
        super().__init__()
        self.dnt = random.randrange(10, 25)

    def price_before_discount(self):
        if tem == 1:
            shirt = random.choice([500, 600, 650, 700, 750, 1000])
            print(f"On {self.web[w-1]}\nPrice of {self.items[tem-1]}: {shirt}\n"
                  f"Discount on {self.items[tem-1]}: {self.dnt}%")
            return shirt, self.dnt
        elif tem == 2:
            mobile = random.choice([14000, 15000, 16000, 17000, 17500, 20000])
            print(f"On {self.web[w-1]}\nPrice of {self.items[tem-1]}: {mobile}\n"
                  f"Discount on {self.items[tem-1]}: {self.dnt}%")
            return mobile, self.dnt
        elif tem == 3:
            laptop = random.choice([35000, 37000, 40000, 41000, 43000, 45000])
            print(f"On {self.web[w-1]}\nPrice of {self.items[tem-1]}: {laptop}\n"
                  f"Discount on {self.items[tem-1]}: {self.dnt}%")
            return laptop, self.dnt
        elif tem == 4:
            shoes = random.choice([1200, 1300, 1400, 1500, 1600, 1700])
            print(f"On {self.web[w-1]}\nPrice of {self.items[tem-1]}: {shoes}\n"
                  f"Discount on {self.items[tem-1]}: {self.dnt}%")
            return shoes, self.dnt
        elif tem == 5:
            fridge = random.choice([30000, 32000, 35000, 36000, 40000, 37000])
            print(f"On {self.web[w-1]}\nPrice of {self.items[tem-1]}: {fridge}\n"
                  f"Discount on {self.items[tem-1]}: {self.dnt}%")
            return fridge, self.dnt
        else:
            smart_tv = random.choice([50000, 53000, 55000, 57000, 60000, 63000])
            print(f"On {self.web[w-1]}\nPrice of {self.items[tem-1]}: {smart_tv}\n"
                  f"Discount on {self.items[tem-1]}: {self.dnt}%")
            return smart_tv, self.dnt

    def price_after_discount(self, Item_price, discount):
        global final_price
        x = (Item_price / 100) * discount
        final_price = Item_price - x
        print(f"\nAfter discount\nPrice of {self.items[tem-1]}: {final_price}\n")


class payment(price_discount):
    def __init__(self):
        super().__init__()
        self.Bank_amount = 150000
        self.product = list()
        self.product_price = list()

    def purchase_or_not(self):
        while True:
            try:
                print("1 --> Purchase\n2 --> Exit")
                akm = int(input("Enter your choice:- "))
                if akm == 1:
                    return 1
                elif akm == 2:
                    return 2
                else:
                    print("Please enter 1 or 2")
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def bank_balance(self):
        return self.Bank_amount


class payment_options(payment):
    def pay_options(self):
        while True:
            try:
                print("1 --> Debit card\n2 --> UPI apps\n3 --> Cash on delivery")
                global opt
                opt = int(input("Enter your choice:- "))
                if 0 < opt < 4:
                    return opt
                else:
                    print("Please enter number between 1 to 3\n")
                    continue
            except Exception as e:
                print(type(e))
                print(e, "\n")

    def select_option(self):
        pin = random.randrange(1000, 9999)
        i = 1
        while i <= 5:
            if opt == 1:
                print(f"Pin: {pin}")
                x = int(input("Enter card pin: "))
                if x == pin:
                    print(f"\nYou purchased {self.items[tem - 1]} in {final_price} rupees")
                    self.Bank_amount -= final_price
                    break
                else:
                    print(f"Oops! wrong pin please try again\nYou have {5 - i} chance remaining\n")
                    i += 1
                    continue
            elif opt == 2:
                print(f"Pin: {pin}")
                y = int(input("Enter UPI pin: "))
                if y == pin:
                    print(f"\nYou purchased {self.items[tem - 1]} in {final_price} rupees")
                    self.Bank_amount -= final_price
                    break
                else:
                    print(f"Oops! wrong pin please try again\nYou have {5 - i} chance remaining\n")
                    i += 1
                    continue
            else:
                print("Enter 1 to confirm order")
                z = int(input("Enter your choice:- "))
                if z == 1:
                    print(f"\nYour order has been confirmed\n"
                          f"It will be delivered in 4 to 5 days\n")
                    break


a = payment_options()
i = 1
while i < 2:
    a.choose_website()
    print()
    a.choose_items()
    print()
    f, g = a.price_before_discount()
    a.price_after_discount(f, g)
    ca = a.purchase_or_not()
    if ca == 2:
        break
    print()
    a.pay_options()
    print()
    a.select_option()
    i += 1
while True:
    try:
        print("\n1 --> Purchase anything else\n2 --> Compare with other websites\n3 --> See bank balance\n4 --> Exit")
        en = int(input("Enter your choice:- "))
        if en == 1:
            print()
            a.choose_website()
            print()
            a.choose_items()
            print()
            f, g = a.price_before_discount()
            a.price_after_discount(f, g)
            ca = a.purchase_or_not()
            if ca == 2:
                continue
            print()
            a.pay_options()
            print()
            a.select_option()
            print()
        elif en == 2:
            print()
            a.choose_website()
            print()
            f, g = a.price_before_discount()
            a.price_after_discount(f, g)
            ca = a.purchase_or_not()
            if ca == 2:
                continue
            print()
            a.pay_options()
            print()
            a.select_option()
            print()
        elif en == 3:
            print(f"\nYour bank balance is {a.bank_balance()} rupees")
        elif en == 4:
            break
        else:
            print("Please enter number between 1 to 4")
            continue
    except Exception as exc:
        print(type(exc))
        print(exc)
