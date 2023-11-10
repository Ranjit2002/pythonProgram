a = str(input("Enter a Number between 5 to 10:-"))

if a == 'quit':
    print("This program has been quit")
elif int(a) < 5 or int(a) > 10:
    raise ValueError("Input must be greater than 4 or less than 11")
else:
    print(a)

