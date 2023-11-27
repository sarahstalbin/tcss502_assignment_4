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
from shapes_with_docs import Shape, Circle, Rectangle, Triangle, Square

# Test for call via Shapes
def dp_test():
    dp = DrawingProgram()

    #add Shape
    dp.add_shape(Circle("Circle", 2))
    # print(dp)
    dp.add_shape(Rectangle("Rectangle", 3, 4))
    dp.add_shape(Triangle("Triangle", 2, 4, 3))
    dp.add_shape(Square("Square", 3))
    dp.add_shape(Square("Triangle", 3))
    dp.add_shape(Circle("Circle", 5))
    dp.add_shape(Square("Square", 2))
    # print(dp.get_name(0))
    # print(dp)

    #remove Shape
    # print(f"this is remove_shape {dp.remove_shape("Circle")}")
    # print(dp)

    #Set Shape
    # dp.set_shape(1,Triangle("Triangle", 1,2,3))

    #print shape
    # print(dp.print_shape("Triangle"))

    #sort Shape
    # dp.sort_shapes()
    # print(dp)

    #iter
    for shape in dp:
        print(shape)
dp_test()

#Test for Call via ShapeFactory

# d = DrawingProgram()
# d.add_shape(ShapeFactory.create_shape("rectangle", length = 5, width=6))
# d.add_shape(ShapeFactory.create_shape("circle", radius = 5))
# print(d)


# creating each shape's array to "sort" them
# list_rec = []
# list_sq = []
# list_cir = []
# list_tri = []
# # print(self.name)
#
# #looping through list and placing Shape objects into their specific array
# for shape in self.list_shapes:
#     if shape.get_name() == "Circle":
#         list_cir.append(shape)
#     if shape.get_name() == "Rectangle":
#         list_rec.append(shape)
#     if shape.get_name() == "Square":
#         list_sq.append(shape)
#     if shape.get_name() == "Triangle":
#         list_tri.append(shape)
#
# #looping through the arrays to put into a string. Need more conditions
# #to check for empty arrays. This code will probably not be the final code
# for shape in list_cir:
#     self.string += str(shape) + ", "
# self.string += "\n"
# for shape in list_rec:
#     self.string += str(shape) + ", "
# for shape in list_sq:
#     self.string += str(shape) + ", "
# self.string += "\n"
# for shape in list_tri:
#     self.string += str(shape) + ", "
# self.string += "\n"
# return f"{self.string}"