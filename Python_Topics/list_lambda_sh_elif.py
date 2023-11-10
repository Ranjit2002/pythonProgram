"""
# LIST COMPREHENSION

square = [x**2 for x in range(1, 11)]
print(square)

cube = [x*x*x for x in range(1, 11)]
print(cube)

Even = [i for i in range(1, 21) if i % 2 == 0]
print(Even)

list1 = [i * 3 for i in range(1, 21) if i % 2 == 0]
print(list1)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]                          # Hard Examples
flattened = [element for row in matrix for element in row]
print(flattened)

# LAMBDA EXPRESSION

square = lambda x: x * x
print(square(2))

cube = lambda x: x * x * x
print(cube(2))

even = lambda x: x % 2 == 0
print(even(2))
print(even(3))

numbers = [2, 3, 4, 5, 6]
bulb = list(map(lambda x: x * x, numbers))
print(bulb)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fil = list(filter(lambda x: x % 2 == 0, num))
print(fil)
"""

# age = int(input("Enter your age:- "))
# print("Can vote") if age >= 18 else print("Cannot vote")
# print("Can vote" if age >= 18 else "Cannot vote")
#
# temperature = int(input("Enter temperature:- "))
# status = "Normal" if temperature <= 30 else "High"          # Not more recommended
# print(status)
# print("Normal" if temperature <= 30 else "High")            # Recommended
# print("Normal") if temperature <= 30 else print("High")     # Recommended
#
# num = [1, 2, 3, 4, 5]   # Jo even numbers hai usko square kar dega list me hi
# squared = [x ** 2 if x % 2 == 0 else x for x in num]
# print(squared)

# x = 5
# print("Even and Positive" if x % 2 == 0 else "Odd")
#
# x = 10
# classification = "Even and positive" if x > 0 else ("Odd" if x % 2 != 0 else "Even and non-positive")
# print(classification)
#
# x = -6
# print("Even and positive" if x > 0 else ("Odd" if x % 2 != 0 else "Even and non-positive"))

import random

a = [23, 56, 67, 879, 345, 1234]

rand = random.choice(a)
print(rand)
