# ==  Compares values
# is  Compares identity

# a = 4
# b = '4'

# print(a is b)     # False
# print(a == b)     # False

# c = [1, 2, 3]
# d = [1, 2, 3]

# print(c is d)   # False    Exact location of object in memory
# print(c == d)   # True     value

# e = 3
# f = 3

# print(e is f)   # True    this is immutable
# print(e == f)   # True    same thing

# a = "Ranjit"
# b = "Ranjit"

# print(a is b)   # True    because string is immutable
# print(a == b)   # True    same thing

# a = (1, 2)
# b = (1, 2)

# print(a is b)   # True      because tuple is immutable
# print(a == b)   # True      same thing

a = None
b = None

print(a is b)
print(a == b)

