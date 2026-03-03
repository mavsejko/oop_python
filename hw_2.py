"""
======================================
1. Создай класс Person с методом set_data(self, name, age), который сохраняет имя и возраст в объект.
Добавь метод get_data(self), который возвращает строку вида "Имя: <name>, Возраст: <age>".
Создай два объекта и задай им разные значения. Выведи информацию по каждому.
======================================
"""


class Person:
    def set_data(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


my_person_1 = Person()
my_person_1.set_data("Alex", 23)
print(my_person_1.get_data())

my_person_2 = Person()
my_person_2.set_data("Misha", 1)
print(my_person_2.get_data())

"""
2. Добавь в класс Point методы set_coords(x, y) и get_coords().
Создай объект p, задай координаты (7, 12), а затем получи и выведи их.
После этого измени координаты на (-3, 5) и снова выведи результат через get_coords().
======================================
"""

class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return f"coords = {self.x}, {self.y}"


p = Point()
p.set_coords(7, 12)
print(p.get_coords())
p.set_coords(-3, 5)
print(p.get_coords())


"""
3. Используя getattr(), получи ссылку на метод get_coords у объекта Point и вызови его.
Проверь, что результат совпадает с обычным вызовом p.get_coords().
======================================
"""

ans = getattr(p, "get_coords")
print(ans())
print(p.get_coords())

"""
4. Создай класс Person, в котором метод __init__() принимает имя и возраст и сохраняет их как атрибуты объекта.
Добавь метод show_info(), который выводит строку "Имя: <name>, возраст: <age>". Создай объект и вызови метод.
======================================
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")


my_person_4 = Person("Maria", 30)
my_person_4.show_info()

"""
5. Добавь в класс Person метод __del__(), который выводит сообщение "Удалён объект: <имя>",
где <имя> — значение поля name. Создай и удали объект вручную с помощью del.
======================================
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")

    def __del__(self):
        print(f"Удалён объект: {self.name}")


my_person_5 = Person("Dasha", 35)
del my_person_5

"""
6. Создай класс Rectangle с инициализацией по умолчанию: ширина 1, высота 1.
Добавь метод area(), который возвращает площадь прямоугольника.
Проверь работу с прямоугольником без аргументов и с заданной шириной и высотой.
======================================
"""


class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


my_rectangle_1 = Rectangle()
print(my_rectangle_1.area())

my_rectangle_2 = Rectangle(2, 4)
print(my_rectangle_2.area())

"""
7. Создай класс Logger, который всегда возвращает один и тот же объект.
При создании экземпляра в __new__ выводи Создание логгера,
а при вызове __init__ — Инициализация логгера.
======================================
"""


class Logger:
    instance = None

    def __new__(cls, *args, **kwargs):
        print("Создание логгера")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("Инициализация логгера")


my_logger_1 = Logger()
my_logger_2 = Logger()

print(my_logger_1 is my_logger_2)