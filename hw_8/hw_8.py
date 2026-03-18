from datetime import datetime
"""
======================================
1. Создай две функции: inner() и outer().
В inner() вызови деление на ноль.
В outer() просто вызови inner().
Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
======================================
"""


def inner():
    result = 3 / 0
    return result


def outer():
    inner()


#outer()

#outer() => inner() => 3/0 (ZeroDivisionError)
"""
2. Добавь вокруг вызова outer() конструкцию try/except,
чтобы перехватить исключение и вывести сообщение
"Ошибка перехвачена на верхнем уровне".
======================================
"""


def inner2():
    result = 3 / 0
    return result


def outer2():
    inner2()


#try:
#    outer2()
#except ZeroDivisionError:
#    print("Ошибка перехвачена на верхнем уровне")


"""
3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
В случае ошибки возвращай строку "Ошибка в inner".
======================================
"""


def inner3():
    try:
        result = 3 / 0
        return result
    except ZeroDivisionError:
        print("Ошибка в inner")


def outer3():
    inner3()


#outer3()

"""
4. Сделай так:
В inner() ошибка не перехватывается.
В outer() ошибка перехватывается через try/except.
В outer() при перехвате напечатай "Ошибка в outer".
======================================
"""


def inner4():
    result = 3 / 0
    return result


def outer4():
    try:
        return inner4()
    except ZeroDivisionError:
        print("Ошибка в outer")


#outer4()
"""
5. Напиши функцию get_value(), которая кидает ValueError.
Напиши тестовую функцию test_get_value(), которая:

Вызывает get_value();
Ловит ValueError;
Завершает тест с assert False, если исключение поймано.
======================================
"""


def get_value():
    raise ValueError


def test_get_value():
    try:
        get_value()
    except ValueError:
        assert False, 'Поймали ValueError'


#test_get_value()

"""
======================================
6. Создай функцию divide(x, y).
Если y == 0, выбрасывай ZeroDivisionError через raise.
Иначе возвращай результат деления.
======================================
"""


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    result = x / y
    return result


#divide(5, 0)
#print(divide(5, 6))

"""
7. Создай функцию sqrt(x), которая:
Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
Иначе возвращает квадратный корень из x.
Проверь поведение функции через try/except.
======================================
"""


class NegativeNumberError(Exception):
    def __str__(self):
        return "Х не должен быть меньше нуля"


def sqrt(x):
    if x < 0:
        raise NegativeNumberError
    return x ** 0.5


#print(sqrt(6))
#try:
#    sqrt(-5)
#except NegativeNumberError as e:
#    print(e)

"""
8. Создай базовый класс MathError.
От него унаследуй:
NegativeNumberError
DivisionByZeroError
В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
Проверь в try/except обработку ошибок через базовый класс MathError.
======================================
"""


class MathError(Exception):
    def __str__(self):
        return "Математическая ошибка"


class NegativeNumberError(MathError):
    def __str__(self):
        return "Отрицательное значение"


class DivisionByZeroError(MathError):
    def __str__(self):
        return "Деление на 0"


def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError
    return x / y


#try:
#    safe_divide(5, 0)
#except MathError as e:
#    print(e)

"""
9. Создай тестовую функцию test_sqrt(), которая:
вызывает sqrt(x) с отрицательным числом;
перехватывает NegativeNumberError;
завершает тест с assert False и сообщением
"Нельзя брать корень из отрицательного числа".
======================================
"""


def sqrt9(x):
    if x < 0:
        raise NegativeNumberError
    return x ** 0.5


def test_sqrt(x):
    try:
        sqrt9(x)
    except NegativeNumberError:
        assert False, "Нельзя брать корень из отрицательного числа"


#test_sqrt(-5)
"""
======================================
10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
Обеспечь закрытие файла через with.
======================================
"""


# with open("sample.txt", encoding="UTF-8") as f:
#     for line in f:
#         print(line, end='')


"""
11. Создай класс BackupList, который:
делает копию списка при входе в with,
при выходе сохраняет изменения, если ошибок не было,
откатывает изменения при ошибке.
Проверь:
успешное изменение списка;
откат при ошибке.
======================================
"""


class BackupList:
    def __init__(self, lst):
        self.lst = lst
        self.backup = None

    def __enter__(self):
        self.backup = self.lst[:]
        return self.lst

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print('Error')
            self.lst[:] = self.backup
            print(f"final list = {self.lst}")
        else:
            print('Success')
            print(f"final list = {self.lst}")
        return False


my_lst1 = [1, 2, 3]

with BackupList(my_lst1) as b_success:
    b_success.append('asd')
    b_success.append(123)

my_lst2 = [1, 2, 3]
try:
    with BackupList(my_lst2) as b_error:
        b_error.append('123')
        b_error.append('fgh')
        1/0
except:
    pass


"""
======================================
12. Создай декоратор-класс Timer,
который измеряет время выполнения функции и выводит результат.
"""


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = datetime.now()
        result = self.func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f'время выполнения функции {duration}')
        return result


@Timer
def some_func():
    return 5 ** 23898


some_func()
