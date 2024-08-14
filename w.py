class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# ساخت یک شیء از کلاس Rectangle با طول 10 و عرض 5
rectangle1 = Rectangle(10, 5)

# محاسبه و چاپ مساحت مستطیل
print(f"The area of the rectangle is: {rectangle1.area()}")

