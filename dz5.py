# Создать генератор для заполнения списка

from string import ascii_letters, ascii_lowercase, ascii_uppercase


a = [i for i in range(10)] # генератор для заполнения списка до 10
b = a[::-1] # перевернули список
c = a[3:7]  # вырезали из списка
print(b)
print(c)


# Создать функцию для генерации списков с аннотациями

def generator()->list:
    '''
    Генератор списка алфавита от А до Z
    '''
    alphabet = list(ascii_uppercase)
    b = [i for i in alphabet] 
    return(b)

print(generator())

# *Сделать функию, которая будет вызываться из генератора и отдавать текущее время
import time
from datetime import datetime

def get_current_time():
    time.sleep(1)
    now = datetime.now()
    return (print(now.strftime("%H:%M:%S")))

print([get_current_time() for i in range(5)])


# **Написать функцию, котора будет принимать в себя список людей, и будет возращать список мужчин и список женщин

person = [
    {'name':'Dmitriy','gender':'M'},
    {'name':'Hanna','gender':'W'},
    {'name':'Julia','gender':'W'},
    {'name':'Evgeniy','gender':'M'},
    {'name':'Hleb','gender':'M'},
    {'name':'Konstantin','gender':'M'},
    {'name':'Anastasia','gender':'W'},
    
]

def guest_list():
    '''
    Функция принимает в себя список гостей, отдает нам общее количество гостей,
    количество и список мужчин,
    количество и список женщин.
    '''
    gen = [d['gender'] for d in person] # генератор списка по которому мы считаем мужчин
    men = [d['name'] for d in person if d['gender'] == 'M'] # генератор списка по которому мы выводим мужчин
    women = [d['name'] for d in person if d['gender'] == 'W']# генератор списка по которому мы выводим женщин
    d,f=0,0
    for i in gen:
        if i == 'M':
            d+=1
        elif i == 'W':
            f+=1
    return(f'Total = {d+f},\nMan = {d}:{men},\nWoman = {f}{women}')

print(guest_list())