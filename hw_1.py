"""
++++++++++++++++++++++++++++++++++++++
Классы и атрибуты
++++++++++++++++++++++++++++++++++++++
======================================
1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
Проверь, как это повлияло на значения у обоих объектов.
Убедись, что __dict__ объектов отражает изменения.
"""


class Dog:
    "Класс для создания разных видов собак"
    species = "canis"
    legs = 4


my_dog_1 = Dog()
my_dog_2 = Dog()
my_dog_1.legs = 2
print(my_dog_1.__dict__)
print(my_dog_2.__dict__)


"""
2. Добавь в класс Dog строку документации, описывающую его назначение.
Затем выведи её на экран.
После этого добавь в объект класса новые атрибуты name и age,
а затем удали name.
Проверь, что произойдёт при попытке снова вывести объект.name.
"""

print(Dog.__doc__)
Dog.name = "Sharik"
Dog.age = 5
print(Dog.name)
print(Dog.age)
delattr(Dog, 'name')
#print(Dog.name) -> AttributeError

"""
3. Создай класс User с атрибутами класса role = "guest" и active = True.
С помощью функций getattr(), setattr(), hasattr() и delattr():

измени значение role на "admin",
проверь наличие active,
добавь новый атрибут email,
удали role.
Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
"""


class User:
    role = "guest"
    active = True


setattr(User, "role", "admin")
print(User.role)
print(hasattr(User, "active"))
setattr(User, "email", "test@mail.ru")
print(User.email)
delattr(User, "role")
#print(User.role)
print(User.__dict__)

