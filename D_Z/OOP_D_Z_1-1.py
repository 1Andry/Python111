from abc import abstractmethod


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def print_info(self):
        print(self)

    @abstractmethod
    def drow(self):
        print(self)


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_square(self):
        return self.length * self.width

    def drow(self):
        return (("*" * self.width + "\n") * self.length)

    def print_info(self):
        print(f"===Прямоугольник===\nдлинна:{self.length}\nширина:{self.width}\nпериметр:{self.get_perimeter()}\
        \nплощадь:{self.get_square()}\nцвет:{self.color}\n{self.drow()}\n")


class Square(Shape):
    def __init__(self, color, length):
        super().__init__(color)
        self.length = length

    def get_perimeter(self):
        return self.length * 4

    def get_square(self):
        return self.length ** 2

    def drow(self):
        return (("*" * self.length + "\n") * self.length)

    def print_info(self):
        print(f"===Квадрат===\nдлинна:{self.length}\nширина:{self.length}\nпериметр:{self.get_perimeter()}\
        \nплощадь:{self.get_square()}\nцвет:{self.color}\n{self.drow()}\n")


class Triangle(Shape):
    def __init__(self, color, length1, length2, length3):
        super().__init__(color)
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    def get_perimeter(self):
        return self.length1 + self.length2 + self.length3

    def get_square(self):
        p = (self.length1 + self.length2 + self.length3) / 2
        return 0.5 * (p * (p - self.length1) * (p - self.length2) * (p - self.length3))

    def drow(self):
        return ("\n".join((i * "*").center(self.length1) for i in range(self.length1) if i % 2 != 0))

    def print_info(self):
        print(f"===Треугольник===\nсторона 1: {self.length1}\nсторона 2: {self.length2}\nсторона 3: {self.length3}\
        \nпериметр:{self.get_perimeter()}\nплощадь:{round(self.get_square(), 2)}\nцвет:{self.color}\n{self.drow()}")


r1 = Rectangle("red", 3, 7)
s1 = Square("green", 3)
t1 = Triangle("yellow", 11, 6, 6)
r1.print_info()
s1.print_info()
t1.print_info()
