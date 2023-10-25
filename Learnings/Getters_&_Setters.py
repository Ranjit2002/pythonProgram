class Science:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property                           # Getter
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter                   # Setter
    def ten_value(self, New_value):
        self._value = New_value / 10


if __name__ == "__main__":
    a = Science(10)
    a.ten_value = 67
    print(a.ten_value)
    a.show()
