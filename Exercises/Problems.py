# a = int(input("Enter a Number:-"))
# print("Greater") if a > 10 else print("Lesser")
#
# even = lambda x: x % 2 == 0
# print(even(22))

# list1 = [23, 45, 66, 86, 98, 564, 345, 234]
# list2 = [i for i in list1 if i % 2 == 0]
# print(list2)


def string(a):
    new = []
    char = ""
    for i in range(len(a)):
        if a[i] != " ":
            char += a[i]
        elif a[i] == " ":
            new.append(char)
            char = ""
    # Append the last word after the loop
    new.append(char)
    return new


# def count(s):
#     new_list = list()
#     new = []
#     char = ""
#     spell = ""
#     for i in range(len(s)):
#         # count = 0
#         if s[i] != " ":
#             char += s[i]
#         elif s[i] == " ":
#             count = 0
#             for j in range(len(s)):
#                 if s[j] != " ":
#                     spell += s[j]
#                 elif s[j] == " ":
#                     if spell == char:
#                         count += 1
#                         spell = ""
#                     else:
#                         spell = ""
#             new_list.append((new.append(char), new.append(count)))
#             char = ""
#     print(new)

# def count(s):
#     words = s.split()  # Split the input string into a list of words
#     word_count = {}
#
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
#     result = [(word, count) for word, count in word_count.items()]
#     print(result)
#
#
# c = "United States Declaration of Independence From Wikipedia declaration the free united states encyclopedia independence"
#
# "The United States Declaration of Independence is the statement adopted by the Second Continental Congress meeting at the Pennsylvania State House Independence Hall in Philadelphia on July 4 1776 which announced that the thirteen American colonies then at war with the Kingdom of GreatBritain regarded themselves as thirteen independent sovereign states no longerunder British rule These states would found a new nation the United States of America"
#
# "John Adams was a leader in pushing for independence which was passed on July 2 with no opposing vote cast A committee of five had already drafted the formal declaration, to be ready when Congress voted on independence John Adams persuaded the committee to select Thomas Jefferson to compose the original draft of the document which Congress would edit to produce the final version. The Declaration was ultimately a formal explanation of why Congress had voted on July 2 to declare independence from great britian more than a year after the outbreak of the American Revolutionary War The next day Adams wrote to his wife Abigail The Second Day of July 1776 will be the most memorable Epocha in the History of America But Independence Day is actually celebrated on July 4 the date that the Declaration of Independence was approved After ratifying the text on July 4 Congress issued the Declaration of Independence in several forms It was initially published as the printed Dunlap broadside that was widely distributed and read to the public The source copy used for this printing has been lost and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft complete with changes made by John Adams and Benjamin Franklin and Jefferson's notes of changes made by Congress are preserved at the Library of Congress The best known version of the Declaration is a signed copy that is displayed at the National Archives in Washington D.C. and which is popularly regarded as the official document This engrossed copy was ordered by Congress on July 19 and signed primarily on August 2. The sources and interpretation of the Declaration have been the subject of much scholarly inquiry The Declaration justified the independence of the United States by listing colonial grievances against King George III and by asserting certain natural and legal rights including a right of revolution Having served its original purpose in announcing independence references to the text of the Declaration were few in the following years Abraham Lincoln made it the centerpiece of his rhetoric (as in the Gettysburg Address of 1863) and his policies Since then it has become a well-known statement on human rights particularly its second sentence We hold these truths to be self-evident that all men are created equal that they are endowed by their Creator with certain unalienable Rights that among these are Life Liberty and the pursuit of Happiness This has been called one of the best known sentences in the English language containing the most potent and consequential words in American history The passage came to represent a moral standard to which the United States should strive This view was notably promoted by Abraham Lincoln who considered the Declaration to be the foundation of his political philosophy and argued that it is a statement of principles through which the United States Constitution should be interpreted The U.S. Declaration of Independence inspired many other similar documents in other countries the first being the  1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands (modern-day Belgium) It also served as the primary model for numerous declarations of independence across Europe and Latin America as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the 19th century"

# e = c.lower()
# count(e)

# def permute(list1):
#     new_list = [[]]
#     for n in list1:
#