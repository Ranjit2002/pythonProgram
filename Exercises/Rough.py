import random


# def armstrong(number):
#     num_str = str(number)
#     num_digits = len(num_str)
#     total = sum(int(digit) ** num_digits for digit in num_str)
#     return total == number
#
#
# a = int(input("Enter a Number:- "))
# if armstrong(a):
#     print(f"{a} is an Armstrong number")
# else:
#     print(f"{a} is not an Armstrong number")

# b = int(input("Enter end:- "))
# a = list(map(lambda x: 2 ** x, range(b+1)))
# for i in a:
#     print(i)

# for i in range(b+1):
#     print(f"The value of 2 raise to the power of {i} is {a[i]}")

# a = [i for i in range(1, 101)]
# b = int(input("Enter a Number to divide:- "))
# c = list(filter(lambda x: x % b == 0, a))
# for i in c:
#     print(i)

# a = int(input("Enter a Number:- "))
#
# print(f"The conversion of decimal number {a} is: ")
# print(bin(a), "in binary")
# print(oct(a), "in octal")
# print(hex(a), "in hexadecimal")

# a = '$'
# print(ord(a))

# print(random.randint(1, 10))    # This will print any number between 1 and 10

# def star_pattern(n):
#     if n > 0:
#         print('* ' * n)
#         star_pattern(n - 1)
#
# # Taking input from the user
# num_rows = int(input("Enter the number of rows for the star pattern: "))
#
# # Printing the star pattern
# star_pattern(num_rows)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
# def fibo_rec(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo_rec(n - 1) + fibo_rec(n - 2)
#
#
# a = int(input("Enter a Number: "))
# print("Please enter a positive number" if a <= 0 else "")
# b = fibo_rec(a)
# for i in range(a):
#     print(fibo_rec(i))

# def fibo(n):
#     x, y, z = 0, 1, 0
#     for i in range(n):
#         print(x)
#         x = x + y
#         y = z
#         z = x

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


a = int(input("Enter a Number:- "))
fibo(a)
