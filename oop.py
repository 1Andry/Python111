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

class Kgfunt:

    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg_funt(self):
        return self.__kg * 2.205

    @kg_funt.setter
    def kg_funt(self, kg):
        if type(kg) == int or type(kg) == float:
            self.__kg = kg


# p1 = Kgfunt(10)
# print(p1.kg_funt)
# p1.kg_funt = 20
# print(p1.kg_funt)

class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.__count += 1

    @staticmethod
    def get_count():
        return Point.__count


p1 = Point()
p1 = Point()
p1 = Point()
print(p1.get_count())
