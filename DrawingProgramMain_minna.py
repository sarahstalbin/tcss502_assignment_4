from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
# from shapes_with_docs import Shape


class DrawingProgramMain(DrawingProgram):

    def run_program(self):

        # Create a drawing program
        drawing_program = DrawingProgram()

        # # Create Shape objects for the drawing_program
        # circle = ShapeFactory.create_shape("Circle", 4)
        # triangle = ShapeFactory.create_shape("Triangle", 6, 8, 9)
        # square = ShapeFactory.create_shape("Square", 4)
        # rectangle = ShapeFactory.create_shape("Rectangle", 5, 7)

        # Add shapes to the drawing program
        drawing_program.add_shape("Circle", 4)
        drawing_program.add_shape("Triangle", 6, 8, 9)
        drawing_program.add_shape("Square", 4)
        drawing_program.add_shape("Rectangle", 5, 7)

        # Print the original list
        print("Original List of Shapes:")  # NEED TO ADD A WAY TO PRINT THIS OUT
        print(drawing_program)

        # Sort the shapes
        drawing_program.sort_shapes()
        print('\nSorted List of Shapes:')
        print(drawing_program)

        # Create more shapes
        # circle2 = ShapeFactory.create_shape("Circle", 2)
        # triangle2 = ShapeFactory.create_shape("Triangle", 2, 3, 4)
        # square2 = ShapeFactory.create_shape("Square", 6)
        # rectangle2 = ShapeFactory.create_shape("Rectangle", 11, 9)

        # Add new shapes to the drawing program
        drawing_program.add_shape("Circle", 2)
        drawing_program.add_shape("Triangle", 2, 3, 4)
        drawing_program.add_shape("Square", 6)
        drawing_program.add_shape("Rectangle", 11, 9)

        print("\nUpdated List with New Shapes:")
        print(drawing_program)

        # Replace some shapes
        # Remove:
        drawing_program.remove_shape("Circle")
        print("\nUpdated List with Circle removed:")
        print(drawing_program)

        # Create more:
        triangle3 = ShapeFactory.create_shape("Triangle", 4, 7, 10)
        circle3 = ShapeFactory.create_shape("Circle", 9)

        # Add new shapes to replace the deleted ones:
        drawing_program.set_shape(2, triangle3)
        drawing_program.set_shape(3, circle3)

        print("\nUpdated List with Replacement Shapes:")
        print(drawing_program)

        # Sort the shapes again
        drawing_program.sort_shapes()
        print('\nSorted List of Shapes:')
        print(drawing_program)


# TESTS
my_fun_program = DrawingProgramMain()
my_fun_program.run_program()