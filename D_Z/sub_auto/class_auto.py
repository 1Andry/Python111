class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def print_info(self):
        print(f"{self.brand}\n{self.model}\n{self.year}\n{self.mileage}")


