import random

class Number:
    def guess_number(self):
        i = 0
        computer = random.randrange(1, 100)
        while True:
            try:
                i += 1
                user = int(input("Guess Number:- "))
                if 0 < user > 100:
                    print("Please enter number between 1 to 100\n")
                    continue
                elif user == computer:
                    print(f"Congratulations! You guessed the correct number\n"
                          f"You guessed it in {i} attempts")
                    break
                elif user > computer:
                    print("Too High...\n")
                    continue
                elif user < computer:
                    print("Too Low...\n")
                    continue
            except Exception as ex:
                print(type(ex))
                print(ex, "\n")


a = Number()
a.guess_number()
