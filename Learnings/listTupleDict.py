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
'''

'''
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
'''


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
