# 1. Написать программу, которая получит имя и возраст, пользователя, проверит > 18 и         
# выдает приветственное сообщение в зависимости от возраста.
# 2. Завернуть в вечный цикл.
# name = input('What is your name?:')
# print(f'Hello {name}')
# while True:
#     age = int(input('How old are you?:'))
#     if age < 18:
#         print(f"Sorry, but your age is {age} and you can't go to Disco!")
#     elif age == 18:
#         print(f"Ooh, your age is {age} and you can go to Disco!")
#     elif age > 18:
#         print(f"Unbelivable, your age is {age} and you can go to Disco or GO HOME!")

# 3. *Сделать программу, в которой нужно будет угадывать число. 
# Число выбирается автоматом от 1 до 100.
# Есть проверка на ввод букв, просит вводить только цифры.
# Подсказки Ryadom do 5,10,20,30 и Daleko, poprobuy esho при вводе числа. 
# Программа закончиться после успешного ввода.
# Выдает ошибку и перезапускает ввод, если введена буква"
# Блок убирает ошибку и перезапускает ввод, если ничего не введено"

import random
number = random.randint(1,100)
while True:
    shout = input('Угадай мое число?:')
#"Выдает ошибку и перезапускает ввод, если введена буква"
    if shout.isalpha():
        print('Invalid, please write only numbers')
        continue
#"Ниже блок убирает ошибку и перезапускает ввод, если ничего не введено"
    try:
        shout = round(eval(shout))
    except ValueError:
        print('Please, enter only digit!')     
        continue
    if shout == number:
        print('Yeahhhhhhh')
        break
    elif shout <= (number + 5) and shout >= (number - 5):
        print('Ryadom do 5')  
    elif shout <= ((number + 6 and number +10)) and shout >= ((number - 6 and number - 10)):
        print('Ryadom do 10')  
    elif shout <= ((number + 11 and number +20)) and shout >= ((number - 11 and number - 20)):
        print('Ryadom do 20')
    elif shout <= ((number + 21 and number +30)) and shout >= ((number - 21 and number - 30)):
        print('Ryadom do 30')
    else:
        print('Daleko, poprobuy esho')