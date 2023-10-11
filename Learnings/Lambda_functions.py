# def double(x):
#     return x * 2
from functools import reduce


# We can give any argument of any function to a function
def apply(fn, value):  # fn is a function
    return 6 + fn(value)


square = lambda x: x * 2  # This and the upper one both are same
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

new = lambda x, y: print(f"{x} x {y} = {x * y}")

# a = int(input("Enter a Number:-"))
# print(square(a))
# print(cube(a))
# print(avg(3, 5, 7))
# print(apply(lambda x: x * x, 2))
# new(2, 6)


# syntax: Lambda arg: expressions
"""Lambda allows multiple args but single expression"""
v = lambda x: x * x
# print(v(3))

num = [23, 4, 7, 9, 98, 48, 76, 879]


def is_even(n):
    return n % 2 == 0


even = list(filter(is_even, num))


# print(even)


def update(n):
    return n * 2


double = list(map(update, even))
# print(double)

double1 = list(map(lambda x: x * 2, even))


# print(double1)


def add_all(a, b):
    return a * b


s = reduce(add_all, double)
# print(s)


s1 = reduce(lambda a, b: a + b, double)


# print(s1)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


# a = fibonacci(10)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


def factorial(n):
    c = 1
    for i in range(1, n + 1):
        c *= i
        yield c


# b = factorial(10)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# a = 'successfully'

# Create an empty dictionary to store character frequencies
# char_count = {}

a = 'successfully'
dict1 = dict()

for i in a:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1


print(dict1)

