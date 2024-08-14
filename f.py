class Book:
    def __init__(self, title, author, pages):
        self.__title = title  # ویژگی خصوصی برای عنوان کتاب
        self.__author = author  # ویژگی خصوصی برای نویسنده
        self.__pages = pages  # ویژگی خصوصی برای تعداد صفحات

    # متدهای عمومی برای دریافت مقادیر
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    # متدهای عمومی برای تنظیم مقادیر
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Number of pages must be positive.")

# مثال از استفاده
my_book = Book("1984", "George Orwell", 328)

# دریافت مقادیر
print("Title:", my_book.get_title())
print("Author:", my_book.get_author())
print("Pages:", my_book.get_pages())

# تنظیم مقادیر جدید
my_book.set_title("Animal Farm")
my_book.set_author("George Orwell")
my_book.set_pages(112)

# دریافت مقادیر جدید
print("\nUpdated Book Info:")
print("Title:", my_book.get_title())
print("Author:", my_book.get_author())
print("Pages:", my_book.get_pages())
