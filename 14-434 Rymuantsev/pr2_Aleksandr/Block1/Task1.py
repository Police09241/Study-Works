import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other):
        # sqrt((x2-x1)^2 + (y2-y1)^2)
        return math.sqrt ((other.x - self.x)**2 + (other.y - self.y)**2)

    def __str__(self):
        return f"Point({self.x}; {self.y})"

point1 = Point(2, 3)
point2 = Point(5, 7)

print(point1)
print(point2)

distance = (point1.distance_to(point2))
print(distance)

