# MAP
def cube(x):
    return x * x * x


# print(cube(2))

l = [2, 3, 4, 5, 6, 7]


# new = []                          # This is a one way to find cube
# for item in l:
#     new.append(cube(item))
# print(new)


# new = map(cube, l)          # This will return a map object
# print(new)

# Now convert it into your desired datatype

# new = list(map(cube, l))        # This is created by using map
# print(new)
new1 = list(map(lambda x: x*x*x, l))    # We can do like this also
print(new1)


# FILTER

def charm(a):
    return a > 3


# bell = filter(charm, l)       # This will also return a filter object
# print(bell)

# Now convert it into your desired datatype

bell = list(filter(charm, l))       # This is created by using filter, filter function returns true or false
print(bell)

# REDUCE

from functools import reduce

list1 = [1, 2, 3, 4, 5]


def sum(x, y):
    return x + y


# sum = reduce(sum, list1)
sum1 = reduce(lambda x, y: x + y, list1)

print(sum1)
