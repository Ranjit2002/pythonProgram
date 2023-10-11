"""
a = input("Enter a Number:-")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("Invalid Input!")

print("End of program")
"""

# We can use multiple except block for different errors
try:
    num = int(input("Enter a integer:-"))
    a = [24, 67]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index error")
finally:
    print("I am a computer")
