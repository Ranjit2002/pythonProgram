def hand_game():
    import random
    print("Select options:-")
    print("1 --> Rock\n2 --> Paper\n3 --> Scissor\n4 --> Exit")
    r = "Rock"
    p = "Paper"
    s = "Scissor"
    while True:
        computer_input = random.randint(1, 3)
        user_input = int(input("\nEnter a number:- "))
        if user_input == 4:
            print("You Exit the game")
            break
        elif user_input > 4:
            print("Enter number between 1 to 3")
            continue
        if computer_input == user_input:
            print("Game Draw!")
            if computer_input == 1 and user_input == 1:
                print(f"Computer choose {r}\nUser choose {r}")
            elif computer_input == 2 and user_input == 2:
                print(f"Computer choose {p}\nUser choose {p}")
            elif computer_input == 3 and user_input == 3:
                print(f"Computer choose {s}\nUser choose {s}")
        elif computer_input < user_input:
            if computer_input == 1 and user_input == 2:
                print("User Wins!")
                print(f"Computer choose {r}\nUser Choose {p}")
            elif computer_input == 1 and user_input == 3:
                print("Computer Wins!")
                print(f"Computer choose {r}\nUser choose {s}")
            elif computer_input == 2 and user_input == 3:
                print("User Wins!")
                print(f"Computer choose {p}\nUser choose {s}")
        elif computer_input > user_input:
            if computer_input == 2 and user_input == 1:
                print("Computer Wins!")
                print(f"Computer choose {p}\nUser choose {r}")
            elif computer_input == 3 and user_input == 2:
                print("Computer Wins!")
                print(f"Computer choose {s}\nUser choose {p}")
            elif computer_input == 3 and user_input == 1:
                print("User Wins!")
                print(f"Computer choose {s}\nUser choose {r}")


hand_game()

