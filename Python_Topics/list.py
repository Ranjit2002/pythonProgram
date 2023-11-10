marks = [43, 65, 23, "Ranjit", True, 1, 4, 8, 54, 88]
'''
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if 4 in marks:
    print("Yes")
else:
    print("No")

if "Ranjit" in marks:  # Same thing applies for string as well
    print("Yes")
else:
    print("No")

if "anj" in "Ranjit":
    print("Yes")
else:
    print("No")

for i in marks:
    print(i, end=" ")


print(marks)
print(marks[1:-1])
print(marks[1:10])
print(marks[1:10:2])  # 2 means it will print first element of list and jump 2 index


lst = [i for i in range(5)]  # (List Comprehension) automatically 0 - 4 values will come inside lst
print(lst)

lst = [i for i in range(10) if i%2==0]  # Numbers which is divisible by 2 means even numbers that will come in this list
print(lst)
'''

lst = [12, 54, 4, 7, 9, 76]
c = 0
for i in lst:
    c += i
print(c)

def String(string_list):
    filter_list = []
    for i in string_list:
        if len(i) > 5:
            filter_list.append(i)
    return filter_list

input = ["Ranjit", "Vishal", "iron", "car", "cat", "setting"]
result = String(input)
print(result)


def even(integer_list):
    filter_list = []
    for i in integer_list:
        if i % 2 == 0:
            filter_list.append(i)
    return filter_list

lst = [23,54, 56, 3, 5, 68, 86, 7, 9]
result = even(lst)
print(result)


def alphabet(string_list):
    sorted_name = sorted(string_list)  # sorted is an inbuilt function to sort string in alphabetical order or integer
    return sorted_name

input_names = ["America", "Brazil", "France", "England", "China", "Japan"]
result = alphabet(input_names)
print(result)


def integer(integer):
    sort_integer = sorted(integer)
    return sort_integer

input_int = [32, 6, 5, 87, 43, 77, 54]
result = integer(input_int)
print(result)

def reverse_list_in_place(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

# Example usage
numbers = [1, 2, 3, 4, 5]
reverse_list_in_place(numbers)
print(numbers)  # Output: [5, 4, 3, 2, 1]


def odd(n):
    filter_list = []
    for i in n:
        if i % 2 != 0:
            filter_list.append(i)
    return filter_list


numbers = [23, 5, 22, 44, 43, 55, 77, 44, 66]
result = odd(numbers)
print(result)

def max_num(values):
    a = 0
    for i in values:
        if i > a:
            a = i
    return a

numbers = [23, 5, 22, 44, 43, 55, 77, 324, 563, 75, 44, 66]
result = max_num(numbers)
print(result)

def find_minimum(numbers):
    if not numbers:
        return None  # Return None for an empty list

    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Example usage
numbers = [5, -3, 12, -8, -21, 43, -12]
min_value = find_minimum(numbers)
print(min_value)  # Output: -8
def two_list(a, b):
    lst = []
    for i in a and b:
        a[i] = lst.append(i)
        b[i] = lst.append(i)


numbers1 = [5, 3, 12, 8, 21, 43, 12]
numbers2 = [23, 5, 22, 44, 43, 55, 77, 324, 563, 75, 44, 66]
result = two_list(numbers1, numbers2)
print(result)


