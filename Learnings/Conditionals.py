'''
a = int(input("Enter your age: "))

# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a<18):
    print("You cannot drive")
else:
    print("You can drive")

num = int(input("Enter the value of num: "))

if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is zero")
elif(num == 999):
    print("Special Case Numbers")
else:
    print("Number is positive")

if(num < 0):
    print("Number is Negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)

timestamp = time.strftime('%M')
print(timestamp)

timestamp = int(time.strftime('%S'))
print(timestamp)

num = float(input("Enter the value of num: "))

if num < 10:
    print("Good Morning")
elif 10 < num <= 12:
    if 10 < num <= 11:
        print("2nd Good Morning")
    elif 11 < num <= 12:
        print("Good Afternoon")
else:
    print("Good Evening")


x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("Input is zero")
    case 5:
        print("input is 5")
    case _ if x != 90:
        print(x, " is not 90")
    case _ if x != 80:
        print(x, " is not 80")
    case _:
        print(x)

def fibonacci(n):
    first = 0
    second = 1

    for i in range(1, n + 1):
        print(first)

        third = first + second
        first = second
        second = third


a = int(input("Enter how many terms you want to print: "))

print("Fibonacci series: ")
fibonacci(a)
'''


# def numbers(n):
#     for i in range(1, n+1):
#         print(i)
#
#
# a = int(input("Enter up to how many numbers you want to print: "))
# numbers(a)


a = ["Apple", "Mango", "Grapes", "Cherry", "Banana"]

# list1 = [i for i, j in enumerate(a)]
list1 = [i for i in a]
print(list1)
