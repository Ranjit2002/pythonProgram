# def sort(n):
#     temp = 0
#     for i in range(len(n+1)):
#         for j in range(len(n+1)):
#              if j < i:
#                  j = temp
#                 temp = i
#                 i = j

# list1 = [3, 67, 99, 34, 5, 87, 6, 76]

# list1 = [3, 67, 99, 34, 5, 87, 6, 76]
# c = 0
# for i in list1:
#     if i > c:
#         c = i
# print(c)
# b = sorted(list1)
# print(b)

# list1 = [3, 67, 99, 34, 5, 87, 6, 76]
# new = list1[:]  # Create a copy of the original list
#
# for i in range(len(new)):
#     for j in range(0, len(new)-i-1):
#         if new[j] > new[j+1]:
#             new[j], new[j+1] = new[j+1], new[j]
#
# print(new)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#
#
# my_list = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_list)
# print("Sorted list:", my_list)

def is_armstrong_number(num):
    # Convert the number to a string to count its digits
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of digits each raised to the power of num_digits
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return digit_sum == num


def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


# Input range
# start_range = int(input("Enter the starting number: "))
# end_range = int(input("Enter the ending number: "))
#
# armstrong_numbers = find_armstrong_numbers(start_range, end_range)
#
# if armstrong_numbers:
#     print("Armstrong numbers in the range:", armstrong_numbers)
# else:
#     print("No Armstrong numbers found in the specified range.")

# a = ["Python is an interpreted programming language"]
# b = "".join(a)
# print(b, type(b))

# a = 'Ranjit'
# print(a.index('j'))
# j = 0
#
# for i in a:
#     if i == 'j':
#         break
#     j += 1
#
# print(j)

# a = ["Ranjit"]
# b = "".join(a)
# print(b)
#
# if b.isalpha():
#     print(True)
# else:
#     print(False)


def replace_underscores(input_str, replace_chars):
    result = ""
    char_index = 0

    for char in input_str:
        if char == "_":
            if char_index < len(replace_chars):
                result += replace_chars[char_index]
                char_index += 1
        else:
            result += char

    return result


# Example usage:
b = "Ran___"
replacement_chars = "dom"
result = replace_underscores(b, replacement_chars)

print(result)
