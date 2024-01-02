import random


class Dome:
    def guess(self):
        print("Welcome\nLet's play Stone Paper Scissor\n1 --> Stone\n2 --> Paper\n3 --> Scissor\n4 --> Exit")
        while True:
            try:
                user = int(input("Enter a Number:- "))
                computer = random.randrange(1, 4)    # This will guess number between 1 to 3
                s = "Stone"
                p = "Paper"
                sc = "Scissor"
                if user < 0 or user > 4:
                    print("\nPlease enter number between 1 to 4\n")
                    continue
                elif user == 4:
                    break
                elif computer == 1:
                    if computer == 1 and user == 1:
                        print(f"\nComputer Choose > {s}\nYou Choose > {s}\nGame Draw!\n")
                    elif computer == 1 and user == 2:
                        print(f"\nComputer Choose > {s}\nYou Choose > {p}\nYou win!\n")
                    elif computer == 1 and user == 3:
                        print(f"\nComputer Choose > {s}\nYou Choose > {sc}\nComputer win!\n")
                elif computer == 2:
                    if computer == 2 and user == 1:
                        print(f"\nComputer Choose > {p}\nYou Choose > {s}\nComputer win!\n")
                    elif computer == 2 and user == 2:
                        print(f"\nComputer Choose > {p}\nYou Choose > {p}\nGame Draw!\n")
                    elif computer == 2 and user == 3:
                        print(f"\nComputer Choose > {p}\nYou Choose > {sc}\nYou win!\n")
                elif computer == 3:
                    if computer == 3 and user == 1:
                        print(f"\nComputer Choose > {sc}\nYou Choose > {s}\nYou win!\n")
                    elif computer == 3 and user == 2:
                        print(f"\nComputer Choose > {sc}\nYou Choose > {p}\nComputer win!\n")
                    elif computer == 3 and user == 3:
                        print(f"\nComputer Choose > {sc}\nYou Choose > {sc}\nGame Draw!\n")
            except Exception as e:
                print(type(e))
                print(e)


# 1 > Stone
# 2 > Paper
# 3 > Scissor

# Stone > Scissor   1 > 3
# Paper > Stone     2 > 1
# Scissor > Paper   3 > 2


b = Dome()
b.guess()
