import random


class countries:
    string = str()
    country = ''
    list1 = list()

    @staticmethod
    def random_country():
        Asia = [
            "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
            "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan",
            "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal",
            "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore",
            "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor Leste", "Turkey",
            "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"
        ]

        copy = random.choice(Asia)
        a = copy.lower()
        return a

    @staticmethod
    def print_space(country):
        new_list = list()
        for i in country:
            if i != ' ':
                new_list.append("_")
            else:
                new_list.append(" ")
        new_str = "".join(new_list)
        return new_str

    @staticmethod
    def input_method(country, space):
        con_list = list(country)
        spa_list = list(space)
        con_str = "".join(con_list)

        try:
            while True:
                a = str(input("Guess word:-"))

                if len(a) > 1:
                    print("Please enter character or only one character!\n")
                    continue
                elif a in con_str:
                    occurrences = [i for i, letter in enumerate(con_list) if letter == a]

                    for ek in occurrences:
                        spa_list[ek] = a

                    new = " ".join(spa_list).upper()
                    print(new, "\n")  # Move this line outside the loop

                    if spa_list == con_list:
                        print("Congratulations!\nYou guessed the correct Country")
                        break

                else:
                    print("Incorrect guess! Try again\n")
        except Exception as ex:
            print(type(ex))
            print(ex)


# import pycountry
#
# all_countries = list(pycountry.countries)
# list1 = list()
#
# for country in all_countries:
#     list1.append(country.name)
#
# print(list1)


"""
    1. Make a method to choose a country
    2. Create a method to print len(country) space like ______
    3. After that create a method to take input and exception handling
"""

c = countries()

b = c.random_country()
d = c.print_space(b)
e = " ".join(d)
print(e)
c.input_method(b, d)
