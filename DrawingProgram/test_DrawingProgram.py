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
from shapes import Shape, Circle, Rectangle, Triangle, Square


def dp_test():
    dp = DrawingProgram()
    dp.add_shape(Circle("Circle", 2))
    dp.add_shape(Circle("Circle", 5))
    dp.add_shape(Rectangle("Rectangle", 3,4))
    # print(dp.get_name(0))
    print(dp)
    # dp.set_shape(1,Triangle("Triangle", 1,2,3))
    # print(dp)
    # print(dp.get_shape(1))
dp_test()
