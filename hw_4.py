from datetime import datetime

"""
======================================
1. Создай класс SecureData, который:

имеет атрибут __secret, задаваемый в __init__;
переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
внутри класса доступ к __secret должен работать.
Проверь:
data = SecureData("пароль123")
print(data.__secret)      # ошибка
print(data.get_secret())  # "пароль123"
======================================
"""


class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == "__secret":
            raise ValueError("Атрибут является приватным")
        return object.__getattribute__(self, name)

    def get_secret(self):
        return self.__secret


# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"

"""
2. Добавь в класс SecureData метод __setattr__,
который запрещает создание любого атрибута с именем token.

Проверь:
data.token = "abc123"  # ❌ AttributeError
data.other = "ok"      # ✅ работает
======================================
"""


class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == "__secret":
            raise ValueError("Атрибут является приватным")
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        if key == "token":
            raise AttributeError("Запрещено создание атрибута с именем token")
        return self.object.__setattr__(key, value)

    def get_secret(self):
        return self.__secret


# data = SecureData("пароль123")
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает
"""
3. Создай класс SafeDict, в котором:

нет атрибута default;
реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
Проверь:
d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"
======================================
"""


class SafeDict:
    def __getattr__(self, name):
        return "N/A"

    def __delattr__(self, name):
        print(f"Удалён атрибут {name}")
        return super().__delattr__(name)


# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"

"""
4. Создай класс Employee с приватными полями __name и __salary.
Добавь @property для поля salary, а также сеттер с валидацией:

зарплата должна быть положительным числом;
если нет — выбрасывать ValueError.
Проверь, что:
e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
e.salary = -100   # ❌ ValueError
======================================
"""


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: int):
        if value <= 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.__salary = value


# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError
"""
5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
и поле реально исчезало.
Проверь:

del e.salary
print(e.__dict__)  # salary нет
"""


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: int):
        if value < 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.__salary = value

    @salary.deleter
    def salary(self):
        print("зарплата удалена")
        return object.__delattr__(self, "_Employee__salary")


# e = Employee("Daniil", 5000)
# del e.salary
# print(e.__dict__)  # salary нет

"""
6. Представь, что ты пишешь обёртку над HTML-формой.
Создай класс LoginForm с полем username, которое реализовано через @property.

Логика:
геттер возвращает self._username
сеттер добавляет лог "username изменён"
Проверь, что:
form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)     # "admin"
======================================
"""


class LoginForm:
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        print("username изменён")
        self._username = value


# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"

"""
7. Создай класс Card, где:
поле __number хранит номер карты (строка);
в @property возвращай номер с маской **** **** **** 1234;
в @setter проверяй, что номер состоит из 16 цифр;
в @deleter логируй удаление номера с текущим временем.
Напиши тесты (через assert)
проверку установки корректного номера;
проверку исключения при вводе короткого номера;
проверку вывода замаскированного номера.
======================================
"""


class Card:

    @staticmethod
    def validate_number(number: str):
        if not (isinstance(number, str) and number.isdigit() and len(number) == 16):
            raise ValueError("Номер карты должен состоять из 16 цифр")

    def __init__(self, number: str):
        self.validate_number(number)
        self.__number = number

    @property
    def number(self):
        return f"**** **** **** {str(self.__number)[-4:]}"

    @number.setter
    def number(self, value):
        self.validate_number(value)
        self.__number = value

    @number.deleter
    def number(self):
        print(f"LOG Карта {self.__number} удалена в {datetime.now()}")
        return object.__delattr__(self, "_Card__number")


test_num = "1111111111111234"
c = Card(test_num)

# проверка правильности установки номера карты
assert c._Card__number == test_num, "Номер карты установлен неверно"

# проверка возможности смены номера на некорректный (менее 16 цифр)
try:
    c.number = "1234"
except ValueError as e:
    assert str(e) == "Номер карты должен состоять из 16 цифр", "неправильная длина номера карты"

# проверка возможности создания карты с некорректным номером (менее 16 цифр)
try:
    c1 = Card("1234")
except ValueError as e:
    assert str(e) == "Номер карты должен состоять из 16 цифр", "неправильная длина номера карты"

# проверка вывода замаскированного номера
assert c.number == f"**** **** **** {str(test_num)[-4:]}", "неправильная работа маски"

"""
8. Создай класс UserData для API регистрации пользователя:
email — строка, содержит @;
age — целое число ≥ 18;
is_active — bool;
свойство .json возвращает словарь для запроса.
Напиши тест (через assert)
проверь, что при age = 15 выбрасывается ValueError;
проверь, что email без @ вызывает ошибку;
проверь, что json возвращает корректную структуру.

"""


class UserData:

    @staticmethod
    def validate_email(email):
        if not "@" in email:
            raise ValueError("email должен содержать @")

    @staticmethod
    def validate_age(age):
        if age < 18:
            raise ValueError("возраст должен быть больше 18")

    def __init__(self, email: str, age: int, is_active: bool):
        self.validate_email(email)
        self.__email = email
        self.validate_age(age)
        self.__age = age
        self.__is_active = is_active

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.validate_email(value)
        self.__email = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.validate_age(value)
        self.__age = value

    @property
    def json(self):
        return {
            "email": self.email,
            "age": self.age,
            "is_active": self.__is_active
        }


test_email, test_age, test_is_active = "test@gmail.ru", 24, False

# проверим, что нельзя создать пользователя младше 18 лет
try:
    u1 = UserData(test_email, 15, test_is_active)
except ValueError as e:
    assert str(e) == "возраст должен быть больше 18", "некорректный возраст"

# проверим, что нельзя поменять возраст на <18
u2 = UserData(test_email, test_age, test_is_active)
try:
    u2.age = 15
except ValueError as e:
    assert str(e) == "возраст должен быть больше 18", "некорректный возраст"
    assert u2.age == test_age

# проверим, что нельзя создать пользователя с некорректным мейлом
try:
    u3 = UserData("testgmail.com", test_age, test_is_active)
except ValueError as e:
    assert str(e) == "email должен содержать @", "некорректный email"

# проверим, что нельзя поменять мейл на некорректный
u4 = UserData(test_email, test_age, test_is_active)
try:
    u4.email = "rtetrasd"
except ValueError as e:
    assert str(e) == "email должен содержать @", "некорректный email"
    assert u4.email == test_email

#проверка корректности вывода данных в json
u5 = UserData(test_email, test_age, test_is_active)
data = u5.json
assert data['email'] == test_email, "email неверный"
assert data['age'] == test_age, "email неверный"
assert data['is_active'] == test_is_active, "is_active неверный"

