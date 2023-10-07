def odd_even(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


# a = int(input("Enter a number:-"))
# odd_even(a)

def armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    total = 0

    for i in num_str:
        total += int(i) ** num_len

    return total == n


# a = int(input("Enter a number:-"))
# if armstrong(a):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# def palindrome(string):
#     low = string.lower()
#     rev = low[::-1]
#     if rev == low:
#         return True
#     return False
#
#
# a = str(input("Enter a String:-"))
# b = palindrome(a)
# print(b)

def palindrome(string):
    low = string.lower()
    new_str = ''
    for i in range(len(string) -1, -1, -1):
        new_str += low[i]

    return new_str == low


# a = str(input("Enter a String:-"))
# if palindrome(a):
#     print("Palindrome String")
# else:
#     print("Not Palindrome String")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# a = int(input("Enter a Number to find factorial:-"))
# b = factorial(a)
# print(f"The factorial of {a} is {b}")

def fibonacci(n):
    first = 0
    second = 1
    third = 0
    for i in range(n):
        print(i+1, ":", first)
        first = first + second
        second = third
        third = first


# a = int(input("Enter a number:-"))
# fibonacci(a)

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# while True:
#     i = int(input("1 --> Check again\n2 --> Exit\n"))
#     if i == 1:
#         a = int(input("Enter a Number:-"))
#         if is_prime(a):
#             print("Prime Number\n")
#         else:
#             print("Not Prime Number\n")
#     elif i == 2:
#         break
#     elif 1 < i > 2:
#         print("Please select numbers from 1 and 2\n")
#         continue

def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# a = int(input("Enter a Number:-"))
# b = Factorial(4)
# print(b)

def divisible(n):
    new = []
    for i in n:
        if i % 15 == 0:
            new.append(i)
    return new


# a = [45, 55, 60, 37, 100, 105, 220]
# b = divisible(a)
# print(b)

def positive(list1):
    new = []
    for i in list1:
        if i > 0:
            new.append(i)
    return new


# a = [23, -43, 65, -74, 90, -89]
# b = positive(a)
# print(b)

def product(list1):
    c = 1
    for i in list1:
        c *= i
    return c


# a = [10, 20, 30]
# b = product(a)
# print(b)


# str = (u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d '
#        u'\u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065')
# print()
# print(str)
# print()

new = '1234567890'
# print(new[:-4])
# print(new[:-1])
# print(new[:])

# print("Original string: ", new)
# print('%.6s' % new)
# print('%.9s' % new)
# print('%.10s' % new)
# print('%s' % new)

n = 20
d = {"x": 200}

# print(type(n)())
# print(type(d)())

# a = 2
# b = 2
# c = 2
# if a == b == c:
#     print(True)
# else:
#     print(False)

def lower_case(string):
    for i in string:
        if i.islower():
            return True
    return False


# a = str(input("Enter a string:-"))
# if lower_case(a):
#     print("Lower case letters exists in this string")
# else:
#     print("Lower case letters doesn't exist in this string")

# str1 = '122.22'
# print("Original String: ", str1)
# print("\nAdded trailing zeros:")
# str1 = str1.ljust(8, '0')
# print(str1)
# str1 = str1.ljust(10, '0')
# print(str1)
# print("\nAdded leading zeros:")
# str1 = '122.22'
# str1 = str1.rjust(8, '0')
# print(str1)
# str1 = str1.rjust(10, '0')
# print(str1)


