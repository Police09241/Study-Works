import math

class Shape:
    def __init__(self,name):
        self.name = name
    def area():
        return 0.0
    def __str__(self):
        return self.name
    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

figures = [Circle("Большой круг", 10), Rectangle("Квадрат", 5, 5), Rectangle("Прямоугольник", 6, 3), Circle("Малый круг", 4)]
sorted(figures, key=lambda f: f.area())

for fig in figures:
    print(f"площадь {fig} равна {fig.area()}")