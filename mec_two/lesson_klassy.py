#
# test = 0  #переменная
# def func():
#     print("Hello!") #функция
#
#
#
# class Cat:
#     test = 0 #атрибут
#
#     def func(self):
#         print("Hello!") #Метод
#
# Cat.age = 1
# Cat.breed = "Siam"
#
# Garfield = Cat() #Экземпляр класса
# Cheshir = Cat() #Экземпляр класса
#
# Garfield.age = 8
# Cheshir.breed = "Egypt"
# # print(Garfield)
# # print(Cheshir)
# # print(Garfield.age)
# # print(Cheshir.age)
# print(Garfield.breed)
# print(Cheshir.breed)
# #Garfield.func()
#
# del Cat
#
# name = Cat()
# print(name)

'''НАСЛЕДОВАНИЕ'''
# class Human:
#     emotion = 'Angry'
#     voice = 'True'
#     attr = 'See'
#
#
# class Doctor(Human):
#     skill = 'Healer'
#
#
# class Teacher(Doctor):
#     pass
#
#
# Dazzle = Doctor()
# Alchemist = Teacher()
#
# print(Dazzle.voice)
# print(Alchemist.voice)
# print(Dazzle.skill)
# print(Alchemist.skill)

# class Employee:
#     def __init__(self, firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#
#     def meet(self):
#         return f'Hello {self.firstname} {self.lastname}!'
#
#     def __str__(self):
#         return f'{self.firstname} {self.lastname}'
#
# Damir = Employee('Damir','Khalilov', 27)
# Alexey = Employee('Alexey','Bogomolov', 25)
# print(Damir.meet())
#print(Alexey.__dict__) '''возвращает словарь с видимымимы отребутами '''
#print(Alexey.__dir__()) ''' все возвращает что может иметь значения к классу'''


class Employee:


    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def first(self):
        return f'Hello {self.firstname}!'


    def last(self):
        return f'Hello {self.lastname}!'


    def yo(self):
        return f'{self.age} y.o!'


    def company(self, company):
        return f'{company}'


    def info(self):
        return f'{self.firstname}\n{self.lastname}\n{self.age}y.o'


    def __str__(self):
        return f"{self.firstname} {self.lastname}"


Ikram = Employee('Ikram', 'Svarov', 18)
Alexey = Employee('Alexey', 'Bogomolov', 26)

print(Ikram.first())
print(Ikram.last())
print(Ikram.yo())
print(Ikram.info())
print(Ikram.company('Google'))












