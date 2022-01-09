class Human:
    name = "name"
    birthday = "00.00.0000"
    phone = "00-00-00"
    country = "country"
    city = "city"
    address = "street, house"

    def print_info(self):
        print(" персональные данные ".center(40, "*"))
        print(f"Имя: {self.name}")
        print(f"Имя: {self.birthday}")
        print(f"Имя: {self.phone}")
        print(f"Имя: {self.country}")
        print(f"Имя: {self.city}")
        print(f"Имя: {self.address}")
        print("=" * 40)

    def input_info(self, name, data, phone, country, city, address):
        self.name = name
        self.birthday = data
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):  # установить имя
        self.name = name

    def get_name(self):  # получить  имя
        return self.name

    def set_birthday(self, bir):
        self.birthday = bir

    def get_birthday(self):
        return self.birthday

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_address(self, add):
        self.address = add

    def get_address(self):
        return self.address


h1 = Human()


# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный")
# h1.print_info()
# h1.set_name("Марина")
# print(h1.get_name())
# h1.print_info()
# print(f"Имя: {h1.get_name()}")
# h1.set_birthday("11.11.2011")
# print(h1.get_birthday())
# h1.set_city("Питер")
# print(h1.get_city())
# h1.set_address("Фрунзе")
# print(h1.get_address())
# h1.print_info()

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __del__(self):
#         print("удаление" + self.__class__.__name__)
# p1 = Point(3, 7)
# print(p1.__dict__)
# p2 = Point()
# print(p2.__dict__)

# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0, ):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
# print(Point.count)
# p1 = Point(5, 10)
# p2 = Point(2, 3)
# p3 = Point(1, 4)
# print(Point.count)

class Robot:
    k = 0

    def __init__(self, name):
        self.name = name
        print("Инициализация :", self.name)
        Robot.k += 1

    def say_hi(self):
        print("Приветствую, Меня зовут:", self.name)

    def __del__(self):
        Robot.k -= 1
        print("выключение:", self.name, "Выключается")
        if Robot.k == 0:
            print(self.name, "был последним")


# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность", Robot.k)
# droid2 = Robot("c-3po")
# droid2.say_hi()
# print("Численность", Robot.k)
# print("\nЗдесь роботы могут проделать работу\n")
# del droid1
# print("Численность", Robot.k)
# del droid2
# print("Численность", Robot.k)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self): # получение координат
#         return self.__x, self.__y
#
#     def __check_value(z): # проверка на тип данных
#         if (isinstance(z, int) or isinstance(z, float)):
#             return True
#         return False
#
#     def set_coords(self, x, y): # изменение координат х, y
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть цифрами")
#
#     def set_coords_x(self, x):  # изменение координат х
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть цифрами")

# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords("2", 4)
# print(p1.get_coords())
# p1.set_coords_x(20)
# print(p1.get_coords())
# print(p1._Point__x)
# import math


# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(z):  # проверка на тип данных
#         if (isinstance(z, int) or isinstance(z, float)):
#             return True
#         return False

#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_data(self):
#         return self.__length, self.__width
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hipotenuse(self):
#         return round(math.sqrt(2 ** self.__length + self.__width ** 2), 2)
#
#     def get_drow(self):
#         return (("*" * self.__width + "\n") * self.__length)
#
#
# r1 = Rectangle(3, 5)
# print(r1.get_data())
# print(r1.get_area())
# print(r1.get_perimetr())
# print(r1.get_hipotenuse())
# print(r1.get_drow())


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __getattr__(self, item):
        return f"в классе {__class__.__name__} отсутствует {item}"

    def get_coords(self):  # получение координат
        return self.__x, self.__y


# z1 = Point()
# print(z1.zz)
# print(z1.__dict__)
#
#
# class Pointer:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coords_x(self):  #
#         return self.__x
#
#
#     @coords_x.setter
#     def coords_x(self, x):  # изменение координат х, y
#         self.__x = x
#
#     def __getattr__(self, item):
#         return f"в классе {__class__.__name__} отсутствует {item}"
#
#     # cordes_x = property(__get_coords_x, __set_coords_x)
#
#
# c1 = Pointer(5, 10)
# c1.cordes_x = 100
# print(c1.__dict__)
# print(c1.cordes_x)

