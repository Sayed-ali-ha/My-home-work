python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# ساخت یک شیء از کلاس Person
person1 = Person("Ali", 30)

# چاپ ویژگی‌های شیء
person1.print_info()
