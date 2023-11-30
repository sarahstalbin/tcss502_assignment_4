import unittest
from shapes import Circle, Square, Rectangle, Triangle


class TestShapes(unittest.TestCase):
    """ Testing the shape class and its child classes"""
    def test_circle_area_perimeter(self):
        """ Testing the area, perimeter and the get_name function of Circle class"""
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)
        self.assertAlmostEqual(circle.perimeter(), 31.41592653589793)
        self.assertEqual(circle.get_name(), "Circle")

    def test_square_area_perimeter(self):
        """ Testing the area, perimeter and the get_name function of Square class"""
        square = Square(4)
        self.assertEqual(square.area(), 16)
        self.assertEqual(square.perimeter(), 16)
        self.assertEqual(square.get_name(), "Square")

    def test_rectangle_area_perimeter(self):
        """ Testing the area, perimeter and the get_name function of Rectangle class"""
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.area(), 24)
        self.assertEqual(rectangle.perimeter(), 20)
        self.assertEqual(rectangle.get_name(), "Rectangle")

    def test_triangle_area_perimeter(self):
        """ Testing the area, perimeter and the get_name function of Triangle class"""
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)  # Testing the area of the Triangle class
        self.assertEqual(triangle.perimeter(), 12)  # Testing the perimeter of the Triangle class
        self.assertEqual(triangle.get_name(), "Triangle")  # Testing the getter function


if __name__ == '__main__':
    unittest.main()
