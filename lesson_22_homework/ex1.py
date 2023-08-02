class Shape:
    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self.border_color = border_color

    def get_inner_color(self):
        return self._inner_color

    def set_inner_color(self, color):
        self._inner_color = color


class Circle(Shape):
    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self.width = width
        self.length = length


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.length = width

    def set_length(self, length):
        self.length = length
        self.width = length



shape = Shape("red", "black")
print(shape.get_inner_color())
shape.set_inner_color("blue")
print(shape.get_inner_color())


circle = Circle("green", "black", 5)
print("circle.radius is ", circle.radius)


rect = Rectangle("yellow", "black", 3, 4)
print("rect.width is ", rect.width)
print("rect.length ", rect.length)


sq = Square("purple", "black", 5, 8)
print("sq.width is ", sq.width)
print("sq.length is", sq.length)
sq.set_length(3)
print("sq.width is ", sq.width)
print("sq.length is", sq.length)
