# first = "My name is {} and I am from {}"
# name = "Ranjit"
# country = "America"
# a = first.format(name, country)
# print(a)
#
# first = f"My name is {name} and I am from {country}"
# print(first)


# a = "234"
#
# b = int(a)
# c = 6
# print(b, type(b))
# print(b + c)


# def fibonacci_series(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# x = int(input("Enter a Number to print fibonacci series up to:- "))
# fibonacci_series(x)

# def fibonacci_generator(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# # Change the value of 'n' to the number of Fibonacci numbers you want to generate
# n = 20
# fib_gen = fibonacci_generator(n)
#
# print(f"Fibonacci Series of {n} numbers:")
# for num in fib_gen:
#     print(num)

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b
#
#
# # Change the value of 'n' to the number of Fibonacci numbers you want to generate
# n = 10
# fibonacci(n)


# a, b = 0, 1
# n = 20  # Change the value of 'n' to the number of Fibonacci numbers you want to generate
#
# for _ in range(n):
#     print(a)
#     a, b = b, a + b

# n = int(input("Enter a Number to print fibonacci series:-"))
# a, b, c = 0, 1, 0
# for i in range(n):
#     print(a)
#     a = a + b
#     b = c
#     c = a

# def concat(num):
#     string = str(num)
#     print(string)
#
#
# s = int(input("Enter a Number:-"))
# concat(s)

# def even(n):
#     list1 = []
#     for i in n:
#         if i % 2 == 0:
#             list1.append(i)
#         elif i == 237:
#             list1.append(i)
#             break
#     return list1
#
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 743, 527
# ]
# b = even(numbers)
# for i in b:
#     print(i)


# def solve(list1, list2):
#     new = set()
#     for i in list1:
#         if i not in list2:
#             new.add(i)
#     return new
#
#
# list_1 = set(["White", "Black", "Red"])
# list_2 = set(["Red", "Green"])
# b = solve(list_1, list_2)
# print(b)

# def gcd_recursive(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd_recursive(b, a % b)
#
#
# num1 = 45
# num2 = 18
#
# gcd_result = gcd_recursive(num1, num2)
#
# print("GCD of", num1, "and", num2, "is:", gcd_result)

# def GCD(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# c = int(input("Enter a Number:-"))
# d = int(input("Enter a Number:-"))
# b = GCD(c, d)
# print(f"The GCD of {c} and {d} is: {b}")

# import math
#
# def lcm(num1, num2):
#     # Calculate the LCM using the formula: LCM = (num1 * num2) / GCD
#     gcd_result = math.gcd(num1, num2)
#     lcm_result = (num1 * num2) // gcd_result
#     return lcm_result
#
#
# # Input two positive integers
# num1 = int(input("Enter the first positive integer: "))
# num2 = int(input("Enter the second positive integer: "))
#
# result = lcm(num1, num2)
#
# print("The LCM of", num1, "and", num2, "is:", result)

# def sum(num1, num2, num3):
#     if num1 == num2 or num2 == num3 or num1 == num3:
#         return 0
#     else:
#         return num1 + num2 + num3
#
#
# a = int(input("Enter first Number:-"))
# b = int(input("Enter second Number:-"))
# c = int(input("Enter third Number:-"))
# d = sum(a, b, c)
# if d == 0:
#     print(f"The sum of {a}, {b} and {c} is: {d}")
# else:
#     print(f"The sum of {a}, {b} and {c} is: {d}")

# def __init__(self, att1, att2, a=2, b=4):
#     self.att1 = att1
#     self.att2 = att2
#     self.a = a
#     self.b = b

# class myClass:
#     def meth(self):
#         list1 = ["Ranjit", "Elon", "Steve"]
#         return list1
#     def name(self, name_list, book_list, book_author):
#         new_name = []
#         for i in name_list:
#             new_name.append(i.lower())
#
#         while True:
#             Name = str(input("Enter name:-"))
#             name = Name.lower()
#
#             if name not in new_name:
#                 print("You are not a student of our library")
#             else:
#                 book_name = int(input("Enter book no.:-"))
#                 if book_name < 1 or book_name > len(book_list):
#                     print("\nEnter proper book no.")
#                     continue
#                 else:
#                     book_list.pop(book_name - 1)
#                     book_author.pop((book_name - 1))
#                     break
#         return book_list, book_author
#
#
# c = myClass()
# name = c.meth()
# book = ["1. Rich dad poor dad", "2. Power of our subconscious mind", "3. The science of getting rich"]
# author = ["1. Robert Kiosaki", "2. Jopeph Murphy", "3. Wallace Wattles"]
# b, a = c.name(name, book, author)
# print(f"\nBooks:{b}\nAuthor:{a}")


def seconds():
    hour = int(input("Enter hours:-"))
    minute = int(input("Enter minutes:-"))
    sec = int(input("Enter seconds:-"))
    hour_sec = hour * 3600
    hour_min = minute * 60
    total_sec = hour_sec + hour_min + sec
    return hour_sec, hour_min, sec, total_sec


# hs, hm, s, ts = seconds()
# print(f"Hour seconds:{hs}\nMinute seconds:{hm}\nSeconds:{s}\nTotal seconds:{ts}")

# Function to calculate the sum of digits
# def sum_of_digits(number):
#     digit_sum = 0
#     while number > 0:
#         digit = number % 10
#         digit_sum += digit
#         number //= 10
#     return digit_sum
#
#
# try:
#     num = int(input("Enter a number: "))
#     result = sum_of_digits(num)
#     print(f"The sum of digits of {num} is {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

# list1 = ["America", "Canada", "Mexico", "Brazil"]
# list2 = list1
# # for i in list1:
# #     list2.append(i)
# list2.append("India")
# print(list2)

list1 = ['a', 23, 'b', 65, 'c', 99]
c = 0
for i in list1:
    # if isinstance(i, int):    # This is the most used method to find anything float, int, string and char anything
    #     c += i
    if type(i) is int:  # We can use this method also
        c += i

# print(c)

list2 = [12, 33, 44, 55, 66, 77, 88, 99]
odd = []
even = []
for i in list2:
    if i % 2 == 0:
        even.append(i)
for j in list2:
    if j % 2 != 0:
        odd.append(j)

# print(even+odd)

list3 = [1, 2, 2, 3, 3, 4, 5, 6, 7, 4]
number = []
# l1 = set()
# for i in list3:
#     l1.add(i)
#
# print(l1)
# for i in list3:
#     if i not in number:
#         # print(i)
#         number.append(i)

# print(list3)

