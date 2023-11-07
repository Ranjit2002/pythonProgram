class methods:
    def table(self):
        a = int(input("Enter a Number to print table:-"))
        for i in range(1, 11):
            print(f"{a} X {i} = {a * i}")

    def star(self):
        line = int(input("Enter how many line you want to print star:-"))
        for i in range(1, line + 1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()

    def rev_star(self):
        a = int(input("Enter how many line you want to print:-"))
        for i in range(1, a + 1):
            for j in range(1, a - i + 2):
                print("*", end=" ")
            print()


m = methods()


# m.table()
# print()
# m.star()
# print()
# m.rev_star()
def recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return n + recursion(n - 1)


# b = recursion(13)
# print(b)

def fibonacci(n):
    if n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# b = fibonacci(10)
# print(b)

def average(*args):
    a = 0
    d = 0
    for i in args:
        a += i
        d += 1
    avg = a / d
    return avg


# b = average(1, 2, 3, 4, 5, 6)
# print(b)

def rec_star(n):
    if n > 0:
        rec_star(n - 1)
        for i in range(n):
            print("*", end=" ")
        print()

def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()


# pattern(10)

# rec_star(5)

# * * * * *
# * * * *
# * * *
# * *
# *

# def print_star_recursive(self, line, i=1, j=1):
#     if i > line:
#         return
#
#     if j <= i:
#         print("*", end=" ")
#         print_star_recursive(self, line, i, j + 1)
#     else:
#         print()
#         print_star_recursive(self, line, i + 1, 1)


# Example usage:
# line = int(input("Enter how many lines you want to print stars: "))
# print_star_recursive(None, line)

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# b = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]
#
# c = [[0, 0, 0],
#      [0, 0, 0],
#      [0, 0, 0]]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         c[i][j] = a[i][j] * b[i][j]
#
# for i in c:
#     print(i)

# r = [[a[i][j] + b[i][j] for j in range(len(a[0])) for i in range(len(a))]]
# print(r)

# Program to multiply two matrices using list comprehension

# take a 3x3 matrix
# A = [[12, 7, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# # take a 3x4 matrix
# B = [[5, 8, 1, 2],
#      [6, 7, 3, 0],
#      [4, 5, 9, 1]]
#
# # result will be 3x4
# result = [[sum(a * b for a, b in zip(A_row, B_col))
#            for B_col in zip(*B)]
#           for A_row in A]
#
# for r in result:
#     print(r)

def odd(n):
    if n == 1:
        return True
    elif n == 0:
        return False
    else:
        return odd(n-2)


# a = int(input("Enter Number to find odd Number:-"))
# b = odd(a)
# print(b)

def palindrome(n):
    to_lower = n.lower()
    rev = to_lower[::-1]
    return to_lower == rev


a = str(input("Enter a string:- "))
if palindrome(a):
    print(f"{a} is a Palindrome string")
else:
    print(f"{a} is not a Palindrome string")
