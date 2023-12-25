import time


def usingWhile():
    i = 1
    while i <= 50000:
        print(i)
        i += 1


def usingFor():
    for i in range(1, 50001):
        print(i)


# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print()
# print(time.time() - init)
# print(t1)

print(time.strftime("%Y/%m/%d  - %H:%M:%S"))
