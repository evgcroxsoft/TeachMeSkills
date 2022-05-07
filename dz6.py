#Задание №1 - Сделать свой Декоратор
#Задание №2 - Сделать лямбда-функцию
#Задание №3 - Сделать функцию и обернуть Декоратором
#Задание №4 - *Задокументировать все

from datetime import datetime
from import_practic import dz6_import

# Создание декоратора
def decorator(bla_bla):
    '''Декоратор считает время между началом и концом выполнения функции'''

    def wrapper(): #обертка
        start = datetime.now()
        bla_bla()
        end = datetime.now()
        result = end - start
        print(result)
    return wrapper #обертка

@decorator #прикрепили декоратор к нашей новой создает функции
def account_time():
    print(dz6_import.animals_list())
    

account_time() # вызвали функцию



# print(print.__doc__)
# print(input.__doc__)

# string_list = ['1','2','3','4','5','6','7','8','9','10']
# def integer_list(x):
#     '''Переводим переменную string в integer'''
#     return(int(x))

# print(list(map(integer_list,string_list)))


# x = lambda a: int('string_list')
# print(x)

# print(list(map(lambda x: x+5,[1,2,3,4])))


# fruits = ['apple','banana','kiwi','apple']

# new_fruits = []
# for i in fruits:
#     if i == 'apple':
#         new_fruits.append(i)
# print(new_fruits)


# test = list(filter(lambda fruit: fruit == 'apple',fruits))
# print(test)

# test = list(map(lambda fruit: fruit == 'apple',fruits))
# print(test)
