
'''
def func(m,g=9.8):
    return m*g"zadacha1"
def sum_range(start, end):    if start > end:
        start, end = end, start    s = 0
    for i in range(start, end+1):        s += i
    return s
a, b = map(int, input("napiwite dva chisla: ").split())print(sum_range(a, b))

a = func (78,6)
print(a)
#print(round(a,4))


()()(()))(()


 f= {
    'key': 'value'
}


def func(**kwargs):
    d = kwargs
    try:
        for i, v in d.items():
            print(i, v)
    except:
        print('Empty list')

# func(key='124')
func(**f)


#Assert
def avg(ranks):
    assert len(ranks) != 0, 'Список ranks не должен быть пустым'
    return round(sum(ranks)/len(ranks), 2)

ranks = []
print("Среднее значение:", avg(ranks))

()()()()()

# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x


# a = get_list()
# # print(a)
# for x in a:
#     print(x)

)()()()

# def get_list():
#     for i in range(1, 10):
#         a = range(i, 11)
#         yield sum(a)/len(a)
        # for p in a:
        #     print(p, end=' ')
        # print('\n')


# a = get_list()
# print(a)
# print(list(a))

)()()()()()(
# генерация нового списка, состоящего только из четных чисел
def get_even(list_of_nums) :
    for i in list_of_nums:
        if i % 2 == 0:
            yield i

# инициализация списка
list_of_nums = [i for i in range(1, 31)]

# вывод начального списка
print ("До фильтрации в генераторе: " +  str(list_of_nums))

# вывод только четных значений из списка
print ("Только четные числа: ", end = " ")
for i in get_even(list_of_nums):
    print (i, end = " ")

    ()()(()()((



'''





































































