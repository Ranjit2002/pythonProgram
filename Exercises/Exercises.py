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

b = float(input("Enter Kilometer:- "))
a.kilo_to_mile(b)
