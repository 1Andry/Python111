class ValidTriangle:
    @classmethod
    def valid(cls, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{value} => только положительное целое число ")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.valid(value)
        instance.__dict__[self.name] = value


class Triangle:
    length1 = ValidTriangle()
    length2 = ValidTriangle()
    length3 = ValidTriangle()

    def __init__(self, length1, length2, length3):
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def truth_triangle(self):
        if self.length1 + self.length2 > self.length3 or self.length2 + self.length3 > self.length1 + \
                self.length1 + self.length3 > self.length2:
            print(f"Треугольник со сторонами ({self.length1}, {self.length2}, {self.length3}) существует")
        else:
            print(f"Треугольник со сторонами ({self.length1}, {self.length2}, {self.length3}) не существует")


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
t1.truth_triangle()
t2.truth_triangle()
t3.truth_triangle()
