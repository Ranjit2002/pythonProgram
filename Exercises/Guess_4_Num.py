class Gaming:
    @staticmethod
    def player_guess():
        import random
        computer = random.randint(10000, 99999)
        str_com = str(computer)
        comp_list = [int(i) for i in str_com]
        return comp_list

    @staticmethod
    def user_input(list1):
        if len(list1) == 0:
            return None
        print("You have 20 chance to guess 5 numbers\nLet's start")
        j = 1
        while j < 21:
            print(f"{j} Chance")
            a = int(input(f"Guess number:-"))
            if a > 9:
                print("Please enter number between 0 to 9\n")
                continue
            elif a >= 0 or a <= 9:
                j += 1
                for i in list1:
                    if a in list1:
                        list1.remove(a)
                        print("You guessed the Right number\n")
                        break
                    else:
                        print("You guessed the Wrong number\n")
                        break
            if len(list1) == 0:
                return True


g = Gaming()
b = g.player_guess()
if g.user_input(b):
    print("You guessed all numbers")
else:
    print("You don't guessed all numbers")


# a = 3453
# b = str(a)
# c = [int(i) for i in b]     # c and the below for loop is same

# for i in c:
#     b.append(i)

# print(c)
