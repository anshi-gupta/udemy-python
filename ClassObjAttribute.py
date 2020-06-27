
class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * self.pi           # Class objects can be called using self as well as the name of the class

    def circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(5)
print(my_circle.circumference())
print(my_circle.area)
