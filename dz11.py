#Переводим Список в итерируемый объект

names_of_guests = ['Dima', 'Petr', 'Olesya']
iter_names = iter(names_of_guests)
print(iter_names)
print(next(iter_names))
print(next(iter_names))
print(next(iter_names))

#Создать генератор геометрической прогрессии:
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
