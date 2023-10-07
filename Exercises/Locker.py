class money:
    def __init__(self):
        self.amount = 200000

    def debit(self):
        try:
            a = int(input("\nEnter how much hundred you want to remove:-\n"))
            if a < 0 or a > 2000:
                print("\nPlease enter no greater than 0 and less than 2000\n")
            elif 0 < a < 2000:
                b = a * 100
                self.amount -= b
                return b
        except Exception as e:
            print(type(e))
            print(e)

    def credit(self):
        return self.amount


a = money()
while True:
    print("1 --> Withdraw\n2 --> Remaining amount\n3 --> Exit\n")
    choice = int(input("Enter your choice:-\n"))
    if choice == 1:
        b = a.debit()
        print(f"Your account has debited {b} rupees\n")
    elif choice == 2:
        d = a.credit()
        print(f"You have {d} rupees remaining\n")
    elif choice == 3:
        break
    else:
        print("Please enter number between 1 to 3\n")
        continue
