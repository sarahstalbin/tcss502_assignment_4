"""
Minna Chae
Drawing Factory
11.25.23
"""
"""
This test case imports from shapes and Drawing Program 
to run the test cases. 
This is done instead of coding within Drawing Program to preserve debugging code
"""


from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
import unittest


class MyDrawingProgramTest(unittest.TestCase):
    def test_add_Shape(self):
        # print("(___________________________Testing DrawingProgram class_________________________________________)")
        # print("---------------Testing add_shapes function---------------")
        program = DrawingProgram()
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        program.add_shape(rectangle_add)
        self.assertIn(rectangle_add, program)

    def test_remove_shape(self):
        # print("---------------Testing remove_shapes function---------------")
        program = DrawingProgram()
        #creating Shapes
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_add = ShapeFactory.create_shape("Circle", 1)
        #Add Shapes
        program.add_shape(rectangle_add)
        program.add_shape(circle_add)
        #Removing Shapes
        remove_count = program.remove_shape("Rectangle")
        #check if rectangle is not in program
        self.assertNotIn(rectangle_add, program)
        self.assertEqual(remove_count, 1)

    def test_sort_empty_list(self):
        program = DrawingProgram()
        with self.assertRaises(IndexError):
            for shape in program:
                print(shape)

    def test_sort_one_shape(self):
        # sorting 1 shape
        # print("---------------Testing sort_shapes one shape---------------")
        #creating Shapes
        program = DrawingProgram()
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        #Add Shapes
        program.add_shape(rectangle_add)
        self.assertIn(rectangle_add, program)


    def test_sort_shapes_asce(self):
        # print("---------------Testing sort_shapes multiple ascending shape---------------")

        # multiple shapes ascending order
        #creating Shapes
        program = DrawingProgram()
        # creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)
        # Add Shapes
        program.add_shape(circle_one)
        program.add_shape(circle_two)
        program.add_shape(rectangle_one)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(square_two)
        program.add_shape(triangle_one)
        program.add_shape(triangle_two)

        expected_order = [circle_one, circle_two, rectangle_one, rectangle_two, square_one,
                          square_two, triangle_one, triangle_two]
        # stringShape = [str(shape) for shape in expected_order]
        # "\n".join(stringShape) + "\n"
        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        # sort shape
        program.sort_shapes()
        self.assertEqual(program.__str__(), expected_string)

    def test_sort_shapes_desc(self):
        # print("---------------Testing sort_shapes multiple descending shape---------------")
        # multiple shapes descending order,
        program = DrawingProgram()
        # creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)

        # Add Shapes
        program.add_shape(circle_one)
        program.add_shape(circle_two)
        program.add_shape(rectangle_one)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(square_two)
        program.add_shape(triangle_one)
        program.add_shape(triangle_two)

        expected_order = [circle_one, circle_two, rectangle_one, rectangle_two, square_one,
                          square_two, triangle_one, triangle_two]

        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        # sort shape
        program.sort_shapes()
        self.assertEqual(program.__str__(), expected_string)


    def test_sort_shapes_random(self):
        # print("---------------Testing sort_shapes multiple random shape---------------")
        # multiple shapes random order
        program = DrawingProgram()
        # creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)

        # Add Shapes
        program.add_shape(rectangle_one)
        program.add_shape(square_two)
        program.add_shape(triangle_two)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(circle_two)
        program.add_shape(triangle_one)
        program.add_shape(circle_one)

        expected_order = [circle_one, circle_two, rectangle_one, rectangle_two, square_one,
                          square_two, triangle_one, triangle_two]

        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        # sort shape
        program.sort_shapes()
        self.assertEqual(program.__str__(), expected_string)

    def test_print_shapes(self):
        # print("---------------Testing print_shapes---------------")
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

        print_shape = program.print_shape("Circle")

        expected_string = str(circle_small) + "\n" + str(circle_large) + "\n"

        self.assertEqual(print_shape, expected_string)


    def test_get_shape(self):
        program = DrawingProgram()
        circle = ShapeFactory.create_shape("Circle", 1)
        program.add_shape(circle)

        get_shape = program.get_shape(0)
        self.assertEqual(get_shape, circle)

    def test_set_shape(self):
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

        adding_shape = ShapeFactory.create_shape("Triangle", 3,6,9)
        program.set_shape(0, adding_shape)

        expected_order = [adding_shape, circle_large, square_small, square_large, rectangle,
                          triangle]

        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        self.assertEqual(program.__str__(), expected_string)


class MyDrawingProgramIteratorTest(unittest.TestCase):
# •	DrawingProgramIterator class functionality
# o	use of for loop as shown above demonstrates this class works
# o	be sure and use it with a DrawingProgram object that has no shapes, one shape, then maybe 5 shapes

    def test_iter_with_many_shapes(self):
        # many shapes
        # print("(___________________________Testing iter class_________________________________________)")
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

        # it1 = program.__iter__()
        # self.assertRaises(StopIteration, shape)
        # with self.assertRaises(StopIteration):
        for shape in program:
            self.assertRaises(StopIteration)

    def test_iter_without_shapes(self):
        #Tests the iter function with no shapes where inter returns an IndexError
        # print("---------------Testing iter class for no shapes---------------")
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
        # for shape in program:
        #     print(shape)
        for shape in program:
            self.assertRaises(StopIteration)

#Test for Call via ShapeFactory
if __name__ == '__main__':
    unittest.main()
