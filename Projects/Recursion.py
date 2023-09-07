"""
import math
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# for i in range(2, 11):
#     print(factorial(i))


# f0 = 0
# f1 = 1
# fn = fn-1 + fn-2

# def fibonacci(n):
#     a, b, c = 0, 1, 0
#
#     for i in range(n):
#         print(a)
#         a = a + b
#         b = c
#         c = a

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


d = int(input("Enter a Number to print fibonacci series:- "))
fibonacci(d)
print(math.pi)

def count_num(n):
    count = 0
    for i in n:
        if i == 4:
            count += 1

    print(f"The number 4 comes {count} times")


l1 = [12, 4, 6, 4, 3, 56, 4, 4, 3, 4]
# count_num(l1)

def copy(string, n):
    if len(string) < 2:
        result = string * 2
    else:
        char2 = string[:2]
        result = char2 * n
    return result


ring = str(input("Enter a string:-"))
num = int(input("Enter the number of copies (non-negative integer):-"))
if num < 2:
    print("Please enter a non-negative integer")
else:
    b = copy(ring, num)
    print(f"{num} copies: {b}", end="")

def found(string):
    vowel = "aeiouAEIOU"
    a = 0
    for i in string:
        if i in vowel:
            a += 1
    return a


ring = str(input("Enter a string:-"))
b = found(ring)
print("There are", b, "vowels in the string")

def is_vowel(string):
    all_vowel = "aeiou"
    return string in all_vowel


print(is_vowel("a"))
print(is_vowel("j"))
"""

# def is_value_in_list(value, value_list):
#     return value in value_list
#
# # Test data
# test_value1 = 3
# test_list1 = [1, 5, 8, 3]
#
# test_value2 = -1
# test_list2 = [1, 5, 8, 3]
#
# # Check if test_value1 is in test_list1
# result1 = is_value_in_list(test_value1, test_list1)
# print(f"{test_value1} -> {test_list1} : {result1}")
#
# # Check if test_value2 is in test_list2
# result2 = is_value_in_list(test_value2, test_list2)
# print(f"{test_value2} -> {test_list2} : {result2}")


def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False


print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))