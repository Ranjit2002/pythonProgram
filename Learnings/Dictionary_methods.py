ep1 = {122: 34, 234: 45, 23: 76}
ep2 = {333: 85, 555: 77}

# print(ep1)
# ep1.clear()   # This will clear all the elements of ep1
# ep1.update(ep2)  # This method will add both dictionary elements together
# ep1.pop(122)  # This method will remove the entered element
# ep1.popitem()   # This method is used to remove the last element and their value
# del ep1[122]    # This method is used to delete the specific element

print(ep1)

x = ('key1', 'key2', 'key3')
y = 0
dict1 = dict.fromkeys(x, y)     # This method will set all key value to 0
print(dict1)

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
