class website_money:
    def website(self):
        money = int(input("Enter how much money do you have? "))
        print("Which website should you choose?")
        print(f"1 --> Amazon\n2 --> Flipkart\n3 --> Meesho\n4 --> Shopsy")
        while True:
            site = int(input("Enter your choice: "))
            if site == 1:
                return "Amazon", money
            elif site == 2:
                return "Flipkart", money
            elif site == 3:
                return "Meesho", money
            elif site == 4:
                return "Shopsy", money
            elif site > 4:
                print("please Enter proper number")
                continue

    def select_item(self):
        print("What you want to purchase?")
        print("1 -->Mobile\n2 -->Smart TV\n3 -->Laptop\n4 -->Clothes")
        while True:
            select = int(input("Enter your choice:-"))
            if select > 4:
                print("Please select proper number")
                continue
            match select:
                case 1:
                    return "Mobile"
                case 2:
                    return "Smart TV"
                case 3:
                    return "Laptop"
                case 4:
                    return "Clothes"
            break

    def brand(self, product):
        if product == "Mobile":
            while True:
                print("\nSelect mobile brand")
                print("1 -->Samsung\n2 -->Apple\n3 -->Redmi\n4 -->Oneplus")
                selected_mobile = int(input("Enter your choice:-"))
                if selected_mobile > 4:
                    print("Please select proper number")
                    continue
                elif selected_mobile == 1:
                    return "Samsung"
                elif selected_mobile == 2:
                    return "Apple"
                elif selected_mobile == 3:
                    return "Redmi"
                else:
                    return "Oneplus"
        elif product == "Smart TV":
            while True:
                print("Select smart TV brand")
                print("1 -->Sony\n2 -->Panasonic\n3 -->Sansui\n4 -->Samsung")
                tv_brand = int(input("Enter your choice:-"))
                if tv_brand > 4:
                    print("Please select proper number")
                    continue
                elif tv_brand == 1:
                    return "Sony"
                elif tv_brand == 2:
                    return "Panasonic"
                elif tv_brand == 3:
                    return "Sansui"
                else:
                    return "Samsung"
        elif product == "Laptop":
            while True:
                print("Select laptop brand")
                print("1 -->Dell\n2 -->Lenovo\n3 -->Samsung\n4 -->Asus")
                laptop_brand = int(input("Enter your choice:-"))
                if laptop_brand > 4:
                    print("Please select proper number")
                    continue
                elif laptop_brand == 1:
                    return "Dell"
                elif laptop_brand == 2:
                    return "Lenovo"
                elif laptop_brand == 3:
                    return "Samsung"
                else:
                    return "Asus"
        else:
            while True:
                print("Select clothes brand")
                print("1 -->Peter England\n2 -->Raymond\n3 -->Allen Solly\n4 -->Gucci")
                clothes_brand = int(input("Enter your choice:-"))
                if clothes_brand > 4:
                    print("Please select proper number")
                    continue
                elif clothes_brand == 1:
                    return "Peter England"
                elif clothes_brand == 2:
                    return "Raymond"
                elif clothes_brand == 3:
                    return "Allen Solly"
                else:
                    return "Gucci"

    def brand_price(self, product, item):
        while True:
            if product == "Mobile":
                if item == "Samsung":
                    return 80000
                elif item == "Apple":
                    return 150000
                elif item == "Redmi":
                    return 30000
                else:
                    return 60000
            elif product == "Smart TV":
                if item == "Sony":
                    return 60000
                elif item == "Panasonic":
                    return 50000
                elif item == "Sansui":
                    return 30000
                else:
                    return 55000
            elif product == "Laptop":
                if item == "Dell":
                    return 40000
                elif item == "Lenovo":
                    return 50000
                elif item == "Samsung":
                    return 70000
                else:
                    return 80000
            else:
                if item == "Peter England":
                    return 3500
                elif item == "Raymond":
                    return 2000
                elif item == "Allen Solly":
                    return 3000
                else:
                    return 2000

    def money_Management(self, money, product_price):
        if money < product_price:
            return (f"Price: {product_price} rupees\nYou have only {money} rupees\n"
                    f"You don't have enough money to purchase this product")
        elif money == product_price:
            return (f"Price: {product_price} rupees\nYou have only {money} rupees\n"
                    f"Now you have 0 rupees\nThanks for coming")
        elif money > product_price:
            rem = money - product_price
            return (f"Price: {product_price} rupees\nYou have {money} rupees\n"
                    f"Now your remaining money is {rem} rupees\nThanks for coming")

# Java's library project
w = website_money()
site, money = w.website()
print(f"Money: {money}\nSite: {site}")
print()
pur = w.select_item()
print(pur)
print()
br = w.brand(pur)
v = w.brand_price(pur, br)
print(f"\nItem: {br}")
c = w.money_Management(money, v)
print(c)
