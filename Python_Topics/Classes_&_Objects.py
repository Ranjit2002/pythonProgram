class person:
    name = "Ranjit"
    occupation = "Software Developer"
    Networth = 500000

    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.Networth}")


a = person()
# a.name = "Elon"
# a.occupation = "Scientist"
# a.Networth = 1000000
# print(a.name)
# print(a.occupation)
# print(a.Networth)
a.info()

b = person()
b.name = "Elon Musk"
b.occupation = "Businessman"
b.Networth = 10000000
b.info()

c = person()
c.info()        # This will print the default values because I have not set any values yet
