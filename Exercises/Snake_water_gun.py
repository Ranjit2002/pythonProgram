import random
# class game:
#     def user_input(self):
#         while True:
#             try:
#                 user = str(input("Enter 'snake' 'water' or 'gun' :\n")).lower()
#                 if user in ["water", "snake", "gun"]:
#                     return user
#                 print("Please enter water, snake or gun only!\n")
#                 continue
#             except Exception as ei:
#                 print(ei)
#
#     def computer_input(self):
#         import random
#         computer = random.choice(["water", "snake", "gun"])
#         return computer
#
#     def new(self):
#         try:
#             while True:
#                 again = str(input("Enter yes or no:-")).lower()
#                 if again == "yes":
#                     return True
#                 elif again == "no":
#                     return False
#                 else:
#                     print("Please enter only 'water', 'snake' or 'gun' only!\n")
#                     continue
#         except Exception as er:
#             print(type(er))
#             print(er)
#
#     def who_won(self, user, computer):
#         try:
#             while True:
#                 if user == computer:
#                     print("Game Draw!\n")
#                     break
#                 elif user == "water" and computer == "snake":
#                     print(f"User choose: {user}\nComputer choose: {computer}Computer win!\n")
#                     break
#                 elif user == "water" and computer == "gun":
#                     print(f"User choose: {user}\nComputer choose: {computer}\nUser win!\n")
#                     break
#                 elif user == "snake" and computer == "water":
#                     print(f"User choose: {user}\nComputer choose: {computer}\nUser win!\n")
#                     break
#                 elif user == "snake" and computer == "gun":
#                     print(f"User choose: {user}\nComputer choose: {computer}\nComputer win!\n")
#                     break
#                 elif user == "gun" and computer == "water":
#                     print(f"User choose: {user}\nComputer choose: {computer}\nComputer win!\n")
#                     break
#                 elif user == "gun" and computer == "snake":
#                     print(f"User choose: {user}\nComputer choose: {computer}\nUser win!\n")
#                     break
#         except Exception as ex:
#             print(type(ex))
#             print(ex)
#
#
# print("Welcome to snake, water and gun game!")
# a = game()
# try:
#     while True:
#         user = a.user_input()
#         comp = a.computer_input()
#         a.who_won(user, comp)
#         print("Do you want to play?")
#         x = a.new()
#         if x:
#             continue
#         else:
#             break
# except Exception as ec:
#     print(type(ec))
#     print(ec)
#
def check():
    computer = random.randint(1, 3)
    print("Welcome to Snake, Water or Gun game")
    print("1 > Snake\n2 > Water\n3 > Gun")
    user = int(input("Enter your choice:- "))
    print(f"\nYour choice > {user}\nComputer's choice > {computer}")
    if computer == user:
        print(f"Game Draw!\n")
    elif computer == 1 and user == 2 or computer == 3 and user == 1 or computer == 2 and user == 3:
        print(f"Computer win\n")
    else:
        print("You win\n")


# Snake beats water     1 beats 2
# Gun beats Snake       3 beats 1
# Water beats Gun       2 beats 3

check()
