from dataclasses import dataclass


class ShapeService:
    DEFAULT_INNER_COLOR = "red"
    DEFAULT_BORDER_COLOR = "black"

    @staticmethod
    def create_default_circle(radius):
        return Circle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_BORDER_COLOR, radius)

    @staticmethod
    def create_default_rectangle(width, length):
        return Rectangle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_BORDER_COLOR, width, length)

    @staticmethod
    def create_default_square(side):
        return Rectangle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_BORDER_COLOR, side, side)

    @staticmethod
    def color_shapes(shapes, inner_color, border_color):
        for shape in shapes:
            shape.inner_color = inner_color
            shape.border_color = border_color


@dataclass
class Circle:
    inner_color: str
    border_color: str
    radius: float


@dataclass
class Rectangle:
    inner_color: str
    border_color: str
    width: float
    length: float

# verificam cum lucreaza
print("Creating a default circle with radius 5...")
circ = ShapeService.create_default_circle(5)

print("Creating a default rectangle with width 2 and length 4...")
rect = ShapeService.create_default_rectangle(2, 4)

print("Adding the circle and rectangle to a shapes list...")
shapes = [circ, rect]

print("Changing colors of all shapes to blue and yellow...")
ShapeService.color_shapes(shapes, "blue", "yellow")

print("Lucrul a fost facut! Created and colored shapes using ShapeService.")

