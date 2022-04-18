from string import ascii_letters, ascii_lowercase, ascii_uppercase
import time

# Создать генератор для заполнения списка

# a = [i for i in range(10)] # генератор для заполнения списка до 10
# b = a[::-1] # перевернули список
# c = a[3:7]  # вырезали из списка
# print(b)
# print(c)


# Создать функцию для генерации списков с аннотациями

# def generator() -> list:
#     '''
#     Генератор списка алфавита от А до Z без букв, которые есть в Имени.
#     '''
#     alphabet = list(ascii_lowercase)
#     name = 'Zhenya'
#     generator_alphabet_without_letter = [let for let in alphabet if let not in name.lower()]
#     return generator_alphabet_without_letter

# print(generator())

# # *Сделать функию, которая будет вызываться из генератора и отдавать текущее время
# import time
# from datetime import datetime

# def get_current_time():
#     time.sleep(1)
#     now = datetime.now()
#     return (now.strftime("%H:%M:%S"))

# print([get_current_time() for i in range(5)])

# new_list = []
# for i in range (1,5):
#     new_list.append(get_current_time())

# print(new_list)


# # **Написать функцию, котора будет принимать в себя список людей, и будет возращать список мужчин и список женщин

person = [
    {'name' : 'Dmitriy', 'gender' : 'M'},
    {'name' : 'Hanna', 'gender' : 'W'},
    {'name' : 'Julia', 'gender' : 'W'},
    {'name' : 'Evgeniy', 'gender' : 'M'},
    {'name' : 'Hleb', 'gender' : 'M'},
    {'name' : 'Konstantin', 'gender' : 'M'},
    {'name' : 'Anastasia', 'gender' : 'W'},
    
]

def guest_list(person):
    '''
    Функция принимает в себя список гостей, отдает нам общее количество гостей,
    количество и список мужчин,
    количество и список женщин.
    '''
    gen = [d['gender'] for d in person] # генератор списка и выводим по ключу всех участников
    men = [d['name'] for d in person if d['gender'] == 'M'] # генератор списка по которому мы выводим мужчин
    women = [d['name'] for d in person if d['gender'] == 'W']# генератор списка по которому мы выводим женщин
    total = (f'Total = {len(gen)},\nMan = {len(men)}:{men},\nWoman = {len(women)}{women}')
    return total

print(guest_list(person))




# #*We have list of guests, we need print new list without guest from exseption list


# list_of_guest = ('Zhenya', 'Katya', 'Masha', 'Fedor', 'Piter', 'Lesya')
# exseption_list = input()

# new_list = [val for val in list_of_guest if val not in (exseption_list)]
# print(new_list)