from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area(), square_2.get_area())

circ_1 = Circle(1)
circ_2 = Circle(100)

print(circ_1.get_area(), circ_2.get_area(), Circle(10).get_area())


figures = [Circle(3), Square(5), rect_1, rect_2, square_1, square_2, circ_1, circ_2]

for figure in figures:
    if isinstance(figure,Square):
        print("Площадь квадрата:", figure.get_area())
    elif isinstance(figure,Circle):
        print(f"Площадь круга: {figure.get_area()}")
    else:
        print("Площадь прямоугольника:", figure.get_area())

