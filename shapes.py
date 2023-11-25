from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        print(self.__str__())

    def __str__(self):
        return "{}, area: {}, perimeter: {}".format(self.get_name(), self.area(), self.perimeter())


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        value_of_area = 3.14 * self.radius * self.radius
        return value_of_area

    def perimeter(self):
        value_of_perimeter = 6.28 * self.radius
        return value_of_perimeter


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        value_of_area = self.length * self.width
        return value_of_area

    def perimeter(self):
        value_of_perimeter = 2 * (self.length + self.width)
        return value_of_perimeter


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        value_of_area = self.side * self.side
        return value_of_area

    def perimeter(self):
        value_of_perimeter = 4 * self.side
        return value_of_perimeter


class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        perimeter = self.perimeter()
        return (perimeter * (perimeter - self.side1) * (perimeter - self.side2) * (perimeter - self.side3)) ** 0.5

    def perimeter(self):
        return (self.side1 + self.side2 + self.side3) / 2


c = Circle("Circle", 2)
r = Rectangle("Rectangle", 4, 5)
s = Square("Square", 5)
t = Triangle("Triangle", 3, 4, 5)
c.draw()
r.draw()
s.draw()
t.draw()
