class methods:
    def table(self):
        a = int(input("Enter a Number to print table:-"))
        for i in range(1, 11):
            print(f"{a} X {i} = {a*i}")

    def star(self):
        line = int(input("Enter how many line you want to print star:-"))
        for i in range(1, line+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()

    def rev_star(self):
        a = int(input("Enter how many line you want to print:-"))
        for i in range(1, a+1):
            for j in range(1, a-i+2):
                print("*", end=" ")
            print()


m = methods()
# m.table()
# print()
# m.star()
# print()
# m.rev_star()
def recursion(n):
    if n == 0:
        return 0
    else:
        return n + recursion(n - 1)


# b = recursion(7)
# print(b)

def fibonacci(n):
    if n == 1 or n == 2:
        return n-1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


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

# def rec_star(n):
#     if n > 0:


# * * * * *
# * * * *
# * * *
# * *
# *
