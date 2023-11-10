import random as r

# randrange()
a = r.randrange(1, 10)  # integer
# print(a)

# random()
b = r.random()  # floating
# print(b)

# randint()
c = r.randint(2, 8)
# print(c)

# uniform()
d = r.uniform(20, 30)
# print(d)

# choice()
p = ["Python", "Java", "C++", "C#", "JS"]
e = r.choice(p)
# print(e)

# tuple()
t = (23, 45, 76, 89, 99)
h = r.choice(t)
# print(h)

# Shuffle method with list and tuple
r.shuffle(p)
# print(p)

a = list(t)
r.shuffle(a)
# print(a)

r.shuffle(t)
# print(t)            # TypeError: 'tuple' object does not support item assignment

