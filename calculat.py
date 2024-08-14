import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        # تنظیمات پنجره اصلی
        self.root = root
        self.root.title("Simple Calculator")

        # ویجت نمایشگر (Entry) برای نمایش اعداد و نتیجه
        self.display = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # ایجاد دکمه‌های ماشین حساب
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', 'C', '=', '+'
        ]

        # ساختار دهی دکمه‌ها در گرید
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        # عملکرد دکمه‌ها
        if char == "C":
            # پاک کردن نمایشگر
            self.display.delete(0, tk.END)
        elif char == "=":
            # محاسبه و نمایش نتیجه
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            # افزودن اعداد و عملیات به نمایشگر
            self.display.insert(tk.END, char)

# ایجاد پنجره اصلی و اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

