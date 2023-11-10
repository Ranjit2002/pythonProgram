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

"""
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


a = int(input("Enter a Number:- "))
fibo(a)
"""

def matrices_addition():
    mat1 = [[11, 25, 32],
            [14, 55, 26],
            [72, 83, 39]]

    mat2 = [[49, 68, 27],
            [16, 65, 24],
            [53, 22, 41]]

    mat3 = [[0, 0, 0] for _ in range(len(mat1))]

    print("First Matrix:- ")
    for row in mat1:
        string = ' '.join(map(str, row))
        print(string)
    print()

    print("Second Matrix:- ")
    for row in mat2:
        string = ' '.join(map(str, row))
        print(string)
    print()

    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            mat3[i][j] = mat1[i][j] * mat2[i][j]

    print("Sum of First and Second Matrix:- ")
    for row in mat3:
        string = ' '.join(map(str, row))
        print(string)

    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
        print()

    for row in mat3:
        res = ' '.join(map(str, row))
        print(res)


def transpose_matrix():
    a = [49, 68, 27,
         16, 65, 24,
         53, 22, 41]

    num_rows = 3
    num_columns = 3
    transposed_a = []

    for j in range(num_columns):
        new_row = []
        for i in range(num_rows):
            new_row.append(a[i * num_columns + j])
        transposed_a.append(new_row)

    for row in transposed_a:
        print(' '.join(map(str, row)))


# transpose_matrix()

# print(f"Pin: {random.randint(1000, 9999)}")

class encap:
    # _name = "Ranjit"
    # __b = 20

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def show(self):
        print(f"The name of the user is {self._name} and the age of the user is {self.__age}")


class new_enc(encap):

    def new_show(self):
        print(f"Name: {self._name}, Age: {self.__age}")      # AttributeError: 'new_enc' object has no attribute '_new_enc__age'    # This is an example of encapsulation that's why we can't access any private object outside the class or any other class which inherits that class


a = new_enc("Ranjit", 21)
# a.show()
# a.new_show()


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod  # Using class method as alternative constructor
    def from_full_name(cls, full_name, salary):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name, salary)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


# a = Employee("Ranjit", "Vishwakarma", 1000000)
# b = Employee.from_full_name("Steve Jobs", 50000)
#
# print(a.get_full_name())
# print(b.get_full_name())

def palindrome(string):
    s = ''.join(filter(str.isalnum, string)).lower()
    return s == string[::-1]


# a = "12321"
# b = palindrome(a)
# print(b)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


# fibonacci(10)

def palindrome(string):
    lo = string.lower()
    s = string[::-1]
    return s == lo


# a = "12321"
# if palindrome(a):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

a = {1: 'Ranjit', 2: 'Elon', 3: 'Steve'}
b = {4: 'Bill', 5: 'Mark', 6: 'Warren'}

for i in a.keys():
    print(i)

