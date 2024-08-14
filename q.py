import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# ساخت یک شیء از کلاس Circle با شعاع 5
circle1 = Circle(5)

# محاسبه و چاپ مساحت دایره
print(f"The area of the circle is: {circle1.area()}")

