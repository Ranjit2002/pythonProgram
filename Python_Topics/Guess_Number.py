import random

computer = random.randint(1, 100)
attempts = 1

while True:
    user = int(input("Guess a Number:-"))
    if user == computer:
        print(f"You Guessed the correct number it was {computer}\nYou Guessed it in {attempts} attempts\n"
              f"Your score is {100 - attempts}")
        break
    elif user > computer:
        a = user - computer
        if a < 20:
            print("Too High...")
        else:
            print("Too too High...")
        attempts += 1
    elif computer > user:
        b = computer - user
        if b < 20:
            print("Too Low...")
        else:
            print("Too too Low...")
        attempts += 1
    print()