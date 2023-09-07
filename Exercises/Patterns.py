"""
n = 7
for i in range(1, n+1):
    for b in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()
"""

# n = 7
# o = 4

# for i in range(n):
#     for j in range(o):
#         if i == 0 or i == 3 or j == 0:
#             print("*", end=" ")
#         elif i == 1 and j == 3 or i == 2 and j == 3:
#             print("*", end=" ")
#         elif i == 4 and j == 1 or i == 5 and j == 2 or i == 6 and j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# print("* * * * ")
# print("*       *")
# print("*       *")
# print("* * * * ")
# print("*   *")
# print("*     *")
# print("*       *")

n = 7
o = 100

for i in range(1, n + 1):
    for j in range(1, o + 1):
        if (i == 1 and j in {1, 2, 3, 4, 5, 6, 7} or i in {1, 2, 3, 4, 5, 6, 7} and j in {4, 9, 34} or
                i in {1, 4, 7} and j in {10, 11, 12, 13, 14, 15} or i == 1 and j == 20 or i == 2 and j in {19, 21} or
                i == 3 and j in {18, 22} or i in {4, 5, 6, 7} and j == 17 or i == 4 and j in {18, 19, 20, 21, 22, 34, 35, 36, 37, 38, 39}
                or i in {4, 5, 6, 7} and j == 24 or i in {3, 4, 5} and j == 26 or i == 2 and j == 27 or
                i == 1 and j in {27, 28, 29, 30, 31} or i == 6 and j in {28, 34} or
                i == 7 and j in {28, 29, 30, 31, 32}):
            print("*", end=" ")
        elif (i in {1, 2, 3, 4, 5, 6, 7} and j in {1, 2, 3, 5, 6, 7, 8, 16} or i == 1 and j in {17, 18, 19, 21, 22, 23, 24} or
              i in {2, 3, 5, 6} and j in {10, 11, 12, 13, 14, 15} or i == 2 and j in {17, 18, 20, 22, 23, 24} or
              i == 3 and j in {17, 19, 20, 21, 23, 24} or i in {4, 5, 6, 7} and j in {18, 19, 20, 21, 22} or
              i in {4, 5, 6, 7} and j == 25 or i == 1 and j in {25, 26, 32} or i == 2 and j in {25, 27, 28, 29, 30, 31, 32, 33} or
              i == 6 and j in {27, 28, 29, 30, 31, 32, 33} or i == 7 and j in {26, 27, 32, 33} or i in {3, 4, 5} and j in {26, 27, 28, 29, 30, 31, 32, 33}):
            print(" ", end=" ")
    print()

# n = 10
# for i in range(n):
#     for b in range(i):
#         print(" ", end=" ")
#     for j in range(n-i+n-i-1):
#         print(chr(65+j), end=" ")
#     print()

# n = int(input("Enter how many lines you want to print:-"))
# i = n
# for i in range(i):
#     for b in range(n-i):
#         print(" ", end=" ")
#     for j in range(2*i-1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for b in range(i):
#         print(" ", end=" ")
#     for j in range(n-i+n-i-1):
#         print("*", end=" ")
#     print()
