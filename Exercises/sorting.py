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



