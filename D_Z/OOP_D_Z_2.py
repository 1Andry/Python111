from abc import ABC, abstractmethod


class Root(ABC):
    def __init__(self, example):
        self.example = example
        self.result = None

    @abstractmethod
    def calculate_the_root(self):
        pass

    @abstractmethod
    def print_result(self):
        print(self)


class LinearEquation(Root):
    def calculate_the_root(self):
        a = None
        b = 0
        for i in range(len(self.example)):
            if self.example[i] == "x":
                a = int(self.example[i - 1])
            else:
                if self.example[i] == "=":
                    b += int(self.example[i - 2] + self.example[i - 1])
        if a == 0 and b == 0:
            self.result = "Бесконечное количество решений."
        elif a != 0 and (b == 0 or abs(a) <= abs(b)):
            self.result = round(-b / a, 2)
            return self.result
        else:
            self.result = "Решений нет."

    def print_result(self):
        print(f"{self.example} is {self.result}")


class SqEquation(Root):
    def calculate_the_root(self):  # "1x^2-2x-3=0"
        a = None
        b = None
        c = 0
        for i in range(len(self.example)):
            if self.example[i] == "x" and self.example[i + 1] == "^":
                a = int(self.example[i - 1])
            elif self.example[i] == "x" and self.example[i + 1] != "^":
                b = int(self.example[i - 1])
            else:
                if self.example[i] == "=":
                    c = int(self.example[i - 2] + self.example[i - 1])
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            self.print_result = 'Корней нет'
            return self.result
        elif discriminant == 0:
            self.print_result = -b / (2 * a)
            return self.result
        else:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            self.result = x1, x2
            return self.result

    def print_result(self):
        print(f"{self.example} is {self.result}")


p1 = LinearEquation("3x+7=0")
p1.calculate_the_root()
p1.print_result()
p2 = SqEquation("1x^2-2x-3=0")
p2.calculate_the_root()
p2.print_result()
