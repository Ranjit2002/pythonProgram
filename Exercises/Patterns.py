"""
n = 7
for i in range(1, n+1):
    for b in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()

n = 7
o = 4

for i in range(n):
    for j in range(o):
        if i == 0 or i == 3 or j == 0:
            print("*", end=" ")
        elif i == 1 and j == 3 or i == 2 and j == 3:
            print("*", end=" ")
        elif i == 4 and j == 1 or i == 5 and j == 2 or i == 6 and j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("* * * * ")
print("*       *")
print("*       *")
print("* * * * ")
print("*   *")
print("*     *")
print("*       *")

n = 5
o = 100

for i in range(1, n+1):
    for j in range(1, o+1):
        if i == 1 and j in {1, 2, 3, 4, 5, 8, 9, 10} or i in {2, 3, 4, 5} and j == 3 or i in {1, 2, 3, 4, 5} and j in {7, 23, 27, 29, 34}\
                or i in {3, 5} and j in {8, 9, 10} or i in {3, 4, 5} and j in {12, 16} or i == 2 and j == 13 or i == 1 and j == 14\
                or i == 2 and j ==15 or i == 3 and j in {13, 14, 15, 24, 25, 26} or i in {2, 3, 4} and j == 18 or i in {1, 5} and j in {19, 20, 21}\
                or i in {1, 3, 5} and j in {30, 31, 32} or i in {1, 3} and j in {35, 36} or i in {2, 5} and j == 37 \
                or i == 4 and j == 36:
            print("*", end=" ")
        elif i in {1, 2, 3, 4, 5} and j in {1, 2, 4, 5, 6, 22, 28} or i in {2, 4} and j in {8, 9, 10, 11, 30, 31, 32, 33} or i in {1, 3, 5} and j in {11, 33}\
                or i == 2 and j == 12 or i == 1 and j in {12, 13} or i == 2 and j == 14 or i in {4, 5} and j in {13, 14, 15}\
                or i == 1 and j in {15, 16, 17} or i == 2 and j in {16, 17} or i in {3, 4, 5} and j == 17 or i in {1, 5} and j == 18\
                or i in {2, 3, 4} and j in {19, 20, 21, 22} or i in {1, 2, 4, 5} and j in {24, 25, 26} or i in {2, 5} and j in {35, 36}\
                or i == 4 and j == 35:
            print(" ", end=" ")
    print()


n = 10
for i in range(n):
    for b in range(i):
        print(" ", end=" ")
    for j in range(n-i+n-i-1):
        print(chr(65+j), end=" ")
    print()

n = int(input("Enter how many lines you want to print:-"))
i = n
for i in range(i):
    for b in range(n-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()
for i in range(n):
    for b in range(i):
        print(" ", end=" ")
    for j in range(n-i+n-i-1):
        print("*", end=" ")
    print()

n = 8

for i in range(1, n+1):
    for j in range(1, i):
        print(" ", end=" ")
    for p in range(2*n-i+1-i):
        print("*", end=" ")
    print()
for i in range(1, n+1):
    for b in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()

def pattern(num):
    k = num
    for i in range(k, 0, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i):
            print("*", end=" ")
        print("\r")
    n = k - 1
    for i in range(0, num):
        for j in range(n, 0, -1):
            print(end=" ")
        n = n - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        num += 1
        print("\r")


pattern(9)

n = 7
for i in range(1, n+1):
    for j in range(1, n-i+2):
        print(chr(64+j), end=" ")
    print()
print()

for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+j), end=" ")
    print()
"""

n = 7
for i in range(1, n+1):
    for j in range(1, 10):
        if i == 1 and j in {1, 2, 3} or i == 2 and j in {1, 2} or i == 3 and j == 1 or i == 5 and j == 1\
                or i == 6 and j in {1, 2} or i == 7 and j in {1, 2, 3} or i == 3 and j == 5\
                or i == 4 and j == 2 or i == 5 and j == 3:
            print(" ", end=" ")
        elif i == 1 and j == 4 or i == 2 and j == 3 or i == 3 and j == 4 or i == 4 and j == 1:
            print(chr(65), end=" ")
        elif i == 5 and j == 2 or i == 6 and j == 3 or i == 7 and j == 4:
            print(chr(61+i), end=" ")
        elif i == 3 and j == 6 or i == 4 and j == 3:
            print(chr(66), end=" ")
        elif i == 5 and j == 4:
            print(chr(67), end=" ")
    print()
