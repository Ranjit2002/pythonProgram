"""
a = 320
b = 653
print("A") if a > b else print("=") if a == b else print("B")
print(1) if a > b else print(2)     # else statement is necessary
print(1) if a > b else ""   # else statement is mandatory

c = 10 if a > b else 0
print(c)
"""

a = int(input("Enter a Number:-"))
print("Even") if a % 2 == 0 else print("Odd")
print(False) if a % 2 != 0 else print(True)
