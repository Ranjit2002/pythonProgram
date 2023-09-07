import random

computer = random.randint(1, 100)

attempt = 1
a = 1
while a < 2:
    user = int(input("Enter a Number between 1 to 100:-  "))
    if computer == user:
        print("\nYou Guess the correct Number it was ", computer, "\nYou guessed it in ", attempt, " attempts")
        a += 1
    elif user < computer:
        print("Too Low...\n")
    elif user > computer:
        print("Too High...\n")
    a += 0
    attempt += 1
'''

print("1--> Degree Celsius to Fahrenheit")
print("2--> Fahrenheit to Degree Celsius")
choice = int(input("Enter your choice:-"))

if choice==1:
    deg = int(input("Enter Degree Celsius:-"))
    fah = (deg * 9 / 5) + 32
    print(deg," Degree Celsius is ",fah," Fahrenheit")
elif choice==2:
    fah = int(input("Enter Fahrenheit:-"))
    deg = (fah - 32) * 5/9
    print(fah," Fahrenheit is ",deg," Degree Celsius")
'''

