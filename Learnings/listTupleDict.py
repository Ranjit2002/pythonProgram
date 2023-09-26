'''
list1 = [4,7.5,[-4,8],["Apple","Mango"]]
print(list1)

tuple1 = (("Ranjit","Vishal"),("Lion","Tiger"))
print(tuple1)

dict1 = {"name":"Ranjit","Age":56,"CanVote":True}
print(dict1)

name = str(input("Enter your name:-"))
age = int(input("Enter your age:-"))


if(age>18):
    print("Name= ",name,"\nAge= ",age,"\nCanVote= ",True)
else:
    print("Name= ", name, "\nAge= ", age, "\nCanVote= ", False)

string = "Ranjit Vishwakarma"
print(string.upper())

list = [34,65,12,67]
list.append(94)
print(list.index(12))
list.insert(3,65)
print(list)
list.pop(4)
print(list)
list.remove(65)
# list.clear()
list.reverse()
print(list)


# var = set(["Ranjit","Sachin","Vishal"])
# print(var)
# var.add("lion")
# # print(var)
# # set.clear(var)
# set.discard()
# print(var)

a = ('a', 'b', 'c')
b = (1, 2, 3)
# c = {'a': 1, 'b': 2, 'c': 3}      # Make a and b like this

result = 0
if len(a) == len(b):
    result = dict(zip(a, b))
print(result)

# input tuple
inputTuple = ((5, "TutorialsPoint"), (6, "Python"), (7, "Codes"))
print("The input Tuple:", inputTuple)

# Here we are iterating through each element (pairs) of the tuple using dictionary comprehension and converting it to the dictionary
resultDictionary = dict((x, y) for x, y in inputTuple)
print(resultDictionary)
'''

# a = {'a': 23, 1: "python", 'b': 36, 2: "interpreter", 'c': "Java", 3: 456}

# for key, value in a.items():
#     if isinstance(key, str):
#         print(f"Key: {key}, Value: {value}")

# for key, value in a.items():
#     if isinstance(key, int):
#         print(f"{key}:{value}")

# a = {'a': [33, 44, 55], 'b': [53, 67, 76], 'c': [42, 87, 99]}
# max_values = {}

# for key, value in a.items():
#     max_values[key] = max(value)
# print(max_values)

# d = {1: 23, 2: 33, 3: 97, 4: 56}
# max_value = max(d.values())
# for key, values in d.items():
#     if values == max_value:
#         print(f"{key}:{values}")

# b = [22, 43, 56, 78]
# c = 0
# for i in b:
#     c += i
# print(c)

# d = (23, 45, 78, 56)
# c = 0
# for i in d:
#     c += i
# print(c)

# d = {23, 45, 78, 56}
# c = 0
# for i in d:
#     c += i
# print(c)

# a = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
# c = 0
# for i in a.values():
#     c += i
# print(c)

# a = int(input("Enter a number:-"))
# b = [23, 65, 78, 90, 45]
# new = []
# for i in b:
#     if i > a:
#         new.append(True)
#     else:
#         new.append(False)
#
# c = d = 0
# for i in new:
#     if i == True:
#         c += 1
#     else:
#         d += 1
#
# if c > d:
#     print(True)
# else:
#     print(False)


# num = [2, 3, 4, 5]
# print()
# print(all(x > 1 for x in num))
# print(all(x > 4 for x in num))
# print()

# s = "My name is Ranjit And I live in America"
# low = s.lower()
# a = str(input("Enter the letter to count:-"))
# b = a.lower()
# # c = s.count(a)    # We can simply use this method also
# # print(c)
# c = 0
# for i in low:
#     if i == b:
#         c += 1
# print(f"There are {c} letters of {b}")

# try:
#     a = str(input("Enter a character:-"))
#     print(ord(a))
# except:
#     print("Some error occurred!")

# a = int(input("Enter first number:-"))
# b = int(input("Enter second number:-"))
# print("\n%d+%d=%d" % (a, b, a+b))


a = {'a': 23, 1: "python", 'b': 36, 2: "interpreter", 'c': "Java", 3: 456}
v = 'AEIOUaeiou'
new = ''
for i, j in a.items():
    if type(j) == str:
        modified_string = ''
        for x in j:
            if x not in v:
                modified_string += x
        a[i] = modified_string
    else:
        new = j

print(a)

