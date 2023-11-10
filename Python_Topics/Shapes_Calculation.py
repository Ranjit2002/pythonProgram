class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def surface_area(self):
        return self.side_length ** 2

# Create an instance of the Square class
side_length = 5
square = Square(side_length)

# Calculate and print the perimeter and surface area
print(f"Perimeter: {square.perimeter()}")
print(f"Surface Area: {square.surface_area()}")
