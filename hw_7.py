from abc import ABC, abstractmethod
from datetime import datetime

"""
======================================
1. Создай три класса: Cat, Dog, Duck.
В каждом реализуй метод speak(), возвращающий уникальную строку.
Создай список из экземпляров этих классов и вызови метод speak()
в цикле.
======================================
"""


class Cat:
    def speak(self):
        return "Meow"


class Dog:
    def speak(self):
        return "Woof"


class Duck:
    def speak(self):
        return "Quack"


#zoo = [Cat(), Dog(), Duck()]
#for item in zoo:
#    print(item.speak())


"""
2. Создай базовый класс Shape
Создай три класса-наследника: Square, Rectangle, Triangle,
в каждом реализуй метод get_pr().
Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
можно обойти в цикле и вызвать get_pr() у каждого.
======================================
"""


class Shape:
    def get_pr(self):
        pass


class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def get_pr(self):
        return self.side * 4


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def get_pr(self):
        return 2 * (self.height + self.width)


class Triangle(Shape):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


#shapes = [Square(5), Rectangle(4, 5), Triangle(1, 3, 3)]
#for s in shapes:
#    print(s.get_pr())


"""
3. Сделай класс Shape абстрактным.
Переопредели get_pr() как @abstractmethod.
Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
======================================
"""


class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass

#s = Shape()


"""
4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
======================================
"""


class A:
    def __init__(self):
        super().__init__()
        print("init A")


class B:
    def __init__(self):
        super().__init__()
        print("init B")


class C:
    def __init__(self):
        super().__init__()
        print("init C")


class D(A, B, C):
    def __init__(self):
        super().__init__()
        print("init D")


#print(D.mro())   #[<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

#d = D()

"""
5. Создай MixinLog (как в уроке).
Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
Создай класс, который наследует оба класса. Создай экземпляр этого класса.
======================================
"""


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id} забронирован в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


class BookingHotel(MixinLog):
    def __init__(self, nights_num: int, room: int, name: str):
        print('Init BookingHotel')
        super().__init__()
        self.nights_num = nights_num
        self.room = room
        self.__guest_name = name
        super().save_sell_log()

    @property
    def guest_name(self):
        return self.__guest_name

    @guest_name.setter
    def guest_name(self, value):
        self.__guest_name = value


