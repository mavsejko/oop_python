from math import pi


"""
======================================
1. Создай класс Circle, в котором:
есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
Проверь результат вызова:
print(Circle.is_valid_radius(500))   # True
print(Circle.is_valid_radius(1500))  # False
======================================
"""


class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r: int):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS


print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))

"""
2. Добавь в класс Circle:
статический метод area(radius),
который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
инициализацию в __init__, которая сохраняет радиус,
только если он проходит валидацию через метод is_valid_radius()
(подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
Пример:
c = Circle(10)
print(c.area(c.radius))  # Площадь круга
======================================
"""


class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r: int):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return pi * radius ** 2

    def __init__(self, r):
        if type(self).is_valid_radius(r):
            self.radius = r


c = Circle(10)
print(c.area(c.radius))  # Площадь круга

"""
3. Расширь Circle, добавив обычный метод print_info, который выводит:
Радиус: ...
Допустимый диапазон: [MIN, MAX]
Метод должен использовать и self, и атрибуты класса через type(self).

Пример вызова:
c.print_info()
======================================
"""


class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r: int):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return pi * radius ** 2

    def __init__(self, r):
        if Circle.is_valid_radius(r):
            self.radius = r

    def print_info(self):
        cls = type(self)
        print(f"""Радиус: {self.radius}
Допустимый диапазон: [{cls.MIN_RADIUS}, {cls.MAX_RADIUS}]""")


c = Circle(10)
c.print_info()

"""
4. Создай класс User, в котором:

приватные атрибуты __login и __password;
метод set_credentials(login, password), который сохраняет их только если оба значения — строки;
метод get_credentials(), который возвращает кортеж из логина и пароля.
Попробуй создать объект и изменить логин снаружи напрямую. Проверь, что это не сработает.
======================================
"""


class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = password

    def get_credentials(self):
        return self.__login, self.__password


my_user = User()
my_user.set_credentials("admin", "12345")
print(my_user.get_credentials())

my_user2 = User()
my_user2.__login = "USER"
print(my_user2.get_credentials())   #(None, None)


"""
5. Добавь в User:

метод check_password(password) — возвращает True,
если переданное значение совпадает с сохранённым паролем;
приватный метод __encrypt_password(password),
который возвращает пароль в верхнем регистре (имитация шифрования);
в set_credentials вызывай __encrypt_password.
Пример:
u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))      # True
print(u.check_password("qwe"))         # False
======================================
"""


class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def __encrypt_password(self, password):
        return password.upper()

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)

    def get_credentials(self):
        return self.__login, self.__password

    def check_password(self, password):
        return self.__encrypt_password(password) == self.__password


u = User()
u.set_credentials("daniil", "qwerty")
print(u.check_password("qwerty"))  # True
print(u.check_password("qwe"))  # False


"""
6. Убедись, что приватный метод __encrypt_password нельзя вызвать извне.
Попробуй это сделать — и поясни результат.
Также выведи напрямую u.__password — и проверь, что будет ошибка.

Попробуй добраться до данных через u._User__password
"""

#u.__encrypt_password('qwert') # object has no attribute '__encrypt_password'
#print(u.__password)  #object has no attribute '__password'

print(u._User__password)

