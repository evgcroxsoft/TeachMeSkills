from getpass import getpass
from wsgiref.validate import InputWrapper


print('Привет!')
yours_name = input('Как Вас зовут?: ')
print('Приятно ' + yours_name +', меня зовут Питон.''\n')
login = input('Пожалуйста придумайте Логин: ')
login2 = input('Пожалуйста введите Логин повторно: ')
while True:
    if login != login2:
        print('Логины не совпадают!')
        login = input('Пожалуйста введите Логин: ')
        login2 = input('Пожалуйста введите Логин повторно: ')
        continue
    print('')
    parol = getpass('Пожалуйста введите Пароль: ')
    parol2 = getpass('Пожалуйста введите Пароль: ')
    print('')
    break
while True:
    if parol != parol2:
        print('Пароли не совпадают!')
        parol = input('Пожалуйста введите Пароль: ')
        parol2 = input('Пожалуйста введите Пароль повторно: ')
        continue
    print('')
    parol = input('Пожалуйста введите Пароль: ')
    parol2 = input('Пожалуйста введите Пароль: ')
    print('')
    break