import tkinter as tk
from tkinter import messagebox

class HomeworkApp:
    def _init_(self, root):
        self.root = root
        self.root.title("math")

        # نمونه‌ای از لیست کارهای خانگی
        self.homework_list = [
            "first home work",
            "second home work",
            "third home work",
           " forth home work"
        ]

        # ساختن لیست ویو
        self.listbox = tk.Listbox(root, height=20, width=20, font=("Helvetica", 12))
        self.listbox.pack(pady=29)

        # پر کردن لیست با کارهای خانگی
        for item in self.homework_list:
            self.listbox.insert(tk.END, item)

        # اتصال کلیک به تابع
        self.listbox.bind("<<ListboxSelect>>", self.on_item_click)

    def on_item_click(self, event):
        # گرفتن اندیس انتخاب شده
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            homework = event.widget.get(index)

            # نمایش پیام با اطلاعات کار خانگی
            messagebox.showinfo("sayed Ali",  "",)

if _name_ == "_main_":
    root = tk.Tk()
    app = HomeworkApp(root)
    root.mainloop()