'''
def calculate(a, b):
    mean = (a*b)/(a+b)
    print(mean)


def isGreater(x, y):
    if x > y:
        print(x, "is greater than", y)
    elif y < x:
        print(y, "is less than", y)


# def average(a=6, b=3):
#     print("The average is: ", (a+b)/2)


def name(fname, mname="Rajesh", lname="Vishwakarma"):
    print("Hello!", fname, mname, lname)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    # print("The average is: ", sum/len(numbers))
    return sum/len(numbers)





a = 9
b = 85
isGreater(a, b)

c = 57
d = 66
isGreater(c, d)


# average(23, 6)
# average()


name("Ranjit")
name("Ranjit", "Thakur")
name("Ranjit", "Singh", "Thakur")

c = average(2, 5, 6)
print(c)
'''


def table(n):
    for i in range(1, 11):
        print(n, "X", i, "=", n * i)


def star(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print("*", end=" ")
        print("")


def starR(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print("*", end=" ")
        print("")


def fibonacci(n):
    first = 0
    second = 1
    for i in range(1, n + 1):
        print(first, end=" ")
        next = first + second
        first = second
        second = next


def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
        print("The average is: ", sum / len(numbers))
    return sum


def fahrenheit(n):
    degree = (n * 9 / 5) + 32
    print(degree)

# table(14)

# star(10)

# starR(5)

# fibonacci(20)

# average(5, 10)

# fahrenheit(67)

# char = '5'
# integer = int(char)
# print(integer)

# integer = 3
# str = str(integer)
# print(str)


# fibonacci(10)


# my_list = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(my_list):
#     print(f"Index {index}: {fruit}")


def details(*a):
    return a


# print(details("Ranjit", 34, "Mumbai", 34254547))


def nex_details(**b):
    print(b)


# nex_details(name="Ranjit", age=34, city="Mumbai", mobile=34636323242)

# a = {"Ranjit": 1, "Steve": 2, "Elon": 3, "Bill": 4}
# print("Yes") if 2 in a else print("No")

# a = ["Mobile", "Laptop", "Fridge"]
# b = [12000, 40000, 34000]

a = "mobile"
b = list()
b.append(a)
print(b)
