برای ایجاد یک کلاس Team با ویژگی‌های خصوصی نام و اعضا و ارائه روش‌هایی برای اضافه کردن و حذف اعضا، می‌توانید از کد زیر استفاده کنید:

python
class Team:
    def __init__(self, name):
        self.__name = name  # ویژگی خصوصی برای نام تیم
        self.__members = []  # ویژگی خصوصی برای لیست اعضا

    # متد عمومی برای دریافت نام تیم
    def get_name(self):
        return self.__name

    # متد عمومی برای تنظیم نام تیم
    def set_name(self, name):
        self.__name = name

    # متد برای اضافه کردن عضو به تیم
    def add_member(self, member):
        if member not in self.__members:
            self.__members.append(member)
            print(f"Member '{member}' added to the team '{self.__name}'.")
        else:
            print(f"Member '{member}' is already in the team '{self.__name}'.")

    # متد برای حذف عضو از تیم
    def remove_member(self, member):
        if member in self.__members:
            self.__members.remove(member)
            print(f"Member '{member}' removed from the team '{self.__name}'.")
        else:
            print(f"Member '{member}' not found in the team '{self.__name}'.")

    # متد برای نمایش تمامی اعضای تیم
    def list_members(self):
        if self.__members:
            print(f"Members of '{self.__name}' team:")
            for member in self.__members:
                print(f"- {member}")
        else:
            print(f"The team '{self.__name}' has no members.")

# مثال از استفاده
my_team = Team("Red Dragons")

# اضافه کردن اعضا
my_team.add_member("Alice")
my_team.add_member("Bob")
my_team.add_member("Charlie")

# نمایش اعضای تیم
my_team.list_members()

# حذف عضو
my_team.remove_member("Bob")

# نمایش اعضای باقی‌مانده
print("\nAfter Removing a Member:")
my_team.list_members()

