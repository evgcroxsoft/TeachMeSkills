# My Name

print('My name is')
name = 'Evgeniy'
print(name)

print('Do you know another name of the name Evgeniy?')

# Input names
g = input('Yes or No: ')
if g == 'Yes':
    print('Super')
elif g == 'No':
    print('Aha, You need to know - Zhenya')
else : print('Mdaaaaaaa')

# Numbers
print('We have to decide: ((2**5)*2-16*2)/(8**8)')
result = ((2**5)*2-16*2)/(8**8)
print('Total result',result)
print('') # отступ
print(type(result)) # вывод типа данных 
print('Type of Result:',type(result) is float) # сравнение типа значения со значением флоат
list = [g, result, name] # создали список значений
print(list)
list[1] = 150000000000 #изменили значение result 
print(list[1]) #вывели значение нужной записи
print(list) #вывели список и удостоверились что все поменялось

print(type(result)) # вывели тип результа
result = int(result)#  перевели тип в интеджер
print(type(result))
print(type(result) is type(g))# сравниваем получаем Нет
g = str(g) # перевели значение джи в стринг
result = str(result) # также и здесь
print(result is g)# сравниваем получаем фелс, так как они не одинаковые
print(result == g)# аналогично
print(type(result) is type(g))# а вот здесь, все ок. Значение тру. Так как типы одинаковые.
print(type(list[0])) # выводим тип первой ячейки листа

formula = ((2**5)*2-16*2)/(8**8)#
print('Total result',formula)
print(type(formula))# видим что формула флоат
formula = int(formula)# переведем в интеджер из флоат
print(type(formula)) # видим что все перевелось


# КАК ВЫВЕСТИ ВСЕ ТИПЫ ДАННЫХ ЗАПИСАННЫХ В list?
# КАК ОКРУГЛИТЬ В БОЛЬШУЮ ИЛИ МЕНЬШУЮ СТОРОНЫ ФЛОАТ (formula)?