"""
Take age or year of birth as an input from the user and tell them when they will turn 100 years old.
Don't use anytype of module like datetime or dateutils.
They can then optionally provide a year and your program must tell their age in that particular year

You should be handling all shorts of errors like:-

1. You are not born yet
2. You seem to be the oldest person alive
3. You can also handle any other error if possible
"""
class umar:
    def old(self):
        try:
            while True:
                global age
                age = int(input("Enter your age or birth year:-"))
                if 0 < age < 150:
                    print(f"Your age is: {age}\nYou will turn 100 at: {2023+100-age}")
                    if 0 < age < 18:
                        print("You are a child")
                        break
                    elif 18 < age < 30:
                        print("Your are a teenager")
                        break
                    elif 30 < age < 50:
                        print("You are a middle man")
                        break
                    elif 50 < age < 80:
                        print("You are a senior citizen")
                        break
                    elif 80 < age < 149:
                        print("You are too old now")
                        break
                    else:
                        print("You are the oldest living person on earth")
                        break
                elif 1950 < age < 2023:
                    print(f"Your age is: {2023-age}\nYou will turn 100 at: {age+100}")
                    if age == 2005:
                        print("You are a child")
                        break
                    elif 1993 < age < 2005:
                        print('You are a teenager')
                        break
                    elif 1973 < age < 1993:
                        print("You are a middle man")
                        break
                    elif 1973 < age < 1943:
                        print("You are a senior citizen")
                        break
                    elif 1943 < age < 1874:
                        print("Now you are too old")
                        break
                    else:
                        print("You are the oldest living person on earth")
                        break
        except Exception as e:
            print(e)

    def optional(self):
        x = int(input("Enter a specific year to know your age in that year:"))
        if x < 2023:
            print("You are not born yet!")
        elif x > 2023:
            y = x - 2023 + age
            print(f"In the year {x}, you will be {y} years old")


a = umar()
a.old()
print()
a.optional()
