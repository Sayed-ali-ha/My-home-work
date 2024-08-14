import tkinter as tk

def show_task(task):
    # ایجاد یک پنجره جدید
    task_window = tk.Toplevel(root)
    task_window.title("Task Details")
    
    # نمایش عنوان کار
    title_label = tk.Label(task_window, text="Task:", font=("Arial", 14))
    title_label.pack(padx=10, pady=5)
    
    task_label = tk.Label(task_window, text=task["title"], font=("Arial", 20))
    task_label.pack(padx=10, pady=5)
    
    # نمایش توضیحات کار
    description_label = tk.Label(task_window, text="Description:", font=("Arial", 9))
    description_label.pack(padx=10, pady=5)
    
    description_text = tk.Text(task_window, wrap="word", height=15, width=50)
    description_text.insert(tk.END, task["description"])
    description_text.config(state=tk.DISABLED)
    description_text.pack(padx=10, pady=5)
    
    # دکمه‌ای برای بستن پنجره جدید
    close_button = tk.Button(task_window, text="Close", command=task_window.destroy)
    close_button.pack(pady=10)

# لیست کارهای خانگی با جزئیات
tasks = [
    {"title": "fib_", "description": "def fibonacci(n): \n  if n <= 0:        return 'Input should be a positive integer.'  \n  elif n == 1:      \n  return 0   \n elif n == 2:     \n   return 1    else:   \n     return fibonacci(n-1) + fibonacci(n-2)n = 10fib_sequence = [fibonacci(i) \n for i in range(1, n + 1)]:\n  print(f'The first {n} numbers in the Fibonacci sequence are: {fib_sequence}') fibonacci(n) "},
    {"title": "Tower of hanoi", "description": "def tower_of_hanoi(n, source, target, auxiliary)  \n  if n == 1:   \n     print(f'Move disk 1 from {source} to {target}')  \n     return   tower_of_hanoi(n - 1, source, auxiliary, target)  \n print(f'Move disk {n} from {source} to {target}') \n  tower_of_hanoi(n - 1, auxiliary, target, source)n = \n tower_of_hanoi(n, 'A', 'C', 'B')\n### توضیح:- n تعداد دیسک‌ها است.\n- source میله مبدا است.\n- target میله مقصد است.\n- auxiliary \nمیله کمکی است.با اجرای این کد برای ۳ دیسک، حرکات به شکل زیر چاپ می‌شود:Move disk 1 from A to C\nMove disk 2 from A to B\nMove disk 1 from C to B\nMove disk 3 from A to C\nMove disk 1 from B to A\nMove disk 2 from B to C\Move disk 1 from A to C"},]

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("To-Do List")

# ایجاد و نمایش لیست کارها
for task in tasks:
    button = tk.Button(root, text=task["title"], font=("Arial", 12), command=lambda t=task: show_task(t))
    button.pack(pady=5)

# شروع برنامه
root.mainloop()

