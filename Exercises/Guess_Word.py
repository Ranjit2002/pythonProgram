import random

string = ['America', 'Russia', 'China', 'India', 'France', 'England', 'Isreal',
          'Pakistan', 'Germany', 'Canada']

i = 3

for j in string:
    print(j, end=", ")

ch = random.choice(string)
low = ch.lower()

while True:
    if i == 0:
        print("Your chance has over")
        break
    print(f"\nYou have only {i} chance to guess the country name:\n")
    a = str(input("Enter country:-"))
    b = a.lower()
    if b == low:
        print("Congratulations! You guessed the correct country")
        break
    else:
        print("No...")
    i -= 1
