"""
Условия
if
elif
else

and , и
or , или
not  отрицания
# oktotorp, sharp, heshteg



"""
#print ('dddd')
#a = input()
#print(a)
#a=input('damir: ')
#print(a)
#print('10',type('10'))
#print(10,type(10))





#1. Напишите скрипт, в котором вы намеренно вызываете исключения. Обработайте их.
#Посмотрите как они работают и сделайте выводы.
'''a = 7
b = 6
try:
    if a > b:
        print(a / 0)
except NameError:
    print('Error')
except ZeroDivisionError:
    raise ZeroDivisionError('ZeroDivisionError: division by zerO')
else:
    print("Ok")
finally:
    print('Final')

print('Hello world')

'''

#1. Напишите скрипт, который запрашивает у пользователя логин
#и пароль. Напишите соответствующую валидацию и сохраните в
#.txt файл. Затем выведите количество "зарегистрированных
#пользователей".

#f = open('text.txt M', 'w')
#d = 'Hello'
#g = f.read()
#if d in g:
#    print(True)
# print(f.(3))
# print(f.readline(3))
# print(f.readlines())
# for i in f:
#     print(i)
# print(*f)
#f.close()


#with open('text.txt M','w') as f:
    # print(f.read())
 #   for i in f:
 #       print(i)


'''with open('file.txt', 'a') as f:
    password = input('Введите пароль:')
    password2 = input('Повторите пароль:')
while len(password) < 8:
    print("Короткий!")
    password = input('Введите пароль:')
    password2 = input('Повторите пароль:')
while "123" in password:
    print("Простой!")
    password = input('Введите пароль:')
    password2 = input('Повторите пароль:')
while password2 != password:
    print("Различаются.")
    password = input('Введите пароль:')
    password2 = input('Повторите пароль:')
else:
    print("Пойдет!")'''








