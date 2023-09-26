"""
# 1 - Python program to find the square root

def sqrt_num(number):
    if number < 0:
        print("Cannot compute square root of a negative number.")
        exit()

    guess = number / 2  # Initial guess is half of the input number

    for _ in range(10):  # You can adjust the number of iterations as needed
        guess = 0.5 * (guess + number / guess)  # Babylonian formula

    return guess

def main():
    number = float(input("Enter a number: "))
    sqrt = sqrt_num(number)
    print(f"The square root of {number} is approximately {sqrt:.2f}")


if __name__ == "__main__":
    main()

# 2 - Python program to calculate the area of triangle

def triangle_area(base, height):
    area = (base * height) / 2
    print(area)


bs = float(input("Enter base value:- "))
hi = float(input("Enter height value:- "))
triangle_area(bs, hi)

# 3 - Python program to swap two variables

def swap(a, b):
    print(f"Before swapping:\nnum1 = {a}\nnum2 = {b}\n")

    temp = a
    a = b
    b = temp
    print(f"After swapping:\nnum1 = {a}\nnum2 = {b}")


swap(2, 4)

# 4 - Python program to convert kilometers into miles

def km_ml(km):
    ans = km / 1.609
    print(f"{km} kilometers is {ans:.2f} miles")


kilo = float(input("Enter Kilometers:- "))
km_ml(kilo)

# 5 - Python program to convert Celsius to Fahrenheit

def temperature(cel):
    fah = (cel * 9/5) + 32
    print(f"{cel} Degrees is {fah:.2f} Fahrenheit")


deg = float(input("Enter Degree Celsius:-"))
temperature(deg)

# 6 - Python program to check if a number is Positive, Negative or 0

def ch_num(num):
    if num < 0:
        print("This is a Negative Number")
    elif num > 0:
        print("This is a positive Number")
    else:
        print("This is a 0")


a = float(input("Enter a Number:- "))
ch_num(a)

# 7 - Python program to check if a number is odd or even

def odd_even(num):
    if num % 2 == 0:
        print("This is a Even Number")
    else:
        print("This is a Odd Number")


a = float(input("Enter a Number:-"))
odd_even(a)

# 8 - Python program to find the largest among three numbers

def large(a, b, c):
    if b < a > c:
        print(f"{a} is the largest number")
    elif a < b > c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")


x = float(input("Enter first number:- "))
y = float(input("Enter second number:- "))
z = float(input("Enter third number:- "))
large(x, y, z)

# 9 - Python program to check prime number

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


# if __name__ == "__main__":
#     main()

# 10 - Python program to print all prime numbers in an interval

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_numbers(index):
    for num in range(2, index + 1):
        if is_prime(num):
            print(num)


end = int(input("Enter the end of the interval: "))

print(f"Prime numbers between {end}:")
prime_numbers(end)


# 11 - Python program to find the factorial of a number

# def factorial(f):         # We can find factorial using this also
#     fac = 1
#     for i in range(1, f + 1):
#         fac = i * fac
#     print(fac)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


a = int(input("Enter a Number to find factorial:-"))
b = factorial(a)
print(f"The factorial of {a} is: {b}")


# 12 - Python program to display the multiplication table code

def table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")


a = int(input("Enter a number:-"))
table(a)

# 13 - Python program to check armstrong number

def armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    return number == sum_of_powers


num = int(input("Enter a number: "))

if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# 14 - python program to find Armstrong number in an interval

def armstrong(num):
    string = str(num)
    length = len(string)
    power = sum(int(digit) ** length for digit in string)

    return num == power


n = int(input("Enter a Number:-"))
for i in range(1, n + 1):
    if armstrong(i):
        print(i)

# 15 - Python program to find the sum of natural numbers

def nat_num(num):
    for i in range(1, num + 1):
        print(i)


a = int(input("Enter a number:-"))
nat_num(a)

# 16 - Python program to find numbers divisible by another number

def divisible(start, end, divisor):
    for i in range(start, end + 1):
        if i % divisor == 0:
            print(i)


a = int(input("Enter the start range:-"))
b = int(input("Enter the end range:-"))
c = float(input("Enter the divisor:-"))

divisible(a, b, c)

# 17 - Python program to find hcf

def find_hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}")

# 18 - Python program to find LCM
def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def find_lcm(x, y):
    return (x * y) // find_gcd(x, y)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}")

# 19 - Python program to check whether if a string is Palindrome or not

def palindrome(string):
    string = string.lower()
    string = string.replace(" ", " ")
    reverse = string[::-1]

    return string == reverse


a = str(input("Enter a string:-"))
if palindrome(a):
    print("Palindrome")
else:
    print("Not Palindrome")

# 20 - Python program to remove punctuations from a string
import string
def punctuation(input_string):
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    cleaned_string = ""

    for char in input_string:
        if char not in symbols:
            cleaned_string += char

    return cleaned_string


s = str(input("Enter a String:-"))
b = punctuation(s)
print(b)

# 21 - Python program to sort words in alphabetic order
def sort(input_string):
    string = input_string.split()
    len_string = len(string)

    for i in range(len_string):
        for j in range(0, len_string - i - 1):
            if string[j][0] > string[j + 1][0]:
                string[j], string[j + 1] = string[j + 1], string[j]

    sorted_string = ' '.join(string)

    return sorted_string


input_string = str(input("Enter a string:-"))
sorted_string = sort(input_string)
print("Original string:", input_string)
print("Sorted string:", sorted_string)

# 22 - Python program to illustrate different set operations

# 1:-

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference (elements in set1 but not in set2)
difference_set1 = set1 - set2
print("Difference (set1 - set2):", difference_set1)

# Difference (elements in set2 but not in set1)
difference_set2 = set2 - set1
print("Difference (set2 - set1):", difference_set2)

# Symmetric Difference (elements in either set, but not both)
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)
# 2:-

# Helper function to perform union of two sets
def union(set1, set2):
    result = set1.copy()
    for i in set2:
        if i not in result:
            result.add(i)
    return result

def intersection(set1, set2):
    new = set()
    for i in set1:
        for j in set2:
            if i == j:
                new.add(i)
    return new

def Difference1(set1, set2):
    new = set()
    for i in set1:
        if i not in set2:
            new.add(i)
    return new

def Difference2(set1, set2):
    new = set()
    for i in set2:
        if i not in set1:
            new.add(i)
    return new

def symmetric(set1, set2):
    diff1 = set1 - set2
    diff2 = set2 - set1
    new = diff1 | diff2
    return new


first = {1, 2, 3, 4, 5}
second = {4, 5, 6, 7, 8}
a = union(first, second)
print(f"Union: {a}")
b = intersection(first, second)
print(f"Intersection: {b}")
c = Difference1(first, second)
print(f"Difference (set1 - set2): {c}")
d = Difference2(first, second)
print(f"Difference (set2 - set1): {d}")
e = symmetric(first, second)
print(f"Symmetric Difference: {e}")

# 23 - Python program to count the number of each vowel

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'  # Both lowercase and uppercase vowels

    vowel_count = {}  # Dictionary to store vowel counts

    for char in input_string:
        if char in vowels:
            char_lower = char.lower()  # Convert the character to lowercase
            if char_lower in vowel_count:
                vowel_count[char_lower] += 1
            else:
                vowel_count[char_lower] = 1

    return vowel_count


# Example usage
input_string = "My name is Ranjit"
result = count_vowels(input_string)

for vowel, count in result.items():
    print(f'{vowel}: {count}')

# 24 - Python program to interchange first and last element in a list

def swap_element(list1):
    # new = list1.pop(0)  # This starting five lines also works
    # old = list1.pop(-1)
    # list1.insert(0, old)
    # list1.insert(len(list1), new)
    # return list1
    if len(list1) < 2:
        return list1

    list1[0], list1[-1] = list1[-1], list1[0]
    return list1


list2 = [1, 2, 3, 4, 5, 54, 64, 456, 34, 76, 86]
b = swap_element(list2)
print(b)


# 25 - Python program to find the smallest number in the list

def smallest_num_in_list(list1):
    if len(list1) == 0:
        return None

    c = list1[0]
    for i in list1:
        if i < c:
            c = i
    return c


list2 = [23, 53, 65, 8, 87, 322, 55, 32]
b = smallest_num_in_list(list2)
print(b)


# 26 - Python program to find the largest number in the list

def largest_num_in_list(list1):
    if len(list1) == 0:
        return None

    c = list1[0]
    for i in list1:
        if i > c:
            c = i
    return c


list2 = [12, 4, 54, 76, 43, 243, 56]
b = largest_num_in_list(list2)
print(b)


# 27 - Python program to print all positive integers in a range

def positive(list1):
    if len(list1) == 0:
        return None
    new = []
    for i in list1:
        if i > 0:
            new.append(i)
    return new


list2 = [-1, -43, 45, 65, 78, -34, 56]
b = positive(list2)
print(b)


# 28 - Python program to print all negative integers in a range

def negative(list1):
    new = []
    if len(list1) == 0:
        return None
    for i in list1:
        if i < 0:
            new.append(i)
    return new


list2 = [-12, -34, 54, 77, -64, -376, 756]
b = negative(list2)
print(b)


# 29 - Python program to print duplicates from a list of integer

def duplicate(input_list):
    count = {}
    duplicates = []

    for i in input_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i, j in count.items():
        if j > 1:
            duplicates.append(i)

    return duplicates


# Example usage:
my_list = [1, 2, 3, 4, 1, 3, 4, 5, 7]
dupl = duplicate(my_list)
print("Duplicate numbers in the list are:", dupl)

# 30 - Remove multiple elements from a list in python

my_list = [11, 5, 17, 18, 23, 50]

# Elements to remove
elements_to_remove = [11, 5, 17, 18, 23, 50]

# Using a list comprehension to create a new list without the elements to remove
my_list = [x for x in my_list if x not in elements_to_remove]

# If you want to remove the elements in-place from the original list, you can use a loop
# for element in elements_to_remove:
#     my_list.remove(element)

print(my_list)

# 31 - Given a python list of numbers. Turn every item of a list into its square given:
# list = [1, 2, 3, 4, 5, 6, 7]

def square(list1):
    if len(list1) == 0:
        return None
    new = []
    for i in list1:
        sq = i * i
        new.append(sq)

    return new


list2 = [1, 2, 3, 4, 5, 6, 7]
b = square(list2)
print(b)
"""

def iterate(list1, list2):
    if len(list1) == 0 == len(list2):
        return None

    list2.reverse()
    for item1, item2 in zip(list1, list2):
        print(item1, item2)


l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]
iterate(l1, l2)
