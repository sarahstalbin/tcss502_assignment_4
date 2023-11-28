from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory


class DrawingProgramMain(DrawingProgram):

    def run_program(self):

        # Create a drawing program
        drawing_program = DrawingProgram()

        # Create Shape objects for the drawing_program
        circle = ShapeFactory.create_shape("Circle", 4)
        triangle = ShapeFactory.create_shape("Triangle", 6, 8, 9)
        square = ShapeFactory.create_shape("Square", 4)
        rectangle = ShapeFactory.create_shape("Rectangle", 5, 7)

        # Add shapes to the drawing program
        drawing_program.add_shape(circle)
        drawing_program.add_shape(triangle)
        drawing_program.add_shape(square)
        drawing_program.add_shape(rectangle)

        # Print the original list
        print("Original List of Shapes:")  # NEED TO ADD A WAY TO PRINT THIS OUT
        print(drawing_program)

        # Sort the shapes
        drawing_program.sort_shapes()
        print('\nSorted List of Shapes:')
        print(drawing_program)

        # Create more shapes
        circle2 = ShapeFactory.create_shape("Circle", 2)
        triangle2 = ShapeFactory.create_shape("Triangle", 2, 3, 4)
        square2 = ShapeFactory.create_shape("Square", 6)
        rectangle2 = ShapeFactory.create_shape("Rectangle", 11, 9)

        # Add new shapes to the drawing program
        drawing_program.add_shape(circle2)
        drawing_program.add_shape(triangle2)
        drawing_program.add_shape(square2)
        drawing_program.add_shape(rectangle2)

        print("\nUpdated List with New Shapes:")
        print(drawing_program)

        # Replace some Shapes
        # Create new Shape objects:
        triangle3 = ShapeFactory.create_shape("Triangle", 4, 7, 10)
        circle3 = ShapeFactory.create_shape("Circle", 9)

        # Replace existing Shapes with the new Shapes
        drawing_program.set_shape(1, triangle3)
        drawing_program.set_shape(3, circle3)

        print("\nUpdated List with Replacement Shapes:")
        print(drawing_program)

        # Sort the shapes again
        drawing_program.sort_shapes()
        print('\nSorted List of Shapes:')
        print(drawing_program)
