"""
class get:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property                       # Getter
    def bell(self):
        return 10 * self._value

    @bell.setter                    # Setter
    def bell(self, new):
        self._value = new / 10


a = get(10)
a.bell = 67
print(a.bell)
a.show()
"""

class ten:
    def __init__(self, number):
        self.num = number

    def show(self):
        print(f"The number is {self.num}")

    @property
    def space(self):
        return self.num * 10

    @space.setter
    def space(self, new_num):
        self.num = new_num / 10


a = ten(5000)
a.space = 400
print(a.space)
a.show()
