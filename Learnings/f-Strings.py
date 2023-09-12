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
