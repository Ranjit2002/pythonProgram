'''
print("Enter any number to perform calculation:")
print("1->Add")
print("2->Subtract")
print("3->Multiply")
print("4->Divide")

choice = input("Enter here:")

num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))

if choice == '1':
    print(num1,"+",num2,"=",(num1+num2))
elif choice == '2':
    print(num1,"-",num2,"=",(num1-num2))
elif choice == '3':
    print(num1, "×", num2, "=", (num1 * num2))
elif choice == '4':
    print(num1, "÷", num2, "=", (num1 / num2))
'''

# There are two type of type casting
# 1.Explicit = Explicit typecasting done by user
# 2.Implicit = Implicit typecasting done by python interpreter

# Explicit typeCasting
a = "45"
b = "7"
print(a, b)
print(int(a)+int(b))

string = "34"
num = 43
string_num = int(string) 
print(num+string_num)

# Implicit typeCasting
c = 2.4
d = 54
print(c+d)

print("Ranjit", 2, 5, sep='~', end="346")
print("Ranjit")



