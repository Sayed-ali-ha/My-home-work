class Student:
    def __init__(self, name, grade, age):
        self.__name = name  # ویژگی خصوصی برای نام
        self.__grade = grade  # ویژگی خصوصی برای درجه
        self.__age = age  # ویژگی خصوصی برای سن

    # متدهای عمومی برای دریافت مقادیر
    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_age(self):
        return self.__age

    # متدهای عمومی برای تنظیم مقادیر
    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    # متد برای نمایش جزئیات شاگرد
    def show_details(self):
        return f"Student Details:\nName: {self.__name}\nGrade: {self.__grade}\nAge: {self.__age}"

# مثال از استفاده
student = Student("Ali", "10th", 15)

# دریافت مقادیر
print(student.get_name())
print(student.get_grade())
print(student.get_age())

# تنظیم مقادیر جدید
student.set_name("Sara")
student.set_grade("11th")
student.set_age(16)

# نمایش جزئیات شاگرد
print("\nUpdated Student Details:")
print(student.show_details())


