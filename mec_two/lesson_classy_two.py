# class Animal:
#     def __init__(self, tiger, lion, monkey):
#         self.__tiger = tiger
#         self.__lion = lion
#         self.monkey = monkey
#
#     def __tiger(self):
#         return self.__lion
#
#
# animals = Animal(tiger='Sherkhan', lion='Mufasa', monkey='Rafiki')
# animals.lion = 'Simba'
# print(animals.lion)
# print(animals.tiger())
'''))(()())'''

'''class Animal:
    def __init__(self, tiger, lion, monkey):
        self.__tiger = tiger
        self.__lion = lion
        self.monkey = monkey

    def __tiger(self):
        return self.__lion


class B(Animal):
    def __init__(self):
        super().__init__() #
# В дрогой папке 
from lesson_classy_two import Animal as d

a = d(tiger='Sherkhan', lion='Mufasa', monkey='Rafiki')
print(a.monkey)
'''
#Создайте класс Factory и внутри создайте 2 метода: Метод engine который возвращает строку "Двигатель создан"
#Метод bridge который возвращает строку "Ходовая часть создана"
#Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе
#Toyota создайте методы wheels и windows.
#Метод wheels возвращает строку "Колёса готовы"
#Метод windows возвращает строку "Стёкла готовы"
#Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
#Результат каждого метода вставьте в лист

class Factory:
    def engine(self):
        return "Двигатель создан"

    def bridge(self):
        return "Ходовая часть создана"


class Toyota(Factory):
    def wheels(self):
        return "Колеса готовы"

    def windows(self):
        return "Стекла готовы"


Toyota = Toyota()

b = [Toyota.wheels(), Toyota.windows(), Toyota.engine(), Toyota.bridge()]
print(b)




