"""
Minna Chae
Drawing Program
TCSS 502
"""
from shapes import Shape, Circle, Rectangle, Triangle, Square


class DrawingProgramMain:

    """creates a drawingProgram and adds shapes to it.
    Sorts, add, replaces shapes
    Add print statement to show how it is done
    """
class DrawingProgram():
    def get_name(self, index):
        # print(f"this is get_name {self.list_shapes[index].get_name()}")
        return self.list_shapes[index].get_name()

    def __init__(self):
        # a constructor/init that can be passed a list of Shapes or nothing at all
        # self.list_string = None
        self.list_shapes = []
        self.size = 0
        self.string = "" #string?

    def __str__(self): #Correct output - I think it's working
        # __str__: returns a string representation of each of the shapes --
        # each shape will be separated from others by a newline (\n)
        list_rec = []
        list_sq = []
        list_cir = []
        list_tri = []
        # print(self.name)
        for shape in self.list_shapes:
            if shape.get_name() == "Circle":
                list_cir.append(shape)
            if shape.get_name() == "Rectangle":
                list_rec.append(shape)
            if shape.get_name() == "Square":
                list_sq.append(shape)
            if shape.get_name() == "Triangle":
                list_tri.append(shape)

        for shape in list_cir:
            self.string += str(shape) + ", "
        self.string += "\n"
        for shape in list_rec:
            self.string += str(shape) + ", "
        for shape in list_sq:
            self.string += str(shape) + ", "
        self.string += "\n"
        for shape in list_tri:
            self.string += str(shape) + ", "
        self.string += "\n"

        return f"{self.string}"


    def add_shape(self, Shape):  #Correct output
        # add_shape(Shape): a method that adds a Shape
        self.list_shapes.append(Shape)
        # print(f"in add_shape this is shape {Shape.get_name()}")
        # print(f"this is list in add_shape {self.list_shapes[0]}")
        # self.list_shapes.push(shape)
        self.size +=1
        #is splice better?

    def remove_shape(self, Shape):
        # remove_shape(Shape): a method that removes ALL shapes that match the one passed as a parameter --
        # it should return in integer value to signify how many of that shape was removed
        self.list_shapes.pop(Shape)
        self.size -=1

    def print_shape(self, shape):
        # print_shape(Shape): prints all shapes that match the type of the shape passed in
        pass

    def sort_shapes(self):
        # sort_shapes(): sorts the list/collection of shapes -- you must use a sort that runs in O(nlogn)
        # for its worst case
        # shapes will be sorted first by name, then by area if names are same
        pass

    def get_shape(self, index): #Correct output
        # get_shape(index): returns the shape at the specified index
        if index >= len(self.list_shapes) or index < 0 or len(self.list_shapes) == 0:
            raise ValueError("Index cannot be greater than the length of the list")
        else:
            return self.list_shapes[index]

    def set_shape(self, index, Shape): #Correct output
        # set_shape(index, Shape): replaces the shape at the specified index
        if index >= len(self.list_shapes) or index < 0 or len(self.list_shapes) == 0:
            raise ValueError("Index cannot be greater than the length of the list")
        else:
            self.list_shapes[index] = Shape


    def __iter__(self):
        return DrawingProgramIterator(self.list_shapes)

class DrawingProgramIterator:
    # Write a DrawingProgramIterator class that provides the ability to iterate across the collection of shapes in
    # DrawingProgram using a for loop
    # See notes/slides on Iterator as well as book chapter "The Iterator Pattern" and the section "The Iterator Protocol"
    def __init__(self, string):
        # self.words = [w.capitalize() for w in string.split()]
        # self.words = [w.capitalize() for i in string] #are we creating the string into an array?
        self.words = string
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self
    # Attributes(instance fields/data)
    # a list/collection of Shapes
        # any other behaviors you feel are necessary for the class
        # assuming drawing_program = DrawingProgram(), the following code should work
        # for shape in drawing_program:
        # print(shape)

