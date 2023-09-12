"""
def product(a, b, c):
    if a == b == c:
        print(a * 9)
    else:
        print(a + b + c)


a = str(input("Enter a String:- "))

if a.startswith("Is") or a.startswith("is"):
    print(a)
else:
    print("Is " + a)
import math


def repeat_string(s, n):
    if n < 0:
        return "Invalid input: n must be a non-negative integer."

    repeated_string = s * n
    return repeated_string


# Taking input from the user
input_string = input("Enter the string to repeat: ")
input_n = int(input("Enter the number of copies: "))

result = repeat_string(input_string, input_n)
print("Result:", result)


# Volume of a sphere


def sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


a = float(input("Enter the radius:-"))
b = sphere(a)
print(f"{b:.2f}")

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return 2 * (n - 17)


a = int(input("Enter a number:-"))
b = difference(a)

if b > 17:
    print(b)
else:
    print(f"The difference between {a} and 17 is: {b}")

my_dict = {
    "Mango": 6,
    "Apple": 5,
    "Banana": 2,
    "Grapes": 34,
    "Cherry": 4
}

for fruit, quantity in my_dict.items():
    if quantity > 2:
        print(f"We have {fruit} {quantity}")

for i in range(4):
    for j in range(i):
        print("*", end=" ")
    print()

n = int(input("Enter number of rows:-"))
for i in range(1, n+1):
    for b in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()

print("* * * *")
print("*     *")
print("*     *")
print("* * * *")
print("* *")
print("*   *")
print("*     *")

n = 7
o = 4

for i in range(n):
    for j in range(o):
        if i == 0 or i == 3 or j == 0:
            print("*", end=" ")
        elif i == 1 and j == 3 or i == 2 and j == 3:
            print("*", end=" ")
        elif i == 4 and j == 1 or i == 5 and j == 2 or i == 6 and j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("* * * * *")
print("*       *")
print("*       *")
print("* * * * *")
print("*   *")
print("*     *")
print("*       *")

def print_pattern():
    for i in range(7):
        for j in range(5):
            if i == 0 or i == 3:
                print("*", end=" ")
            elif j == 0 and (i != 0 and i != 3):
                print("*", end=" ")
            elif i == 1 and j == 4 or i == 2 and j == 4:
                print("*", end=" ")
            elif i == 4 and j == 2 or i == 5 and j == 3 or i == 6 and j == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


print_pattern()

def sum(a, b):
    plus = a + b
    if plus in range(15, 20):
        return 20
    else:
        return a + b


num1 = int(input("Enter first Number:- "))
num2 = int(input("Enter second Number:- "))
d = sum(num1, num2)
print(d)
"""


# def equal(a, b):
#     if a - b == 5 or a - b == -5:
#         return True
#     elif a != b and a + b != 5:
#         return False
#     return True
#
#
# n1 = int(input("Enter first Number:-"))
# n2 = int(input("Enter second Number:-"))
# c = equal(n1, n2)
# print(c)

# def add_num(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return 'Input must be integers!'
#     return a + b
#
#
# print(add_num(3, 6))
# print(add_num(3, 83))
# print(add_num('3', 4))
# print(add_num('3', '43'))

# def name_age_address(name, age, address):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Address: {address}")
#
#
# n = str(input("Enter your name:-"))
# ag = int(input("Enter your age:-"))
# add = str(input("Enter your address:-"))
# name_age_address(n, ag, add)

# a = 5  # Binary: 0101
# b = 3  # Binary: 0011
# result = a ^ b  # Binary result: 0110 (Decimal: 6)
# print(result)
#
# base = 2
# exponent = 3
# result = base ^ exponent  # Equivalent to 2^3, result is 8
# print(result)

# import struct
# print(struct.calcsize("P") * 8)

# import platform
# import os
# print("Name of the operating system:", os.name)
# print("\nName of the OS system:", platform.system())
# print("\nVersion of the operating system:", platform.release())

# n = "2365.875"
# print(float(n))
# a = float(n)
# print(a)

# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# for i in range(97, 123):
#     print(chr(i))

# import random
# def game():
#     computer = random.randint(97, 123)
#     char = chr(computer)
#     attempt = 1
#     i = 1
#     while i < 2:
#         user = str(input("Enter a Alphabet:-"))
#         lower = user.lower()
#         if lower == char:
#             print(f"You Guessed the correct Number it was {char}\nYou guessed it in {attempt} attempts")
#             i += 1
#         elif lower > char:
#             print("Too High...")
#             attempt += 1
#             print()
#         elif lower < char:
#             print("Too Low...")
#             attempt += 1
#             print()
#         i += 0
#
#
# game()

# def add(n):
#     a = []
#     for i in n:
#         a += i
#     return a
#
#
# num = int(input("Enter a Number:-"))
# b = add(num)
# print(b)


