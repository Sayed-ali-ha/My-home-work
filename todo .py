import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        # تنظیمات پنجره اصلی
        self.root = root
        self.root.title("To-Do List")

        # لیست وظایف
        self.tasks = []

        # ویجت برای نمایش عنوان برنامه
        self.title_label = tk.Label(root, text="My To-Do List", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # ویجت لیست باکس برای نمایش وظایف
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # فریم برای دکمه‌ها
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # ویجت ورودی برای اضافه کردن وظیفه جدید
        self.task_entry = tk.Entry(root, width=42)
        self.task_entry.pack(pady=5)

        # دکمه اضافه کردن وظیفه
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left", padx=10)

        # دکمه حذف وظیفه
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side="right", padx=10)

    def add_task(self):
        # گرفتن متن ورودی از Entry
        task = self.task_entry.get()

        if task:  # اگر ورودی خالی نباشد
            self.tasks.append(task)  # اضافه کردن وظیفه به لیست وظایف
            self.listbox.insert(tk.END, task)  # افزودن وظیفه به لیست باکس
            self.task_entry.delete(0, tk.END)  # پاک کردن ورودی
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")  # نمایش هشدار در صورت خالی بودن ورودی

    def delete_task(self):
        try:
            # گرفتن اندیس وظیفه انتخاب شده
            selected_task_index = self.listbox.curselection()[0]
            # حذف وظیفه از لیست و لیست باکس
            self.listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")  # نمایش هشدار در صورت عدم انتخاب وظیفه

# ایجاد پنجره اصلی و اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
