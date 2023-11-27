import unittest
from shapes import Shape, Circle, Square, Rectangle, Triangle


class MyShapesTests(unittest.TestCase):
    """ Testing the shape class and its child classes"""
    def test_circle(self):
        circle = Circle("Circle", 4)  # Testing the area of the Circle class
        result = circle.area()
        self.assertEqual(result, 50.24)  # comparing the result(first) to the value(second)
        circle = Circle("Circle", 4)  # Testing the perimeter of the Circle class
        result = circle.perimeter()
        self.assertEqual(result, 25.12)  # assertEqual allows to compare the result with the value

    def test_square(self):
        square = Square("Square", 5)  # Testing the area of the Square class
        result = square.area()
        self.assertEqual(result, 25)
        square = Square("Square", 5)  # Testing the perimeter of the Square class
        result = square.perimeter()
        self.assertEqual(result, 20)

    def test_rectangle(self):
        rectangle = Rectangle("Rectangle", 4, 5)  # Testing the area of the Rectangle class
        result = rectangle.area()
        self.assertEqual(result, 20)
        rectangle = Rectangle("Rectangle", 4, 5)  # Testing the perimeter of the Rectangle class
        result = rectangle.perimeter()
        self.assertEqual(result, 18)

    def test_triangle(self):
        triangle = Triangle("Triangle", 3, 4, 5)  # Testing the area of the Triangle class
        result = triangle.area()
        self.assertEqual(result, 6.0)
        triangle = Triangle("Triangle", 3, 4, 5)  # Testing the perimeter of the Triangle class
        result = triangle.perimeter()
        self.assertEqual(result, 6.0)

    def test_circle_name(self):  # Testing the getter function of Shape class
        circle = Circle("Circle", 4)
        result = circle.get_name()
        self.assertEqual(result, "Circle")

    def test_square_name(self):
        square = Square("Square", 5)
        result = square.get_name()
        self.assertEqual(result, "Square")

    def test_rectangle_name(self):
        rectangle = Rectangle("Rectangle", 4, 5)
        result = rectangle.get_name()
        self.assertEqual(result, "Rectangle")

    def test_triangle_name(self):
        triangle = Triangle("Triangle", 3, 4, 5)
        result = triangle.get_name()
        self.assertEqual(result, "Triangle")


if __name__ == '__main__':
    unittest.main()
