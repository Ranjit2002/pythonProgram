def square(n):
    """Takes in a number n,returns the square of n"""  # This is docstring written just after the function name
    print(n ** 2)


# square(5)
# print(square.__doc__)

# PEP 8
# PEP 8 is a document that provides guidelines and best practices on how to write Python code.
# PEP stands for Python Enhancement Proposal

def cube(x):
    """Returns the cube of the input number"""
    print(x*x*x)


# cube(13)
# print(cube.__doc__)

a = []
b = [2, 3, 4, 5]
c = 0
for i in range(len(b)):
    c += b[i]

print(c)
