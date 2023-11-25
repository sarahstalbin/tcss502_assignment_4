"""
Minna Chae
Drawing Program
TCSS 502

"""

# from shapes import Shape
from abc import ABC, abstractmethod

class DrawingProgramMain:
    """creates a drawingProgram and adds shapes to it.
    Sorts, add, replaces shapes
    Add print statement to show how it is done
    """
class DrawingProgram(ABC):
    # @abstractmethod
    def get_name(self):
        pass
        # self.list_string

    def __init__(self):
        # a constructor/init that can be passed a list of Shapes or nothing at all
        self.list_shapes = []
        self.size = 0
        self.string = "" #string?

    def __str__(self):
        # __str__: returns a string representation of each of the shapes --
        # each shape will be separated from others by a newline (\n)
        # list = self.list_shapes
        # for shape in self.list_shapes:
        return self.get_name
        # return self.list_shapes

    def add_shape(self, shape):
        # add_shape(Shape): a method that adds a Shape
        # self.list_shapes.append(shape)
        self.list_shapes.push(shape)
        self.size +=1
        #is splice better?

    def remove_shape(self, shape):
        # remove_shape(Shape): a method that removes ALL shapes that match the one passed as a parameter -- it should return in integer value to signify how many of that shape was removed
        self.list_shapes.pop(shape)
        self.size -=1

    def print_shape(self, shape):
        # print_shape(Shape): prints all shapes that match the type of the shape passed in
        pass

    def sort_shapes(self):
        # sort_shapes(): sorts the list/collection of shapes -- you must use a sort that runs in O(nlogn) for its worst case
        # shapes will be sorted first by name, then by area if names are same
        pass

    def get_shape(self, index):
        # get_shape(index): returns the shape at the specified index
        return self.list_shapes(index)

    def set_shape(self, index, shape):
        # set_shape(index, Shape): replaces the shape at the specified index
        pass

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

