"""
x = 4           # This is a global variable
print(x)

def hello():
    x = 5                               # This is the local variable it is accessible within the function
    y = 1
    print(f"The local x is {x}")
    print("Hello Ranjit")


print(f"The global x is {x}")
hello()
x = 5
print(f"The global x is {x}")
"""

x = 10              # This is the global variable

def myfunction():
    global x        # Declaring x
    x = 5           # Changing the value of global variable x
    y = 5           # This is the local variable
    print(y)


myfunction()
print(x)
