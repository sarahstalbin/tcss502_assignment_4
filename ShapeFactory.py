from shapes_with_docs import Circle
from shapes_with_docs import Square
from shapes_with_docs import Rectangle
from shapes_with_docs import Triangle


class ShapeFactory:
    """
    Creates and returns shape objects for DrawingProgram.
    """

    @staticmethod
    def create_shape(shape_name, **kwargs):
        """
        Creates a shape of a specified type using the relevant data for building that shape. Returns the shape.
        :param shape_name: name of the shape object to be created.
        :param kwargs: variable shape data required based on the type of shape to be created.
        :return: a Circle, Square, Rectangle, or Triangle object.
        """
        if shape_name == "circle":
            return Circle(shape_name, **kwargs)
        elif shape_name == "square":
            return Square(shape_name, **kwargs)
        elif shape_name == "rectangle":
            return Rectangle(shape_name, **kwargs)
        elif shape_name == "triangle":
            return Triangle(shape_name, **kwargs)
        raise AssertionError("Shape type is not valid.")


r = ShapeFactory.create_shape("rectangle", length=3, width=5)
s = ShapeFactory.create_shape("square", side=6)
t = ShapeFactory.create_shape("triangle", side1=2, side2=3, side3=5)
c = ShapeFactory.create_shape("circle", radius=5)

print(r.length)
print(s.side)
print(t.side2)
print(c.radius)

