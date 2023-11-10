'''
name = "Ranjit"

for i in name:
    print(i)
    if(i == "j"):
        print("This is something new")   # This is an example to print String

colors = ["Red", "Green", "Blue", "Yellow"]

for x in colors:
    print(x)
    for i in x:
        print(i)

for k in range(1, 9):  # 1 is the starting range of printing and it will print upto 9-1
    print(k)


for k in range(1, 12, 3):  # It will leave 3 numbers after 1 and direct print 4 again 3 numbers and print 7
    print(k)


def table(n):
    for i in range(1, 10+1):
        print(n, "X", i, "=", n*i)


a = int(input("Enter the number to print table:- "))
table(a)


def even():
    count = 0
    for x in range(2, 50+1, 2):
        count += 1
        print(x)
    print("\nTotal even Numbers up to 50 is:- ", count)


even()   # We can print even numbers by using even method


for i in range(1, 51):
    if i % 2 == 0:
        print(i)  # We can print even numbers like this also


for i in range(3):
    print(i)


i=0
while(i <= 3):
    print(i)
    i += 1


i = int(input("Enter the number:-"))
while(i<=40):
    i = int(input("Enter the input:-"))
    print(i)


i = 5
while(i>0):
    print(i)
    i -= 1
    if(i == 2):
        break
else:
    print("I am inside loop")
'''

'''

Q1
i = 5
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print("")


Q2
a = int(input("Enter how many natural numbers sum do you want:- "))
count = 0
j = (a*2)

i = 2
while(i <= j):
    if i % 2 == 0:
        print(i)
        count += i
    i += 1
print("The sum of ", a, " Natural Numbers is:- ", count)

Q3
t = int(input("Enter a Number to print table:- "))
for i in range(1, 10+1):
    print(t, "X", i, "=", t*i)

Q4
j=10
for i in range(j, 0, -1):
    print(10, "X", j, "=", 10*j)
    j -= 1

Q5
a = int(input("Enter a given Number to find factorial:- "))
j = 1

for i in range(a, 0, -1):
    j *= i  

print(j)

Q6
a = int(input("Enter a given Number to find factorial:- "))
j = 1
i = 1
while i <= a:
    j *= i
    i += 1

print(j)

Q7
i = 5
j = i

while j >= 1:
    print('* ' * j)
    j -= 1

Q8
j = 0
for i in range(1, 11):
    print(8, "X", i, "=", i*8)
    j += (8*i)

print(j)


a = int(input("Enter a Number to print even Numbers:- "))
j = a*2
count = 0

i = 1
while i <= j:
    if i % 2 == 0:
        print(i)
        count += i
    i += 1

print("The sum of even Numbers up to ", a, " is:- ", count)
'''

# for i in range(1, 15):
#     if i == 10:
#         print("Skip the iteration")
#         continue
#     print(5, "X", i, "=", 5*i)

class num1:
    def __init__(self):
        print("My name is Ranjit\nMy name is Steve")

    def even(self):
        for i in range(1, 11):
            if i % 2 == 0:
                print(i)


class num2(num1):
    def __init__(self):
        super().__init__()
        print("\nMy name is harry\nMy name is Bill")

    def odd(self):
        for i in range(1, 11):
            if i % 2 != 0:
                print(i)


a = num2()
print()
a.even()
print()
a.odd()
