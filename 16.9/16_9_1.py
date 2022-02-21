class Shapes:
    def att_to_string(self):
        name = self.__class__.__name__
        attributes = self.__dict__.values()
        return name + '(' + ', '.join(map(str, attributes)) + ')'


class Rectangle(Shapes):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Quadrilateral(Shapes):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4


class Circle(Shapes):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class Triangle(Shapes):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


rectangle = Rectangle(1, 2, 50, 100)# координаты начала и длины сторон
quadrilateral = Quadrilateral(0, 0, 0, 10, 10, 0, 10, 10)# координаты точек
circle = Circle(1, 2, 15)# координаты центра и радиус
triangle = Triangle(1, 2, -1, 2, 0, 0)# координаты точек

print(rectangle.att_to_string())
print(quadrilateral.att_to_string())
print(circle.att_to_string())
print(triangle.att_to_string())

