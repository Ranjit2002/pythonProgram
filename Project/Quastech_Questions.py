import math
import datetime
import json


class First_question:
    def area(self):
        while True:
            try:
                global radius
                radius = float(input("Enter radius of a circle:-"))
                print(f"\nArea of a circle whose radius is {radius} is {math.pi * (radius * radius):.2f}")
                break
            except Exception as ex:
                print(type(ex))
                print(ex, '\n')

    def perimeter(self):
        print(f"Perimeter of a circle whose radius is {radius} is {2 * math.pi * radius:.2f}")


a = First_question()
a.area()
a.perimeter()


class Second_question:
    def week(self):
        today = datetime.date.today()
        weeknumber = today.isocalendar()[1]
        print(f"The current week is {weeknumber}")


c = Second_question()
c.week()


class Third_question:
    def json(self):
        python_dict = {"name": "Elon", "age": 52, "city": "California"}
        json_data = json.dumps(python_dict)
        print(f"JSON Data:- {json_data}")


r = Third_question()
r.json()


class Fourth_question:
    def packing(self):
        return "SpaceX", "Elon Musk", 52


f = Fourth_question()
company, owner, age = f.packing()
print(f"Company:- {company}\nOwner:- {owner}\nAge:- {age}")


class Fifth_question:
    def count(self):
        up = dn = sp = 0
        while True:
            try:
                a = str(input("Enter a sentence:- "))
                for i in a:
                    if i == ' ':
                        sp += 1
                    elif i.isupper():
                        up += 1
                    else:
                        dn += 1
                print(f"Capital Letters:- {up}\nSmall Letters:- {dn}\nSpaces are:- {sp}")
                break
            except Exception as e:
                print(type(e))
                print(e, '\n')


h = Fifth_question()
h.count()


class Sixth_question:
    def sort(self):
        dict1 = {3: 1, 1: 3, 2: 4, 4: 2}
        items = list(dict1.items())
        n = len(dict1.items())
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][1] > items[j + 1][1]:
                    items[j], items[j + 1] = items[j + 1], items[j]

        sorted_dict = dict(items)
        print(f"Sorted dictionary:- {sorted_dict}")


s = Sixth_question()
s.sort()


class Seventh_question:
    def car(self):
        print("This is a Car function")

        def supercar():
            print("This is a Supercar function inside a car function")

        supercar()


e = Seventh_question()
e.car()


class Eighth_question:
    def merge_dict(self, dict1, dict2):
        d1 = dict1.copy()
        d1.update(dict2)
        print(d1)


i = Eighth_question()
dt1 = {'a': 1, 'b': 2}
dt2 = {'c': 3, 'd': 4}
i.merge_dict(dt1, dt2)


class Ninth_question:
    def square(self):
        list1 = [i for i in range(1, 11)]
        a = map(lambda x: x ** 2, list1)
        b = list(a)
        print(b)


n = Ninth_question()
n.square()


class Tenth_question:
    def add(self):
        list1 = [i for i in range(2, 14) if i % 2 != 0]
        list2 = [i for i in range(2, 14) if i % 2 == 0]
        a = map(lambda x, y: x + y, list1, list2)
        b = list(a)
        print(f"list1:- {list1}\nlist2:- {list2}\nAfter adding:- {b}")


t = Tenth_question()
t.add()
