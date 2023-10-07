class encryption:
    @staticmethod
    def coding(string):
        new = []
        word = ''
        if len(string) == 0:
            return None
        for i in string:
            import random
            characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            ra_sq = ''.join(random.choice(characters) for _ in range(3))
            if i == ' ':
                if len(word) <= 2:
                    new.append(word[::-1])
                    word = ''
                elif len(word) > 2:
                    c = word[0]
                    d = word[1:]
                    new_wd = ra_sq + d + c + 'Phx'
                    new.append(new_wd)
                    word = ''
                else:
                    new.append(word)
                    word = ''
            else:
                word += i
        g = word[1:]
        f = word[0]
        chr = "Qvy" + g + f + "tsH"
        new.append(chr)
        new_str = " ".join(new)     # " ".join() method is used to convert list in to string
        return new_str

    @staticmethod
    def decoding(code_string):
        list1 = list()
        word = ''
        if len(code_string) == 0:
            return None
        for i in code_string:
            if i == ' ':
                if len(word) <= 2:
                    new_wd = word[::-1]
                    list1.append(new_wd)
                    word = ''
                elif len(word) > 2:
                    c = word[3:-3]
                    b = c[:-1]
                    d = c[-1]
                    f = d + b
                    list1.append(f)
                    word = ''
            else:
                word += i
        s = word[3:-3]
        t = s[:-1]
        u = s[-1]
        v = u + t
        list1.append(v)
        new_str = " ".join(list1)
        return new_str


e = encryption()
while True:
    print("1 --> Code\n2 --> Decode\n3 --> Exit")
    a = int(input("Enter your choice:-"))
    if a < 0 or a > 3:
        print("Please enter proper number\n")
        continue
    elif a == 1:
        coding = str(input("Enter string to code:-"))
        b = e.coding(coding)
        print(f"Coded String: {b}")
        print()
    elif a == 2:
        cd = str(input("Enter string to decode:-"))
        d = e.decoding(cd)
        print(f"Decoded String:- {d}")
        print()
    elif a == 3:
        break



"""
Write a python program to translate a message into secret code language. Use the rules below
to translate normal english into secret code

Coding :-
If: the word contains at least 3 characters, remove the first letters and append it at the end
    now append three random characters at the starting and the end
else:
    simply reverse the string

Decoding :-
If: the word contains less than 3 characters, reverse it
else:
    remove 3 random characters from start and end. Now remove the last letter and append to the beginning

Your program should ask whether you want to code or decode
"""
