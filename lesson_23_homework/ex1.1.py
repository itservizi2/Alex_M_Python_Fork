from dataclasses import dataclass


class Shape:
    def __init__(self, inner_color, border_color):
        self.inner_color = inner_color
        self.border_color = border_color

    def __eq__(self, other):
        return isinstance(other, self.__class__)


@dataclass
class Circle(Shape):
    radius: float = 0

    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circles together")
        return Circle(self.inner_color, self.border_color, self.radius + other.radius)

    def __sub__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only subtract Circles")
        radius = self.radius - other.radius
        return Circle(self.inner_color, self.border_color, max(0, radius))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Circle(self.inner_color, self.border_color, self.radius * other)
        raise TypeError("Can only multiply by number")


@dataclass
class Rectangle(Shape):
    width: float = 0
    length: float = 0

    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Can only add Rectangles together")
        return Rectangle(self.inner_color, self.border_color,
                         self.width + other.width, self.length + other.length)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Can only subtract Rectangles")
        width = max(0, self.width - other.width)
        length = max(0, self.length - other.length)
        return Rectangle(self.inner_color, self.border_color, width, length)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Rectangle(self.inner_color, self.border_color,
                             self.width * other, self.length * other)
        raise TypeError("Can only multiply by number")


# Verificari cu exemple

c1 = Circle("red", "black", 5)
c2 = Circle("blue", "black", 10)

print("c1.area ", c1.area)
print("c2.area ", c2.area)

print("c1 == c2", c1 == c2)
print(f"Conditia urmatoare  c1 == Circle('red', 'black', 5), is {c1 == Circle('red', 'black', 5)}")


c3 = c1 + c2
print("c3.radius ", c3.radius)
c4 = c2 - c1
print("c4.radius ", c4.radius)

c5 = c1 * 3
print("c5.radius", c5.radius)

r1 = Rectangle("red", "black", 10, 20)
r2 = Rectangle("blue", "black", 5, 10)

print("r1.area", r1.area)
print("r2.area", r2.area)

r3 = r1 + r2
print("r3.width, r3.length", r3.width, r3.length)

r4 = r1 - r2
print("r4.width, r4.length ", r4.width, r4.length)

r5 = r1 * 2
print("r5.width, r5.length", r5.width, r5.length)


