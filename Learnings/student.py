# class student:
#     address = "Mumbai"
#     branch = "Education plus"
#
#     def python(self):
#         print(self.branch)


# a = student()
# a.python()
# student.python(student)     # I can do like this also


class student:
    address = "Mumbai"
    branch = "Education plus"

    def python(self):
        try:
            name = str(input("Enter your name:-"))
            roll_no = int(input("Enter roll no:-"))
            p_fees = 30000
            print(f"\nName: {name}\nRoll no: {roll_no}\nPython course fees: {p_fees}\n"
                  f"Address: {self.address}\nBranch: {self.branch}\n")
        except Exception as e:
            print(type(e))
            print(e)

    def java(self):
        try:
            name = str(input("Enter your name:-"))
            roll_no = int(input("Enter roll no:-"))
            p_fees = 40000
            print(f"\nName: {name}\nRoll no: {roll_no}\nJava course fees: {p_fees}\n"
                  f"Address: {self.address}\nBranch: {self.branch}\n")
        except Exception as e:
            print(type(e))
            print(e)

    def JS(self):
        try:
            name = str(input("Enter your name:-"))
            roll_no = int(input("Enter roll no:-"))
            p_fees = 50000
            print(f"\nName: {name}\nRoll no: {roll_no}\nJavaScript course fees: {p_fees}\n"
                  f"Address: {self.address}\nBranch: {self.branch}\n")
        except Exception as e:
            print(type(e))
            print(e)


# a = student()
# a.python()
# a.java()
# a.JS()

import random


def get_user_choice():
    user_choice = input("Enter 'snake', 'water', or 'gun': ").lower()
    while user_choice not in ['snake', 'water', 'gun']:
        print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")
        user_choice = input("Enter 'snake', 'water', or 'gun': ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'snake' and computer_choice == 'water') or \
            (user_choice == 'water' and computer_choice == 'gun') or \
            (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"


def snake_water_gun_game():
    print("Welcome to Snake, Water, and Gun Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


# Run the game
snake_water_gun_game()

