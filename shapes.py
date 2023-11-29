from abc import ABC, abstractmethod  # importing abstract base class


class Shape(ABC):  # ABC - abstract base class
    """ Creating a shape class which is an ABC class type. The methods in this class are: constructor,
    get_name, area(abstract method) and perimeter(abstract method), draw which prints the str method
    and a str method which has the string representation of get_name, area and perimeter"""

    def __init__(self, name):
        """  constructor for initialising name
          param : name """

        self.name = name

    def get_name(self):
        """  method to get name
        return: name"""

        return self.name

    @abstractmethod
    def area(self):
        """  abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """  abstract method for perimeter"""
        pass

    def draw(self):
        """ method to draw shapes which prints the str method"""
        print(self.__str__())

    def __str__(self):
        """  str method returns name, area and perimeter from the child classes"""
        return "{}, area: {}, perimeter: {}".format(self.get_name(), self.area(), self.perimeter())


class Circle(Shape):
    """ class Circle is a child class of Shape which gives the name of the class its area and perimeter """
    def __init__(self, radius):
        """ gets name from the Shape class
        param: radius"""
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """ overriding area method from shape class and calculating area of circle"""
        value_of_area = 3.141592653589793 * self.radius * self.radius
        return value_of_area

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of circle"""
        value_of_perimeter = 6.283185307179586 * self.radius
        return value_of_perimeter


class Rectangle(Shape):
    """ class Rectangle is a child class of Shape which gives the name of the class its area and perimeter"""
    def __init__(self, length, width):
        """  gets name from the Shape class
        param: length, width"""
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        """ overriding area method from shape class and calculating area of rectangle"""
        value_of_area = self.length * self.width
        return value_of_area

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of rectangle"""
        value_of_perimeter = 2 * (self.length + self.width)
        return value_of_perimeter


class Square(Shape):
    """ class Square is a child class of Shape which gives the name of the class its area and perimeter"""
    def __init__(self, side):
        """  gets name from the Shape class
                param: side"""
        super().__init__("Square")
        self.side = side

    def area(self):
        """ overriding area method from shape class and calculating area of square"""
        value_of_area = self.side * self.side
        return value_of_area

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of square"""
        value_of_perimeter = 4 * self.side
        return value_of_perimeter


class Triangle(Shape):
    """ class Triangle is a child class of Shape which gives the name of the class its area and perimeter"""
    def __init__(self, side1, side2, side3):
        """  gets name from the Shape class
                param: side1, side2, side3"""
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """ overriding area method from shape class and calculating area of triangle"""
        half_perimeter = self.perimeter() / 2
        return (half_perimeter * (half_perimeter - self.side1) * (half_perimeter - self.side2) * (
                half_perimeter - self.side3)) ** 0.5

    def perimeter(self):
        """  overriding perimeter method from shape class and calculating perimeter of triangle"""
        return self.side1 + self.side2 + self.side3


