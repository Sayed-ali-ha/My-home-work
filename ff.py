class Car:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def start_engine(self):
        print(f"The {self.year} {self.model} engine is now running!")

# ساخت یک شیء از کلاس Car
car1 = Car(2022, "Toyota Corolla")

# چاپ جریان موتر
car1.start_engine()

