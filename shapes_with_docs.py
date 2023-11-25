from abc import ABC, abstractmethod  # importing abstract base class


class Shape(ABC):  # ABC - abstract base class

    def __init__(self, name):  # constructor for initialising name
        self.name = name

    def get_name(self):  # method to get name
        return self.name

    @abstractmethod
    def area(self):  # abstract method for area
        pass

    @abstractmethod
    def perimeter(self):  # abstract method for perimeter
        pass

    def draw(self):
        print(self.__str__())  # printing the str method in draw method

    def __str__(self):  # str method returns name, area and perimeter from the child classes
        return "{}, area: {}, perimeter: {}".format(self.get_name(), self.area(), self.perimeter())


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)  # getting name from the shape class
        self.radius = radius  # initialising radius parameter for circle class

    def area(self):  # overriding area method from shape class and calculating area of circle
        value_of_area = 3.14 * self.radius * self.radius
        return value_of_area

    def perimeter(self):  # overriding perimeter method from shape class and calculating perimeter of circle
        value_of_perimeter = 6.28 * self.radius
        return value_of_perimeter


class Rectangle(Shape):
    def __init__(self, name, length, width):  # initialising length and width parameter for rectangle class
        super().__init__(name)  # getting name from the shape class
        self.length = length
        self.width = width

    def area(self):  # overriding area method from shape class and calculating area of rectangle
        value_of_area = self.length * self.width
        return value_of_area

    def perimeter(self):  # overriding perimeter method from shape class and calculating perimeter of rectangle
        value_of_perimeter = 2 * (self.length + self.width)
        return value_of_perimeter


class Square(Shape):
    def __init__(self, name, side):  # initialising side parameter for square class
        super().__init__(name)
        self.side = side

    def area(self):  # overriding area method from shape class and calculating area of square
        value_of_area = self.side * self.side
        return value_of_area

    def perimeter(self):  # overriding perimeter method from shape class and calculating perimeter of square
        value_of_perimeter = 4 * self.side
        return value_of_perimeter


class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):  # initialising side1, side2, side3 parameter for triangle class
        super().__init__(name)   # getting name from the shape class
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):  # overriding area method from shape class and calculating area of triangle
        perimeter = self.perimeter()
        return (perimeter * (perimeter - self.side1) * (perimeter - self.side2) * (perimeter - self.side3)) ** 0.5

    def perimeter(self):  # overriding perimeter method from shape class and calculating perimeter of triangle
        return (self.side1 + self.side2 + self.side3) / 2


c = Circle("Circle", 4)
r = Rectangle("Rectangle", 4, 5)
s = Square("Square", 5)
t = Triangle("Triangle", 3, 4, 5)
c.draw()
r.draw()
s.draw()
t.draw()
