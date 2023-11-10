class year:
    def leap(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    def prime_numbers(self, n):
        if n <= 0:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def pr_num_interval(self, n):
        for i in range(2, n+1):
            if self.prime_numbers(i):
                print(i)

    def factorial(self, n):
        if n == 0 or n == 1:
            return n
        return n * self.factorial(n - 1)


a = year()
# c = int(input("Enter the year:- "))
# b = a.leap(c)
# if b:
#     print(f"{c} is a leap year")
# else:
#     print(f"{c} was not a leap year")

# a1 = int(input("Enter a Number:- "))
# c = a.prime_numbers(a1)
# if c:
#     print(f"{a1} is a prime number")
# else:
#     print(f"{a1} is not a prime number")

# a2 = int(input("Enter up to how much:- "))
# a.pr_num_interval(a2)

a3 = int(input("Enter a number to find factorial:-"))
b = a.factorial(a3)
print(f"The factorial of {a3} is {b}")
