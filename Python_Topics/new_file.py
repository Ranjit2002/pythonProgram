def cube(n):
    new = []
    for i in range(1, n):
        new.append(i * i * i)
    c = 0
    for j in new:
        c += j
    return c


# a = int(input("Enter a Number:-"))
# b = cube(a)
# print(b)

def not_same(list1):
    i = 0
    while i < len(list1) - 1:
        j = i + 1
        while j < len(list1):
            if list1[j] == list1[i]:
                return False
            j += 1
        i += 1
    return True


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if not_same(a):
#     print("Every element is different")
# else:
#     print("Same element found")

# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))

def add_element(list1):
    new = []
    c = 0
    i = 0
    while i < len(list1) - 1:
        if c + list1[i] == 10 and len(new) < 3:
            new.append(list1[i])
        i += 1
        return new


# a = [1, -6, 4, 2, -1, 2, 0, -2, 0]
# b = add_element(a)
# print(b)

# numbers = []
# for num in range(1000):
#   num=str(num).zfill(3)
# print(num)
# numbers.append(num)


string_words = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.

John Adams persuaded the committee to select Thomas Jefferson to compose the original
draft of the document, which Congress would edit to produce the final version.
The Declaration was ultimately a formal explanation of why Congress had voted on July
2 to declare independence from Great Britain, more than a year after the outbreak of
the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
Second Day of July 1776, will be the most memorable Epocha, in the History of America."
But Independence Day is actually celebrated on July 4, the date that the Declaration of
Independence was approved.

After ratifying the text on July 4, Congress issued the Declaration of Independence in
several forms. It was initially published as the printed Dunlap broadside that was widely
distributed and read to the public. The source copy used for this printing has been lost,
and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
popularly regarded as the official document. This engrossed copy was ordered by Congress on
July 19 and signed primarily on August 2.

The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''

# word_list = string_words.split()
#
# word_freq = [word_list.count(n) for n in word_list]
#
# print("String:\n {} \n".format(string_words))
# print("List:\n {} \n".format(str(word_list)))
# print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))


string = ('German Unity Day From Wikipedia, the free encyclopedia The Day of German Unity (German: Tag der '
          'DeutschenEinheit) is the national day of Germany, celebrated on 3 October as a public holiday. It '
          'commemorates the anniversary of German reunification in 1990, when the goal of a united Germany that '
          'originated in the middle of the 19th century, was fulfilled again. Therefore, the name addresses ' 
          'the re-union nor the union, but the unity of Germany. The Day of German Unity on 3 October has been the '
          'German national holiday since 1990, when the reunification was formally completed')

for i in string:
    pass


# Lambda functions

even = lambda x: x % 2 == 0
# print(even(2))
# print(even(3))

# Decorator
def decorate(fn):
    def new():
        print("Hey User")
        fn()
        print("Thanks for using this function")
    return new

@decorate
def hello():
    print("Hello World")


# hello()

# Generator
def generator():
    for j in range(1, 100+1):
        yield j


# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in generator():
#     print(i)

