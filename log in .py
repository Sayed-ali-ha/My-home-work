import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        # تنظیمات پنجره اصلی
        self.root = root
        self.root.title("Login Form")

        # برچسب برای نام کاربری
        self.username_label = tk.Label(root, text="Username", font=("Arial", 14))
        self.username_label.grid(row=0, column=0, pady=10, padx=10)

        # ورودی برای نام کاربری
        self.username_entry = tk.Entry(root, font=("Arial", 14))
        self.username_entry.grid(row=0, column=1, pady=10, padx=10)

        # برچسب برای کلمه عبور
        self.password_label = tk.Label(root, text="Password", font=("Arial", 14))
        self.password_label.grid(row=1, column=0, pady=10, padx=10)

        # ورودی برای کلمه عبور
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 14))
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)

        # دکمه ورود
        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Arial", 14))
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

        # پیام وضعیت ورود
        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
        self.status_label.grid(row=3, column=0, columnspan=2)

    def login(self):
        # گرفتن ورودی‌های کاربر
        username = self.username_entry.get()
        password = self.password_entry.get()

        # بررسی اعتبار نام کاربری و کلمه عبور (به صورت ساده)
        if username == "admin" and password == "password":
            self.status_label.config(text="Login successful!", fg="green")
        else:
            self.status_label.config(text="Invalid username or password", fg="red")

# ایجاد پنجره اصلی و اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


