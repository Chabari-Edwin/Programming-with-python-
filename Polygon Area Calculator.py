class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


# Example usage
rect = Rectangle(10, 5)
print(rect)
print("Area:", rect.get_area())
print("Perimeter:", rect.get_perimeter())
print("Diagonal:", rect.get_diagonal())
print(rect.get_picture())

sq = Square(9)
print(sq)
print("Area:", sq.get_area())
print("Perimeter:", sq.get_perimeter())
print("Diagonal:", sq.get_diagonal())
print(sq.get_picture())

rect.set_width(15)
rect.set_height(10)
print(rect)

sq.set_side(5)
print(sq)
sq.set_width(7)
print(sq)
sq.set_height(3)
print(sq)

rect = Rectangle(15, 10)
print("Amount inside:", rect.get_amount_inside(Square(5)))

rect = Rectangle(4, 8)
print("Amount inside:", rect.get_amount_inside(Rectangle(3, 6)))

rect = Rectangle(2, 3)
print("Amount inside:", rect.get_amount_inside(Rectangle(3, 6)))