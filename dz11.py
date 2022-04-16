import re

#Переводим Список в итерируемый объект

names_of_guests = ['Dima', 'Petr', 'Olesya']
iter_names = iter(names_of_guests)
print(iter_names)
print(next(iter_names))
print(next(iter_names))
print(next(iter_names))

# 1. DZ - Создать генератор геометрической прогрессии:
def func():
    print('Подсчет геометрической прогрессии')
    a = int(input('Ведите значение 1: '))
    b = int(input('Ведите значение 2: '))
    memb = int(input('Ведите количество членов прогрессии: '))
    for n in range(1,memb):
        c = b ** n
        d = c * a
        yield d


do = func()
for l in do:
    print(l)


# Дополнительно создал список

names = ['Dima','Petr','Olesya']

'''ГЕНЕРАТОР'''
def generator(names): # Генератора это функция, которая содержит вместо RETURN -> YIELD! 
    for u in names:
        yield u # Елд, запоминает состояние аргумента!

generator_itr = generator(names) # Нам нужно создать переменную, которая будет равна функции generator(names)
print(next(generator_itr)) # Выводим с помощью NEXT каждое следующее имя в списке names через созданную функцию
print(next(generator_itr))
print(next(generator_itr))

'''ИТЕРАТОР'''
iter_names = iter(names)
print(next(iter_names))
print(next(iter_names))
print(next(iter_names))

'''ЦИКЛ'''
for i in names: # Аргумент 'i' в списке имен проходит по первому значению, потом по второму и третьему и выходит
    print(i)


# 2. DZ - *Сделать функцию для фильтрации емейла (регуляркой)
'''
Правила валидации имейлов "username@hostname":
username может в себе содержать:
латиницу
цифры
знаки!# %&'*+-/=?^_`{|}~
точку, за исключением первого и последнего знака,которая не может повторяться
- hostname состоит из нескольких компонентов, разделенных точкой и не превышающей 63 символа. 
Компоненты, в свою очередь, состоят из латинский букв, цифр и дефисов, причем дефисы не могут быть в начале 
или в конце компонента.
'''

def check_email ():

    value = input('Enter you email: ')
    pattern = r"^[a-zA-Z0-9!s%&'*+\-\/=?^_`{|}~]+@[a-zA-Z0-9_]+\.{1}[a-zA-Z0-9_]{,63}$" 
    # TODO не получается: 
    # 1. Не знаю как прописать в первой части выражения к примеру как "!" ограничить до 1 ввода; 
    # 2. Во второй часьти выражения Как заставить сделать дефисы но не в начале или в конце компонента.

    print(f'Lenght:{len(value)}')
    if re.fullmatch(pattern,value):
        print ('Match')
    else:
        print('No Match')


check_email ()