class Billing(BookingHotel):
    def __init__(self, price_per_night: int, nights_num: int, room: int, name: str):
        super().__init__(nights_num=nights_num, room=room, name=name)
        self.price_per_night = price_per_night
        print('Init Billing')

    def calculate_price(self):
        return self.price_per_night * self.nights_num

    def save_sell_log(self):
        print(f"Чек {self.id} оплачено  {self.calculate_price()} в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def payment(self, card: str):
        print(f"оплата прошла успешно по карте {card}")
        self.save_sell_log()


#b = Billing(1200, 10, 402, "Max")
#b.payment("1234123412341234")


"""
6. В Goods и MixinLog реализуй print_info().
Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
Измени порядок наследования — изменилась ли логика?
======================================
======================================
Далее задания можете сделать через классы, функции или без них.
======================================
======================================
"""


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.price}, {self.weight}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id} продан в {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def print_info(self):
        print(f"INFO MixinLog {self.id}")


class NoteBook(Goods, MixinLog):
    pass


class NoteBook1(MixinLog, Goods):
    pass

n = NoteBook('test_notebook', 50_000, 1500)
n.print_info() #test_notebook, 1500, 50000, если Goods, MixinLog

#n1 = NoteBook1()
#n1.print_info() #INFO MixinLog 1, если MixinLog, Goods

#т е в первом случае заходим в init  Goods, идем к родителю, дергаем его инит, получаем
# инит миксинлог, возвращаемся к себе, записываем себе все переданные атрибуты,
# вызываем свой метод print_info (ближайшего родителя)
# во втором случае идем сразу в миксинлог, проходим его init, берем его же print_info


"""
7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
и выведи сообщение: "На ноль делить нельзя!"
======================================
"""


def calc(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


#x, y = int(input()), int(input())
#calc(x, y)

"""
8. Расширь программу из Задания 1:
Добавь обработку ошибки (как называется ошибка найди сам),
если пользователь ввёл не числа, а текст.
Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
======================================
"""


def calc_1(a, b):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except ValueError:
        print("Ошибка ввода: введите два числа через пробел")


#x, y = [i for i in input().split()]
#calc_1(x, y)


"""
9. Модифицируй код так, чтобы после обработки конкретных ошибок
был ещё один общий except, который перехватывает все остальные ошибки и выводит:
"Произошла неизвестная ошибка"
======================================
"""


def calc_2(a, b):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except ValueError:
        print("Ошибка ввода: введите два числа через пробел")
    except:
        print("Произошла неизвестная ошибка")


#calc_2([1], 2)
"""
10. При перехвате исключений из 7 и 8 заданий,
сохрани ошибку в переменную e и выведи её текст:
======================================
"""


def calc_3(a, b):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as e:
        print(f"На ноль делить нельзя!\n"
              f"{str(e)}")
    except ValueError as e:
        print(f"Ошибка ввода: введите два числа через пробел\n"
              f"{str(e)}")
    except:
        print("Произошла неизвестная ошибка")


#x, y = [i for i in input().split()]
#calc_3(x, y)
"""
11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
======================================
"""


def calc_4(a, b):
    try:
        print(int(a)/int(b))
    except ArithmeticError as e:
        print(f"{str(e)}")
    except ValueError as e:
        print(f"Ошибка ввода: введите два числа через пробел\n"
              f"{str(e)}")
    except:
        print("Произошла неизвестная ошибка")


#x, y = [i for i in input().split()]
#calc_4(x, y)

"""
12. Запроси у пользователя два числа и выполни деление.
Если деление прошло успешно без ошибок — выведи
"Деление выполнено успешно" через (но не в блоке try)
======================================
"""


def calc_5(a, b):
    try:
        print(int(a)/int(b))
    except ArithmeticError as e:
        print(f"{str(e)}")
    except ValueError as e:
        print(f"Ошибка ввода: введите два числа через пробел\n"
              f"{str(e)}")
    except:
        print("Произошла неизвестная ошибка")
    else:
        print("Деление выполнено успешно")


#x, y = [i for i in input().split()]
#calc_5(x, y)


"""
13. Расширь код из Задания 12:
Добавь блок, в котором будет выводиться
"Работа программы завершена", независимо от успеха деления.
======================================
"""


def calc_6(a, b):
    try:
        print(int(a)/int(b))
    except ArithmeticError as e:
        print(f"{str(e)}")
    except ValueError as e:
        print(f"Ошибка ввода: введите два числа через пробел\n"
              f"{str(e)}")
    except:
        print("Произошла неизвестная ошибка")
    else:
        print("Деление выполнено успешно")
    finally:
        print("Работа программы завершена")


#x, y = [i for i in input().split()]
#calc_6(x, y)
"""
14. Реализуй две вложенные конструкции:
Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
Внутренний try/except ловит деление на ноль.
======================================
"""


def calc_7(a, b):
    try:
        a, b = int(a), int(b)
        try:
            print(a / b)
        except ArithmeticError as e:
            print(f"{str(e)}")
        else:
            print("Деление выполнено успешно")
    except ValueError as e:
        print(f"Ошибка ввода: введите два числа через пробел\n"
              f"{str(e)}")
    finally:
        print("Работа программы завершена")


#x, y = [i for i in input().split()]
#calc_7(x, y)
"""
15. Вынеси обработку деления в отдельную функцию divide(x, y)
с собственным try/except.
Во внешнем коде обработай только ошибку ввода.
"""


def divide(x, y):
    try:
        print(x / y)
    except ArithmeticError as e:
        print(f"{str(e)}")
    else:
        print("Деление выполнено успешно")


def calc_8(a, b):
    try:
        a, b = int(a), int(b)
        divide(a, b)
    except ValueError as e:
        print(f"Ошибка ввода: введите два числа через пробел\n"
              f"{str(e)}")
    finally:
        print("Работа программы завершена")


x, y = [i for i in input().split()]
calc_8(x, y)
