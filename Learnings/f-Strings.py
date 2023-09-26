"""
letter = "My name is {} and I am from {}"
name = "Ranjit"
country = "America"
a = letter.format(name, country)
print(a)

letter = "My name is {1} and I am from {0}"
name = "Ranjit"
country = "America"
a = letter.format(country, name)  # You can use this if you are giving first args country and second name
print(a)

about = f"My name is {name} and I am from {country}"  # Use f-sting this is most recommended method
name = "Ranjit"
country = "America"
print(about)

price = 49.09999
txt = f"for only {price:.2f} dollars"
print(txt)

print(f"{2 * 30}")

string = "32"
a = int(string)
print(type(a))
print(a)
"""

# a = "Python is an interpreted high level programming language"
# print(a[13:24])
# b = a.split()   # Converts a string into a list
# print(b[3])

p = "Python is Very easy Language"
s = c = 0
for i in p:
    if i.islower():
        s += 1
    elif i.isupper():
        c += 1

# print(f"Small Letters: {s}\nCapital Letters: {c}")

a = 'Python'
user = int(input("Enter a Number:-"))
list1 = list(a)
for i in list1:
    if user > len(list1):
        print("Please enter number less than 7")
        break
    else:
        list1.pop(user-1)
        pro = " , ".join(list1)
        print(pro)
        break

