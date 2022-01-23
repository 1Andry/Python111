class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density  # плотность

    def edit_density(self, value):  # изменение плотности
        self.density = value

    def calc_v(self, m):  # вычисление объема
        v = round(m / self.density, 2)
        print(f"Объем:{m} кг {self.name} равен {v} kg/m^3")
        return v

    def calc_m(self, v):
        m = v * self.density
        print(f"Вес:{v} m^3 {self.name} равен {m} kg")
        return m

    def print_info(self):
        print(f"Жидкость:{self.name}\n(плотность = {self.density} kg/m^3)")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def edit_strength(self, strength):  # изменение крепкости
        self.strength = strength

    def print_info(self):
        super().print_info()
        print(f"крепкость: {self.strength:.0%}")

    def calc_v(self, m):
        v = super().calc_v(m)
        v_alk = round(v * self.strength, 2)
        print(f"Обьем алкаголя {m} кг {self.name} состовляет {v_alk} m^3")
        return v, v_alk

    def calc_m(self, v):
        m = super().calc_m(v)
        m_alk = m * self.strength
        print(f"Вес алкоголя {v} m^3 {self.name} состовляет {m_alk} кг")
        return m, m_alk


p2 = Alcohol("wine", 1000, 14)
p2.edit_density(1200)
p2.calc_v(300)
p2.calc_m(0.5)
p2.print_info()
p2.edit_strength(12)
p2.print_info()
print(p2.strength)
p2.calc_v(300)
p2.print_info()
