class School:
    def __init__(self, name):
        self.__name = name  # ویژگی خصوصی برای نام مدرسه
        self.__students = []  # ویژگی خصوصی برای لیست شاگردان

    # متد عمومی برای دریافت نام مدرسه
    def get_name(self):
        return self.__name

    # متد عمومی برای تنظیم نام مدرسه
    def set_name(self, name):
        self.__name = name

    # متد برای اضافه کردن شاگرد به مدرسه
    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
            print(f"Student '{student}' added to the school '{self.__name}'.")
        else:
            print(f"Student '{student}' is already in the school '{self.__name}'.")

    # متد برای حذف شاگرد از مدرسه
    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            print(f"Student '{student}' removed from the school '{self.__name}'.")
        else:
            print(f"Student '{student}' not found in the school '{self.__name}'.")

    # متد برای نمایش تمامی شاگردان مدرسه
    def list_students(self):
        if self.__students:
            print(f"Students in '{self.__name}' school:")
            for student in self.__students:
                print(f"- {student}")
        else:
            print(f"The school '{self.__name}' has no students.")

# مثال از استفاده
my_school = School("Greenwood High")

# اضافه کردن شاگردان
my_school.add_student("Alice Johnson")
my_school.add_student("Bob Smith")
my_school.add_student("Charlie Brown")

# نمایش شاگردان مدرسه
my_school.list_students()

# حذف شاگرد
my_school.remove_student("Bob Smith")

# نمایش شاگردان باقی‌مانده
print("\nAfter Removing a Student:")
my_school.list_students()