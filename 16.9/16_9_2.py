class Rectangle:
    def __init__(self, x, y):
        self.width = x
        self.length = y

    def get_area(self):
        return self.width * self.length


rect = Rectangle(5, 10)
print(f"Прямоугольник с длинной {rect.length}, шириной {rect.width} и площадью {rect.get_area()}")