'''
all
a = 'wqecs'
print(all(a))  #  если все обьекты пригодны для итерации
###
'''
'''#any
a = 1234,
print(any(a))  #  проверит все и найдет одну то что нужно
'''
'''#chr
a = 1234
print(chr(24))  #
'''
'''# divmod
 
))  #
'''
'''
a = '1234'
for i , r  enumerate(a):
    print(i)

'''
'''a = 'python'
b = 'best'
print('%s is the %s'% (a,b))
print('{} is the {}'.format (a,b))
print(f'{a} is the {b}')
'''

'''
a = [i for i in range(1,11)]
b= filter(lambda x:x%2==0,a)#  даст четные числа

print(a)
'''


'''a = 'python'
b = 'best'
# print(eval('25 + 3'))
# divmod(25, 3) | 25 // 3 | 25 % 3
# print('%s is the %s' %(a, b))
# print('{} is the {}'.format(a, b))
# print(f'{a} is the {b}')

Alisher Kenzhebek uulu, [10.02.2023 14:50]
"""
Функция filter() в Python применяет другую функцию 
к заданному итерируемому объекту 
(список, строка, словарь и так далее), проверяя, 
нужно ли сохранить конкретный элемент или нет.
 Простыми словами, она отфильтровывает то, 
 что не проходит и возвращает все остальное.
 
"""

# a = [i for i in range(1, 11)]
# b = filter(lambda x: x % 2 == 0, a)
# # f = list(b)
# # print(f)
# for i in b:
#     print(i)


# city = ('Bishkek', "Osh", "Batken", "Kara-Balta")
# # b = filter(str.isalpha, city)
# b = filter(lambda x: len(x) % 2 ==0,filter(str.isalpha, city))
# print(list(b))

Alisher Kenzhebek uulu, [10.02.2023 15:04]
# b = map(int, ['1', '2', '3', '4', '5', '6', '7'])
# print(b)
# a = sum(b)
# a = min(b)
# a = max(b)
# a = sum(b) #Дважды пройтись по коллекции нельзя!
# print(a)
# print(next(b))
# print(next(b))
# print(next(b))
# for x in b:
#     print(x, end=" ")

----------------------------------
b = (int(x) for x in ['1', '2', '3', '4', '5', '6', '7'])
a = list(b)
print(a)
----------------------------------
'''
a = 'python'
b = 'best'
# print(eval('25 + 3'))
# divmod(25, 3) | 25 // 3 | 25 % 3
# print('%s is the %s' %(a, b))
# print('{} is the {}'.format(a, b))
# print(f'{a} is the {b}')


"""
Функция filter() в Python применяет другую функцию 
к заданному итерируемому объекту 
(список, строка, словарь и так далее), проверяя, 
нужно ли сохранить конкретный элемент или нет.
 Простыми словами, она отфильтровывает то, 
 что не проходит и возвращает все остальное.
"""

# a = [i for i in range(1, 11)]
# b = filter(lambda x: x % 2 == 0, a)
# # f = list(b)
# # print(f)
# for i in b:
#     print(i)


# city = ('Bishkek', "Osh", "Batken", "Kara-Balta")
# # b = filter(str.isalpha, city)
# b = filter(lambda x: len(x) % 2 ==0,filter(str.isalpha, city))
# print(list(b))


# b = map(int, ['1', '2', '3', '4', '5', '6', '7'])
# print(b)
# a = sum(b)
# a = min(b)
# a = max(b)
# a = sum(b) #Дважды пройтись по коллекции нельзя!
# print(a)
# print(next(b))
# print(next(b))
# print(next(b))
# for x in b:
#     print(x, end=" ")

'''----------------------------------
b = (int(x) for x in ['1', '2', '3', '4', '5', '6', '7'])
a = list(b)
print(a)
----------------------------------'''

# s = map(int, input().split())
# # s = input().split()
# a = list(s)
# print(a)


# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9, 10]
# c = [12, 13, 14, 15, 16, 17, 18]
# d = 'python'

# z = zip(a, b, c, d)
# for x in z:
#     print(x)


# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9, 10]
# c = [12, 13, 14, 15, 16, 17, 18]
# d = 'python'

# # z1, z2, z3, z4 = zip(a, b, c, d)
# # print(z1, z2, z3, z4, sep="\n")

# z1, *z2 = zip(a, b, c, d)
# print(z1, z2)


# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8, 9, 10]
# c = [12, 13, 14, 15, 16, 17, 18]
# d = 'python'

# z = zip(a, b, c, d)
# # lz = list(z)
# # print(*lz)
# t = tuple(z)
# print(t)











































