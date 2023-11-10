class Math:
    def __init__(self, num):
        self.num = num

    def numtoadd(self, n):
        self.num += n

    def show(self):
        print(f"The num is {self.num}")

    @staticmethod       # When you make a staticmethod you don't need to write self
    def add(x, y):      # You can use this method a.add() or Math.add()
        return x + y    # Math is a class name and a is a instance of class


a = Math(5)
print(a.num)
a.numtoadd(6)
print(a.num)
print(a.add(14, 7))
print(Math.add(14, 27))
Math.show(a)
# class name.method name(instance name)