# class Kgfunt:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg_funt(self):
#         return self.__kg * 2.205
#
#     @kg_funt.setter
#     def kg_funt(self, kg):
#         if type(kg) == int or type(kg) == float:
#             self.__kg = kg


# p1 = Kgfunt(10)
# print(p1.kg_funt)
# p1.kg_funt = 20
# print(p1.kg_funt)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count


# p1 = Point()
# p1 = Point()
# p1 = Point()
# print(p1.get_count())

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, n):
        self.__old = n

    @old.deleter
    def old(self):
        del self.__old


# p1 = Person("Irina", 36)
# print(p1.name)
# p1.name = "Iror"
# # del p1.name
# print(p1.__dict__)
# p1.old = 21
# print(p1.__dict__)

# class Change:
#     @staticmethod
#     def inc(x):
#         return x+1
#     @staticmethod
#     def dec(x):
#         return x-1
#
# print(Change.inc(11), Change.dec(10))
# import math
# class Mat:
#     @staticmethod
#     def maximum(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def minimum(a, b, c, d):
#         return min(a, b, c, d)
#     @staticmethod
#     def mid(a, b, c, d):
#         return round((a+b+c+d)/4,2)
#
#     @staticmethod
#     def fact(x):
#         return math.factorial(x)
#
# print(Mat.maximum(3,5,11,9))
# print(Mat.minimum(3,5,7,9))
# print(Mat.mid(3,5,7,9))
# print(Mat.fact(5))
# import math
#
#
# class Area:
#     count = 0
#
#     # def __init__(self):
#     #     Area.count += 1
#
#     @staticmethod
#     def triangle_aria(a, b, c):
#         Area.count += 1
#         p = (a + b + c) / 2
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_aria2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_aria(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print("Площадь треугольника", Area.triangle_aria(3, 4, 5))
# print("Площадь треугольника через основание и высоту", Area.triangle_aria2(6, 7))
# print("Площадь квадрата", Area.square_aria(7))
# print("количество подсчетов", Area.get_count())
# pl = Area()
# print("Площадь треугольника", pl.triangle_aria(3, 4, 5))
# print("Площадь треугольника через основание и высоту", pl.triangle_aria2(6, 7))
# print("количество подсчетов", Area.get_count())
#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def date_validate(data_as_string):
#         if data_as_string.count(".") == 2:
#             day, month, year = map(int, data_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
# dates = [
#     "30.12.2000",
#     "30-12-2000",
#     "01.01.2000",
#     "12.31.2000",
# ]
# for d in dates:
#     if Date.date_validate(d):
#         date = Date.from_string(d)
#         st = date.string_to_db()
#         print(st)
#     else:
#         print("не правильная строка с датами")
# string_date = "23.10.2021"
# day, month, year = map(int, string_date.split("."))
# print(day, month, year)
# d1 = Date.from_string("23.10.2021")
# print(d1.string_to_db())
# date = Date(day, month, year)
# print(date.string_to_db())

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"

    def __init__(self, surname, num, persent, value=0):
        self.surname = surname
        self.num = num  # номер счета
        self.persent = persent
        self.value = value  # сумма в рублях
        print(f"Счет #{self.num} принадлежит {self.surname}был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*"*50)
        print(f"Счет #{self.num} принадлежит {self.surname}был закрыт.")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    def edit_owner(self, surname):
        self.surname = surname

    def add_persents(self):
        print("Начисленно", self.value * self.persent)


    def convert_to_usd(self):
        print(f"состояние счета {Account.convert(self.value, Account.rate_usd)} USD")

    def convert_to_eur(self):
        print(f"состояние счета {Account.convert(self.value, Account.rate_eur)} EUR")

    def print_balanse(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 50)
        print(f"Номер счета: #{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balanse()
        print(f"Проценты: {self.persent:.0%}")
        print("-" * 50)


acc = Account("Долгих", "12345", 0.03, 1000)
# acc = Account(num="12345", surname="Долгих", persent=0.03,, value = 1000)
acc.print_balanse()
# acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
acc.convert_to_usd()
acc.edit_owner("Дюма")
acc.print_info()
acc.add_persents()
acc