from math import pi

"""
======================================
1. Создай базовый класс Shape с методом area(), который возвращает 0.
Отнаследуй два класса: Circle и Square.
Переопредели метод area() так, чтобы он возвращал площадь круга или квадрата.

c = Circle(5)
s = Square(4)

print(c.area())  # ~78.5
print(s.area())  # 16
======================================
"""


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, r: int):
        self.r = r

    def area(self):
        return round(pi * self.r ** 2, 1)


class Square(Shape):
    def __init__(self, a: int):
        self.a = a

    def area(self):
        return self.a ** 2


#c = Circle(5)
#s = Square(4)

#print(c.area())  # ~78.5
#print(s.area())  # 16

"""
2. Создай базовый класс BasePage с методом open(url).
Сделай добавь магический init, в котором указан текст на странице (любой)
От него унаследуй LoginPage и добавь метод find(text).
Проверь, что методы из базового класса тоже доступны:
page = LoginPage()
page.open("https://example.com/login")
page.text("Зима")
Вывод в консоли:
На странице найден текст: "Зима"
======================================
"""


class BasePage:
    def __init__(self, text_from_the_page='some_textЗима'):
        self.text_from_the_page = text_from_the_page

    def open(self, url):
        print(f"Открыта страница {url}")


class LoginPage(BasePage):
    def find(self, txt):
        if txt in self.text_from_the_page:
            print(f"На странице найден текст: \"{txt}\"")
        else:
            print(f"На странице не найден текст: \"{txt}\"")

    def text(self, value):
        self.find(value)


#page = LoginPage()
#page.open("https://example.com/login")
#page.text("Зима")


"""
3. Создай свой класс ResultList,
который наследует list и добавляет метод success_count(),
возвращающий количество успешных результатов (где item["status"] == "passed").

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

print(results.success_count())  # 2
======================================
"""


class ResultList(list):
    def success_count(self):
        cnt = 0
        for item in self:
            if item["status"] == "passed":
                cnt += 1
        return cnt


results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

#print(results.success_count())  # 2

"""
4. Создай классы BaseStep и LoginStep, отнаследуй второй от первого.
 Создай объект step = LoginStep()
 Проверь, что он является экземпляром и LoginStep, и BaseStep, и object.

print(issubclass(LoginStep, BaseStep))  # True
print(isinstance(step, BaseStep))       # True
print(isinstance(step, object))         # True
======================================
"""


class BaseStep:
    pass


class LoginStep(BaseStep):
    pass


#step = LoginStep()

#print(issubclass(LoginStep, BaseStep))  # True
#print(isinstance(step, BaseStep))       # True
#print(isinstance(step, object))         # True


"""
5. Создай класс ExtendedDict, который наследуется от dict,
и переопредели __str__, чтобы словарь красиво выводился в формате:
ключ: значение
ключ: значение
Пример:
d = ExtendedDict(a=1, b=2)
print(d)
Ожидаемый вывод:
a: 1
b: 2
======================================
"""


class ExtendedDict(dict):
    def __str__(self):
        return '\n'.join([f"{key}: {value}" for key, value in self.items()])


#d = ExtendedDict(a=1, b=2)
#print(d)

"""
6. Создай два класса:

Widget: принимает x, y и сохраняет как self.x, self.y;
Button: наследует Widget, добавляет label, но обязательно вызывает super().
Проверь, что всё сохраняется корректно.

btn = Button(100, 200, "OK")
print(btn.x, btn.y, btn.label)  # 100 200 OK
======================================
"""


class Widget:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Button(Widget):
    def __init__(self, x: int, y: int, label: str):
        super().__init__(x, y)
        self.label = label


#btn = Button(100, 200, "OK")
#print(btn.x, btn.y, btn.label)  # 100 200 OK

"""
7. Модифицируй Button, чтобы не вызывать super() вовсе.
Что произойдёт? Проверь через print(btn.__dict__).
======================================
"""


class Widget:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Button(Widget):
    def __init__(self, x: int, y: int, label: str):
        #self.x = x
        #self.y = y
        self.label = label

btn = Button(100, 200, "OK")
print(btn.__dict__) #{'label': 'OK'}
#  Без super() или ручного переопределения всех полей, объект дочернего класса будет «недособранным», потеряет всё, что должен был получить от родителя

"""
8. Создай классы:
Logger — метод log(self, msg) просто печатает сообщение;
HTMLLogger(Logger) — переопредели метод log.
logger = HTMLLogger()
logger.log("Login successful")

Ожидаемый вывод (обрати внимание что выводится 2 строки:
одна из log класса Logger, другая из log класса HTMLLogger):
[LOG] Login successful
<p>Login successful</p>
"""


class Logger:
    def log(self, msg: str):
        print("[LOG]", msg)


class HTMLLogger(Logger):
    def log(self, msg: str):
        super().log(msg)
        print(f"<p>{msg}</p>")


logger = HTMLLogger()
logger.log("Login successful")
