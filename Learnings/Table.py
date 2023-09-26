'''
def mul_table(num):
    for i in range(1,10+1):
        result=num*i
        print(num,"x",i,"=",(num*i))

tab = int(input("Enter a Number to print table:-"))
mul_table(tab)


num = int(input("Enter any Number to check the number is palindrome or not:-"))
print(num.bit_length())



# def Name(name):
#     print("Hello",name)
#
# name = str(input("Enter your name:-"))
# Name(name)

# x = input("Enter first Number:- ")
# y = input("Enter second Number:- ")
# print(int(x)+int(y))

name = "Ranjit vishwakarma"
friend = 'Vishal'
anotherfriend = 'Suraj'
print(name,friend,anotherfriend)

apple = """He said,
         I want to eat an apple
         and a grapes
         to"""
print(apple)
print(name)
print(name[0])

for ch in apple:
    print(ch)
'''


# def BMI(weight_kg,height_m):
#     bmi = weight_kg / height_m**2
#     return bmi
#
# weight = float(input("Enter your weight in kg:-"))
# height = float(input("Enter your height in meters:-"))
#
# bmi = BMI(weight,height)
# print("Your BMI index is:-",bmi)

# def calculate(weight, height):
#     val = height / 3.281
#     bmi = weight / (val**2)
#     return bmi
#
#
# kg = float(input("Enter your weight in Kg:- "))
# foot = float(input("Enter your height in foot:-"))
#
# convert = calculate(kg, foot)
# value = f"{convert:.2f}"
#
# print("Your BMI is: ", value)
"""

questions = ["When was Chandrayaan 3 launched?", "How much is the depth of kola superdeep borehole?",
             "Which one of these is the moon of mars?", "Titan is the moon of which planet?",
             "Which is the tallest statue in the world?", "Which is the biggest country in America?",
             "Which is the fastest object ever made by humans?"]

answers = [
    "14 july,2023\n12 july,2023\n15 july,2023\n16 july,2023",
    "11,112 meters\n11,034 meters\n12,110 meters\n12,262 meters",
    "Ceres\nPhobos\nEuropa\nGanymede",
    "Jupiter\nUranus\nSaturn\nNeptune",
    "Statue of Liberty\nStatue of unity\nStatue of Peace\nStatue of Love",
    "Canada\nUnited States\nBrazil\nMexico",
    "Voyager 1\nNew Horizons\nCassini\nParker solar probe"
]

prizes = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

options = [1, 4, 2, 3, 2, 1, 4]

score = 0

i = 0
while i < len(questions):
    print(questions[i])
    print(answers[i])
    a = int(input("Enter option no.: "))
    if options[i] == a:
        score += prizes[i]
        print("Correct!")
    else:
        print("Incorrect! Game Over.")
        break

    i += 1

print("Your final score:", score)
"""

# a = 'My name is ranjit'
# word = ''
# for i in range(len(a) -1, -1, -1):
#     if a[i] == ' ':
#         old = word[::-1]
#         print(old)
#         break
#     else:
#         word += a[i]

# for i in range(len(a)-1, -1, -1):
#     if a[i] == ' ':
#         print(a[i])
#         break
#     else:
#         print(a[i])

# r = 'ranjit'
# d = r[0]
# c = r[1:]

# f = 'gdf' + c + d + 'xzv'
# print(f)

# na = "My name is ranjit"
# letter = ''
# app = []
# for i in na:
#     if i == ' ':
#         app.append(letter)
#         letter = ''
#     elif i == len(na)-1:
#         app.append(letter)
#     else:
#         letter += i
#
# print(app)

# na = "My nate is ranjit"
# letter = ''
# app = []
#
# for i in na:
#     if i == ' ':
#         app.append(letter)
#         letter = ''
#     elif i == na[-1]:
#         letter += i
#         app.append(letter)
#     else:
#         letter += i
#
# print(app)

# na = "My nate is ranjit"
# letter = ''
# app = []
#
# for index, char in enumerate(na):
#     if char == ' ':
#         app.append(letter)
#         letter = ''
#     elif index == len(na) - 1:
#         letter += char
#         app.append(letter)
#     else:
#         letter += char
#     print(index)
#     print(char)

"""
Decoding :-
If: the word contains less than 3 characters, reverse it
else:
    remove 3 random characters from start and end. Now remove the last letter and append to the beginning

Your program should ask whether you want to code or decode
"""

def decoding(string):
    list1 = list()
    word = ''
    if len(string) == 0:
        return None
    for i in string:
        if i == ' ':
            if len(word) <= 2:
                new_wd = word[::-1]
                list1.append(new_wd)
                word = ''
            elif len(word) > 2:
                c = word[3:-3]
                b = c[:-1]
                d = c[-1]
                f = d + b
                list1.append(f)
                word = ''
        else:
            word += i
    s = word[3:-3]
    t = s[:-1]
    u = s[-1]
    v = u + t
    list1.append(v)
    new_str = " ".join(list1)
    print(new_str)


a = str(input("Enter a string:-"))
decoding(a)


# yM qEHamenPhx si qLRanjitrPhx WKTndaPhx I ma PQEromfPhx QvymericaAtsH     # Coded String

# a = 'dsganjitrsgh'
# c = a[3:-3]     # to remove 3 - 3 char from start and end
# b = c[:-1]      # to remove last char
# d = c[-1]       # to remove all char except last
# f = d + b       # concatenating string
# print(f)        # printing

