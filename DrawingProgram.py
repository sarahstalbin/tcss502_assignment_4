"""
Minna Chae
Drawing Program
TCSS 502
"""
from shapes import Circle, Square, Triangle, Rectangle
from ShapeFactory import ShapeFactory


# class DrawingProgramMain:

"""creates a drawingProgram and adds shapes to it.
Sorts, add, replaces shapes
Add print statement to show how it is done
"""
class DrawingProgram:
    def __init__(self):
        # a constructor/init that can be passed a list of Shapes or nothing at all
        # self.list_string = None
        self.list_shapes = []
        self.size = 0 #do we need size if we can find the size via len(list_shapes)
        self.string = "" #string?

    def __str__(self):  # Correct output - I think it's working
        # __str__: returns a string representation of each of the shapes --
        # each shape will be separated from others by a newline (\n)
        formatted_list = [str(shape) for shape in self.list_shapes]
        return "\n".join(formatted_list) + "\n"


    def add_shape(self, shape_name):  #Correct output
        # Thoughts: is it better to sort in add_shape?
        # add_shape(Shape): a method that adds a Shape

        # self.list_shapes.append(ShapeFactory)
        # print(shape_name.get_name)

            # don't need if condition with updated Shape code
            # aShape = ShapeFactory.create_shape(shape_name, *args)

        self.list_shapes.append(shape_name)
        self.size += 1

    def remove_shape(self, shape_name):
        # remove_shape(Shape): a method that removes ALL shapes that match the one passed as a parameter --
        # it should return in integer value to signify how many of that shape was removed

        if len(self.list_shapes) == 0:
            return "There are no Shapes in the list"
        else:
            remove_shape_counter = 0
            for inList in self.list_shapes:
                if inList.get_name().lower() == shape_name.lower():
                    self.list_shapes.remove(inList)
                    remove_shape_counter += 1
                    self.size -= 1
        return remove_shape_counter

    def print_shape(self, shape_name):
        # print_shape(Shape): prints all shapes that match the type of the shape passed in
        if len(self.list_shapes) == 0:
            return "There are no Shapes in the list"
        else:
            string = ""
            for shape in self.list_shapes:
                if shape.get_name().lower() == shape_name.lower():
                    string += str(shape) + "\n"
        return string

    def sort_shapes(self):
        # sort_shapes(): sorts the list/collection of shapes -- you must use a sort that runs in O(nlogn)
        # for its worst case
        # shapes will be sorted first by name, then by area if names are same
        if len(self.list_shapes) == 0:
            return IndexError("There are no Shapes in the list")
        else:
            self.list_shapes.sort(key=lambda x: (x.name, x.area()))


    def get_shape(self, index): #Correct output
        # get_shape(index): returns the shape at the specified index
        if len(self.list_shapes) == 0:
            return "There are no Shapes in the list"
        elif index >= len(self.list_shapes) or index < 0 or len(self.list_shapes) == 0:
            raise IndexError
        else:
            return self.list_shapes[index]


    def set_shape(self, index, shape_name): #Correct output
        # set_shape(index, Shape): replaces the shape at the specified index
        if len(self.list_shapes) == 0:
            return "There are no Shapes in the list"
        elif index >= len(self.list_shapes) or index < 0 or len(self.list_shapes) == 0:
            raise IndexError
        else:
            # aShape = ShapeFactory.create_shape(shape_name, *args)
            self.list_shapes[index] = shape_name

    def clear_all_shapes(self):
        #clears all the shapes from the list
        if len(self.list_shapes) == 0:
            return "There are no Shapes in the list"
        else:
            del self.list_shapes[:]
            return f"The is is empty"


    def __iter__(self): #code taken from the text book
        if len(self.list_shapes) == 0:
            raise IndexError("There are no Shapes in the list")
        else:
            return DrawingProgramIterator(self.list_shapes)

class DrawingProgramIterator:
    # Write a DrawingProgramIterator class that provides the ability to iterate across the collection of shapes in
    # DrawingProgram using a for loop
    # See notes/slides on Iterator as well as book chapter "The Iterator Pattern" and the section "The Iterator Protocol"

    #code in __init__, __next__, and __iter__ were taken from the text book
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


dp = DrawingProgram()
shape = ShapeFactory.create_shape("Circle", 2)
dp.test_get_lower(shape)
# dp.add_shape(shape)