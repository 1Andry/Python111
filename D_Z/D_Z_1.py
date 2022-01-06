from math import pi


class Sphere:

    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def set_radius(self, r):
        if Sphere.check_modul(r):
            self.radius = r
        else:
            print("Радиус должен быть цифрами и больше 0")

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_voleume(self):
        v = (4 / 3) * pi * (self.radius ** 3)
        print("объем шара:", v)

    def get_squere(self):
        s = 4 * pi * (self.radius ** 2)
        print("площадь внешней поверхности сферы:", s)

    def get_center(self):
        print(self.x, self.y, self.z)

    def is_point_inside(self, x, y, z):
        if Sphere.check_value(x) and Sphere.check_value(y) and Sphere.check_value(z):
            self.x = x
            self.y = y
            self.z = z
            if (self.x ** 2 + self.y ** 2 + self.z ** 2) <= (self.radius ** 2):
                print(f"({self.x}, {self.y}, {self.z}):", True)
            else:
                print(f"({self.x}, {self.y}, {self.z}):", False)
        else:
            print("Координаты должны быть цифрами ")

    def check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def check_modul(z):
        if isinstance(z, int) or isinstance(z, float) and z >= 0:
            return True
        return False


h1 = Sphere(0.6, 0, 0, 0)
print(h1.__dict__)
h1.get_voleume()
h1.get_center()
h1.get_squere()
h1.is_point_inside(0, -1.5, 0)
h1.set_radius(1.6)
h1.is_point_inside(0, -1.5, 0)
