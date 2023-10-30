import random


class questions:
    def add_2_numbers(self, a, b):
        return a + b

    def hello_world(self):
        return "Hello World!"

    # def square_root(self, number, epsilon=1e-6):
    #     guess = number / 2.0  # Initial guess (you can choose a different initial guess if needed)
    #
    #     while abs(guess * guess - number) > epsilon:
    #         guess = (guess + number / guess) / 2.0
    #     return guess

    # OR WE CAN USE THIS METHOD ALSO

    def square_root(self, n):
        return n ** 0.5

    def triangle_area(self, height, base):
        return (height * base) / 2

    def swap_variables(self, x, y):
        x, y = y, x
        return x, y

    def kilo_to_mile(self, km):
        a = km / 1.609
        print(f"{km} kilometers is {a:.2f} miles")

    def pos_0_neg(self, i):
        print("Positive Number") if i > 0 else ""
        print("Negative Number") if i < 0 else ""
        print("Zero") if i == 0 else ""

    def odd_even(self, i):
        if i % 2 == 0:
            print(f"{i} is an Even Number")
        else:
            print(f"{i} is an Odd Number")

    def leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    def largest_among_3_num(self, x, y, z):
        print(x, "is the largest number") if y < x > z else ""
        print(y, "is the largest number") if x < y > z else ""
        print(z, "is the largest number") if y < z > x else ""

    def prime_number(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def prime_num_in_interval(self, n):
        for i in range(2, n):
            if self.prime_number(i):
                print(f"{i}")

    def random_number(self):
        x = random.randrange(1, 100000)
        print(x)

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def multiplication_table(self, n):
        for i in range(1, 11):
            print(f"{n} X {i} = {n * i}")

    def fibonacci_series(self, n):
        a, b = 0, 1
        for i in range(n):
            print(a)
            a, b = b, a + b

    def armstrong_number(self, number):
        num_str = str(number)
        num_digit = len(num_str)
        total = sum(int(digit) ** num_digit for digit in num_str)
        return total == number

    def arm_num_in_interval(self, start, end):
        for i in range(start, end + 1):
            if a.armstrong_number(i):
                print(i)

    def sum_of_n_num(self, end):
        c = 0
        for i in range(1, end + 1):
            c += i
        print(f"The sum of {end} natural number is {c}")

    def anonymous_function(self, end):
        list1 = list(map(lambda x: 2 ** x, range(end + 1)))
        for i in list1:
            print(i)

    def num_div_by_ano_num(self, divider):
        a = [i for i in range(1, 101)]
        b = list(filter(lambda x: x % divider == 0, a))
        for i in b:
            print(i)

    def dec_to_bin_oct_hex(self, num):
        print(f"The conversion of decimal number {num} is: ")
        print(f"{bin(num)} in binary")
        print(f"{oct(num)} in octal")
        print(f"{hex(num)} in hexadecimal")

    def ASCII_value(self, string):
        a = str(string)
        print(f"The ASCII value of {string} is {ord(a)}")

    # def HCF_GCD(self, num1, num2):
    #     if num1 > num2:
    #         smaller = num2
    #     else:
    #         smaller = num1
    #     for i in range(1, smaller+1):
    #         if (num1 % i == 0) and (num2 % i == 0):
    #             hcf = i
    #     return hcf

    def HCF_GCD(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def factors_of_a_num(self, num):
        print(f"The factors of {num} is : ")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)

    def shuffle_cards(self):
        import itertools
        deck = list(itertools.product(range(1, 14), ["Clubs", "Hearts", "Spades", "Diamonds"]))
        random.shuffle(deck)
        print(deck)
        for i in range(5):
            print(deck[i][0], "of", deck[i][1])

    def calendar(self):
        import calendar
        year = int(input("Enter year > "))
        month = int(input("Enter month > "))
        calendar = calendar.month(year, month)
        print(calendar)

    def fibo_recursion(self, n):
        if n <= 0:
            return "Invalid input"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibo_recursion(n - 1) + self.fibo_recursion(n - 2)

    def sum_using_recursion(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return n + self.sum_using_recursion(n - 1)

    def star(self, n):
        num = 1
        for i in range(1, n + 1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()

    def factorial_using_recursion(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial_using_recursion(n - 1)

    def dec_to_bin_using_recursion(self, n):
        if n > 1:
            self.dec_to_bin_using_recursion(n // 2)
        print(n % 2, end="")

    def add_two_matrices(self):
        mat1 = [1, 2, 3,
                4, 5, 6,
                7, 8, 9],

        mat2 = [9, 8, 7,
                6, 5, 4,
                3, 2, 1]

        mat3 = [[0, 0, 0] for _ in range(len(mat1))]

        # for i in range(len(mat1)):
        #     for j in range(len(mat1[0])):
        #         mat3[i][j] = mat1[i][j] + mat2[i][j]
        #     print()

        for row in mat1:
            string = " ".join(map(str, row))
            print(string)


a = questions()

# b = int(input("Enter first number:- "))
# c = int(input("Enter second number:- "))
# d = a.add_2_numbers(b, c)
# print(f"The sum of {b} and {c} is {d}")

# print(a.hello_world())

# a1 = int(input("Enter a number to find square root:- "))
# c = a.square_root(a1)
# print(c // 1)
# print(c)

# c = int(input("Enter height:- "))
# d = int(input("Enter base:- "))
# b = a.triangle_area(c, d)
# print(f"The area of a triangle is {b}")

# b = int(input("X = "))
# c = int(input("Y = "))
# x, y = a.swap_variables(b, c)
# print(f'X = {x}\nY = {y}')

# b = float(input("Enter Kilometer:- "))
# a.kilo_to_mile(b)

# b = int(input("Enter a Number:- "))
# a.pos_0_neg(b)

# b = int(input("Enter a Number:- "))
# a.odd_even(b)

# b = int(input("Enter a year:- "))
# c = a.leap_year(b)
# if c:
#     print(f"{b} is a leap year")
# else:
#     print(f"{b} is not a leap year")

# b = int(input("Enter first number:- "))
# c = int(input("Enter second number:- "))
# d = int(input("Enter third number:- "))
# a.largest_among_3_num(b, c, d)

# b = int(input("Enter a Number:- "))
# c = a.prime_number(b)
# if c:
#     print(f"{b} is a prime number")
# else:
#     print(f"{b} is not a prime number")

# b = int(input("Enter a Number:- "))
# a.prime_num_in_interval(b)

# a.random_number()

# b = float(input("Enter temperature in degree celsius:- "))
# c = a.celsius_to_fahrenheit(b)
# print(f"{b} degree celsius is {c:.2f} fahrenheit")

# b = int(input("Enter a number to find factorial:- "))
# print(a.factorial(b))

# b = int(input("Enter a number to print table:- "))
# a.multiplication_table(b)

# b = int(input("Enter a number:- "))
# a.fibonacci_series(b)

# b = int(input("Enter a Number:- "))
# c = a.armstrong_number(b)
# if c:
#     print(f"{b} is an Armstrong Number")
# else:
#     print(f"{b} is not an Armstrong Number")

# b = int(input("Enter starting:- "))
# c = int(input("Enter ending:- "))
# a.arm_num_in_interval(b, c)

# b = int(input("Enter end:- "))
# a.sum_of_n_num(b)

# b = int(input("Enter end:- "))
# a.anonymous_function(b)

# b = int(input("Enter divider:- "))
# a.num_div_by_ano_num(b)

# b = int(input("Enter a Number:- "))
# a.dec_to_bin_oct_hex(b)

# b = input("Enter only one number, symbol or character to find the ASCII:- ")
# a.ASCII_value(b)

# b = int(input("Enter first Number:- "))
# c = int(input("Enter second Number:- "))
# d = a.HCF_GCD(b, c)
# print(f"The HCF/GCD of {b} and {c} is {d}")

# b = int(input("Enter a Number:- "))
# a.factors_of_a_num(b)

# a.shuffle_cards()

# a.calendar()

# b = int(input("Enter a Number:- "))
# c = a.fibo_recursion(b)
# print(c)

# b = int(input("Enter a Number:- "))
# c = a.sum_using_recursion(b)
# print(c)

# a.star(5)

# c = a.factorial_using_recursion(5)
# print(c)

# a.dec_to_bin_using_recursion(32)

a.add_two_matrices()
