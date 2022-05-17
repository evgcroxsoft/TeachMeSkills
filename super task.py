#Всем привет!)
# Задание для тех кто уже справился с дз и хочет доп. нагрузку (это необязательно):

# Написать программу, которая будет предлагать меню (в консоле) с возможными действиями пользователю, 
# пока пусть будут два действия: авторизация и регистрация.
# При успешной регистрации данные пользователя должны быть записаны в файл, а
# при авторизации, система должна проверять, есть ли данные о пользователе, 
# который пытается авторизоваться, в файле.
# Файл можно назвать users.txt
# Регистрация/авторизация должна быть с помощью email и password.
# С помощью декоратора необходимо проверять несколько условий:
#  1. Подходит ли email под рамки name@<domain>.com.
#  2. Имеет ли password специальные символы и заглавные буквы.
#  3. Длина пароля должна быть больше 8 символов.

import re

database_file = 'user.txt'

def validate_credentials(func):
    
    def wrapper(email,password):
        if not len(password) > 8:
            raise Exception('Password less than 8 characters')



        func(email,password)
    return wrapper

def ask_credentials() -> tuple:
    email = input('Email: ')
    password = input('Password: ')
    return email, password

def log_in(email: str, password: str):
    credentials = f'{email}:{password}'
    with open(database_file, 'r') as users_file:
        if credentials in users_file.read():
            print('Logged in!!!\n')
        else:
            print('Invalid login or password\n')

@validate_credentials
def sign_up(email: str, password: str):
    with open(database_file, 'a') as users_file:
        credentials = f'{email}:{password}\n'
        users_file.writelines([credentials])

def menu():
    while True:
        print('Menu: \n1 - Log in\n2 - Sign up\n0 - Exit')
        user_choice = int(input('Your choice: '))

        if user_choice == 1:
            email,password = ask_credentials()
            log_in(email,password)
        elif user_choice == 2:
            email,password = ask_credentials()
            sign_up(email,password)
        elif user_choice == 0:
            break

menu()

# from click import password_option

# def validate_credentials (func):

#     def wrapper(username,password):
#         pattern = r"^[a-zA-Z0-9!s%&'*+\-\/=?^_`{|}~]+@[a-zA-Z0-9_]+\.{1}[a-zA-Z0-9_]{,63}$" 
#         while True:
#             if re.fullmatch(pattern,username) !=True:
#                 print('Емейл введен не корректно')

#             lengh = len(password)
#             if lengh < 7:
#                 print('Пароль меньше 8 символов')
#             func()
#     return wrapper

# def create_record():
#     print('Данные сохранены!')

# @validate_credentials
# def register_user(username,password):
#     pass


# def menu():
#     '''Menu and choice'''
#     print("Меню - сделайте свой выбор:")
#     print("'1' - Авторизация")
#     print("'2' - Регистрация")
#     choice = int(input(''))
#     if choice == 2:
#         register_user('sdfsdfsddsf','sdfsdfsdf')

# menu()

# def registration():
#     print('Вы в меню регистрации:')
#     login = input('Ведите свой емейл: ')
#     password = input('Ведите свой пароль: ')
#     '''login and password write in file'''
#     pass




# menu()



# def menu ():
#     print("Меню:")
#     print("Авторизация: нажмите 1")
#     print("Регистрация: нажмите 2")
#     # choice = int(input())
#     # if choice == 1:
#     #     print("Меню Авторизации.")
#     #     input('Ведите логин: ')
#     #     input('Ведите пароль: ')


# menu()

# def regex (func):

#     def wrapper(*args,**kwarks):
#         if args == 1:
#         func()
#     return wrapper


# def check_email ():

#     value = input('Enter you email: ')
#     pattern = r"^[a-zA-Z0-9!s%&'*+\-\/=?^_`{|}~]+@[a-zA-Z0-9_]+\.{1}[a-zA-Z0-9_]{,63}$" 

#     print(f'Lenght:{len(value)}')
#     if re.fullmatch(pattern,value):
#         print ('Match')
#     else:
#         print('No Match')


# check_email ()