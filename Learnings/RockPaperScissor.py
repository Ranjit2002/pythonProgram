import random

print("1->Rock")
print("2->Paper")
print("3->Scissor")
print("<4->Exit")

a = 1
while a < 2:
    computer = random.randint(1, 3)
    user = int(input("Enter your choice:-"))
    if user == 1:
        if computer == 1:
            print("Game Draw!\n")
        elif computer == 2:
            print("Computer won!\n")
        else:
            print("User won!\n")
    elif user == 2:
        if computer == 1:
            print("User won!\n")
        elif computer == 2:
            print("Game Draw!\n")
        else:
            print("Computer won!\n")
    elif user == 3:
        if computer == 1:
            print("Computer won!\n")
        elif computer == 2:
            print("User won!")
        else:
            print("Game Draw!\n")
    else:
        a += 1
a += 0
