'''
names = "Ranjit Vishwakarma"
print(len(names))
print(names[0:6])
'

fruit = "Mango"
print(len(fruit))
print(fruit[0:4]) # Prints from 0-4
print(fruit[1:4]) # Prints from 1-4
print(fruit[:4]) # Prints from 0-4
print(fruit[:]) # Prints the whole string
print(fruit[:-3]) # print(fruit[0:-3]) this will print len of fruit -3
print(fruit[0:len(fruit)-3]) # This will print the same thing as the above method
print(fruit[-1:len(fruit)-3]) #
print(fruit[-3:-1]) # It will print fruit.len -3 upto fruit.len -1 means 2:4

nm = "Harry"
print(nm[-4:-2])  # 1:3
print(nm[1:3])


a = "!!!Harry !!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip('!'))  # rstrip() methods removes any symbol from the string but not removes any symbol before character
print(a.replace("Harry", "Elon"))  # This method will change all the harry with Elon
print(a.split(" "))  # It will convert the whole String with list, they are seperate with spaces
b = "introduction to pYTHon"
print(b.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))  # This will add 25 more spaces at the beginning of the String
print(a.count("Harry"))  # This will return how many times Harry comes in String a
print(str1.endswith("!!!"))  # This will return true if str1 last 3 digits is !!!
print(str1.endswith("to", 4, 10))  # This will check that from index 4 to 10 "to" is coming or not
'''

# str1 = "He's name is Dan. He is an honest man"
# print(str1.find("is"))  # This will return the index of "is" if "is" was not there in the String it will return -1
# print(str1.index("Dan"))  # If Dan was not there in the String it will return error if it is there it will return the index
# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())  # If str1 is an AlphaNumeric string then it will return true otherwise false
# str1 = "Welcome"
# print(str1.isalpha())  # If str1 have any numbers inside it then it will return false otherwise true
#
# str1 = "hello world"
# print(str1.islower())
#
# str1 = "My name is Ranjit \n"
# print(str1.isprintable())  # If all the characters are printable then it will return true is some cases false when \n is there in the string
#
# str1 = "    "
# print(str1.isspace())  # It will return true if str1 have wide spaces like using tab button otherwise not and if the string was empty
#
# str1 = "World Health Organisation"
# print(str1.istitle())  # If every word first letter is capital then it will return true otherwise false
#
# str1 = "I am Ranjit"
# print(str1.istitle())  # Like this
#
# str1 = "Python is a Interpreted language"
# print(str1.startswith("Python"))
#
# str1 = "My name is RANjit"
# print(str1.swapcase())  # It changes the uppercase ot lowercase and lowercase to uppercase
#
# str2 = "His name is Dan. He is an honest man"
# print(str2.title())  # It will convert all words first letter into capital


# import random
#
# # Define the set of characters you want to choose from
# characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#
# # Generate a random 3-character sequence
# random_sequence = ''.join(random.choice(characters) for _ in range(3))
#
# print(random_sequence)

# value = int(input("Enter a Number:-"))
# if value < 0:
#     raise ValueError("Input must be a non-negative number.")
# else:
#     print(value)

# words = ["Hello", "World", "Python"]
#
# result = '*'.join(words)
#
# print(result)

# string = "Hello World"
#
# # Adding the word "beautiful" after the 6th character
# result = string[:6] + "r " + string[6:]
#
# print(result)
# import random
#
# a = ["America", "Russia", "China", "India"]
# rand = random.choice(a)
# print(rand)

# while True:
#     b = str(input("Enter a char:-"))
#     if b in rand:
#         print("Yes")
#         break
#     else:
#         print("No")


a = "Mango"
# print(len(a))
# print(a, "is a", len(a), "letter word")
# print(a[0:4])
# print(a[1:4])
# print(a[:4])
# print(a[:])
# print(a[:-3])
# print(a[:len(a)-3])
# print(a[-1:len(a)-3])
# print(a[-3:-1])     # 2:4

# m = "Harry"
# print(m[-4:-2])
#
# e = ["_1", "_2", "_3", "_4", "_5"]
# b = a.index('n')                        # This will return the index of n which is 3
# print(b)                                # This will print
# e.pop(b-1)                              # This will remove the element
# e.insert(b, 'n')                # This will insert the element
# print(e)                                # This will print e

# print(eval("2+4"))

b = (34, 556)
print(type(b))
