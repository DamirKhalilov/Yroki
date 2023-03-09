'''# def square(integer):
#     s = integer ** 2
#     return s
f = [1, 3, 4]

def square(integer):
    return integer ** 2


def summ(integer, string):
    return int(integer) * str(string)


# g = summ(string='astr', integer=10)
# print(g)
summ(string='astr', integer=10)
print(summ(string='astr', integer=10))


def hello():
    return 'Hello world'


def append():
    s = hello()
    return s + '!!!'

# d = square(4)
# print(d)
# print(square(4))'''
################()))()()()()(
'''name = input('Your name: ')
last_name = input('Your last_name: ')
age = int(input('Your age: '))


def func(name,last_name,age):
    if age < 25 :
        return f'Привет {name} {last_name}, тебе {age} пацанчик!'
    elif age > 25 and age < 33:
        return f'Привет {name} {last_name}, тебе {age} машина!'
    else:
        return f'Привет {name} {last_name}, тебе {age} дедушка!'

if age >=18:
    print(func(name=name, last_name=last_name, age=age))
else:
    print('Forbidden!')


# q = func(name=name, last_name=last_name, age=age)
# print(q)
'''
'''Напишите функцию, которая принимает в себя произвольный список из чисел и возвращает кортеж, внутри которого
# хранится самое маленькое и самое большое число из списка.'''
# d = [i for i in range(54)]
#
#
# def func(list):
#     big = max(list)  # d(filter(lambda x: max(x), tuple))
#     little = min(list)  # d(filter(lambda x: min(x), tuple))
#     tup = (big, little)
#     return tup
#
#
# c = func(list=d)
# print(c)

''' Напишите функцию, которая принимает в себя строку и в случае, если вся строка состоит из уникальных символов,
 верните True, иначе False.'''
# stre = input("Введите символы: ")
#
#
# def funs(str):
#     if len(str) == len(set(str)):
#         return True
#     if len(str) != len(set(str)):
#         return False
#
#
# s = funs(str=stre)
# print(s)

'''Задача'''
# country ={
#     "name": ['USA','China','Canada','Italy',
#             'France','Germany','Russia','Irak'],
#     "lvl": ['сильные','сильные','сильные',
#            'средние','средние','средние','слабые',
#             'слабые'],
# }
#
#
# def word():
#     global country
#     for i in range(len(country['name'])):
#         print(f'{country["name"][i]}  -  уровень: {country["lvl"][i]}  (по данным за 15 лет).')
#
#
# word()
