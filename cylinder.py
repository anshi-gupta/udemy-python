
class Cylinder():
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * (self.radius**2) * self.height 

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius**2 + 2 * Cylinder.pi * self.radius * self.height


c = Cylinder(10, 10)

print("The volume of cylinder is {}".format(c.volume()))
print("The surface area of cylinder is {}".format(c.surface_area()))