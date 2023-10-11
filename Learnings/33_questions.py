"""
# Q1 - Python program to find the square root
def square_root(n):
    root = n ** 0.5
    return root


a = int(input("Enter a number to find square root:-"))
b = square_root(a)
print(f"The square of {a} is: {b:.2f}")

# Q2 - Python program to calculate the area of a triangle
def triangle_area(Base, Height):
    area = (Height * Base) / 2
    return area


height = float(input("Enter base:-"))
base = float(input("Enter height:-"))
c = triangle_area(base, height)
print(f"The area of triangle is: {c:.2f}")

# Q3 - Python program to swap two variables
def swap_variables(a, b):
    temp = a
    a = b
    b = temp
    print("a =", a)
    print("b =", b)


c = int(input("Enter a variable:-"))
d = int(input("Enter b variable:-"))
swap_variables(c, d)

# Q4 - Python program to convert kilometer to miles
def km_to_miles(km):
    mile = km / 1.609
    return mile


a = float(input("Enter km:-"))
b = km_to_miles(a)
print(f"{a} kilometers is: {b:.2f} miles")

# Q5 - Python program to convert Celsius to Fahrenheit
def cel_fah(Celsius):
    fah = (Celsius * 9/5) + 32
    return fah


a = float(input("Enter temperature in degree celsius:-"))
b = cel_fah(a)
print(f"{a} Degree Celsius is: {b:.2f} Fahrenheit")

# Q6 - Python program to check is a number is positive, negative or zero
def check_number(n):
    if n > 0:
        print("Positive Number")
    elif n < 0:
        print("Negative Number")
    else:
        print("Zero")


a = float(input("Enter a Number:-"))
check_number(a)

# Q7 - Python program to check if a number is odd or even
def odd_even(n):
    if n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")


a = int(input("Enter a Number:-"))
odd_even(a)

# Q8 - Python program to find largest among three numbers
def max_number(first, second, third):
    if first > second and first > third:
        print(f"{first} is the largest number")
    elif second > first and second > third:
        print(f"{second} is the largest number")
    else:
        print(f"{third} is the largest number")


a = float(input("Enter first Number:-"))
b = float(input("Enter second Number:-"))
c = float(input("Enter third Number:-"))
max_number(a, b, c)

# Q9 - Python program to check prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
9


num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Q10 - Python program to print all prime number in an interval
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_num(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i)


a = int(input("Enter the end of the prime number:-"))
print(f"Prime number between {a} is: ")
prime_num(a)

# Q11 - Python program to find the factorial of a number
def factorial(n):
    if n in {0, 1}:
        return 1
    else:
        return n * factorial(n-1)


a = int(input("Enter a number to find factorial:-"))
b = factorial(a)
print(f"The factorial of {a} is: {b}")

# Q12 - Python program to display the multiplication table code
def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")


a = int(input("Enter a Number to print table:-"))
table(a)

# Q13 - Python program to check Armstrong number
def armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_power = sum(int(digit) ** num_digits for digit in num_str)

    return n == sum_of_power


a = int(input("Enter a number:-"))
if armstrong(a):
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")

# Q14 - Python program to find Armstrong number in an interval
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_power = sum(int(digit) ** num_digits for digit in num_str)

    return n == sum_of_power

def Arm_num(start, end):
    for i in range(start, end+1):
        if is_armstrong(i):
            print(i)


st = int(input("Enter the start: "))
en = int(input("Enter the end: "))
Arm_num(st, en)

# Q15 - Python program to find the sum of natural numbers
def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print(f"The sum of {n} natural is {total}")


a = int(input("Enter a number:-"))
sum(a)

# Q16 - Python program to find numbers divisible by another number
def num_div(start, end, divisor):
    for i in range(start, end+1):
        if i % divisor == 0:
            print(i)


a = int(input("Enter start: "))
b = int(input("Enter end: "))
c = int(input("Enter divisor: "))
num_div(a, b, c)

# Q17 - Python program to find HCF or GCD
def hcf_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


n1 = int(input("Enter first number:-"))
n2 = int(input("Enter second number:-"))
b = hcf_gcd(n1, n2)
print(f"The HCF/GCD of {n1} and {n2} is: {b}")

# Q18 - Python program to find LCM
def LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm


num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))
b = LCM(num1, num2)
print(b)

# Q19 - Python program to check whether a string is palindrome or not
def palindrome(string):
    lower = string.lower()
    reverse = lower[::-1]
    if reverse == lower:
        return True
    return False


a = str(input("Enter a string:-"))
if palindrome(a):
    print("Palindrome")
else:
    print(f"Not palindrome")

# Q20 - Python program to remove punctuations from a string
def punctuations(string):
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    new_string = ""

    for i in string:
        if i not in symbols:
            new_string += i
    return new_string


a = str(input("Enter a string with punctuations:-"))
b = punctuations(a)
print(b)

# Q21 - Python program to sort words in Alphabetic order
def sort_chr(inp_string):
    string = list(inp_string)
    new_str = ''.join(sorted(string, key=lambda x: (x.lower(), x)))
    return new_str


a = str(input("Enter a string:-"))
b = sort_chr(a)
print(b)

# Q22 - Python program to illustrate different set operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

def update(set1, set2):
    s1 = set1.copy()
    s2 = set2.copy()
    s1.update([345])
    s2.update([567])
    print(f"Update set1: {s1} Update set2: {s2}")


update(set1, set2)

def add(set1, set2):
    s1 = set1.copy()
    s2 = set2.copy()
    s1.add(32)
    s2.add(56)
    print(f"Add set1: {s1} Add set2: {s2}")


add(set1, set2)

def is_Subset(set1, set2):
    if set1.issubset(set2):
        print(f"set1 is not subset of set2")
    else:
        print(f"set2 is not subset of set1")


is_Subset(set1, set2)

def dis_join(set1, set2):
    if set1.isdisjoint(set2):
        print(f"set1 and set2 are disjoint (have no common elements)")
    else:
        print(f"set1 and set2 are not disjoint")


dis_join(set1, set2)
def union(set1, set2):
    result = set1.copy()
    for i in set2:
        if i not in set1:
            result.add(i)
    print(f"Union: {result}")


union(set1, set2)

def intersections(set1, set2):
    new_set = set()
    for i in set1:
        if i in set2:
            new_set.add(i)
    print(f"Intersection: {new_set}")


intersections(set1, set2)
def symmetric(set1, set2):
    new = set()
    for i in set1:
        if i not in set2:
            new.add(i)
    for j in set2:
        if j not in set1:
            new.add(j)
    print(f"Symmetric Difference: {new}")


symmetric(set1, set2)

# Q23 - Python program to count the number of each vowel
def count_vowel(string):
    new_str = string.lower()
    vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for i in new_str:
        for j in vowel:
            if i == j:
                vowel[i] += 1
    return vowel


a = str(input("Enter a string:-"))
b = count_vowel(a)
for letter, count in b.items():
    if count > 0:
        print(f"{letter}:{count}")

# Q24 - Python program to interchange first and last element in a list
def change(list1):
    print(f"Original list: {list1}")
    a = list1.pop(0)
    b = list1.pop(len(list1)-1)
    list1.append(a)
    list1.insert(0, b)
    print(f"After changing: {list1}")


c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
change(c)

# Q25 - Python program to find the smallest number in a list
def smallest(list1):
    for i in range(len(list1)-1):
        if list1[i] < list1[i + 1]:
            list1[i + 1] = list1[i]
    c = list1.pop(len(list1)-1)
    print(c)


a = [23, 65, 787, 2, 345, 678]
smallest(a)

# Q26 - Python program to find the largest number in a list
def largest(list1):
    c = 0
    for i in list1:
        if i > c:
            c = i
    print(c)


a = [235, 45, 2, 873, 567, 98]
largest(a)

# Q27 - Python program to print all positive number in a range
def positive_number(list1):
    for i in list1:
        if i < 0:
            list1.remove(i)
    print(list1)


a = [22, -34, 54, -56, 67, -89]
positive_number(a)

# Q28 - Python program to print all negative number in a range
def negative_number(list1):
    for i in list1:
        if i > 0:
            list1.remove(i)
    print(list1)


a = [22, -34, 54, -56, 67, -89]
negative_number(a)

# Q29 - Python program to print duplicates from a list of integers
def duplicates(list1):
    new = set()
    i = 0
    while i < len(list1)-1:
        if i < len(list1):
            j = i + 1
            while j < len(list1):
                if list1[i] == list1[j]:
                    new.add(list1[j])
                j += 1
        i += 1
    new_l = list(new)
    print(f'Duplicates elements: {new_l}')


a = [1, 2, 2, 3, 4, 4, 5, 4, 6, 4, 7, 3, 6, 8, 9, 8, 8, 4, 2]
duplicates(a)

# Q30  - Remove multiple elements from a list in python
def remove_elements(list1, list2):
    # using list comprehension
    # new_list = [x for x in list1 if x not in list2]
    # print(new_list)

    for i in list1:
        if i in list2:
            list1.remove(i)
    print(list1)


a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 4, 6]
remove_elements(a, b)

# Q31 - Given a Python list of numbers. Turn every item of a list into its square Given:
#  List = [1, 2, 3, 4, 5, 6, 7]

def square(list1):
    for i in range(len(list1)):
        list1[i] = list1[i] * list1[i]
    print(list1)


List = [1, 2, 3, 4, 5, 6, 7]
square(List)

# Q32 - Given a two Python list. Iterate both lists simultaneously such that
# list1 should display item in original order and list2 in reverse order.
# list1=[10,20,30,40]
# list2=[100,200,300,400]

def iterate(list1, list2):
    list2.sort(reverse=True)
    print(f"List1: {list1}")
    print(f"List2: {list2}")


List1 = [10, 20, 30, 40]
List2 = [100, 200, 300, 400]
iterate(List1, List2)
"""
