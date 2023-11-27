from shapes_with_docs import Circle, Square, Rectangle, Triangle


class ShapeFactory:
    """
    Creates and returns Shape objects for DrawingProgram. All shapes should be created via the ShapeFactory.

    Contains one method: create_shape(), which creates a Shape object of a specified type along with the relevant
    data for creating that Shape.
    """

    @staticmethod
    def create_shape(shape_name, *args):
        """
        Creates a Shape object of a specified type using the relevant data for building that Shape. Returns the Shape.
        :param shape_name: name of the shape object to be created.
        :param kwargs: variable shape data required based on the type of shape to be created.
        :return: a Circle, Square, Rectangle, or Triangle object.
        """
        if shape_name == "circle":
            return Circle(shape_name, *args)
        elif shape_name == "square":
            return Square(shape_name, *args)
        elif shape_name == "rectangle":
            return Rectangle(shape_name, *args)
        elif shape_name == "triangle":
            return Triangle(shape_name, *args)
        raise AssertionError("Shape type is not valid.")

