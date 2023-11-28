"""
Minna Chae
Drawing Factory
11.25.23
"""
"""
This test case imports from shapes (aqueno's code) and Drawing Program 
to run the test cases. 
This is done instead of coding within Drawing Program to preserve debugging code
"""


from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
from shapes import Shape, Circle, Rectangle, Triangle, Square
import unittest

#o	make sure you demonstrate all required methods behave properly
# o	make sure you show edge cases for those methods as necessary (e.g.
# sort operates on empty list of shapes,
# •	DrawingProgram class functionality for sorting:
    # 1 shape,
    # multiple shapes ascending order,
    # multiple shapes descending order,
    # multiple shapes random order)

# Test for call via Shapes
class MyDrawingProgramTest(unittest.TestCase):
    def test_add_Shape(self):
        print("(___________________________Testing DrawingProgram class_________________________________________)")
        # print("---------------Testing add_shapes function---------------")
        program = DrawingProgram()
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        # circle_add = ShapeFactory.create_shape("Circle", 4)
        # triangle_add = ShapeFactory.create_shape("Triangle", 2, 4, 3)
        # square_add = ShapeFactory.create_shape("Square", 3)
        program.add_shape(rectangle_add)
        # program.add_shape(circle_add)
        # program.add_shape(triangle_add)
        # program.add_shape(square_add)
        self.assertIn(rectangle_add, program)

    def test_remove_shape(self):
        # self.program = DrawingProgram()
        # print("---------------Testing remove_shapes function---------------")
        program = DrawingProgram()

        #creating Shapes
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        # circle_add = ShapeFactory.create_shape("Circle", 4)
        # triangle_add = ShapeFactory.create_shape("Triangle", 2, 4, 3)
        # square_add = ShapeFactory.create_shape("Square", 3)

        #Add Shapes
        program.add_shape(rectangle_add)
        # program.add_shape(circle_add)
        # program.add_shape(triangle_add)
        # program.add_shape(square_add)

        #Removing Shapes
        remove_count = program.remove_shape("Rectangle")
        # program.remove_shape(circle_add)
        # program.remove_shape(triangle_add)
        # program.remove_shape(square_add)

        self.assertEqual(remove_count, 1)

    def test_sort_one_shape(self):
        # sorting 1 shape
        # print("---------------Testing sort_shapes one shape---------------")
        program = DrawingProgram()

        #creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)
        #Add Shapes
        program.add_shape(circle_one)
        program.add_shape(circle_two)
        program.add_shape(rectangle_one)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(square_two)
        program.add_shape(triangle_one)
        program.add_shape(triangle_two)


        #sort shape
        program.sort_shapes()




    def test_sort_shapes_asce(self):
        print("---------------Testing sort_shapes multiple ascending shape---------------")

        # multiple shapes ascending order
        #creating Shapes
        program = DrawingProgram()
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        #Add Shapes
        program.add_shape(rectangle_add)


    def test_sort_shapes_desc(self):
        # print("---------------Testing sort_shapes multiple descending shape---------------")
        # multiple shapes descending order,
        pass


    def test_sort_shapes_random(self):
        # print("---------------Testing sort_shapes multiple random shape---------------")
        # multiple shapes random order
        pass
    def test_print_shapes(self):
        pass
    def test_get_shape(self):
        pass
    def test_set_shape(self):
        pass


class MyDrawingProgramIteratorTest(unittest.TestCase):
# •	DrawingProgramIterator class functionality
# o	use of for loop as shown above demonstrates this class works
# o	be sure and use it with a DrawingProgram object that has no shapes, one shape, then maybe 5 shapes

    def test_iter_with_many_shapes(self):
        # many shapes
        print("(___________________________Testing iter class_________________________________________)")
        print("---------------Testing iter class for many shapes---------------")
        program = DrawingProgram()
        circle_small = ShapeFactory.create_shape("Circle", 1)
        circle_large = ShapeFactory.create_shape("Circle", 5)
        square_small = ShapeFactory.create_shape("Square", 1)
        square_large = ShapeFactory.create_shape("Square", 5)
        rectangle = ShapeFactory.create_shape("Rectangle", 2, 3)
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)

        program.add_shape(circle_small)
        program.add_shape(circle_large)
        program.add_shape(square_small)
        program.add_shape(square_large)
        program.add_shape(rectangle)
        program.add_shape(triangle)
        for shape in program:
            print(shape)

    def test_iter_without_shapes(self):
        #Tests the iter function with no shapes where inter returns an IndexError
        print("---------------Testing iter class for no shapes---------------")
        program = DrawingProgram()
        with self.assertRaises(IndexError):
            for shape in program:
                print(shape)

    def test_iter_one_shape(self):
        #Tests the iter one shape
        print("---------------Testing iter class for one shape---------------")
        program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1)
        program.add_shape(circle_one)
        for shape in program:
            print(shape)


#
# def dp_test():
    #
    #
    #     dp = DrawingProgram()
    #
    #     #add Shape
    #     dp.add_shape(Circle("Circle", 2))
    #     # print(dp)
    #     dp.add_shape(Rectangle("Rectangle", 3, 4))
    #     dp.add_shape(Triangle("Triangle", 2, 4, 3))
    #     dp.add_shape(Square("Square", 3))
    #     dp.add_shape(Square("Triangle", 3))
    #     dp.add_shape(Circle("Circle", 5))
    #     dp.add_shape(Square("Square", 2))
    #     # print(dp.get_name(0))
    #     print(dp)
    #
    #     # remove Shape
    #     print(f"this is remove_shape {dp.remove_shape(Circle("Circle", 2))}")
    #     print(dp)
    #
    #     #Set Shape
    #     # dp.set_shape(1,Triangle("Triangle", 1,2,3))
    #
    #     #print shape
    #     print(dp.print_shape(Triangle("Triangle", 2, 4, 3)))
    #
    #     #sort Shape
    #     # dp.sort_shapes()
    #     # print(dp)
    #


#Test for Call via ShapeFactory
if __name__ == '__main__':
    unittest.main()
