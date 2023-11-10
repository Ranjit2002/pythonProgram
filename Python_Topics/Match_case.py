"""
import os
os.system("python --version")
"""

x = int(input("Enter a Number:- "))

match x:            # This is like switch case of java, but we don't have to use break statement here
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 5:
        print("x is 5")
    case _ if x != 30:
        print(x, "is not 30")
    case _ if x != 50:
        print(x, "is not 50")
    case _ if x % 2 == 0:
        print(x, "is an even number")
    case _:                            # _ means anything
        print(x)


