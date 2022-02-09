from sub_auto import class_auto


class ElectricAuto(class_auto.Car):
    def __init__(self, power, brand, model, year, mileage):
        super().__init__(brand, model, year, mileage)
        self.power = power

    def print_info(self):
        super().print_info()
        print(f"Этот автомобиль имеет мощьность {self.power} ")


c = ElectricAuto("100%", "Tesla", "T", "2018", 90000)
c.print_info()
